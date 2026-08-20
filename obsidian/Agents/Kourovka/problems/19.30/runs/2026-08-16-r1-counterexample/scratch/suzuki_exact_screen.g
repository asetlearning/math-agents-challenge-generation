LoadPackage("ctbllib");;

VanishingData := function(name)
  local t, irr, ord, sizes, zeros, vi, nonvi;
  t := CharacterTable(name);
  irr := Irr(t);
  ord := OrdersClassRepresentatives(t);
  sizes := SizesConjugacyClasses(t);
  zeros := List([1..Length(ord)],
                j -> Filtered([1..Length(irr)], i -> IsZero(irr[i][j])));
  vi := Filtered([1..Length(ord)], j -> not IsEmpty(zeros[j]));
  nonvi := Difference([1..Length(ord)], vi);
  Print("IDENTIFIER=", Identifier(t), "\n");
  Print("IS_ORDINARY_TABLE=", IsOrdinaryTable(t), "\n");
  Print("IS_SIMPLE=", IsSimple(t), "\n");
  Print("SIZE=", Size(t), "\n");
  Print("SIZE_FACTORS=", FactorsInt(Size(t)), "\n");
  Print("NCLASSES=", NrConjugacyClasses(t), "\n");
  Print("NIRR=", Length(irr), "\n");
  Print("CHARACTER_DEGREES=", List(irr, chi -> chi[1]), "\n");
  Print("CLASS_ORDERS=", ord, "\n");
  Print("CLASS_SIZES=", sizes, "\n");
  Print("ZERO_CHARACTER_INDICES_BY_CLASS=", zeros, "\n");
  Print("VANISHING_CLASS_INDICES=", vi, "\n");
  Print("FIRST_ZERO_CHARACTER_BY_VANISHING_CLASS=",
        List(vi, j -> zeros[j][1]), "\n");
  Print("NONVANISHING_CLASS_INDICES=", nonvi, "\n");
  Print("VANISHING_ORDER_SET=", Set(List(vi, j -> ord[j])), "\n");
  Print("NONVANISHING_ORDER_SET=", Set(List(nonvi, j -> ord[j])), "\n");
  Print("CHECK_SUM_CLASS_SIZES=", Sum(sizes), "\n");
  Print("CHECK_SUM_DEGREE_SQUARES=", Sum(irr, chi -> chi[1]^2), "\n");
end;;

Print("GAP_VERSION=", GAPInfo.Version, "\n");
Print("CTBLLIB_VERSION=", PackageInfo("ctbllib")[1].Version, "\n");
VanishingData("Sz(8)");
VanishingData("Sz(32)");
QUIT;

