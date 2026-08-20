LoadPackage("ctbllib");
LoadPackage("atlasrep");

tbl := CharacterTable("L4(3)");
pb := PrimeBlocks(tbl, 2);
irr := Irr(tbl);
Print("GAP_VERSION=", GAPInfo.Version, "\n");
Print("CTBLLIB_VERSION=", InstalledPackageVersion("ctbllib"), "\n");
Print("ATLASREP_VERSION=", InstalledPackageVersion("atlasrep"), "\n");
Print("TABLE_ID=", Identifier(tbl), " ORDER=", Size(tbl), " ORDER_FACTORS=", FactorsInt(Size(tbl)), " NIRR=", Length(irr), "\n");
Print("PRIME_BLOCKS=", pb, "\n");
Print("DEGREES=", List(irr, chi -> chi[1]), "\n");

g := AtlasGroup("L4(3)", IsPermGroup);
if g = fail then
  Print("ATLAS_GROUP=fail\n");
else
  Print("ATLAS_GROUP=success SIZE=", Size(g), " DEGREE=", LargestMovedPoint(g),
        " CENTER_SIZE=", Size(Center(g)), " IS_SIMPLE=", IsSimpleGroup(g), "\n");
  Print("ATLAS_GENERATORS=", GeneratorsOfGroup(g), "\n");
  s := SylowSubgroup(g, 2);
  Print("SYLOW2_SIZE=", Size(s), " EXPONENT=", Exponent(s),
        " STRUCTURE=", StructureDescription(s), "\n");
  Print("SYLOW2_GENERATORS=", GeneratorsOfGroup(s), "\n");
fi;
QUIT;
