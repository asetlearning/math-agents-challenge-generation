if LoadPackage("ctbllib") = fail then
  Error("CTblLib unavailable");
fi;

p := 3;
t := CharacterTable("3.U3(8)");
if t = fail then
  Error("ordinary table 3.U3(8) unavailable");
fi;

Print("GAP_VERSION=", GAPInfo.Version, "\n");
Print("CTBLLIB_VERSION=", InstalledPackageVersion("ctbllib"), "\n");
Print("TABLE_ID=", Identifier(t), "\n");
Print("TABLE_ORDER=", Size(t), "\n");
Print("NR_CLASSES=", NrConjugacyClasses(t), "\n");
Print("NR_IRR=", Length(Irr(t)), "\n");

pb := PrimeBlocks(t, p);
if pb = fail then
  Error("ordinary 3-block data unavailable");
fi;
Print("NR_3BLOCKS=", Length(pb.defect), "\n");
Print("BLOCK_VECTOR=", pb.block, "\n");
Print("DEFECT_VECTOR=", pb.defect, "\n");

L := SU(3,8);
Cen := Center(L);
Print("MATRIX_GROUP_ORDER=", Size(L), "\n");
Print("CENTER_ORDER=", Size(Cen), "\n");
Print("CENTER_STRUCTURE=", StructureDescription(Cen), "\n");
Print("QUOTIENT_ORDER=", Size(L)/Size(Cen), "\n");

if Size(t) <> Size(L) then
  Error("table and matrix-group orders disagree");
fi;
if Size(L) <> 8^3 * (8^3+1) * (8^2-1) then
  Error("matrix-group order disagrees with SU3 order formula");
fi;
if Size(Cen) <> Gcd(3,8+1) then
  Error("matrix-group center disagrees with SU3 center formula");
fi;

Print("END_SU38_IDENTITY_PROBE\n");
