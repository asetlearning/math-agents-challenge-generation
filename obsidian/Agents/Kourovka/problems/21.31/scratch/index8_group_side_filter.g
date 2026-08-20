pairs := [ [2,2], [9,5], [11,5], [17,1], [19,2], [27,3], [29,4], [38,5], [40,5] ];
Print("GAP_VERSION=",GAPInfo.Version,"\n");
for pair in pairs do
  H := SmallGroup(252,pair[1]);;
  Ks := Filtered(NormalSubgroups(H),
    x -> IdGroup(x)=[12,pair[2]] and IdGroup(FactorGroup(H,x))=[21,1]);;
  K := Ks[1];;
  C := Centralizer(H,K);;
  Print("H_ID=",IdGroup(H)," K_ID=",IdGroup(K),
        " CENTER_K=",Size(Centre(K)),
        " CENTRALIZER_K=",Size(C),
        " KC_ORDER=",Size(ClosureGroup(K,C)),
        " CENTRALIZER_QUOTIENT_ORDER=",Size(C)/Size(Intersection(C,K)),
        " GLOBAL_CENTRALIZER_FILTER=",ClosureGroup(K,C)=H,"\n");
od;
QUIT;
