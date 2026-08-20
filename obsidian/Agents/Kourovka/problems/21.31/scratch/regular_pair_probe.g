if not IsBound(HID) or not IsBound(MID) then
  Error("set integer globals HID and MID before reading this file");
fi;
H := SmallGroup(252,HID);;
M := SmallGroup(252,MID);;
A := AutomorphismGroup(M);;
Print("GAP_VERSION=",GAPInfo.Version," H_ID=",IdGroup(H),
      " M_ID=",IdGroup(M)," AUT_ORDER=",Size(A),"\n");
t0 := Runtime();;
homs := AllHomomorphismClasses(H,A);;
Print("HOM_CLASSES=",Length(homs)," HOM_RUNTIME_MS=",Runtime()-t0,"\n");
regularCount := 0;;
for j in [1..Length(homs)] do
  f := homs[j];;
  ext := SemidirectProduct(H,f,M);;
  hsub := Image(Embedding(ext,1));;
  msub := Image(Embedding(ext,2));;
  if not IsNormal(ext,msub) then Error("second embedded factor not normal"); fi;
  comps := ComplementClassesRepresentatives(ext,msub);;
  regs := Filtered(comps,C->Size(Intersection(C,hsub))=1);;
  if Length(regs)>0 then
    regularCount := regularCount+Length(regs);
    Print("ACTION_CLASS=",j," IMAGE_ORDER=",Size(Image(f)),
          " COMPLEMENT_CLASSES=",Length(comps),
          " REGULAR_CLASSES=",Length(regs),"\n");
  fi;
od;
Print("REGULAR_CLASSES_TOTAL=",regularCount,
      " TOTAL_RUNTIME_MS=",Runtime()-t0,"\n");
QUIT;
