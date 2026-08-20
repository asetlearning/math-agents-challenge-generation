pairs := [ [2,2], [9,5], [11,5], [17,1], [19,2], [27,3], [29,4], [38,5], [40,5] ];
Print("GAP_VERSION=",GAPInfo.Version,"\n");
for pair in pairs do
  H := SmallGroup(252,pair[1]);;
  Kmatches := Filtered(NormalSubgroups(H),
    K -> IdGroup(K)=[12,pair[2]] and IdGroup(FactorGroup(H,K))=[21,1]);;
  elems := AsList(H);;
  P := Action(H,elems,OnRight);;
  Print("H_ID=",IdGroup(H)," K_ID=",[12,pair[2]],
        " K_MATCHES=",Length(Kmatches),
        " M_ID=",IdGroup(H)," M_SOLUBLE=",IsSolvableGroup(H),
        " TRANSLATION_IMAGE_ORDER=",Size(P),
        " DEGREE=",Length(MovedPoints(P)),
        " TRANSITIVE=",IsTransitive(P,[1..Size(H)]),
        " STABILIZER_ORDER=",Size(Stabilizer(P,1)),"\n");
od;
QUIT;
