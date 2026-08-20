base := ElementaryAbelianGroup(4);
bpcgs := Pcgs(base);
n := Length(bpcgs);
mats := List(bpcgs, x -> IdentityMat(1,GF(2)));
modu := GModuleByMats(mats,GF(2));
coh := TwoCohomology(base,modu);
cspace := Image(coh.cohom);
classes := Elements(cspace);
centralCamina := [];

for j in [1..Length(classes)] do
  cocycle := PreImagesRepresentative(coh.cohom,classes[j]);
  ext := ExtensionSQ(coh.collector,base,modu,cocycle);
  ker := ModuleOfExtension(ext);
  z := GeneratorsOfGroup(ker)[1];
  pass := Size(Centre(ext))=2;
  if pass then
    for cc in ConjugacyClasses(ext) do
      x := Representative(cc);
      if not x in ker and not IsConjugate(ext,x,x*z) then
        pass := false;
        break;
      fi;
    od;
  fi;
  if pass then Add(centralCamina,[j,IdGroup(ext)]); fi;
od;

Print("GAP_VERSION=",GAPInfo.Version,
      " BASE_ID=",IdGroup(base),
      " H2_DIM=",Dimension(cspace),
      " H2_CLASSES=",Length(classes),"\n");
Print("CENTRAL_CAMINA_CLASS_COUNT=",Length(centralCamina),
      " CLASS_INDEX_AND_EXTENSION_ID=",centralCamina,"\n");
Print("RUN_COMPLETE=true\n");
QUIT;
