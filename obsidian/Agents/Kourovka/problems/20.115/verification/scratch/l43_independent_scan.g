# Independent bounded validator for the ordinary CTblLib table L4(3).
# This implementation does not read or invoke the claimant's GAP script.

if LoadPackage("ctbllib") <> true then
  Error("CTblLib could not be loaded");
fi;

t := CharacterTable("L4(3)");
if t = fail then
  Error("ordinary library table L4(3) is unavailable");
fi;

chars := Irr(t);
orders := OrdersClassRepresentatives(t);
sizes := SizesConjugacyClasses(t);
nrows := Length(chars);
nclasses := Length(orders);
gorder := Size(t);
formulaOrder := QuoInt(3^6 * (3^2-1) * (3^3-1) * (3^4-1), Gcd(4,3-1));

if not IsOrdinaryTable(t) or UnderlyingCharacteristic(t) <> 0 then
  Error("the requested table is not ordinary");
fi;
if nrows <> 29 or nclasses <> 29 then
  Error("unexpected table dimensions");
fi;
if gorder <> formulaOrder or Sum(sizes) <> gorder then
  Error("order or class-size consistency failure");
fi;
if Set(ClassPositionsOfCenter(t)) <> [1] then
  Error("unexpected center classes");
fi;
if not ForAll(chars, x -> ScalarProduct(t,x,x) = 1) then
  Error("an Irr row is not norm one");
fi;
degreeSquareSum := Sum(List(chars,x->x[1]^2));
if degreeSquareSum <> gorder then
  Error("irreducible degree-square sum does not equal the group order");
fi;
for a in [1..nrows] do
  for b in [a+1..nrows] do
    if ScalarProduct(t,chars[a],chars[b]) <> 0 then
      Error("distinct Irr rows are not orthogonal");
    fi;
  od;
od;

pairCount := 0;
nonzeroCount := 0;
violationCount := 0;
allValuesCyclotomic := true;
rowNonzero := List([1..nrows], x -> 0);
classNonzero := List([1..nclasses], x -> 0);
nonzeroPatterns := [];
violations := [];

for r in [1..nrows] do
  degree := chars[r][1];
  rowPattern := "";
  if not IsPosInt(degree) then
    Error("non-positive or non-integral character degree");
  fi;
  for c in [1..nclasses] do
    pairCount := pairCount + 1;
    v := chars[r][c];
    if not IsCyc(v) then
      allValuesCyclotomic := false;
    fi;
    isNonzero := not IsZero(v);
    if isNonzero then
      Add(rowPattern,'1');
    else
      Add(rowPattern,'0');
    fi;
    divisor := orders[c] * degree;
    dividesViaRational := IsInt(gorder / divisor);
    dividesViaRemainder := RemInt(gorder, divisor) = 0;
    if dividesViaRational <> dividesViaRemainder then
      Error("independent divisibility formulations disagree");
    fi;
    if isNonzero then
      nonzeroCount := nonzeroCount + 1;
      rowNonzero[r] := rowNonzero[r] + 1;
      classNonzero[c] := classNonzero[c] + 1;
      if not dividesViaRational then
        violationCount := violationCount + 1;
        Add(violations,[r,c,degree,orders[c],v,divisor]);
      fi;
    fi;
  od;
  Add(nonzeroPatterns,rowPattern);
od;

Print("GAP_VERSION ",GAPInfo.Version,"\n");
Print("CTBLLIB_VERSION ",InstalledPackageVersion("ctbllib"),"\n");
Print("IDENTIFIER ",Identifier(t),"\n");
Print("INFO_TEXT ",InfoText(t),"\n");
Print("ORDINARY ",IsOrdinaryTable(t),"\n");
Print("UNDERLYING_CHARACTERISTIC ",UnderlyingCharacteristic(t),"\n");
Print("SIMPLE_TABLE ",IsSimpleCharacterTable(t),"\n");
Print("ORDER ",gorder,"\n");
Print("PSL4_3_FORMULA_ORDER ",formulaOrder,"\n");
Print("CLASS_SIZE_SUM ",Sum(sizes),"\n");
Print("IRR_DEGREE_SQUARE_SUM ",degreeSquareSum,"\n");
Print("IRR_PAIRWISE_ORTHONORMAL true\n");
Print("CENTER_CLASS_POSITIONS ",ClassPositionsOfCenter(t),"\n");
Print("ROWS ",nrows," CLASSES ",nclasses," PAIRS ",pairCount,"\n");
Print("ALL_VALUES_CYCLOTOMIC ",allValuesCyclotomic,"\n");
Print("DEGREES ",List(chars,x->x[1]),"\n");
Print("CLASS_ORDERS ",orders,"\n");
Print("ROW_NONZERO_COUNTS ",rowNonzero,"\n");
Print("CLASS_NONZERO_COUNTS ",classNonzero,"\n");
Print("NONZERO_PATTERNS ",nonzeroPatterns,"\n");
Print("NONZERO_PAIRS ",nonzeroCount,"\n");
Print("VIOLATIONS ",violationCount,"\n");
Print("VIOLATION_DATA ",violations,"\n");

if pairCount <> nrows*nclasses or nonzeroCount <> Sum(rowNonzero)
   or nonzeroCount <> Sum(classNonzero) then
  Error("coverage/count invariant failure");
fi;
if violationCount <> Length(violations) then
  Error("violation count invariant failure");
fi;

QUIT;
