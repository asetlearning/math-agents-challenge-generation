# Exact bounded screen for TRI3 seeds among every installed SmallGroup(3^7,i).
# GAP 4.12.1 / SmallGrp 1.5.3.  No random choices.

ORDER := 3^7;

FindNoncommutingPair := function(S)
  local i, j;
  if Length(S) < 2 then
    return fail;
  fi;
  for i in [1..Length(S)-1] do
    for j in [i+1..Length(S)] do
      if S[i] * S[j] <> S[j] * S[i] then
        return [S[i], S[j]];
      fi;
    od;
  od;
  return fail;
end;

CentralOrderThreeSubgroups := function(G)
  local one, zs, out, z, cs;
  one := One(G);
  zs := Filtered(Elements(Center(G)), x -> Order(x) = 3);
  out := [];
  for z in zs do
    cs := Set([one, z, z^2]);
    if not ForAny(out, r -> r.set = cs) then
      Add(out, rec(z := z, set := cs));
    fi;
  od;
  return out;
end;

ValidateCentralProduct := function(seed)
  local G, S, z, pair, roots, D, e1, e2, dz, N, nat, H, hels,
        HP, predicted, hpGroup, expectedOrder, orderOK, pgroupOK,
        exponentOK, equalityOK, closureOK, root1, root2, value1, value2,
        rootOK, noncommOK, allOK;
  G := seed.G;
  S := seed.S;
  z := seed.C.z;
  pair := seed.pair;
  roots := seed.roots;

  D := DirectProduct(G, G);
  e1 := Embedding(D, 1);
  e2 := Embedding(D, 2);
  dz := Image(e1, z) * Image(e2, z^-1);
  N := Subgroup(D, [dz]);
  nat := NaturalHomomorphismByNormalSubgroup(D, N);
  H := Image(nat);

  expectedOrder := ORDER^2 / 3;
  orderOK := Size(H) = expectedOrder;
  pgroupOK := IsPGroup(H) and Size(H) = 3^13;
  exponentOK := Exponent(H) = 9;

  # Independent complete enumeration of every cube in H.
  hels := Elements(H);
  HP := Set(List(hels, h -> h^3));

  # Separately reconstruct the quotient image q(S x S).
  predicted := Set(Concatenation(List(S,
    a -> List(S, b -> Image(nat, Image(e1, a) * Image(e2, b))))));
  equalityOK := HP = predicted;
  hpGroup := Subgroup(H, HP);
  closureOK := Size(hpGroup) = Length(HP);

  root1 := Image(nat, Image(e1, roots[1]));
  root2 := Image(nat, Image(e1, roots[2]));
  value1 := Image(nat, Image(e1, pair[1]));
  value2 := Image(nat, Image(e1, pair[2]));
  rootOK := root1^3 = value1 and root2^3 = value2
            and value1 in HP and value2 in HP;
  noncommOK := value1 * value2 <> value2 * value1;

  allOK := orderOK and pgroupOK and exponentOK and equalityOK
           and closureOK and rootOK and noncommOK;
  Print("H_CHECK id=", seed.id,
        " order=", Size(H),
        " exponent=", Exponent(H),
        " complete_cube_size=", Length(HP),
        " predicted_cube_size=", Length(predicted),
        " complete_equals_predicted=", equalityOK,
        " cube_set_subgroup=", closureOK,
        " rooted_noncommuting_pair=", rootOK and noncommOK,
        " all_revision2_rows=", allOK, "\n");
  return allOK;
end;

loaded := LoadPackage("smallgrp");
Print("TRI3_ORDER2187_BEGIN gap_version=", GAPInfo.Version,
      " smallgrp_loaded=", loaded, "\n");

if not SmallGroupsAvailable(ORDER) then
  Print("STATUS=BLOCKER reason=SmallGroups_library_order_2187_not_installed\n");
else
  nr := NumberSmallGroups(ORDER);
  Print("library_order=", ORDER, " group_count=", nr, "\n");
  countExp9 := 0;
  countNoncomm := 0;
  countCContained := 0;
  countProjectedSubgroup := 0;
  countFibreGate := 0;
  seedHits := 0;
  fullHit := false;

  for i in [1..nr] do
    G := SmallGroup(ORDER, i);
    if Exponent(G) <> 9 then
      if i mod 100 = 0 then
        Print("PROGRESS i=", i, " exp9=", countExp9,
              " noncomm=", countNoncomm, " fibre_gate=", countFibreGate,
              "\n");
      fi;
      continue;
    fi;
    countExp9 := countExp9 + 1;

    els := Elements(G);
    S := Set(List(els, x -> x^3));
    pair := FindNoncommutingPair(S);
    if pair = fail then
      if i mod 100 = 0 then
        Print("PROGRESS i=", i, " exp9=", countExp9,
              " noncomm=", countNoncomm, " fibre_gate=", countFibreGate,
              "\n");
      fi;
      continue;
    fi;
    countNoncomm := countNoncomm + 1;
    roots := [First(els, x -> x^3 = pair[1]),
              First(els, x -> x^3 = pair[2])];

    crecs := CentralOrderThreeSubgroups(G);
    for cr in crecs do
      if not ForAll(cr.set, c -> c in S) then
        continue;
      fi;
      countCContained := countCContained + 1;

      SC := Set(Concatenation(List(S,
        s -> List(cr.set, c -> s * c))));
      K := Subgroup(G, SC);
      if Size(K) <> Length(SC) then
        continue;
      fi;
      countProjectedSubgroup := countProjectedSubgroup + 1;

      cosets := [];
      for s in S do
        cos := Set(List(cr.set, c -> c * s));
        if Position(cosets, cos) = fail then
          Add(cosets, cos);
        fi;
      od;
      fibres := List(cosets,
        cos -> Length(Filtered(cos, x -> x in S)));
      if Length(cosets) <> Size(K) / 3 then
        Error("internal coset coverage mismatch at SmallGroup(2187,", i, ")");
      fi;
      if (not ForAll(fibres, n -> n = 2 or n = 3))
         or (not (2 in fibres)) then
        continue;
      fi;
      countFibreGate := countFibreGate + 1;
      seedHits := seedHits + 1;

      pcgs := Pcgs(G);
      Print("SEED_HIT id=[", ORDER, ",", i, "]",
            " cube_size=", Length(S),
            " projected_subgroup_size=", Size(K)/3,
            " fibre_histogram=", Collected(fibres), "\n");
      Print("CGEN_EXP=", ExponentsOfPcElement(pcgs, cr.z), "\n");
      Print("VALUE1_EXP=", ExponentsOfPcElement(pcgs, pair[1]),
            " ROOT1_EXP=", ExponentsOfPcElement(pcgs, roots[1]), "\n");
      Print("VALUE2_EXP=", ExponentsOfPcElement(pcgs, pair[2]),
            " ROOT2_EXP=", ExponentsOfPcElement(pcgs, roots[2]), "\n");

      seed := rec(id := [ORDER, i], G := G, S := S, C := cr,
                  pair := pair, roots := roots);
      if ValidateCentralProduct(seed) then
        fullHit := true;
        Print("STATUS=FULL_WITNESS id=[", ORDER, ",", i, "]\n");
        break;
      else
        Print("SEED_REJECTED_AFTER_H_CHECK id=[", ORDER, ",", i, "]\n");
      fi;
    od;

    if fullHit then
      break;
    fi;
    if i mod 100 = 0 then
      Print("PROGRESS i=", i, " exp9=", countExp9,
            " noncomm=", countNoncomm,
            " central_C_in_S=", countCContained,
            " projected_subgroup=", countProjectedSubgroup,
            " fibre_gate=", countFibreGate, "\n");
    fi;
  od;

  if fullHit then
    Print("COMPLETE_SCAN=no reason=stopped_at_full_witness\n");
  else
    Print("COMPLETE_SCAN=yes groups=", nr,
          " exp9=", countExp9,
          " noncomm_cube_seed=", countNoncomm,
          " central_C_in_S=", countCContained,
          " projected_subgroup=", countProjectedSubgroup,
          " fibre_gate=", countFibreGate,
          " seed_hits=", seedHits, "\n");
    Print("STATUS=NO_SEED_IN_ORDER_2187_LAYER\n");
  fi;
fi;

QUIT;
