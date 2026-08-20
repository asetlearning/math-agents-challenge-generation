# Exact Bose--Mesner calculation for the hypothetical intersection array
# {35,27,6;1,9,30}.  Coefficient vectors use the basis A0,A1,A2,A3.
k := 35;; b1 := 27;; b2 := 6;; c2 := 9;; c3 := 30;;
a1 := k-b1-1;; a2 := k-b2-c2;; a3 := k-c3;;

# Left multiplication by N=A0+A1, using the intersection-array products.
TimesN := function(v)
  local w;
  w := ShallowCopy(v); # contribution of A0
  w[1] := w[1] + k*v[2];
  w[2] := w[2] + v[1] + a1*v[2] + b1*v[3];
  w[3] := w[3] + c2*v[2] + a2*v[3] + b2*v[4];
  w[4] := w[4] + c3*v[3] + a3*v[4];
  return w;
end;

R := [ [1,0,0,0], [1,1,0,0], [0,1,1,0], [0,0,1,1], [0,0,0,1] ];
Print("IA={",k,",",b1,",",b2,";1,",c2,",",c3,"} a=[0,",a1,",",a2,",",a3,"]\n");
for i in [1..5] do
  Print("N*R",i-1,"=",TimesN(R[i]),"\n");
od;
Print("recurrence: N R0=R1; N R1=36R0+9R2; N R2=35R1+30R3; N R3=27R2+36R4; N R4=6R3\n");
Print("bipartite_lift_IA={36,35,27,6;1,9,30,36}\n");
QUIT;
