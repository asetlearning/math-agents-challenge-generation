# Frozen GAP computation for Kourovka 20.49, revision 1.
# Scope: every SmallGroups isomorphism representative of order 1..255.
# For every nonsoluble representative, exhaust every ordered pair and record
# the exponent distribution of the generated two-generator subgroups.

outPath := "Agents/Kourovka/problems/20.49/runs/2026-08-17-r1-nonsoluble-pair-orbits/scratch/sg255_all_pairs.out";
out := OutputTextFile(outPath, false);
SetPrintFormattingStatus(out, false);

bound := 255;
totalCatalogueGroups := 0;
solubleGroups := 0;
nonsolubleGroups := 0;
candidateGroups := 0;
totalPairs := 0;
startRuntime := Runtime();

Print(out, "KOUROVKA_20_49_SG255_ALL_PAIRS_V1\n");
Print(out, "gap_version=", GAPInfo.Version, "\n");
Print(out, "smallgrp_static_version=1.5.3\n");
Print(out, "bound=", bound, "\n");
Print(out, "ordered_pairs=yes\n");

for n in [1..bound] do
  if not SmallGroupsAvailable(n) then
    Print(out, "FATAL unavailable_order=", n, "\n");
    CloseStream(out);
    Error("SmallGroups library unavailable at an order inside the frozen layer");
  fi;

  nr := NumberSmallGroups(n);
  totalCatalogueGroups := totalCatalogueGroups + nr;
  Print(out, "ORDER order=", n, " catalogue_count=", nr, "\n");

  for idx in [1..nr] do
    id := [n, idx];
    G := SmallGroup(id);

    if Size(G) <> n then
      Print(out, "FATAL id=", id, " reconstructed_size=", Size(G), "\n");
      CloseStream(out);
      Error("SmallGroup reconstruction has the wrong size");
    fi;

    if IsSolvableGroup(G) then
      solubleGroups := solubleGroups + 1;
    else
      nonsolubleGroups := nonsolubleGroups + 1;
      groupStart := Runtime();
      els := Elements(G);
      eG := Exponent(G);
      pairExponents := [];
      fullExponentPairs := 0;
      firstWitness := fail;

      for i in [1..Length(els)] do
        for j in [1..Length(els)] do
          H := Group([els[i], els[j]]);
          eH := Exponent(H);

          if eG mod eH <> 0 then
            Print(out, "FATAL id=", id, " pair=[", i, ",", j,
                  "] subgroup_exponent=", eH, " ambient_exponent=", eG, "\n");
            CloseStream(out);
            Error("Subgroup exponent failed to divide ambient exponent");
          fi;

          Add(pairExponents, eH);
          if eH = eG then
            fullExponentPairs := fullExponentPairs + 1;
            if firstWitness = fail then
              firstWitness := [i, j, Order(els[i]), Order(els[j]), Size(H)];
            fi;
          fi;
        od;
      od;

      expectedPairs := n^2;
      if Length(pairExponents) <> expectedPairs then
        Print(out, "FATAL id=", id, " tested_pairs=", Length(pairExponents),
              " expected_pairs=", expectedPairs, "\n");
        CloseStream(out);
        Error("Ordered-pair enumeration was incomplete");
      fi;

      totalPairs := totalPairs + expectedPairs;
      exponentHistogram := Collected(pairExponents);

      if fullExponentPairs = 0 then
        candidateGroups := candidateGroups + 1;
        status := "COUNTEREXAMPLE_CANDIDATE";
      else
        status := "HAS_FULL_EXPONENT_PAIR";
      fi;

      Print(out, "GROUP id=", id,
            " status=", status,
            " exponent=", eG,
            " tested_pairs=", expectedPairs,
            " full_exponent_pairs=", fullExponentPairs,
            " first_witness=[i,j,ord_i,ord_j,subgroup_size]=", firstWitness,
            " exponent_histogram=", exponentHistogram,
            " runtime_ms=", Runtime() - groupStart,
            "\n");
    fi;
  od;
od;

Print(out, "SUMMARY total_catalogue_groups=", totalCatalogueGroups,
      " soluble_groups=", solubleGroups,
      " nonsoluble_groups=", nonsolubleGroups,
      " exhaustive_ordered_pairs=", totalPairs,
      " candidate_groups=", candidateGroups,
      " runtime_ms=", Runtime() - startRuntime,
      "\n");
CloseStream(out);
QUIT;
