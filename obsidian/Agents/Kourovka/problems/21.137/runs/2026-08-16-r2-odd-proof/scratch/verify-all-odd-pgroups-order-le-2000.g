SizeScreen([ 1000, 40 ]);
Print("GAP_VERSION=", GAPInfo.Version, "\n");
HasExactExponentP2 := function(els, p, one)
  local x;
  if not ForAll(els, x -> x^(p^2) = one) then return false; fi;
  return ForAny(els, x -> x^p <> one);
end;
PowerValues := function(els, p)
  local values, x;
  values := [];
  for x in els do AddSet(values, x^p); od;
  return values;
end;
IsProductClosed := function(values)
  local a, b;
  for a in values do
    for b in values do
      if not a*b in values then return false; fi;
    od;
  od;
  return true;
end;
IsPairwiseCommuting := function(values)
  local a, b;
  for a in values do
    for b in values do
      if a*b <> b*a then return false; fi;
    od;
  od;
  return true;
end;
coverage := [
  [ 3,  [ 9, 27, 81, 243, 729 ] ],
  [ 5,  [ 25, 125, 625 ] ],
  [ 7,  [ 49, 343 ] ],
  [ 11, [ 121, 1331 ] ],
  [ 13, [ 169 ] ],
  [ 17, [ 289 ] ],
  [ 19, [ 361 ] ],
  [ 23, [ 529 ] ],
  [ 29, [ 841 ] ],
  [ 31, [ 961 ] ],
  [ 37, [ 1369 ] ],
  [ 41, [ 1681 ] ],
  [ 43, [ 1849 ] ]
];
expectedOrders := [];
for n in [1..2000] do
  factors := FactorsInt(n);
  if Length(factors) >= 2 and Length(Set(factors)) = 1 and IsOddInt(factors[1]) then
    Add(expectedOrders, n);
  fi;
od;
coveredOrders := Set(Concatenation(List(coverage, row -> row[2])));
if coveredOrders <> expectedOrders then
  Error("hard-coded coverage does not equal all odd prime-power orders <= 2000");
fi;
Print("COVERAGE_AUDIT=all_odd_prime_power_orders_le_2000 ORDERS=", coveredOrders, "\n");
allExpP2 := 0;
allClosed := 0;
allBad := 0;
for row in coverage do
  p := row[1];
  for n in row[2] do
    total := NrSmallGroups(n);
    expP2 := 0;
    closed := 0;
    bad := 0;
    for id in [1..total] do
      G := SmallGroup(n,id);
      els := Elements(G);
      one := One(G);
      hasExactExponent := HasExactExponentP2(els, p, one);
      if hasExactExponent then
        expP2 := expP2 + 1;
        vals := PowerValues(els, p);
        isClosed := IsProductClosed(vals);
        if isClosed then
          closed := closed + 1;
          isAbelianDirect := IsPairwiseCommuting(vals);
          if not isAbelianDirect then
            bad := bad + 1;
            Print("COUNTEREXAMPLE_CANDIDATE p=", p, " order=", n,
                  " id=", id, " |values|=", Length(vals), "\n");
          fi;
        fi;
      fi;
    od;
    allExpP2 := allExpP2 + expP2;
    allClosed := allClosed + closed;
    allBad := allBad + bad;
    Print("P=", p, " ORDER=", n, " TOTAL=", total,
          " EXPONENT_P2=", expP2, " POWER_SET_SUBGROUP_DIRECT=", closed,
          " NONABELIAN_DIRECT=", bad, "\n");
  od;
od;
Print("SUMMARY EXPONENT_P2=", allExpP2,
      " POWER_SET_SUBGROUP_DIRECT=", allClosed,
      " NONABELIAN_DIRECT=", allBad, "\n");
QUIT;
