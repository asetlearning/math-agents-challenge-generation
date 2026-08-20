G := AlternatingGroup(8);;
A := AutomorphismGroup(G);;
Print("GAP=", GAPInfo.Version, "\n");
Print("Size(A8)=", Size(G), " Size(Aut(A8))=", Size(A), "\n");
classes := ConjugacyClasses(G);;
involutionClasses := Filtered(classes, c -> Order(Representative(c)) = 2);;
Print("involution class sizes=", List(involutionClasses, Size), "\n");
for c in involutionClasses do
  Print("representative=", Representative(c), " size=", Size(c), "\n");
od;
inner := InnerAutomorphismsAutomorphismGroup(A);;
Print("inner size=", Size(inner), " outer quotient size=", Index(A, inner), "\n");
QUIT;
