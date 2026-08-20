# Deterministic structural precursor for a possible order-512 minimal
# counterexample.  Exhaustively scans SmallGroup(256,id).  The filters before
# HasSMPExact are proved necessary consequences of SMP, so the SMP catalogue
# remains complete.  Quotient-specific conditions are applied only after an
# exact SMP pass and are reported separately as PARENT_ELIGIBLE.

HasSMPExact := function(G)
  local irr, signatures, sig, i, j;
  # Garonzi--Marion, Proposition 2.1: <x>^G is the intersection of
  # the irreducible-character kernels containing x.  Thus the Boolean
  # kernel-containment column below is an exact normal-closure signature.
  irr := Irr(G);
  signatures := [];
  for i in [1..NrConjugacyClasses(G)] do
    sig := [];
    for j in [1..Length(irr)] do
      Add(sig, irr[j][i] = irr[j][1]);
    od;
    if sig in signatures then
      return false;
    fi;
    Add(signatures, sig);
  od;
  return true;
end;

PassesRationalGeneratorFilter := function(G)
  local reps, x, ox;
  reps := List(ConjugacyClasses(G), Representative);
  for x in reps do
    ox := Order(x);
    if not IsConjugate(G, x, x^-1) then
      return false;
    fi;
    # For a cyclic 2-group of order at least 8, -1 and 3 generate the unit
    # group modulo ox.  Thus inverse- and cube-conjugacy test rationality.
    if ox >= 8 and not IsConjugate(G, x, x^3) then
      return false;
    fi;
  od;
  return true;
end;

ord := 256;
total := NumberSmallGroups(ord);
if not IsBound(idfirst) then idfirst := 1; fi;
if not IsBound(idlast) then idlast := total; fi;
if idfirst < 1 or idlast > total or idfirst > idlast then
  Error("invalid inclusive ID range");
fi;
metabelian := 0;
elementaryab := 0;
derivedexp := 0;
rationalfilter := 0;
testedsmp := 0;
smpids := [];
parentids := [];
Print("GAP_VERSION=", GAPInfo.Version, "\n");
Print("ORDER=", ord, " NUMBER_SMALL_GROUPS=", total,
      " ID_RANGE=", [idfirst, idlast], "\n");
for id in [idfirst..idlast] do
  G := SmallGroup(ord, id);
  D := DerivedSubgroup(G);
  if IsAbelian(D) then
    metabelian := metabelian + 1;
    abinv := AbelianInvariants(G/D);
    if ForAll(abinv, n -> n = 2) then
      elementaryab := elementaryab + 1;
      if Exponent(D) <= 8 then
        derivedexp := derivedexp + 1;
        if PassesRationalGeneratorFilter(G) then
          rationalfilter := rationalfilter + 1;
          testedsmp := testedsmp + 1;
          if HasSMPExact(G) then
            Add(smpids, id);
            cls := NilpotencyClassOfGroup(G);
            ZG := Centre(G);
            gexp := Exponent(G);
            order16centerpass := true;
            if gexp = 16 then
              order16centerpass := Size(ZG) = 2;
              if order16centerpass then
                for x in List(ConjugacyClasses(G), Representative) do
                  if Order(x) = 16 and not x^8 in ZG then
                    order16centerpass := false;
                    break;
                  fi;
                od;
              fi;
            fi;
            d := Length(abinv);
            # A possible order-512 minimal counterexample cannot have d=6.
            # If K=G' has order 8, then K is D8 or Q8.  With
            # C=C_G(K), M=KC is an index-two class-2 subgroup, M/Z(G) is
            # elementary abelian, and conjugation by an element outside M
            # induces an involutive isometry on M/Z(G).  Its displacement
            # space is K/Z(G), hence must be totally isotropic, whereas the
            # commutator form on K/Z(G) is nondegenerate.  Contradiction.
            d6structuralpass := d <> 6;
            dm := LogInt(Size(D), 2);
            drank := Length(AbelianInvariants(D));
            shapepairs := [];
            if drank >= 2 then
              for r in [1..QuoInt(drank, 2)] do
                b := dm - 2*r;
                if b >= 0 and b <= d and (d-b) mod 2 = 0 then
                  Add(shapepairs, [r, b]);
                fi;
              od;
            fi;
            coarseparent := d >= 3 and cls >= 3 and gexp <= 16
                            and order16centerpass and d6structuralpass
                            and dm = 8-d
                            and not IsCyclic(D)
                            and Exponent(ZG) = 2
                            and Length(shapepairs) > 0;
            shapewitnesses := [];
            if coarseparent then
              normals := NormalSubgroups(G);
              for np in [1..Length(normals)] do
                B := normals[np];
                if IsSubgroup(D, B) and IsSubgroup(Centre(D), B) then
                  b := LogInt(Size(B), 2);
                  if b <= d and (d-b) mod 2 = 0 then
                    qinv := AbelianInvariants(FactorGroup(D, B));
                    if Length(qinv) > 0 and Length(qinv) mod 2 = 0
                       and ForAll(qinv, n -> n = 2) then
                      Add(shapewitnesses, [np, b, Length(qinv)]);
                    fi;
                  fi;
                fi;
              od;
            fi;
            parenteligible := coarseparent and Length(shapewitnesses) > 0;
            Print("SMP_ID=", id,
                  " CLASS=", cls,
                  " GROUP_EXPONENT=", gexp,
                  " ORDER16_CENTER_PASS=", order16centerpass,
                  " D6_STRUCTURAL_PASS=", d6structuralpass,
                  " ABELIANIZATION_INVARIANTS=", abinv,
                  " DERIVED_ORDER=", Size(D),
                  " DERIVED_INVARIANTS=", AbelianInvariants(D),
                  " DERIVED_EXPONENT=", Exponent(D),
                  " CENTER_ORDER=", Size(ZG),
                  " CENTER_INVARIANTS=", AbelianInvariants(ZG),
                  " CENTRAL_TYPE_SHAPE_PAIRS_R_B=", shapepairs,
                  " CENTRAL_TYPE_NORMAL_WITNESSES_POS_B_RANK=", shapewitnesses,
                  " PARENT_ELIGIBLE=", parenteligible, "\n");
            if parenteligible then
              Add(parentids, id);
            fi;
          fi;
        fi;
      fi;
    fi;
  fi;
  if (id-idfirst+1) mod 5000 = 0 then
    Print("CHECKPOINT_ID=", id, " METABELIAN_SO_FAR=", metabelian,
          " ELEMENTARY_AB_SO_FAR=", elementaryab,
          " DERIVED_EXP_SO_FAR=", derivedexp,
          " RATIONAL_FILTER_SO_FAR=", rationalfilter,
          " TESTED_SMP_SO_FAR=", testedsmp,
          " SMP_SO_FAR=", Length(smpids),
          " PARENT_ELIGIBLE_SO_FAR=", Length(parentids), "\n");
  fi;
od;
Print("METABELIAN_TOTAL=", metabelian,
      " ELEMENTARY_AB_TOTAL=", elementaryab,
      " DERIVED_EXP_TOTAL=", derivedexp,
      " RATIONAL_FILTER_TOTAL=", rationalfilter,
      " TESTED_SMP_TOTAL=", testedsmp,
      " SMP_COUNT=", Length(smpids),
      " PARENT_ELIGIBLE_COUNT=", Length(parentids), "\n");
Print("SMP_IDS=", smpids, "\n");
Print("PARENT_ELIGIBLE_IDS=", parentids, "\n");
QUIT;
