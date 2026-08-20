# Exact arithmetic for IA {77,60,13;1,12,65}.
x:=Indeterminate(Rationals,"x");;
k:=77;; b1:=60;; b2:=13;; c1:=1;; c2:=12;; c3:=65;;
a1:=k-b1-c1;; a2:=k-b2-c2;; a3:=k-c3;;
k2:=k*b1/c2;; k3:=k2*b2/c3;; v:=1+k+k2+k3;;
L:=[[0,k,0,0],[c1,a1,b1,0],[0,c2,a2,b2],[0,0,c3,a3]];;
fac:=Factors(CharacteristicPolynomial(L));;
eig:=List(fac,function(f) local cc; cc:=CoefficientsOfUnivariatePolynomial(f); return -cc[1]/cc[2]; end);;
nonprincipal:=Difference(eig,[k]);;
mult:=SolutionMat(TransposedMat([List([1..3],i->1),nonprincipal,List(nonprincipal,z->z^2)]),[v-1,-k,v*k-k^2]);;
p2:=z->(z^2-a1*z-k)/c2;;
p3:=z->((z-a2)*p2(z)-b1*z)/c3;;
Print("IA={77,60,13;1,12,65} a=",[0,a1,a2,a3]," layers=",[1,k,k2,k3]," v=",v,"\n");
Print("handshakes=",[k*a1,k2*a2,k3*a3]," parities=",List([k*a1,k2*a2,k3*a3],z->z mod 2),"\n");
Print("A1_eig=",eig," mult=",Concatenation([1],mult),"\n");
Print("A2_eig=",List(eig,p2)," A3_eig=",List(eig,p3),"\n");
Print("Gamma2_srg=[540,385,280,260] spectrum=[385^1,25^77,-5^462]\n");
Print("Gamma3_srg=[540,77,4,12] spectrum=[77^1,5^385,-13^154]\n");
Print("A1plusA3_srg=[540,154,28,50] spectrum=[154^1,4^462,-26^77]\n");
Print("induced_relation_degrees_rows_layer1_layer2_layer3=",
      [[16,60,0],[52,280,52],[12,60,4]],"\n");
Print("all_induced_handshakes=",
      [[77*16,77*60,77*0],[385*52,385*280,385*52],
       [77*12,77*60,77*4]],"\n");
Print("M_spectrum=[78^1,18^77,0^385,-12^77] rankQ=155\n");
Print("identities: X2=65I+4X+12J-12B; XB=13J-13I-13X-B\n");
Print("identities: M(B+13I)=13J; M2=60I+6M+12J-12B\n");
Print("identities: B2=65I-8B+12J; D2=72I-6D+12J; MD=13J-12M\n");
QUIT;
