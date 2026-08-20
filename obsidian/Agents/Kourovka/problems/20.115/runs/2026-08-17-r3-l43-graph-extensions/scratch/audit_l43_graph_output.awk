BEGIN {
  FS = "\\|"
  expected_pairs["2.L4(3).2_2"] = 580
  expected_pairs["2.L4(3).2_3"] = 289
  expected_nonzero["2.L4(3).2_2"] = 84
  expected_nonzero["2.L4(3).2_3"] = 36
}

function fields(    i,p,key,value) {
  delete f
  for (i = 2; i <= NF; i++) {
    p = index($i, "=")
    if (p > 0) {
      key = substr($i, 1, p - 1)
      value = substr($i, p + 1)
      f[key] = value
    }
  }
}

$1 == "RUN" { run_records++; next }
$1 == "SOURCE" { source_records++; next }

$1 == "TABLE" {
  fields()
  table_records[f["id"]]++
  next
}

$1 == "STRUCTURE" {
  fields()
  structure_records[f["id"]]++
  if (f["structural_pass"] != "true") bad_structure++
  next
}

$1 == "OUTER_CLASS" {
  fields()
  outer[f["table"], f["class"]] = 1
  outer_count[f["table"]]++
  next
}

$1 == "FAITHFUL_ROW" {
  fields()
  faithful[f["table"], f["row"]] = 1
  faithful_count[f["table"]]++
  if (f["kernel_positions"] != "[ 1 ]") bad_kernel++
  next
}

$1 == "PAIR" {
  fields()
  t = f["table"]
  key = t SUBSEP f["row"] SUBSEP f["class"]
  if (key in seen_pair) duplicate_pairs++
  seen_pair[key] = 1
  pair_count[t]++
  if (!((t SUBSEP f["row"]) in faithful)) bad_row_membership++
  if (!((t SUBSEP f["class"]) in outer)) bad_class_membership++
  if (f["kernel_positions"] != "[ 1 ]") bad_kernel++
  if ((f["value"] != "0") != (f["nonzero"] == "true")) bad_nonzero++
  if ((f["degree"] + 0) * (f["class_order"] + 0) != (f["product"] + 0)) bad_product++
  if ((24261120 % (f["product"] + 0)) != (f["remainder"] + 0)) bad_remainder++
  if (((f["remainder"] + 0) == 0) != (f["divides"] == "true")) bad_divides++
  should_violate = (f["nonzero"] == "true" && (f["remainder"] + 0) != 0)
  if (should_violate != (f["violation"] == "true")) bad_violation_flag++
  if (f["nonzero"] == "true") nonzero_count[t]++
  if (f["violation"] == "true") violation_count[t]++
  next
}

$1 == "SUMMARY" {
  fields()
  t = f["table"]
  summary_records[t]++
  summary_pairs[t] = f["pairs"] + 0
  summary_nonzero[t] = f["nonzero_pairs"] + 0
  summary_violations[t] = f["violations"] + 0
  if (f["structural_pass"] != "true") bad_structure++
  next
}

{ unknown_records++ }

END {
  for (t in expected_pairs) {
    if (table_records[t] != 1 || structure_records[t] != 1 || summary_records[t] != 1) bad_record_counts++
    if (pair_count[t] != expected_pairs[t] || summary_pairs[t] != expected_pairs[t]) bad_pair_counts++
    if (nonzero_count[t] != expected_nonzero[t] || summary_nonzero[t] != expected_nonzero[t]) bad_nonzero_counts++
    if (violation_count[t] != 0 || summary_violations[t] != 0) bad_violation_counts++
  }
  pass = (run_records == 1 && source_records == 1 && unknown_records == 0 &&
          bad_structure == 0 && bad_kernel == 0 && duplicate_pairs == 0 &&
          bad_row_membership == 0 && bad_class_membership == 0 &&
          bad_nonzero == 0 && bad_product == 0 && bad_remainder == 0 &&
          bad_divides == 0 && bad_violation_flag == 0 &&
          bad_record_counts == 0 && bad_pair_counts == 0 &&
          bad_nonzero_counts == 0 && bad_violation_counts == 0)
  print "RUN_RECORDS", run_records + 0
  print "SOURCE_RECORDS", source_records + 0
  print "TABLE_2_PAIRS", pair_count["2.L4(3).2_2"] + 0
  print "TABLE_2_NONZERO", nonzero_count["2.L4(3).2_2"] + 0
  print "TABLE_2_VIOLATIONS", violation_count["2.L4(3).2_2"] + 0
  print "TABLE_3_PAIRS", pair_count["2.L4(3).2_3"] + 0
  print "TABLE_3_NONZERO", nonzero_count["2.L4(3).2_3"] + 0
  print "TABLE_3_VIOLATIONS", violation_count["2.L4(3).2_3"] + 0
  print "DUPLICATE_PAIRS", duplicate_pairs + 0
  print "BAD_ROW_MEMBERSHIP", bad_row_membership + 0
  print "BAD_CLASS_MEMBERSHIP", bad_class_membership + 0
  print "BAD_NONZERO", bad_nonzero + 0
  print "BAD_PRODUCTS", bad_product + 0
  print "BAD_REMAINDERS", bad_remainder + 0
  print "BAD_DIVIDES", bad_divides + 0
  print "BAD_VIOLATION_FLAGS", bad_violation_flag + 0
  print "UNKNOWN_RECORDS", unknown_records + 0
  print "AUDIT_PASS", (pass ? "true" : "false")
  exit(pass ? 0 : 1)
}
