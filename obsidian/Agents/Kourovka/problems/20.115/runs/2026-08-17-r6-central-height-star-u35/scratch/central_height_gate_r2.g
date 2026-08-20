SetUserPreference("UseColor", false);
LogTo("Agents/Kourovka/problems/20.115/runs/2026-08-17-r6-central-height-star-u35/scratch/central_height_gate.out");

Print("BEGIN R6_CENTRAL_HEIGHT_STAR_U35\n");
Print("GAP_VERSION=", GAPInfo.Version, "\n");

LoadPackage("CTblLib");
t := CharacterTable("3.U3(5)");
if t = fail then
  Error("ordinary table 3.U3(5) unavailable");
fi;
if Identifier(t) <> "3.U3(5)" or Size(t) <> 378000 then
  Error("wrong ordinary table identity");
fi;

p := 3;
pb := PrimeBlocks(t,p);
irr := Irr(t);
ords := OrdersClassRepresentatives(t);
names := ClassNames(t);
blocks := [1..Length(pb.defect)];

Print("TABLE_IDENTIFIER=", Identifier(t), "\n");
Print("TABLE_ORDER=", Size(t), "\n");
Print("BLOCK_VECTOR=", pb.block, "\n");
Print("BLOCK_DEFECTS=", pb.defect, "\n");
Print("CHARACTER_HEIGHTS=", pb.height, "\n");
Print("NUMBER_BLOCKS=", Length(blocks), "\n");

noncentral3 := Filtered([1..Length(ords)], i -> ords[i] = 3 and i > 3);
if Length(noncentral3) <> 1 then
  Error("noncentral order-three class is not unique");
fi;
c3pos := noncentral3[1];
Print("UNIQUE_NONCENTRAL_ORDER3_POS=", c3pos,
      " NAME=", names[c3pos], "\n");

g := SU(3,5);
if Size(g) <> 378000 then
  Error("SU(3,5) constructor has wrong order");
fi;
z := Centre(g);
if Size(z) <> 3 then
  Error("SU(3,5) center is not C3");
fi;
syl := SylowSubgroup(g,3);
if Size(syl) <> 27 or not IsSubgroup(syl,z) then
  Error("principal defect representative failed");
fi;

xlist := Filtered(Elements(syl), x -> Order(x) = 3 and not x in z);
if IsEmpty(xlist) then
  Error("no noncentral order-three element in fixed Sylow subgroup");
fi;
x := xlist[1];
d2 := Group(Concatenation(GeneratorsOfGroup(z),[x]));
if Size(d2) <> 9 or not IsSubgroup(d2,z) then
  Error("candidate defect-two representative does not have order nine");
fi;

Print("GROUP_ORDER=", Size(g), " CENTER_ORDER=", Size(z),
      " SYLOW3_ORDER=", Size(syl), "\n");
Print("CENTER_GENERATORS=", GeneratorsOfGroup(z), "\n");
Print("SYLOW3_GENERATORS=", GeneratorsOfGroup(syl), "\n");
Print("DEFECT2_GENERATORS=", GeneratorsOfGroup(d2), "\n");

allpass := true;
for b in blocks do
  rows := Positions(pb.block,b);
  d := pb.defect[b];
  if d = 3 then
    db := syl;
    cert := "principal Sylow 3-subgroup";
  elif d = 2 then
    support := Filtered(rows, r -> irr[r][c3pos] <> 0);
    if IsEmpty(support) then
      Error("defect-two block lacks Theorem-3.5 support on unique 3-class");
    fi;
    db := d2;
    cert := Concatenation("Theorem 3.5 support rows ", String(support));
  elif d = 1 then
    db := z;
    cert := "central C3 contained in every defect group";
  else
    Error("unexpected block defect; explicit representative unavailable");
  fi;
  if Size(db) <> 3^d or not IsSubgroup(db,z) then
    Error("explicit representative has wrong size or misses center");
  fi;
  q := FactorGroup(db,z);
  qexp := Exponent(q);
  threshold := Size(q)/qexp;
  Print("BLOCK=", b, " ROWS=", rows, " DEFECT=", d,
        " D_SIZE=", Size(db), " DZ_SIZE=", Size(q),
        " DZ_EXPONENT=", qexp, " THRESHOLD=", threshold,
        " CERT=", cert, "\n");
  for r in rows do
    lhs := 3^pb.height[r];
    pass := lhs <= threshold;
    Print("ROW=", r, " BLOCK=", b, " DEGREE=", irr[r][1],
          " HEIGHT=", pb.height[r], " HEIGHT_POWER=", lhs,
          " THRESHOLD=", threshold, " PASS=", pass, "\n");
    if not pass then
      allpass := false;
    fi;
  od;
od;

Print("ALL_HEIGHT_THRESHOLDS_PASS=", allpass, "\n");
Print("END R6_CENTRAL_HEIGHT_STAR_U35\n");
LogTo();
QUIT_GAP(0);
