# Independent Validator enumeration for the bounded S8(3) exclusion.
# This does not read or call the claimant's program.

t := CharacterTable("S8(3)");
if t = fail then Error("CTblLib table S8(3) is unavailable"); fi;

chars := Irr(t);
classSizes := SizesConjugacyClasses(t);
orders := OrdersClassRepresentatives(t);
numberClasses := Length(classSizes);

Print("GAP_VERSION=", GAPInfo.Version, "\n");
Print("CTBLLIB_VERSION=", InstalledPackageVersion("ctbllib"), "\n");
Print("TABLE_IDENTIFIER=", Identifier(t), "\n");
Print("TABLE_SIZE=", Size(t), "\n");
Print("TABLE_IS_SIMPLE=", IsSimple(t), "\n");
Print("NUMBER_CLASSES=", numberClasses, "\n");
Print("NUMBER_IRREDUCIBLES=", Length(chars), "\n");
Print("IDENTITY_INDEX_DATA=size:", classSizes[1], ",order:", orders[1],
      ",number_order_one:", Number(orders, x -> x = 1), "\n");

if numberClasses <> 278 then Error("unexpected class count"); fi;
if Length(chars) <> numberClasses then Error("character table is not square"); fi;
if classSizes[1] <> 1 or orders[1] <> 1 or Number(orders, x -> x = 1) <> 1 then
  Error("identity class indexing check failed");
fi;

pairCount := 0;
divisibleTriples := 0;
characterComparisons := 0;
compatibleTriples := [];

# If K_i K_j is exactly K_k, uniform conjugation implies that
# |K_i||K_j|/|K_k| is an integer, and every irreducible character obeys
# chi(i)chi(j)=chi(1)chi(k).  We use no strict-size or Szep filter here.
for i in [2..numberClasses] do
  for j in [2..numberClasses] do
    pairCount := pairCount + 1;
    for k in [1..numberClasses] do
      if (classSizes[i] * classSizes[j]) mod classSizes[k] <> 0 then
        continue;
      fi;
      divisibleTriples := divisibleTriples + 1;
      ok := true;
      for chi in chars do
        characterComparisons := characterComparisons + 1;
        if chi[i] * chi[j] <> chi[1] * chi[k] then
          ok := false;
          break;
        fi;
      od;
      if ok then Add(compatibleTriples, [i,j,k]); fi;
    od;
  od;
od;

Print("ORDERED_NONIDENTITY_PAIRS=", pairCount, "\n");
Print("DIVISIBLE_CANDIDATE_TRIPLES=", divisibleTriples, "\n");
Print("EXACT_CHARACTER_COMPARISONS=", characterComparisons, "\n");
Print("COMPATIBLE_TRIPLES=", compatibleTriples, "\n");
Print("FINAL_COMPATIBLE_COUNT=", Length(compatibleTriples), "\n");
QUIT;
