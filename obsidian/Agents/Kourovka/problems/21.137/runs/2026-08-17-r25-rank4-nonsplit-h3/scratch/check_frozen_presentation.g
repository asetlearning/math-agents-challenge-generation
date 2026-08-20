# Exact frozen presentation diagnostic for RANK4-NONSPLIT-H3.
F := FreeGroup("e1","e2","f1","f2","c","s","t","X","Y","Z");;
e1:=F.1;; e2:=F.2;; f1:=F.3;; f2:=F.4;; c:=F.5;; s:=F.6;; t:=F.7;;
xx:=F.8;; yy:=F.9;; zz:=F.10;;

rels := [];;
Append(rels,[e1^3,e2^3,f1^3,f2^3,c^3,s^3,t^3]);;
Append(rels,[Comm(e1,f1)*c^-1,Comm(e2,f2)*c^-1]);;
Append(rels,[Comm(e1,e2),Comm(e1,f2),Comm(e2,f1),Comm(f1,f2)]);;
for v in [e1,e2,f1,f2] do
  for zc in [c,s,t] do Add(rels,Comm(v,zc)); od;
od;
Append(rels,[Comm(c,s),Comm(c,t),Comm(s,t)]);;

imgsX := [e1*s,e1*e2*s,f1*f2^2,f2,c,c^2*s,s*t];;
imgsY := [e1*s,e2,e2*f1,e1*f2,c,c*s,s*t];;
imgsZ := [e1,e2*s^2,e1^2*f1*c^2,f2*s,c,s,c*t];;
kgens := [e1,e2,f1,f2,c,s,t];;
for i in [1..7] do
  Add(rels,xx*kgens[i]*xx^-1*imgsX[i]^-1);
  Add(rels,yy*kgens[i]*yy^-1*imgsY[i]^-1);
  Add(rels,zz*kgens[i]*zz^-1*imgsZ[i]^-1);
od;

kxy := e1^2*f1^2*f2*c;;
kxz := e2^2*f2^2*c;;
kyz := e2*f2*c;;
Append(rels,[xx^3*f2^-1,yy^3*e2^-1,zz^3,
             Comm(xx,yy)*zz^-1*kxy^-1,
             Comm(xx,zz)*kxz^-1,
             Comm(yy,zz)*kyz^-1]);;

Gfp := F/rels;;
qs := PQuotient(Gfp,3,10);;
epi := EpimorphismQuotientSystem(qs);;
P := Image(epi);;
srcgens := GeneratorsOfGroup(Source(epi));;
img := List(srcgens,g->Image(epi,g));;
Kp := Subgroup(P,img{[1..7]});;
Qp := FactorGroup(P,Kp);;
Print("class-10 3-quotient order: ",Size(P),"\n");
Print("class-10 3-quotient class: ",NilpotencyClassOfGroup(P),"\n");
Print("descending-series ranks: ",qs!.RanksOfDescendingSeries,"\n");
Print("kernel-generator subgroup order: ",Size(Kp),"\n");
Print("quotient-by-kernel order: ",Size(Qp),"\n");
Print("generator orders: ",List(img,Order),"\n");
Print("c,s,t killed flags: ",List(img{[5..7]},IsOne),"\n");
Print("kernel derived/center orders: ",Size(DerivedSubgroup(Kp))," ",Size(Centre(Kp)),"\n");
QUIT;
