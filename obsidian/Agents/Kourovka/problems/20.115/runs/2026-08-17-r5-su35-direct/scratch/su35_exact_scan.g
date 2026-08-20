#############################################################################
## Frozen one-table exact scan for Kourovka Problem 20.115.
## Authorized table: CharacterTable("3.U3(5)") only.
#############################################################################

LogTo("Agents/Kourovka/problems/20.115/runs/2026-08-17-r5-su35-direct/scratch/su35_exact_scan.out");

if LoadPackage("ctbllib") <> true then
  Error("CTblLib did not load");
fi;

pkginfo := PackageInfo("ctbllib");
if pkginfo = fail or Length(pkginfo) = 0 then
  Error("CTblLib package metadata unavailable");
fi;

tbl := CharacterTable("3.U3(5)");
if tbl = fail then
  Error("CharacterTable(\"3.U3(5)\") unavailable");
fi;

identifier := Identifier(tbl);
grouporder := Size(tbl);
ordinary := IsOrdinaryTable(tbl);
perfect := IsPerfect(tbl);
quasisimple := IsQuasisimple(tbl);
chars := Irr(tbl);
nrrows := Length(chars);
nrclasses := NrConjugacyClasses(tbl);
classnames := AtlasClassNames(tbl);
classorders := OrdersClassRepresentatives(tbl);
classsizes := SizesConjugacyClasses(tbl);
degrees := List(chars, chi -> chi[1]);
centrepos := ClassPositionsOfCentre(tbl);
centresize := Sum(classsizes{centrepos});
centreorders := classorders{centrepos};
quotientorder := grouporder / centresize;
degreesquaresum := Sum(degrees, d -> d^2);
allcyclotomic := ForAll(chars, chi -> ForAll(chi, IsCyc));

if identifier <> "3.U3(5)" then
  Error("unexpected table identifier");
fi;
if ordinary <> true then
  Error("table is not ordinary");
fi;
if perfect <> true or quasisimple <> true then
  Error("table is not perfect quasisimple data");
fi;
if grouporder <> 378000 then
  Error("unexpected group order");
fi;
if nrrows <> 40 or nrclasses <> 40 then
  Error("unexpected table dimensions");
fi;
if centresize <> 3 or Length(centrepos) <> 3 or Set(centreorders) <> [ 1, 3 ] then
  Error("unexpected centre data");
fi;
if quotientorder <> 126000 then
  Error("unexpected central quotient order");
fi;
if degreesquaresum <> grouporder then
  Error("degree-square sum mismatch");
fi;
if not ForAll(degrees, IsInt) then
  Error("a row degree is not an integer");
fi;
if not ForAll(classorders, n -> IsInt(n) and n > 0) then
  Error("a class order is not a positive integer");
fi;
if not allcyclotomic then
  Error("a stored ordinary value is not an exact cyclotomic");
fi;

Print("META\tGAP_VERSION\t", GAPInfo.Version, "\n");
Print("META\tCTBLLIB_VERSION\t", pkginfo[1].Version, "\n");
Print("META\tTABLE_IDENTIFIER\t", identifier, "\n");
Print("META\tIS_ORDINARY\t", ordinary, "\n");
Print("META\tIS_PERFECT\t", perfect, "\n");
Print("META\tIS_QUASISIMPLE\t", quasisimple, "\n");
Print("META\tGROUP_ORDER\t", grouporder, "\n");
Print("META\tNR_ROWS\t", nrrows, "\n");
Print("META\tNR_CLASSES\t", nrclasses, "\n");
Print("META\tGRID_SIZE\t", nrrows * nrclasses, "\n");
Print("META\tDEGREE_SQUARE_SUM\t", degreesquaresum, "\n");
Print("META\tCENTRE_POSITIONS\t", centrepos, "\n");
Print("META\tCENTRE_ORDERS\t", centreorders, "\n");
Print("META\tCENTRE_SIZE\t", centresize, "\n");
Print("META\tCENTRAL_QUOTIENT_ORDER\t", quotientorder, "\n");
Print("META\tALL_VALUES_EXACT_CYCLOTOMIC\t", allcyclotomic, "\n");
Print("INFO_TEXT_BEGIN\n", InfoText(tbl), "\nINFO_TEXT_END\n");

for j in [ 1 .. nrclasses ] do
  Print("CLASS\t", j,
        "\tlabel=", classnames[j],
        "\torder=", classorders[j],
        "\tsize=", classsizes[j],
        "\tcentral=", j in centrepos, "\n");
od;

for i in [ 1 .. nrrows ] do
  Print("ROW\t", i, "\tdegree=", degrees[i], "\n");
od;

nonzerocount := 0;
violationcount := 0;
for i in [ 1 .. nrrows ] do
  for j in [ 1 .. nrclasses ] do
    value := chars[i][j];
    nonzero := value <> 0;
    product := degrees[i] * classorders[j];
    remainder := grouporder mod product;
    violation := nonzero and remainder <> 0;
    if nonzero then
      nonzerocount := nonzerocount + 1;
    fi;
    if violation then
      violationcount := violationcount + 1;
    fi;
    Print("CELL\trow=", i,
          "\tclass=", j,
          "\tlabel=", classnames[j],
          "\tdegree=", degrees[i],
          "\tclass_order=", classorders[j],
          "\tvalue=", value,
          "\tnonzero=", nonzero,
          "\tproduct=", product,
          "\tremainder=", remainder,
          "\tviolation=", violation, "\n");
  od;
od;

Print("SUMMARY\tTOTAL_PAIRS\t", nrrows * nrclasses, "\n");
Print("SUMMARY\tNONZERO_PAIRS\t", nonzerocount, "\n");
Print("SUMMARY\tVIOLATIONS\t", violationcount, "\n");

LogTo();
QUIT_GAP(0);
