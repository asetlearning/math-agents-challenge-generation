#############################################################################
## Independent Validator reconstruction for the one-table 3.U3(5) claim.
## This is deliberately class-major and uses exact quotient integrality, not
## the claimant's row-major modulo loop.
#############################################################################

outpath := "Agents/Kourovka/problems/20.115/verification/scratch/validator_su35_scan.out";
LogTo(outpath);
SizeScreen([ 100000, 100000 ]);

if LoadPackage("ctbllib") <> true then
  Error("ctbllib unavailable");
fi;

packageinfo := PackageInfo("ctbllib");
if packageinfo = fail or Length(packageinfo) = 0 then
  Error("ctbllib metadata unavailable");
fi;

table := CharacterTable("3.U3(5)");
if table = fail then
  Error("the sole authorized table is unavailable");
fi;

characters := Irr(table);
numberrows := Length(characters);
numberclasses := NrConjugacyClasses(table);
orders := OrdersClassRepresentatives(table);
sizes := SizesConjugacyClasses(table);
labels := AtlasClassNames(table);
degrees := List(characters, chi -> chi[1]);
grouporder := Size(table);
centrepositions := ClassPositionsOfCentre(table);
centreorder := Sum(sizes{centrepositions});

orthogonalityfailures := [];
for i in [ 1 .. numberrows ] do
  for k in [ 1 .. numberrows ] do
    scalar := ScalarProduct(table, characters[i], characters[k]);
    expectedscalar := 0;
    if i = k then
      expectedscalar := 1;
    fi;
    if scalar <> expectedscalar then
      Add(orthogonalityfailures, [ i, k, scalar ]);
    fi;
  od;
od;

allcyclic := ForAll(characters,
                    chi -> ForAll(chi, value -> IsCyc(value)));

Print("VMETA\tGAP_VERSION\t", GAPInfo.Version, "\n");
Print("VMETA\tCTBLLIB_VERSION\t", packageinfo[1].Version, "\n");
Print("VMETA\tIDENTIFIER\t", Identifier(table), "\n");
Print("VMETA\tINFO_TEXT\t", ReplacedString(InfoText(table), "\n", " | "), "\n");
Print("VMETA\tORDINARY\t", IsOrdinaryTable(table), "\n");
Print("VMETA\tPERFECT\t", IsPerfect(table), "\n");
Print("VMETA\tQUASISIMPLE\t", IsQuasisimple(table), "\n");
Print("VMETA\tGROUP_ORDER\t", grouporder, "\n");
Print("VMETA\tSU3_ORDER_FORMULA\t", 5^3 * (5^2 - 1) * (5^3 + 1), "\n");
Print("VMETA\tCENTRE_FORMULA\t", Gcd(3, 5 + 1), "\n");
Print("VMETA\tCENTRE_POSITIONS\t", centrepositions, "\n");
Print("VMETA\tCENTRE_ORDER\t", centreorder, "\n");
Print("VMETA\tQUOTIENT_ORDER\t", grouporder / centreorder, "\n");
Print("VMETA\tNUMBER_ROWS\t", numberrows, "\n");
Print("VMETA\tNUMBER_CLASSES\t", numberclasses, "\n");
Print("VMETA\tCLASS_SIZE_SUM\t", Sum(sizes), "\n");
Print("VMETA\tDEGREE_SQUARE_SUM\t", Sum(degrees, degree -> degree^2), "\n");
Print("VMETA\tALL_VALUES_CYCLOTOMIC\t", allcyclic, "\n");
Print("VMETA\tORTHOGONALITY_FAILURES\t", Length(orthogonalityfailures), "\n");

for j in [ 1 .. numberclasses ] do
  Print("VCLASS\tindex=", j,
        "\tlabel=", labels[j],
        "\torder=", orders[j],
        "\tsize=", sizes[j],
        "\tcentral=", j in centrepositions, "\n");
od;

for i in [ 1 .. numberrows ] do
  Print("VROW\tindex=", i, "\tdegree=", degrees[i], "\n");
od;

nonzeropairs := 0;
failedpairs := [];
cellcount := 0;

for j in [ 1 .. numberclasses ] do
  for i in [ 1 .. numberrows ] do
    cellcount := cellcount + 1;
    value := characters[i][j];
    iszero := IsZero(value);
    if not iszero then
      nonzeropairs := nonzeropairs + 1;
    fi;
    product := degrees[i] * orders[j];
    exactquotient := grouporder / product;
    divides := IsInt(exactquotient);
    if not iszero and not divides then
      Add(failedpairs, [ i, j, degrees[i], orders[j], value ]);
    fi;
    Print("VCELL\trow=", i,
          "\tclass=", j,
          "\tlabel=", labels[j],
          "\tdegree=", degrees[i],
          "\tclass_order=", orders[j],
          "\tvalue=", String(value),
          "\tnonzero=", not iszero,
          "\tproduct=", product,
          "\tdivides=", divides, "\n");
  od;
od;

Print("VSUMMARY\tCELLS\t", cellcount, "\n");
Print("VSUMMARY\tNONZERO\t", nonzeropairs, "\n");
Print("VSUMMARY\tFAILED_DIVISIBILITIES\t", Length(failedpairs), "\n");

if Identifier(table) <> "3.U3(5)" or
   IsOrdinaryTable(table) <> true or
   IsPerfect(table) <> true or
   IsQuasisimple(table) <> true or
   grouporder <> 378000 or
   grouporder <> 5^3 * (5^2 - 1) * (5^3 + 1) or
   centreorder <> Gcd(3, 5 + 1) or
   grouporder / centreorder <> 126000 or
   numberrows <> 40 or numberclasses <> 40 or
   Sum(sizes) <> grouporder or
   Sum(degrees, degree -> degree^2) <> grouporder or
   allcyclic <> true or
   Length(orthogonalityfailures) <> 0 then
  Error("independent table-semantics invariant failed");
fi;

LogTo();
QUIT_GAP(0);

