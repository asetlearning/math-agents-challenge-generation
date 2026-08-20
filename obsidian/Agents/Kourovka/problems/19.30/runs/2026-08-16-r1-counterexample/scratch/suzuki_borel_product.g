LoadPackage("ctbllib");;

VanishingOrders := function(t)
  local ord, irr, vi;
  ord := OrdersClassRepresentatives(t);
  irr := Irr(t);
  vi := Filtered([1..Length(ord)],
                 j -> ForAny(irr, chi -> IsZero(chi[j])));
  return Set(ord{vi});
end;;

for data in [
  rec(q := 8,  borel := "2^(3+3):7"),
  rec(q := 32, borel := "2^(5+5):31")
] do
  t := CharacterTable(data.borel);
  n := data.q^2 + 1;
  borelV := VanishingOrders(t);
  productV := Set(List(Cartesian(borelV, DivisorsInt(n)),
                       pair -> Lcm(pair[1], pair[2])));
  Print("Q=", data.q, " BOREL_TABLE=", data.borel,
        " BOREL_ORDER=", Size(t), " CYCLIC_FACTOR_ORDER=", n,
        " PRODUCT_ORDER=", Size(t)*n, "\n");
  Print("BOREL_SPECTRUM=", Set(OrdersClassRepresentatives(t)), "\n");
  Print("BOREL_VANISHING_ORDERS=", borelV, "\n");
  Print("PRODUCT_VANISHING_ORDERS=", productV, "\n");
od;
QUIT;

