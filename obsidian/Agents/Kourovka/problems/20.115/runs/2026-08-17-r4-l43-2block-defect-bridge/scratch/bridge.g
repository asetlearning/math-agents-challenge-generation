LoadPackage("ctbllib");

p := 2;
tbl := CharacterTable("L4(3)");
irr := Irr(tbl);
pb := PrimeBlocks(tbl, p);
names := ClassNames(tbl);
orders := OrdersClassRepresentatives(tbl);
cents := SizesCentralizers(tbl);

# GAP's standard degree-40 permutation realization of PSL(4,3).
g := PSL(4,3);
syl := SylowSubgroup(g, p);
sylgens := SmallGeneratingSet(syl);

# The unique table class of order four and centralizer order 1440 is 4a.
pos4a := Filtered([1 .. Length(orders)],
                  j -> orders[j] = 4 and cents[j] = 1440);

# Every 2-element class meets a Sylow 2-subgroup.  Locate a concrete 4a
# representative in this fixed Sylow subgroup by the class invariant above.
x4a := fail;
for y in Elements(syl) do
  if Order(y) = 4 and Size(Centralizer(g, y)) = 1440 then
    x4a := y;
    break;
  fi;
od;
if x4a = fail then
  Error("no explicit 4a representative found in the fixed Sylow subgroup");
fi;

d2 := Subgroup(g, [x4a]);
triv := TrivialSubgroup(g);
defectgroups := [syl, d2, triv, triv, triv, triv];
defectprintgens := [sylgens, [x4a], [], [], [], []];
defectexponents := List(defectgroups, Exponent);

Print("GAP_VERSION=", GAPInfo.Version, "\n");
Print("CTBLLIB_VERSION=", InstalledPackageVersion("ctbllib"), "\n");
Print("TABLE_ID=", Identifier(tbl), " TABLE_ORDER=", Size(tbl),
      " TABLE_NIRR=", Length(irr), "\n");
Print("GROUP_CONSTRUCTOR=PSL(4,3) GROUP_ORDER=", Size(g),
      " PERM_DEGREE=", LargestMovedPoint(g),
      " CENTER_SIZE=", Size(Center(g)),
      " IS_SIMPLE=", IsSimpleGroup(g), "\n");
for i in [1 .. Length(GeneratorsOfGroup(g))] do
  Print("GROUP_GENERATOR ", i, " = ", GeneratorsOfGroup(g)[i], "\n");
od;

Print("BLOCK_ASSIGNMENT=", pb.block, "\n");
Print("BLOCK_DEFECTS=", pb.defect, "\n");
Print("BLOCK_HEIGHTS=", pb.height, "\n");
Print("CLASS4A_UNIQUENESS_POSITIONS=", pos4a,
      " NAME=", names[pos4a[1]],
      " ORDER=", orders[pos4a[1]],
      " CENTRALIZER=", cents[pos4a[1]], "\n");
Print("BLOCK2_SUPPORT_ROW=16 CLASS_POS=", pos4a[1],
      " VALUE=", irr[16][pos4a[1]], " NONZERO=", irr[16][pos4a[1]] <> 0,
      "\n");

for b in [1 .. Length(pb.defect)] do
  Print("BLOCK ", b,
        " DEFECT=", pb.defect[b],
        " ORDINARY_ROWS=", Positions(pb.block, b),
        " D_SIZE=", Size(defectgroups[b]),
        " D_EXPONENT=", defectexponents[b], "\n");
  for i in [1 .. Length(defectprintgens[b])] do
    Print("BLOCK ", b, " DEFECT_GENERATOR ", i, " = ",
          defectprintgens[b][i], "\n");
  od;
  Print("BLOCK ", b, " PRINTED_GENERATORS_RECONSTRUCT_SIZE=",
        Size(Subgroup(g, defectprintgens[b])), "\n");
od;

Print("BLOCK2_GENERATOR_CLASS_CHECK ORDER=", Order(x4a),
      " CENTRALIZER=", Size(Centralizer(g, x4a)),
      " GENERATOR=", x4a, "\n");

Print("ROW_DATA_BEGIN\n");
allpass := true;
for i in [1 .. Length(irr)] do
  b := pb.block[i];
  degree := irr[i][1];
  chardef := PValuation(Size(tbl) / degree, p);
  bound := p^chardef;
  pass := defectexponents[b] <= bound;
  allpass := allpass and pass;
  Print("ROW=", i,
        " BLOCK=", b,
        " DEGREE=", degree,
        " V2_DEGREE=", PValuation(degree, p),
        " CHAR_2_DEFECT=", chardef,
        " TWO_POWER_BOUND=", bound,
        " D_EXPONENT=", defectexponents[b],
        " PASS=", pass, "\n");
od;
Print("ROW_DATA_END\n");
Print("ALL_BLOCK_EXPONENT_VS_CHARACTER_DEFECT_PASS=", allpass, "\n");
QUIT;
