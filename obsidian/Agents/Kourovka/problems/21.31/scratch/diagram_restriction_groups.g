T := SmallGroup(168,42);;
P := SmallGroup(21,1);;
autP := AutomorphismGroup(P);;
if IsBound(CLASS_SPECS) then
  classes := CLASS_SPECS;
else
  classes := [
    [1,"split"],[1,"nonsplit"],
    [2,"split"],[2,"nonsplit"],
    [3,"split"],
    [4,"split"],[4,"nonsplit"],
    [5,"split"],[5,"nonsplit"]
  ];
fi;
Print("GAP_VERSION=",GAPInfo.Version," P_ID=",IdGroup(P),
      " AUT_P_SIZE=",Size(autP)," AUT_P_DESC=",StructureDescription(autP),"\n");
for spec in classes do
  kid := spec[1];; kind := spec[2];;
  K := SmallGroup(12,kid);;
  autK := AutomorphismGroup(K);;
  allowedK := autK;
  z := One(K);;
  if kind="nonsplit" then
    z := First(Elements(Centre(K)),x->Order(x)=2);;
    allowedK := Stabilizer(autK,z);;
  fi;
  H := DirectProduct(K,P);;
  embK := Embedding(H,1);; embP := Embedding(H,2);;
  gensK := GeneratorsOfGroup(K);; gensP := GeneratorsOfGroup(P);;
  gensH := Concatenation(List(gensK,x->Image(embK,x)),
                         List(gensP,x->Image(embP,x)));;
  actionGens := [];;
  for a in GeneratorsOfGroup(allowedK) do
    imgs := Concatenation(List(gensK,x->Image(embK,Image(a,x))),
                          List(gensP,x->Image(embP,x)));
    Add(actionGens,GroupHomomorphismByImages(H,H,gensH,imgs));
  od;
  for b in GeneratorsOfGroup(autP) do
    imgs := Concatenation(List(gensK,x->Image(embK,x)),
                          List(gensP,x->Image(embP,Image(b,x))));
    Add(actionGens,GroupHomomorphismByImages(H,H,gensH,imgs));
  od;
  Print("CLASS_K=",IdGroup(K)," KIND=",kind,
        " H_ID=",IdGroup(H)," AUT_K_SIZE=",Size(autK),
        " Z_ORDER=",Order(z)," ALLOWED_K_SIZE=",Size(allowedK),
        " ALLOWED_K_DESC=",StructureDescription(allowedK),
        " AI_SIZE=",Size(allowedK)*Size(autP),
        " AI_PRODUCT_FACTORS=[",StructureDescription(allowedK),",",StructureDescription(autP),"]",
        " AI_GENERATORS=",Length(actionGens),
        " ALL_BIJECTIVE=",ForAll(actionGens,IsBijective),"\n");
od;
Print("RUN_COMPLETE=true\n");
QUIT;
