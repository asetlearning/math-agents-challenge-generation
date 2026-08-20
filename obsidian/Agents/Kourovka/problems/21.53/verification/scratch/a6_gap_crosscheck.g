G := AlternatingGroup(6);;
classes := ConjugacyClasses(G);;
involutionClasses := Filtered(classes, c -> Order(Representative(c)) = 2);;
D := AsList(involutionClasses[1]);;
pairOrders := [];;
for i in [1..Length(D)-1] do
  for j in [i+1..Length(D)] do
    Add(pairOrders, Order(D[i] * D[j]));
  od;
od;
profiles := Set(List(D, x -> List([2,3,4,5],
  t -> Number(D, y -> y <> x and Order(x*y) = t))));;
Print("GAP_VERSION=", GAPInfo.Version, "\n");
Print("Size(A6)=", Size(G), " IsAbelian=", IsAbelian(G), " IsSimple=", IsSimple(G), "\n");
Print("involution class count=", Length(involutionClasses),
      " sizes=", List(involutionClasses, Size), "\n");
Print("unordered product-order counts=", Collected(pairOrders), "\n");
Print("valency profiles [2,3,4,5]=", profiles, "\n");
QUIT;
