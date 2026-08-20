T := GL(3,2);
S := SchurCover(T);
K := SmallGroup(12,5);
centerK := Centre(K);
z := First(Elements(centerK), x -> Order(x)=2);
s := First(Elements(Centre(S)), x -> Order(x)=2);
product := DirectProduct(K,S);
imageK := Image(Embedding(product,1));
diag := Subgroup(product,[Image(Embedding(product,1),z)*Image(Embedding(product,2),s)]);
G := FactorGroup(product,diag);
q := NaturalHomomorphismByNormalSubgroup(product,diag);
embeddedK := Image(q,imageK);
quotient := FactorGroup(G,embeddedK);
Print("GAP_VERSION=", GAPInfo.Version, "\n");
Print("K_ID=", IdGroup(K), " Z_ORBIT_REP_ORDER=", Order(z), "\n");
Print("PRODUCT_ORDER=", Size(product), " DIAGONAL_ORDER=", Size(diag),
      " G_ORDER=", Size(G), "\n");
Print("EMBEDDED_K_ORDER=", Size(embeddedK), " EMBEDDED_K_ID=", IdGroup(embeddedK),
      " QUOTIENT_ORDER=", Size(quotient), " QUOTIENT_ID=", IdGroup(quotient), "\n");
Print("RADICAL_ORDER=", Size(RadicalGroup(G)),
      " RADICAL_ID=", IdGroup(RadicalGroup(G)),
      " RADICAL_EQUALS_EMBEDDED_K=", RadicalGroup(G)=embeddedK, "\n");
Print("RUN_COMPLETE=true\n");
QUIT;
