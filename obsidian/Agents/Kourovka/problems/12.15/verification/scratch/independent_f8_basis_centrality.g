ids := [53342,53343,53355,53356,53357,53358,53359];;
Print("GAP_VERSION=",GAPInfo.Version,"\n");

for id in ids do
  base := SmallGroup(256,id);
  bpcgs := Pcgs(base);
  n := Length(bpcgs);
  f8 := bpcgs[n];
  mats := List(bpcgs, x -> IdentityMat(1,GF(2)));
  modu := GModuleByMats(mats,GF(2));
  coh := TwoCohomology(base,modu);
  cspace := Image(coh.cohom);
  cbasis := BasisVectors(Basis(cspace));
  noncentralBasis := [];

  for j in [1..Length(cbasis)] do
    cocycle := PreImagesRepresentative(coh.cohom,cbasis[j]);
    ext := ExtensionSQ(coh.collector,base,modu,cocycle);
    epcgs := Pcgs(ext);
    lifts := epcgs{[1..n]};
    ef8 := MappedPcElement(f8,bpcgs,lifts);
    if ForAny(bpcgs, k -> not IsOne(Comm(ef8,
         MappedPcElement(k,bpcgs,lifts)))) then
      Add(noncentralBasis,j);
    fi;
  od;

  Print("BASE=[256,",id,"]",
        " H2_DIM=",Length(cbasis),
        " F8=",f8,
        " F8_BASE_CENTRAL=",f8 in Centre(base),
        " NONCENTRAL_BASIS_CLASS_INDICES=",noncentralBasis,
        " ALL_BASIS_LIFTS_CENTRAL=",Length(noncentralBasis)=0,"\n");
od;
Print("RUN_COMPLETE=true\n");
QUIT;
