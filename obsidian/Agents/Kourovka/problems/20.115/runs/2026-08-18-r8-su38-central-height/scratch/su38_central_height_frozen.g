SetUserPreference("UseColor", false);
LogTo("Agents/Kourovka/problems/20.115/runs/2026-08-18-r8-su38-central-height/scratch/su38_central_height_frozen.out");

Print("BEGIN_SU38_CENTRAL_HEIGHT_FROZEN\n");
Print("GAP_VERSION=", GAPInfo.Version, "\n");

Gate := function(condition, message)
  if not condition then
    Print("FATAL_GATE=", message, "\n");
    LogTo();
    QUIT_GAP(1);
  fi;
end;

ValuationAt := function(n, p)
  local v;
  v := 0;
  while n mod p = 0 do
    n := QuoInt(n,p);
    v := v + 1;
  od;
  return v;
end;

Gate(LoadPackage("ctbllib") = true, "CTblLib unavailable");
Print("CTBLLIB_VERSION=", InstalledPackageVersion("ctbllib"), "\n");

p := 3;
q := 8;
t := CharacterTable("3.U3(8)");
Gate(t <> fail, "ordinary table 3.U3(8) unavailable");
Gate(Identifier(t) = "3.U3(8)", "ordinary table identifier mismatch");
Gate(Size(t) = 16547328, "ordinary table order mismatch");

irr := Irr(t);
degs := List(irr, chi -> chi[1]);
Gate(Length(irr) = 82, "ordinary character count mismatch");
Gate(Sum(List(degs, n -> n^2)) = Size(t),
     "ordinary degree completeness mismatch");

pb := PrimeBlocks(t,p);
Gate(pb <> fail, "ordinary 3-block data unavailable");
expectedDefects := [5,2,2,2,1,1,1,1,1,1];
Gate(pb.defect = expectedDefects, "3-block defect vector mismatch");
Gate(Length(pb.block) = Length(irr), "3-block membership length mismatch");
Gate(Set(pb.block) = [1..10], "3-block labels incomplete");
Gate(Length(pb.height) = Length(irr), "3-block height vector incomplete");

a := ValuationAt(Size(t),p);
Gate(a = 5, "wrong 3-valuation of group order");
Gate(ValuationAt(q+1,p) = 2, "wrong v3(q+1)");

orders := OrdersClassRepresentatives(t);
sizes := SizesConjugacyClasses(t);
names := ClassNames(t);
centralPositions := Positions(sizes,1);
Gate(centralPositions = [1,2,3], "center-class positions mismatch");
Gate(List(centralPositions, c -> orders[c]) = [1,3,3],
     "center-class orders mismatch");

candidatePositions := Filtered([1..Length(orders)],
  c -> orders[c] = 9 and Size(t)/sizes[c] = 4536);
Gate(candidatePositions = [7,8,9,10,11,12],
     "order-nine repeated-eigenvalue class gate failed");
for b in [2..4] do
  for c in candidatePositions do
    support := Filtered(Positions(pb.block,b),
                        r -> not IsZero(irr[r][c]));
    Gate(Length(support) > 0,
         Concatenation("empty defect-two support: block ",String(b),
                       " class ",String(c)));
  od;
od;

L := SU(3,q);
Cen := Center(L);
Gate(Size(L) = Size(t), "SU(3,8) and table orders disagree");
Gate(Size(L) = q^3*(q^3+1)*(q^2-1), "SU3 order formula mismatch");
Gate(Size(Cen) = Gcd(3,q+1), "SU3 center formula mismatch");
Gate(Size(Cen) = 3, "central subgroup is not C3");

P := SylowSubgroup(L,p);
Gate(Size(P) = 3^a, "principal defect representative is not Sylow");
Gate(IsSubgroup(P,Cen), "center is not contained in chosen Sylow subgroup");
Q1 := FactorGroup(P,Cen);
Gate(Size(Q1) = 81, "principal defect quotient order mismatch");
Gate(Exponent(Q1) = 9, "principal defect quotient exponent mismatch");

F := GF(q^2);
cyclicCandidates := Filtered(Elements(P), y ->
  Order(y) = 9 and
  Degree(MinimalPolynomial(F,y)) = 2 and
  y^3 in Cen and y^3 <> One(L));
Gate(Length(cyclicCandidates) = 18,
     "unexpected repeated-eigenvalue order-nine candidates");
x := cyclicCandidates[1];
D2 := Group([x]);
Gate(x in L, "cyclic defect representative is not in SU(3,8)");
Gate(Size(D2) = 9, "cyclic defect representative has wrong order");
Gate(IsSubgroup(D2,Cen), "center is not contained in cyclic representative");
Q2 := FactorGroup(D2,Cen);
Gate(Size(Q2) = 3, "defect-two quotient order mismatch");
Gate(Exponent(Q2) = 3, "defect-two quotient exponent mismatch");

QZ := FactorGroup(Cen,Cen);
Gate(Size(QZ) = 1 and Exponent(QZ) = 1,
     "central defect quotient mismatch");

thresholds := [Size(Q1)/Exponent(Q1),
               Size(Q2)/Exponent(Q2),
               Size(Q2)/Exponent(Q2),
               Size(Q2)/Exponent(Q2),
               Size(QZ)/Exponent(QZ),
               Size(QZ)/Exponent(QZ),
               Size(QZ)/Exponent(QZ),
               Size(QZ)/Exponent(QZ),
               Size(QZ)/Exponent(QZ),
               Size(QZ)/Exponent(QZ)];
Gate(thresholds = [9,1,1,1,1,1,1,1,1,1],
     "defect quotient threshold vector mismatch");

Print("TABLE_ID=", Identifier(t), " TABLE_ORDER=", Size(t),
      " NR_IRR=", Length(irr), " ORDER_3_VALUATION=", a,
      " V3_QPLUS1=", ValuationAt(q+1,p), "\n");
Print("BLOCK_VECTOR=", pb.block, "\n");
Print("DEFECT_VECTOR=", pb.defect, "\n");
Print("STORED_HEIGHT_VECTOR=", pb.height, "\n");
Print("CENTER_CLASS_POSITIONS=", centralPositions,
      " CENTER_CLASS_NAMES=", List(centralPositions,c -> names[c]), "\n");
Print("CYCLIC_DEFECT_CLASS_POSITIONS=", candidatePositions,
      " CLASS_NAMES=", List(candidatePositions,c -> names[c]), "\n");
for b in [2..4] do
  for c in candidatePositions do
    support := Filtered(Positions(pb.block,b),
                        r -> not IsZero(irr[r][c]));
    Print("DEFECT2_SUPPORT BLOCK=", b, " CLASS_POS=", c,
          " CLASS_NAME=", names[c], " ROWS=", support,
          " VALUES=", List(support,r -> irr[r][c]), "\n");
  od;
od;
Print("MATRIX_GROUP_ORDER=", Size(L), " CENTER_ORDER=", Size(Cen),
      " QUOTIENT_ORDER=", Size(L)/Size(Cen), "\n");
Print("CENTER_GENERATORS=", GeneratorsOfGroup(Cen), "\n");
Print("PRINCIPAL_DEFECT_GENERATORS=", GeneratorsOfGroup(P), "\n");
Print("D1_ORDER=", Size(P), " D1_MOD_CENTER_ORDER=", Size(Q1),
      " D1_MOD_CENTER_EXPONENT=", Exponent(Q1), "\n");
Print("CYCLIC_CANDIDATE_COUNT=", Length(cyclicCandidates), "\n");
Print("D2_GENERATOR=", x, "\n");
Print("D2_MINPOLY=", MinimalPolynomial(F,x),
      " D2_GENERATOR_CUBE=", x^3, "\n");
Print("D2_ORDER=", Size(D2), " D2_MOD_CENTER_ORDER=", Size(Q2),
      " D2_MOD_CENTER_EXPONENT=", Exponent(Q2), "\n");
Print("D5_TO_D10_ORDER=", Size(Cen),
      " QUOTIENT_ORDER=", Size(QZ),
      " QUOTIENT_EXPONENT=", Exponent(QZ), "\n");
Print("THRESHOLD_VECTOR=", thresholds, "\n");

rowCount := 0;
allPass := true;
for b in [1..Length(pb.defect)] do
  rows := Positions(pb.block,b);
  derivedDefect := Maximum(List(rows,
    r -> a-ValuationAt(degs[r],p)));
  Gate(derivedDefect = pb.defect[b],
       Concatenation("degree-derived defect mismatch in block ",String(b)));
  Print("BLOCK=", b, " ROWS=", rows, " DEFECT=", derivedDefect,
        " QUOTIENT_EXPONENT=",
        [Exponent(Q1),Exponent(Q2),Exponent(Q2),Exponent(Q2),
         Exponent(QZ),Exponent(QZ),Exponent(QZ),Exponent(QZ),
         Exponent(QZ),Exponent(QZ)][b],
        " THRESHOLD=", thresholds[b], "\n");
  for r in rows do
    derivedHeight := ValuationAt(degs[r],p)-(a-derivedDefect);
    Gate(derivedHeight = pb.height[r],
         Concatenation("degree-derived height mismatch at row ",String(r)));
    pass := p^derivedHeight <= thresholds[b];
    Print("ROW=", r, " BLOCK=", b, " DEGREE=", degs[r],
          " V3_DEGREE=", ValuationAt(degs[r],p),
          " DERIVED_HEIGHT=", derivedHeight,
          " HEIGHT_POWER=", p^derivedHeight,
          " THRESHOLD=", thresholds[b], " PASS=", pass, "\n");
    rowCount := rowCount + 1;
    allPass := allPass and pass;
  od;
od;

Gate(rowCount = 82, "ordinary row audit incomplete");
Gate(allPass, "at least one central-height threshold failed");
Print("ROW_COUNT=", rowCount, " ALL_THRESHOLDS_PASS=", allPass, "\n");
Print("END_SU38_CENTRAL_HEIGHT_FROZEN\n");
LogTo();
QUIT_GAP(0);
