LoadPackage("ctbllib");;

p := 2;;
t := CharacterTable("L4(3)");;
bt := BrauerTable(t, p);;
irr := Irr(t);;
dm := DecompositionMatrix(bt);;

AssertTrue := function(condition, label)
  if not condition then
    Error(Concatenation("ASSERTION_FAILED: ", label));
  fi;
end;;

# Recover the blocks as connected components of the bipartite support graph of
# the decomposition matrix.  This deliberately does not use PrimeBlocks or the
# ordchars fields of BlocksInfo.
nr := Length(dm);;
nc := Length(dm[1]);;
unseen := [1 .. nr];;
components := [];;
while Length(unseen) > 0 do
  rows := [unseen[1]];;
  cols := [];;
  changed := true;;
  while changed do
    newcols := Set(Concatenation(List(rows,
      i -> Filtered([1 .. nc], j -> dm[i][j] <> 0))));;
    newrows := Filtered([1 .. nr],
      i -> ForAny(newcols, j -> dm[i][j] <> 0));;
    changed := (newrows <> rows) or (newcols <> cols);;
    rows := newrows;;
    cols := newcols;;
  od;
  Add(components, rec(rows := rows, cols := cols));
  unseen := Difference(unseen, rows);;
od;

AssertTrue(nr = 29, "ordinary row count");
AssertTrue(nc = 12, "Brauer row count");
AssertTrue(Length(components) = 6, "six support components");

# The largest elementary divisor of a block Cartan matrix is the order of a
# defect group.  Thus this reconstructs each block defect from the decomposition
# matrix, instead of reading the defect field returned by PrimeBlocks.
for b in [1 .. Length(components)] do
  rows := components[b].rows;;
  cols := components[b].cols;;
  subdm := List(rows, i -> List(cols, j -> dm[i][j]));;
  cartan := TransposedMat(subdm) * subdm;;
  elementary := ElementaryDivisorsMat(cartan);;
  defectsize := Maximum(List(elementary, AbsInt));;
  defect := LogInt(defectsize, p);;
  AssertTrue(p^defect = defectsize, Concatenation("2-power defect size B", String(b)));
  components[b].cartan := cartan;;
  components[b].elementary := elementary;;
  components[b].defect := defect;;
od;

expectedRows := [
  [1..15],
  [16..19],
  [23], [24], [25], [26]
];;
Append(expectedRows[1], [20..22]);;
Append(expectedRows[1], [27..29]);;
expectedDefects := [7, 2, 0, 0, 0, 0];;
for b in [1 .. 6] do
  AssertTrue(components[b].rows = expectedRows[b],
    Concatenation("row membership B", String(b)));
  AssertTrue(components[b].defect = expectedDefects[b],
    Concatenation("defect B", String(b)));
od;

# GAP's documented PSL constructor gives the action of PSL(4,3) on the 40
# projective lines.  Reconstruct the claimant's printed principal-defect
# certificate directly from its three permutations.
g := PSL(4,3);;
d1gens := [
  (2,10)(3,8)(4,9)(5,6)(14,15)(17,40)(18,39)(19,38)(20,26)(21,28)(22,27)(23,25)(29,36)(30,35)(31,37)(33,34),
  (2,26)(3,28)(4,27)(5,34)(6,33)(7,32)(8,21)(9,22)(10,20)(11,13)(14,15)(17,40)(18,38)(19,39)(30,31)(35,37),
  (1,39)(2,8)(3,15)(4,27)(5,11)(6,24)(7,18)(9,36)(10,33)(12,21)(13,30)(14,34)(16,35)(17,31)(19,20)(22,23)(25,29)(26,37)(28,32)(38,40)
];;
AssertTrue(ForAll(d1gens, y -> y in g), "principal generators lie in PSL(4,3)");
d1 := Group(d1gens);;

x := (1,11,12,13)(2,14,20,17)(3,35,34,39)(4,29,27,25)(5,37,28,19)(6,31,21,38)(7,16,32,24)(8,30,33,18)(9,36,22,23)(10,15,26,40);;
AssertTrue(x in g, "block-2 certificate element lies in PSL(4,3)");
AssertTrue(x in d1, "block-2 certificate element lies in displayed Sylow subgroup");

expectedOrder := 3^6 * (3^2-1) * (3^3-1) * (3^4-1) / Gcd(4,3-1);;
AssertTrue(Size(g) = expectedOrder, "PSL order formula");
AssertTrue(Size(g) = Size(t), "permutation group and ordinary table orders agree");
AssertTrue(Size(Center(g)) = 1, "centerless PSL model");
AssertTrue(IsSimpleGroup(g), "simple PSL model");
AssertTrue(Size(d1) = p^PValuation(Size(g),p), "displayed D1 is Sylow");

d1Orders := Collected(List(Elements(d1), Order));;
d1Exponent := Exponent(d1);;
AssertTrue(d1Exponent = 8, "displayed D1 exponent");

orders := OrdersClassRepresentatives(t);;
centralizers := SizesCentralizers(t);;
classNames := ClassNames(t);;
xCentralizer := Size(Centralizer(g,x));;
matchingClasses := Filtered([1 .. Length(orders)],
  j -> orders[j] = Order(x) and centralizers[j] = xCentralizer);;
AssertTrue(matchingClasses = [8], "unique table class with x invariants");
class4a := matchingClasses[1];;
AssertTrue(classNames[class4a] = "4a", "matching table class named 4a");
AssertTrue(irr[16][class4a] = 16, "row 16 nonzero on 4a");
AssertTrue(16 in components[2].rows, "row 16 lies in reconstructed block 2");
AssertTrue(Order(x) = 4, "block-2 certificate has order four");
AssertTrue(Size(Group([x])) = 4, "block-2 cyclic certificate size");

defectExponents := [d1Exponent, Order(x), 1, 1, 1, 1];;
allPass := true;;
rowBlock := [];;
for i in [1 .. nr] do
  rowBlock[i] := PositionProperty(components, c -> i in c.rows);;
od;

Print("GAP_VERSION=", GAPInfo.Version, "\n");
Print("CTBLLIB_VERSION=", InstalledPackageVersion("ctbllib"), "\n");
Print("TABLE_ID=", Identifier(t), " TABLE_ORDER=", Size(t),
      " NIRR=", Length(irr), " NBRAUER=", nc, "\n");
Print("TABLE_INFO=", InfoText(t), "\n");
Print("MODEL=PSL(4,3)_PROJECTIVE_LINES DEGREE=", LargestMovedPoint(g),
      " ORDER=", Size(g), " CENTER=", Size(Center(g)),
      " SIMPLE=", IsSimpleGroup(g), "\n");
Print("RECONSTRUCTED_BLOCK_COUNT=", Length(components), "\n");
for b in [1 .. 6] do
  Print("BLOCK=", b,
        " ORDINARY_ROWS=", components[b].rows,
        " BRAUER_COLUMNS=", components[b].cols,
        " CARTAN=", components[b].cartan,
        " ELEMENTARY_DIVISORS=", components[b].elementary,
        " DEFECT=", components[b].defect,
        " DEFECT_GROUP_EXPONENT=", defectExponents[b], "\n");
od;
Print("D1_GENERATORS_IN_G=", ForAll(d1gens, y -> y in g),
      " D1_SIZE=", Size(d1), " D1_EXPONENT=", d1Exponent,
      " D1_ELEMENT_ORDER_COUNTS=", d1Orders, "\n");
Print("X_IN_G=", x in g, " X_IN_D1=", x in d1,
      " X_ORDER=", Order(x), " X_CENTRALIZER=", xCentralizer,
      " MATCHING_TABLE_CLASSES=", matchingClasses,
      " CLASS_NAME=", classNames[class4a], "\n");
Print("BLOCK2_SUPPORT_ROW=16 VALUE_ON_4A=", irr[16][class4a],
      " ROW_BLOCK=", rowBlock[16], "\n");
Print("ROW_CERTIFICATES_BEGIN\n");
for i in [1 .. nr] do
  degree := irr[i][1];;
  quotient := Size(t) / degree;;
  AssertTrue(IsInt(quotient), Concatenation("integral codegree row ", String(i)));
  oddpart := quotient;;
  charDefect := 0;;
  twoBound := 1;;
  while RemInt(oddpart, p) = 0 do
    charDefect := charDefect + 1;;
    twoBound := twoBound * p;;
    oddpart := oddpart / p;;
  od;
  b := rowBlock[i];;
  pass := defectExponents[b] <= twoBound;;
  allPass := allPass and pass;;
  Print("ROW=", i,
        " BLOCK=", b,
        " DEGREE=", degree,
        " CHAR_2_DEFECT=", charDefect,
        " TWO_BOUND=", twoBound,
        " BLOCK_EXPONENT=", defectExponents[b],
        " PASS=", pass, "\n");
od;
Print("ROW_CERTIFICATES_END\n");
AssertTrue(allPass, "all 29 block-exponent inequalities");
Print("ALL_29_INEQUALITIES_PASS=", allPass, "\n");
Print("ALL_ASSERTIONS_PASS=true\n");
QUIT;
