T := SmallGroup(168,42);
P := Representative(First(ConjugacyClassesSubgroups(T), c -> Size(Representative(c))=21));
autT := AutomorphismGroup(T);
stabTP := Filtered(Elements(autT), a -> Image(a,P)=P);
gensP := GeneratorsOfGroup(P);
restrictions := List(stabTP, a -> GroupHomomorphismByImages(P,P,gensP,List(gensP,x->Image(a,x))));
restrictionGroup := Group(restrictions);
identityRestrictionCount := Number(restrictions, r -> IsOne(r));

Print("GAP_VERSION=", GAPInfo.Version, "\n");
Print("T_ID=", IdGroup(T), " AUT_T_SIZE=", Size(autT),
      " P_ID=", IdGroup(P), " AUT_P_SIZE=", Size(AutomorphismGroup(P)), "\n");
Print("AUT_T_P_SIZE=", Length(stabTP),
      " RESTRICTION_IMAGE_SIZE=", Size(restrictionGroup),
      " RESTRICTION_KERNEL_SIZE=", identityRestrictionCount, "\n");

if IsBound(TEST_SPECS) then
  specs := TEST_SPECS;
else
  specs := [ [1,"split"],[1,"nonsplit"], [2,"split"],[2,"nonsplit"],
             [3,"split"], [4,"split"],[4,"nonsplit"],
             [5,"split"],[5,"nonsplit"] ];
fi;
for spec in specs do
  kid := spec[1]; kind := spec[2];
  K := SmallGroup(12,kid);
  autK := AutomorphismGroup(K);
  z := One(K);
  if kind="nonsplit" then z := First(Elements(Centre(K)),x->Order(x)=2); fi;
  allowed := Stabilizer(autK,z);
  H := DirectProduct(K,P);
  embK := Embedding(H,1); embP := Embedding(H,2);
  gensK := GeneratorsOfGroup(K); gensP2 := GeneratorsOfGroup(P);
  gensH := Concatenation(List(gensK,x->Image(embK,x)),List(gensP2,x->Image(embP,x)));
  mapsK := List(GeneratorsOfGroup(allowed), a ->
    GroupHomomorphismByImages(H,H,gensH,
      Concatenation(List(gensK,x->Image(embK,Image(a,x))),List(gensP2,x->Image(embP,x)))));
  mapsP := List(GeneratorsOfGroup(AutomorphismGroup(P)), b ->
    GroupHomomorphismByImages(H,H,gensH,
      Concatenation(List(gensK,x->Image(embK,x)),List(gensP2,x->Image(embP,Image(b,x))))));
  generated := Group(Concatenation(mapsK,mapsP));
  Print("K_ID=", IdGroup(K), " KIND=", kind,
        " Z_ORDER=", Order(z), " AUT_K_SIZE=", Size(autK),
        " STAB_Z_SIZE=", Size(allowed), " AUT_P_SIZE=", Size(AutomorphismGroup(P)),
        " EXPECTED_AI_SIZE=", Size(allowed)*Size(AutomorphismGroup(P)),
        " GENERATED_AI_SIZE=", Size(generated),
        " GENERATORS=", Length(GeneratorsOfGroup(generated)),
        " ALL_GENERATORS_BIJECTIVE=", ForAll(GeneratorsOfGroup(generated),IsBijective), "\n");
od;
Print("RUN_COMPLETE=true\n");
QUIT;
