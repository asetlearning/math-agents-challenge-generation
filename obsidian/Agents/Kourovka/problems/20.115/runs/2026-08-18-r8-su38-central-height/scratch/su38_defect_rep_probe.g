SetUserPreference("UseColor", false);
if LoadPackage("ctbllib") = fail then
  Error("CTblLib unavailable");
fi;

t := CharacterTable("3.U3(8)");
irr := Irr(t);
pb := PrimeBlocks(t,3);
orders := OrdersClassRepresentatives(t);
sizes := SizesConjugacyClasses(t);
names := ClassNames(t);

ppos := Filtered([1..Length(orders)], i -> orders[i] in [1,3,9,27,81,243]);
Print("THREE_POWER_CLASS_POSITIONS=", ppos, "\n");
for c in ppos do
  Print("CLASS_POS=", c, " NAME=", names[c], " ORDER=", orders[c],
        " SIZE=", sizes[c], " CENTRALIZER=", Size(t)/sizes[c], "\n");
  for b in [1..Length(pb.defect)] do
    rows := Positions(pb.block,b);
    support := Filtered(rows, r -> not IsZero(irr[r][c]));
    if Length(support) > 0 then
      Print("  BLOCK=", b, " SUPPORT=", support, "\n");
    fi;
  od;
od;

L := SU(3,8);
Cen := Center(L);
P := SylowSubgroup(L,3);
Print("SYLOW_ORDER=", Size(P), " SYLOW_EXPONENT=", Exponent(P),
      " CENTER_INCLUDED=", IsSubgroup(P,Cen), "\n");
Print("SYLOW_STRUCTURE=", StructureDescription(P), "\n");
Q := FactorGroup(P,Cen);
Print("SYLOW_MOD_CENTER_ORDER=", Size(Q),
      " SYLOW_MOD_CENTER_EXPONENT=", Exponent(Q), "\n");
Print("SYLOW_ELEMENT_ORDER_COUNTS=",
      Collected(List(Elements(P),Order)), "\n");
Print("END_SU38_DEFECT_REP_PROBE\n");
