LoadPackage("grape", false);

q := 27;;
G := PSL(2,q);;
classes := ConjugacyClasses(G);;
iclasses := Filtered(classes, c -> Order(Representative(c)) = 2);;
if Length(iclasses) <> 1 then Error("wrong involution class count"); fi;
D := AsList(iclasses[1]);;

gamma := Graph(
  G,
  D,
  OnPoints,
  function(x,y)
    return x <> y and Order(x*y) = 2;
  end,
  true
);;

aut2 := AutGroupGraph(gamma);;

Print("Q27_ORTHOGONALITY_AUDIT_OK\n");
Print("GAP_VERSION=", GAPInfo.Version, "\n");
Print("GRAPE_VERSION=", PackageInfo("grape")[1].Version, "\n");
Print("GROUP_ORDER=", Size(G), "\n");
Print("INVOLUTION_CLASS_COUNT=", Length(iclasses), "\n");
Print("VERTEX_COUNT=", Length(D), "\n");
Print("VALENCY=", VertexDegree(gamma,1), "\n");
Print("AUT2_ORDER=", Size(aut2), "\n");
Print("EXPECTED_PGAMMAL2_ORDER=", q*(q^2-1)*3, "\n");
QUIT;
