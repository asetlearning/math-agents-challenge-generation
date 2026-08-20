F := FreeGroup("z","a","u","v","r","k","l");;
z:=F.1;; a:=F.2;; u:=F.3;; v:=F.4;; r:=F.5;; k:=F.6;; l:=F.7;;
rels := [
  z^2, a^2, u^2, v^2, r^2, k^2, l^2,
  Comm(z,a), Comm(z,u), Comm(z,v), Comm(z,r), Comm(z,k), Comm(z,l),
  Comm(a,u), Comm(a,v), Comm(a,k), Comm(a,l), Comm(a,r)/z,
  Comm(u,v)/z,
  Comm(u,r), Comm(v,r),
  Comm(u,k), Comm(v,k)/a,
  Comm(u,l)/(a*z), Comm(v,l),
  Comm(r,k)/u, Comm(r,l)/v, Comm(k,l)
];;
Gfp := F/rels;;
iso := IsomorphismPcGroup(Gfp);;
if iso = fail then
  Print("pc=fail\n");
  QUIT_GAP(1);
fi;
G := Image(iso);;
im := List(GeneratorsOfGroup(Gfp), x -> Image(iso,x));;
Print("size=", Size(G), " derived=", Size(DerivedSubgroup(G)),
      " centre=", Size(Centre(G)), " class=", NilpotencyClassOfGroup(G), "\n");
Print("orders=", List(im,Order), " H=", Size(Subgroup(G,im{[1..4]})),
      " Eindex=", Index(G,Subgroup(G,im{[1..4]})), "\n");
els := Elements(G);;
found := false;;
for i in [1..Length(els)] do
  ni := NormalClosure(G,Subgroup(G,[els[i]]));
  for j in [i+1..Length(els)] do
    nj := NormalClosure(G,Subgroup(G,[els[j]]));
    if ni=nj and not IsConjugate(G,els[i],els[j]) then
      Print("witness-x=", PreImagesRepresentative(iso,els[i]),
            " y=", PreImagesRepresentative(iso,els[j]), "\n");
      Print("orders=",Order(els[i]),",",Order(els[j]),
            " classes=",Size(ConjugacyClass(G,els[i])),",",Size(ConjugacyClass(G,els[j])),
            " normal=",Size(ni)," gens=",List(GeneratorsOfGroup(ni), x->PreImagesRepresentative(iso,x)),"\n");
      Print("centralizer-x=",Size(Centralizer(G,els[i]))," ",List(GeneratorsOfGroup(Centralizer(G,els[i])),x->PreImagesRepresentative(iso,x)),"\n");
      Print("centralizer-y=",Size(Centralizer(G,els[j]))," ",List(GeneratorsOfGroup(Centralizer(G,els[j])),x->PreImagesRepresentative(iso,x)),"\n");
      Print("defects-x=",List(im, g->PreImagesRepresentative(iso,Comm(els[i],g))),"\n");
      Print("defects-y=",List(im, g->PreImagesRepresentative(iso,Comm(els[j],g))),"\n");
      Print("class-x=",List(AsList(ConjugacyClass(G,els[i])),x->PreImagesRepresentative(iso,x)),"\n");
      Print("class-y=",List(AsList(ConjugacyClass(G,els[j])),x->PreImagesRepresentative(iso,x)),"\n");
      found := true;
      break;
    fi;
  od;
  if found then break; fi;
od;
