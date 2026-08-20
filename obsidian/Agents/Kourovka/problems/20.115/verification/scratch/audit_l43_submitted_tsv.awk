BEGIN {
  FS = "\t";
  group_order = 6065280;
  expected = 0;
  pair_count = 0;
  nonzero_count = 0;
  violation_count = 0;
  bad_sequence = 0;
  bad_grid = 0;
  bad_nonzero = 0;
  bad_product = 0;
  bad_divides = 0;
  bad_violation = 0;
  bad_row_data = 0;
  bad_class_data = 0;
  bad_fields = 0;
  split_pair_records = 0;
  pending_pair = 0;
  summary_count = 0;
}

function audit_pair(idx,row,cls,cname,degree,class_order,exact_value,recorded_nonzero,recorded_product,recorded_divides,recorded_violation,    key,computed_nonzero,computed_product,computed_divides,computed_violation) {
  pair_count++;
  expected++;
  if (idx != expected || idx != (row-1)*29+cls) bad_sequence++;
  key = row SUBSEP cls;
  if (row < 1 || row > 29 || cls < 1 || cls > 29 || seen[key]++) bad_grid++;

  if (!(row in row_degree)) row_degree[row] = degree;
  if (row_degree[row] != degree || degree <= 0 || int(degree) != degree) bad_row_data++;
  if (cls == 1 && exact_value != sprintf("%d",degree)) bad_row_data++;

  if (!(cls in stored_class_order)) {
    stored_class_order[cls] = class_order;
    stored_class_name[cls] = cname;
  }
  if (stored_class_order[cls] != class_order || stored_class_name[cls] != cname || class_order <= 0) bad_class_data++;

  computed_nonzero = (exact_value == "0" ? "false" : "true");
  if (recorded_nonzero != computed_nonzero) bad_nonzero++;
  if (computed_nonzero == "true") {
    nonzero_count++;
    row_nonzero[row]++;
    class_nonzero[cls]++;
  }
  nonzero_pattern[row] = nonzero_pattern[row] (computed_nonzero == "true" ? "1" : "0");

  computed_product = degree * class_order;
  if (recorded_product != computed_product) bad_product++;
  computed_divides = (group_order % computed_product == 0 ? "true" : "false");
  if (recorded_divides != computed_divides) bad_divides++;
  computed_violation = (computed_nonzero == "true" && computed_divides == "false" ? "true" : "false");
  if (recorded_violation != computed_violation) bad_violation++;
  if (computed_violation == "true") violation_count++;
}

pending_pair {
  if (NF != 3) {
    bad_fields++;
  } else {
    audit_pair(p_idx,p_row,p_cls,p_cname,p_degree,p_class_order,p_exact_value,p_nonzero,
               $1+0,$2,$3);
  }
  pending_pair = 0;
  next;
}

$1 == "PAIR" {
  if (NF == 12) {
    audit_pair($2+0,$3+0,$4+0,$5,$6+0,$7+0,$8,$9,$10+0,$11,$12);
  } else if (NF == 10 && $10 == "") {
    split_pair_records++;
    pending_pair = 1;
    p_idx = $2+0;
    p_row = $3+0;
    p_cls = $4+0;
    p_cname = $5;
    p_degree = $6+0;
    p_class_order = $7+0;
    p_exact_value = $8;
    p_nonzero = $9;
  } else {
    bad_fields++;
  }
  next;
}

$1 == "SUMMARY" {
  summary_count++;
  summary_pairs = $3 + 0;
  summary_nonzero = $5 + 0;
  summary_violations = $7 + 0;
}

END {
  if (pending_pair) bad_fields++;
  for (r=1;r<=29;r++) {
    for (c=1;c<=29;c++) {
      key = r SUBSEP c;
      if (!(key in seen)) bad_grid++;
    }
  }

  printf "PAIR_COUNT %d\n", pair_count;
  printf "NONZERO_COUNT %d\n", nonzero_count;
  printf "VIOLATION_COUNT %d\n", violation_count;
  printf "BAD_SEQUENCE %d\n", bad_sequence;
  printf "BAD_GRID %d\n", bad_grid;
  printf "BAD_NONZERO_FLAGS %d\n", bad_nonzero;
  printf "BAD_PRODUCTS %d\n", bad_product;
  printf "BAD_DIVISIBILITY_FLAGS %d\n", bad_divides;
  printf "BAD_VIOLATION_FLAGS %d\n", bad_violation;
  printf "BAD_ROW_DATA %d\n", bad_row_data;
  printf "BAD_CLASS_DATA %d\n", bad_class_data;
  printf "BAD_PAIR_FIELD_COUNTS %d\n", bad_fields;
  printf "SPLIT_PAIR_RECORDS %d\n", split_pair_records;
  printf "SUMMARY_RECORDS %d\n", summary_count;
  printf "SUMMARY_VALUES %d %d %d\n", summary_pairs, summary_nonzero, summary_violations;

  printf "DEGREES [";
  for (r=1;r<=29;r++) printf "%s%d", (r==1 ? "" : ", "), row_degree[r]+0;
  printf "]\n";
  printf "CLASS_ORDERS [";
  for (c=1;c<=29;c++) printf "%s%d", (c==1 ? "" : ", "), stored_class_order[c]+0;
  printf "]\n";

  printf "ROW_NONZERO_COUNTS [";
  for (r=1;r<=29;r++) printf "%s%d", (r==1 ? "" : ", "), row_nonzero[r]+0;
  printf "]\n";
  printf "CLASS_NONZERO_COUNTS [";
  for (c=1;c<=29;c++) printf "%s%d", (c==1 ? "" : ", "), class_nonzero[c]+0;
  printf "]\n";
  printf "NONZERO_PATTERNS [";
  for (r=1;r<=29;r++) printf "%s\"%s\"", (r==1 ? "" : ", "), nonzero_pattern[r];
  printf "]\n";

  failure = (pair_count != 841 || nonzero_count != 495 || violation_count != 0 ||
             bad_sequence || bad_grid || bad_nonzero || bad_product || bad_divides ||
             bad_violation || bad_row_data || bad_class_data || bad_fields ||
             summary_count != 1 || summary_pairs != pair_count ||
             summary_nonzero != nonzero_count || summary_violations != violation_count);
  printf "AUDIT_PASS %s\n", (failure ? "false" : "true");
  exit failure;
}
