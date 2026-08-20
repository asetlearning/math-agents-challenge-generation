divisors := DivisorsInt(29120);;
nonzero := [];;
unsupported := [];;
for d in divisors do
  n := NumberPerfectGroups(d);
  if n = fail then
    Add(unsupported, d);
  elif n > 0 then
    Add(nonzero, [d,n]);
  fi;
od;
Print("DIVISOR_COUNT=", Length(divisors), "\n");
Print("UNSUPPORTED_DIVISOR_ORDERS=", unsupported, "\n");
Print("NONZERO_PERFECT_COUNTS=", nonzero, "\n");
g := PerfectGroup(29120,1);;
Print("ORDER_29120_PERFECT_GROUP_1_STRUCTURE=", StructureDescription(g), "\n");
Print("ORDER_29120_PERFECT_GROUP_1_IS_SIMPLE=", IsSimple(g), "\n");
QUIT;

