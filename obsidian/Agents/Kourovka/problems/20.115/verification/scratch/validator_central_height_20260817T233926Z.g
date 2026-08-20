SetUserPreference("UseColor", false);
LogTo("Agents/Kourovka/problems/20.115/verification/scratch/validator_central_height_20260817T233926Z.out");

Print("BEGIN VALIDATOR_SU35_CENTRAL_HEIGHT\n");
Print("GAP_VERSION=", GAPInfo.Version, "\n");

ValuationAt := function(n, p)
  local v;
  v := 0;
  while n mod p = 0 do
    n := QuoInt(n, p);
    v := v + 1;
  od;
  return v;
end;

if LoadPackage("CTblLib") <> true then
  Error("CTblLib did not load");
fi;

p := 3;
t := CharacterTable("3.U3(5)");
if t = fail then
  Error("ordinary table unavailable");
fi;
if Identifier(t) <> "3.U3(5)" or Size(t) <> 378000 then
  Error("ordinary table identity gate failed");
fi;

irr := Irr(t);
degs := List(irr, chi -> chi[1]);
if Length(irr) <> 40 or Sum(List(degs, n -> n^2)) <> Size(t) then
  Error("ordinary character degree completeness gate failed");
fi;

pb := PrimeBlocks(t, p);
expectedBlock := [ 1,1,2,1,1,1,2,2,1,3,4,5,6,7,1,1,2,2,1,1,
                   1,1,1,1,2,2,1,1,2,2,3,3,4,4,5,5,6,6,7,7 ];
expectedDefect := [ 3,2,1,1,1,1,1 ];
expectedHeight := [ 0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,
                    1,1,1,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0 ];
if pb.block <> expectedBlock then
  Error("submitted block membership does not replicate");
fi;
if pb.defect <> expectedDefect then
  Error("submitted block defects do not replicate");
fi;
if pb.height <> expectedHeight then
  Error("submitted heights do not replicate");
fi;

a := ValuationAt(Size(t), p);
if a <> 3 then
  Error("wrong 3-part of table order");
fi;

for b in [1..Length(pb.defect)] do
  rows := Positions(pb.block, b);
  derivedDefect := Maximum(List(rows, r -> a - ValuationAt(degs[r], p)));
  if derivedDefect <> pb.defect[b] then
    Error("defect is inconsistent with ordinary degrees");
  fi;
  for r in rows do
    derivedHeight := ValuationAt(degs[r], p) - (a - derivedDefect);
    if derivedHeight <> pb.height[r] then
      Error("height is inconsistent with degree and defect");
    fi;
  od;
od;

classOrders := OrdersClassRepresentatives(t);
classSizes := SizesConjugacyClasses(t);
centralPositions := Positions(classSizes, 1);
noncentralOrderThree := Filtered([1..Length(classOrders)],
  i -> classOrders[i] = 3 and classSizes[i] > 1);
if centralPositions <> [1,2,3] then
  Error("the three center classes are not exactly table positions 1,2,3");
fi;
if noncentralOrderThree <> [7] then
  Error("noncentral order-three class is not uniquely position 7");
fi;
c3pos := noncentralOrderThree[1];
block2rows := Positions(pb.block, 2);
support := Filtered(block2rows, r -> not IsZero(irr[r][c3pos]));
if support <> [3,7,8] then
  Error("exact block-2 support on the noncentral order-three class changed");
fi;

g := SU(3,5);
if Size(g) <> 378000 then
  Error("SU(3,5) group order gate failed");
fi;

zmat := [
  [ Z(5^2)^16, 0*Z(5), 0*Z(5) ],
  [ 0*Z(5), Z(5^2)^16, 0*Z(5) ],
  [ 0*Z(5), 0*Z(5), Z(5^2)^16 ]
];

d1g1 := [
  [ Z(5^2)^8, 0*Z(5), 0*Z(5) ],
  [ 0*Z(5), Z(5^2)^8, 0*Z(5) ],
  [ 0*Z(5), 0*Z(5), Z(5^2)^8 ]
];
d1g2 := [
  [ Z(5^2)^20, Z(5^2)^16, Z(5)^2 ],
  [ Z(5), Z(5^2)^20, Z(5^2)^15 ],
  [ Z(5^2)^16, Z(5^2), Z(5^2)^14 ]
];
d1g3 := [
  [ Z(5^2)^8, Z(5)^2, Z(5^2) ],
  [ Z(5^2)^10, Z(5^2)^2, Z(5^2)^8 ],
  [ Z(5^2)^9, Z(5^2)^14, Z(5^2)^8 ]
];
xmat := [
  [ Z(5)^0, Z(5)^0, Z(5^2)^13 ],
  [ Z(5), Z(5)^3, Z(5^2)^20 ],
  [ Z(5^2)^5, Z(5^2)^10, Z(5)^0 ]
];

submittedMatrices := [ zmat, d1g1, d1g2, d1g3, xmat ];
if not ForAll(submittedMatrices, m -> m in g) then
  Error("at least one submitted matrix is not in SU(3,5)");
fi;
if List(submittedMatrices, Order) <> [3,3,3,3,3] then
  Error("a submitted matrix has unexpected order");
fi;

z := Group([zmat]);
zg := Centre(g);
if Size(zg) <> 3 or Size(z) <> 3 or not IsSubgroup(zg, z) then
  Error("submitted central generator does not generate the full center");
fi;

d1 := Group([d1g1,d1g2,d1g3]);
if Size(d1) <> 27 or not IsSubgroup(g, d1) or not IsSubgroup(d1, z) then
  Error("submitted principal defect representative failed");
fi;
q1 := FactorGroup(d1, z);
if Size(q1) <> 9 or Exponent(q1) <> 3 then
  Error("principal defect quotient failed");
fi;

if xmat in z then
  Error("submitted x is central");
fi;
d2 := Group([zmat,xmat]);
if Size(d2) <> 9 or not IsSubgroup(g, d2) or not IsSubgroup(d2, z) then
  Error("submitted defect-two representative failed");
fi;
q2 := FactorGroup(d2, z);
if Size(q2) <> 3 or Exponent(q2) <> 3 then
  Error("defect-two quotient failed");
fi;

qz := FactorGroup(z, z);
if Size(qz) <> 1 or Exponent(qz) <> 1 then
  Error("central defect quotient failed");
fi;

thresholds := [ Size(q1)/Exponent(q1), Size(q2)/Exponent(q2),
                Size(qz)/Exponent(qz), Size(qz)/Exponent(qz),
                Size(qz)/Exponent(qz), Size(qz)/Exponent(qz),
                Size(qz)/Exponent(qz) ];
if thresholds <> [3,1,1,1,1,1,1] then
  Error("threshold vector changed");
fi;

Print("TABLE=", Identifier(t), " ORDER=", Size(t),
      " CHARACTERS=", Length(irr), " ORDER_3_VALUATION=", a, "\n");
Print("BLOCK_VECTOR=", pb.block, "\n");
Print("DEFECT_VECTOR=", pb.defect, "\n");
Print("HEIGHT_VECTOR=", pb.height, "\n");
Print("CENTER_CLASS_POSITIONS=", centralPositions,
      " UNIQUE_NONCENTRAL_ORDER3=", noncentralOrderThree, "\n");
Print("BLOCK2_ORDER3_SUPPORT=", support, " VALUES=",
      List(support, r -> irr[r][c3pos]), "\n");
Print("GROUP_ORDER=", Size(g), " CENTER_ORDER=", Size(zg),
      " QUOTIENT_ORDER=", Size(g)/Size(zg), "\n");
Print("SUBMITTED_MATRIX_ORDERS=", List(submittedMatrices, Order), "\n");
Print("D1_ORDER=", Size(d1), " D1Z_ORDER=", Size(q1),
      " D1Z_EXPONENT=", Exponent(q1), "\n");
Print("D2_ORDER=", Size(d2), " D2Z_ORDER=", Size(q2),
      " D2Z_EXPONENT=", Exponent(q2), "\n");
Print("D3_TO_D7_ORDER=", Size(z), " QUOTIENT_ORDER=", Size(qz),
      " QUOTIENT_EXPONENT=", Exponent(qz), "\n");

rowCount := 0;
allPass := true;
for b in [1..Length(pb.defect)] do
  rows := Positions(pb.block, b);
  derivedDefect := Maximum(List(rows, r -> a - ValuationAt(degs[r], p)));
  Print("BLOCK=", b, " ROWS=", rows, " DEFECT=", derivedDefect,
        " THRESHOLD=", thresholds[b], "\n");
  for r in rows do
    derivedHeight := ValuationAt(degs[r], p) - (a - derivedDefect);
    pass := p^derivedHeight <= thresholds[b];
    Print("ROW=", r, " BLOCK=", b, " DEGREE=", degs[r],
          " V3_DEGREE=", ValuationAt(degs[r], p),
          " DERIVED_HEIGHT=", derivedHeight,
          " HEIGHT_POWER=", p^derivedHeight,
          " THRESHOLD=", thresholds[b], " PASS=", pass, "\n");
    rowCount := rowCount + 1;
    allPass := allPass and pass;
  od;
od;

if rowCount <> 40 or not allPass then
  Error("forty-row threshold audit failed");
fi;
Print("ROW_COUNT=", rowCount, " ALL_THRESHOLDS_PASS=", allPass, "\n");
Print("END VALIDATOR_SU35_CENTRAL_HEIGHT\n");
LogTo();
QUIT_GAP(0);
