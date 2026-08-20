# Frozen v3 exact checker for Kourovka Problem 20.115, cycle 12.
# Scope: exactly the ordinary CTblLib table identifier "6.A7".
# Mathematical logic is unchanged from v2; only screen width and output naming differ.

if LoadPackage( "ctbllib", false ) <> true then
  Error( "CTblLib is unavailable" );
fi;
SizeScreen( [ 4096, 1000 ] );;

outpath := "Agents/Kourovka/problems/20.115/runs/2026-08-18-r12-six-a7-direct-source-predicate/audit_6a7_v3.tsv";
tbl := CharacterTable( "6.A7" );
if tbl = fail then
  Error( "installed table identifier 6.A7 is absent" );
fi;

id := Identifier( tbl );
ord := Size( tbl );
ncl := NrConjugacyClasses( tbl );
irr := Irr( tbl );
nrows := Length( irr );
names := ClassNames( tbl );
orders := OrdersClassRepresentatives( tbl );
classsizes := SizesConjugacyClasses( tbl );
centralizers := SizesCentralizers( tbl );
centrepos := ClassPositionsOfCentre( tbl );
base := CharacterTable( "A7" );
if base = fail then
  Error( "installed quotient table identifier A7 is absent" );
fi;
fusion := GetFusionMap( tbl, base );
if fusion = fail then
  Error( "no certified CTblLib class fusion from 6.A7 to A7" );
fi;
kernelpos := Filtered( [ 1 .. ncl ], k -> fusion[k] = 1 );

identity_ok := id = "6.A7"
  and IsLibraryCharacterTableRep( tbl )
  and IsOrdinaryTable( tbl )
  and UnderlyingCharacteristic( tbl ) = 0
  and ord = 15120
  and IsPerfect( tbl )
  and IsQuasisimple( tbl )
  and Identifier( base ) = "A7"
  and Size( base ) = 2520
  and ord / Size( base ) = 6
  and Length( fusion ) = ncl
  and Set( kernelpos ) = Set( centrepos )
  and Sum( kernelpos, k -> classsizes[k] ) = 6;

shape_ok := nrows = ncl
  and Length( names ) = ncl
  and Length( orders ) = ncl
  and Length( classsizes ) = ncl
  and Length( centralizers ) = ncl
  and ForAll( irr, chi -> Length( chi ) = ncl )
  and Sum( classsizes ) = ord
  and ForAll( [ 1 .. ncl ], k -> classsizes[k] * centralizers[k] = ord );

irred_ok := ForAll( irr, IsIrreducibleCharacter );
orthogonality_ok := true;
for i in [ 1 .. nrows ] do
  for j in [ 1 .. nrows ] do
    sp := ScalarProduct( tbl, irr[i], irr[j] );
    if ( i = j and sp <> 1 ) or ( i <> j and sp <> 0 ) then
      orthogonality_ok := false;
    fi;
  od;
od;

Print( "GAP_VERSION\t", GAPInfo.Version, "\n" );
Print( "CTBLLIB_VERSION\t", PackageInfo( "ctbllib" )[1].Version, "\n" );
Print( "TABLE_REQUEST\t6.A7\n" );
Print( "TABLE_IDENTIFIER\t", id, "\n" );
Print( "IS_LIBRARY_TABLE\t", IsLibraryCharacterTableRep( tbl ), "\n" );
Print( "IS_ORDINARY_TABLE\t", IsOrdinaryTable( tbl ), "\n" );
Print( "UNDERLYING_CHARACTERISTIC\t", UnderlyingCharacteristic( tbl ), "\n" );
Print( "GROUP_ORDER\t", ord, "\n" );
Print( "IS_PERFECT_TABLE\t", IsPerfect( tbl ), "\n" );
Print( "IS_QUASISIMPLE_TABLE\t", IsQuasisimple( tbl ), "\n" );
Print( "QUOTIENT_TABLE_IDENTIFIER\t", Identifier( base ), "\n" );
Print( "QUOTIENT_ORDER\t", Size( base ), "\n" );
Print( "CENTRAL_ORDER_RATIO\t", ord / Size( base ), "\n" );
Print( "CENTRE_CLASS_POSITIONS\t", centrepos, "\n" );
Print( "QUOTIENT_KERNEL_CLASS_POSITIONS\t", kernelpos, "\n" );
Print( "QUOTIENT_KERNEL_ORDER\t", Sum( kernelpos, k -> classsizes[k] ), "\n" );
Print( "IDENTITY_GATE\t", identity_ok, "\n" );
Print( "CLASS_COUNT\t", ncl, "\n" );
Print( "IRREDUCIBLE_ROW_COUNT\t", nrows, "\n" );
Print( "SHAPE_GATE\t", shape_ok, "\n" );
Print( "ALL_ROWS_IRREDUCIBLE\t", irred_ok, "\n" );
Print( "FULL_ROW_ORTHOGONALITY\t", orthogonality_ok, "\n" );
Print( "INFO_TEXT\t", InfoText( tbl ), "\n" );
Print( "CLASS_NAMES\t", names, "\n" );
Print( "CLASS_ORDERS\t", orders, "\n" );
Print( "CLASS_SIZES\t", classsizes, "\n" );
Print( "CHARACTER_DEGREES\t", List( irr, chi -> chi[1] ), "\n" );

if not identity_ok then
  Error( "6.A7 identity gate failed" );
fi;
if not shape_ok then
  Error( "row/class completeness gate failed" );
fi;
if not irred_ok or not orthogonality_ok then
  Error( "ordinary irreducibility gate failed" );
fi;

PrintTo( outpath,
  "row\tdegree\tclass\tclass_name\tclass_order\tvalue\texact_nonzero\tproduct\tgroup_order\tremainder\tdivides\n" );
total := 0;
nonzero := 0;
zeros := 0;
violations := 0;
for i in [ 1 .. nrows ] do
  degree := irr[i][1];
  Print( "ROW\t", i, "\tDEGREE\t", degree,
         "\tLENGTH\t", Length( irr[i] ),
         "\tIRREDUCIBLE\t", IsIrreducibleCharacter( irr[i] ),
         "\tSELF_SCALAR\t", ScalarProduct( tbl, irr[i], irr[i] ), "\n" );
  for j in [ 1 .. ncl ] do
    total := total + 1;
    val := irr[i][j];
    exact_nonzero := val <> 0;
    product := orders[j] * degree;
    remainder := ord mod product;
    divides := remainder = 0;
    if exact_nonzero then
      nonzero := nonzero + 1;
      if not divides then
        violations := violations + 1;
        Print( "VIOLATION\tROW\t", i,
               "\tDEGREE\t", degree,
               "\tCLASS\t", j,
               "\tCLASS_NAME\t", names[j],
               "\tCLASS_ORDER\t", orders[j],
               "\tVALUE\t", val,
               "\tPRODUCT\t", product,
               "\tGROUP_ORDER\t", ord,
               "\tREMAINDER\t", remainder, "\n" );
      fi;
    else
      zeros := zeros + 1;
    fi;
    AppendTo( outpath,
      i, "\t", degree, "\t", j, "\t", names[j], "\t", orders[j], "\t",
      val, "\t", exact_nonzero, "\t", product, "\t", ord, "\t",
      remainder, "\t", divides, "\n" );
  od;
od;

Print( "TOTAL_CELLS\t", total, "\n" );
Print( "EXACT_NONZERO_CELLS\t", nonzero, "\n" );
Print( "ZERO_CELLS\t", zeros, "\n" );
Print( "VIOLATION_COUNT\t", violations, "\n" );
Print( "COVERAGE_GATE\t", total = nrows * ncl and nonzero + zeros = total, "\n" );
if violations = 0 then
  Print( "FINAL_STATUS\tZERO_HIT\n" );
else
  Print( "FINAL_STATUS\tHIT\n" );
fi;
Print( "TERMINAL_SENTINEL\tKOUROVKA_20_115_6A7_AUDIT_V3_COMPLETE_EXACTLY_ONCE\n" );

QUIT_GAP( 0 );
