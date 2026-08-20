# Exact distance-graph SRG parameters for selected feasible intersection arrays.
SRGForRelation := function(ia,rel)
  local k,b1,b2,c2,c3,a1,a2,a3,k2,k3,v,B,fac,roots,eig,M,rhs,mult,
        p2,p3,P,vals,ppar,lam,mu;
  k:=ia[1]; b1:=ia[2]; b2:=ia[3]; c2:=ia[5]; c3:=ia[6];
  a1:=k-b1-1; a2:=k-b2-c2; a3:=k-c3;
  k2:=k*b1/c2; k3:=k2*b2/c3; v:=1+k+k2+k3;
  B:=[[0,k,0,0],[1,a1,b1,0],[0,c2,a2,b2],[0,0,c3,a3]];
  fac:=Factors(CharacteristicPolynomial(B));
  roots:=List(fac,f->-CoefficientsOfUnivariatePolynomial(f)[1]/CoefficientsOfUnivariatePolynomial(f)[2]);
  eig:=Concatenation([k],Difference(roots,[k]));
  M:=[List([1..3],i->1),eig{[2..4]},List(eig{[2..4]},z->z^2)];
  rhs:=[v-1,-k,v*k-k^2]; mult:=Concatenation([1],SolutionMat(TransposedMat(M),rhs));
  p2:=z->(z^2-a1*z-k)/c2;
  p3:=z->((z-a2)*p2(z)-b1*z)/c3;
  P:=List(eig,z->[1,z,p2(z),p3(z)]); vals:=[1,k,k2,k3];
  ppar:=function(i,j,h) return Sum([1..4],e->mult[e]*P[e][i]*P[e][j]*P[e][h])/(v*vals[h]); end;
  lam:=ppar(rel,rel,rel); mu:=First(List([2..4],h->[h,ppar(rel,rel,h)]),z->z[1]<>rel and z[2]<>0);
  return [v,vals[rel],lam,mu[2]];
end;

arrays := [
 [39,25,10,1,5,30], [77,60,13,1,12,65], [19,6,8,1,1,12],
 [87,66,16,1,11,72], [119,96,18,1,16,102]
];
for ia in arrays do
  Print("IA={",ia{[1..3]},";",ia{[4..6]},"} G2=",SRGForRelation(ia,3)," G3=",SRGForRelation(ia,4),"\n");
od;
QUIT;
