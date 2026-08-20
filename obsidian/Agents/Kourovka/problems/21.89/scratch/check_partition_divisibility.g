# Exact bounded check for Kourovka 21.89.
# Usage: gap -q -c 'limit:=10000;; Read(".../check_partition_divisibility.g"); QUIT;'
if not IsBound(limit) then limit := 1000; fi;;
divisors := [];;
primeGtN := 0;;
valuationOnly := 0;;
examplesPrimeGtN := [];;
examplesValuationOnly := [];;
closestPrimeRatio := fail;;

FactorialValuation := function(n, q)
  local total;
  total := 0;
  while n > 0 do
    n := QuoInt(n, q);
    total := total + n;
  od;
  return total;
end;;

for n in [1..limit] do
  pn := NrPartitions(n);
  collected := Collected(FactorsInt(pn));
  # GAP represents FactorsInt(1) as [1]; ignore that unit explicitly.
  failures := Filtered(collected, pair -> pair[1] > 1 and pair[2] > FactorialValuation(n, pair[1]));
  if Length(failures) = 0 then
    Add(divisors, n);
  elif n >= 40 then
    record := rec(n := n, p_n := pn, factors := collected, failures := failures);
    if ForAny(failures, pair -> pair[1] > n) then
      primeGtN := primeGtN + 1;
      largestPrime := Maximum(List(collected, pair -> pair[1]));
      if closestPrimeRatio = fail or largestPrime * closestPrimeRatio.n < closestPrimeRatio.q * n then
        closestPrimeRatio := rec(n := n, q := largestPrime);
      fi;
      if Length(examplesPrimeGtN) < 10 then Add(examplesPrimeGtN, record); fi;
    else
      valuationOnly := valuationOnly + 1;
      if Length(examplesValuationOnly) < 10 then Add(examplesValuationOnly, record); fi;
    fi;
  fi;
od;

Print("GAP_VERSION=", GAPInfo.Version, "\n");
Print("LIMIT=", limit, "\n");
Print("DIVISORS=", divisors, "\n");
Print("N_GE_40_OBSTRUCTED_BY_PRIME_GT_N=", primeGtN, "\n");
Print("N_GE_40_OBSTRUCTED_ONLY_BY_VALUATION=", valuationOnly, "\n");
Print("FIRST_PRIME_GT_N_EXAMPLES=", examplesPrimeGtN, "\n");
Print("FIRST_VALUATION_ONLY_EXAMPLES=", examplesValuationOnly, "\n");
Print("CLOSEST_LARGEST_PRIME_RATIO=", closestPrimeRatio, "\n");
