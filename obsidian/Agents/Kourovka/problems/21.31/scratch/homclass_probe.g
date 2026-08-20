if not IsBound(HID) or not IsBound(MID) then
  Error("set integer globals HID and MID before reading this file");
fi;
hId := HID;
mId := MID;
H := SmallGroup(252,hId);
M := SmallGroup(252,mId);
A := AutomorphismGroup(M);
Print("GAP_VERSION=", GAPInfo.Version, " H_ID=", IdGroup(H),
      " M_ID=", IdGroup(M), " AUT_ORDER=", Size(A), "\n");
t := Runtime();
homs := AllHomomorphismClasses(H,A);
Print("HOM_CLASSES=",Length(homs)," RUNTIME_MS=",Runtime()-t,"\n");
Print("IMAGE_ORDERS=",Collected(List(homs,f->Size(Image(f)))),"\n");
QUIT;
