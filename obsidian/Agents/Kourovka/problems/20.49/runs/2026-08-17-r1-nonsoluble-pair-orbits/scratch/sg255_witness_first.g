# Frozen GAP computation for Kourovka 20.49, revision 1.
# Scope: every SmallGroups isomorphism representative of order 1..255.
# For each nonsoluble representative, stop at the first full-exponent pair.
# A group with no such witness necessarily reaches and certifies all |G|^2 pairs.
# Standard output is the primary raw artifact and must be redirected by the
# separately frozen shell command. Standard error is redirected separately.

SizeScreen([4096, 4096]);

bound := 255;
totalCatalogueGroups := 0;
solubleGroups := 0;
nonsolubleGroups := 0;
candidateGroups := 0;
totalPairsTested := 0;
startRuntime := Runtime();

Print("KOUROVKA_20_49_SG255_WITNESS_FIRST_V1\n");
Print("gap_version=", GAPInfo.Version, "\n");
Print("smallgrp_static_version=1.5.3\n");
Print("bound=", bound, "\n");
Print("catalogue_iteration=all_indices\n");
Print("candidate_rule=exhaust_all_ordered_pairs_without_exponent_equality\n");

for n in [1..bound] do
  if not SmallGroupsAvailable(n) then
    Print("FATAL unavailable_order=", n, "\n");
    Error("SmallGroups library unavailable at an order inside the frozen layer");
  fi;

  nr := NumberSmallGroups(n);
  totalCatalogueGroups := totalCatalogueGroups + nr;
  orderSoluble := 0;
  orderNonsoluble := 0;
  Print("ORDER_START order=", n, " catalogue_count=", nr, "\n");

  for idx in [1..nr] do
    id := [n, idx];
    G := SmallGroup(id);

    if Size(G) <> n then
      Print("FATAL id=", id, " reconstructed_size=", Size(G), "\n");
      Error("SmallGroup reconstruction has the wrong size");
    fi;

    if IsSolvableGroup(G) then
      solubleGroups := solubleGroups + 1;
      orderSoluble := orderSoluble + 1;
    else
      nonsolubleGroups := nonsolubleGroups + 1;
      orderNonsoluble := orderNonsoluble + 1;
      groupStart := Runtime();
      els := Elements(G);
      eG := Exponent(G);
      testedPairs := 0;
      found := false;
      firstWitness := fail;
      pairExponents := [];

      for i in [1..Length(els)] do
        for j in [1..Length(els)] do
          H := Group([els[i], els[j]]);
          eH := Exponent(H);
          testedPairs := testedPairs + 1;
          Add(pairExponents, eH);

          if eG mod eH <> 0 then
            Print("FATAL id=", id, " pair=[", i, ",", j,
                  "] subgroup_exponent=", eH,
                  " ambient_exponent=", eG, "\n");
            Error("Subgroup exponent failed to divide ambient exponent");
          fi;

          if eH = eG then
            found := true;
            firstWitness := [i, j, Order(els[i]), Order(els[j]), Size(H), eH];
            break;
          fi;
        od;
        if found then
          break;
        fi;
      od;

      totalPairsTested := totalPairsTested + testedPairs;

      if found then
        Print("GROUP id=", id,
              " status=HAS_FULL_EXPONENT_PAIR",
              " ambient_exponent=", eG,
              " tested_pairs_until_witness=", testedPairs,
              " witness=[i,j,ord_i,ord_j,subgroup_size,subgroup_exponent]=",
              firstWitness,
              " runtime_ms=", Runtime() - groupStart,
              "\n");
      else
        expectedPairs := n^2;
        if testedPairs <> expectedPairs then
          Print("FATAL id=", id,
                " tested_pairs=", testedPairs,
                " expected_pairs=", expectedPairs, "\n");
          Error("Candidate ordered-pair enumeration was incomplete");
        fi;
        candidateGroups := candidateGroups + 1;
        exponentHistogram := Collected(pairExponents);
        Print("GROUP id=", id,
              " status=COUNTEREXAMPLE_CANDIDATE",
              " ambient_exponent=", eG,
              " exhaustive_ordered_pairs=", testedPairs,
              " exponent_histogram=", exponentHistogram,
              " runtime_ms=", Runtime() - groupStart,
              "\n");
      fi;
    fi;
  od;

  Print("ORDER_DONE order=", n,
        " catalogue_count=", nr,
        " soluble_count=", orderSoluble,
        " nonsoluble_count=", orderNonsoluble,
        "\n");
od;

Print("SUMMARY total_catalogue_groups=", totalCatalogueGroups,
      " soluble_groups=", solubleGroups,
      " nonsoluble_groups=", nonsolubleGroups,
      " pairs_tested=", totalPairsTested,
      " candidate_groups=", candidateGroups,
      " runtime_ms=", Runtime() - startRuntime,
      "\n");
QUIT;

