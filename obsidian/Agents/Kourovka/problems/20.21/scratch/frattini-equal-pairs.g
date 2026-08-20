ids := [[96,69],[192,996]];;
idC:=IdGroup(CyclicGroup(12));; idA:=IdGroup(AlternatingGroup(4));;
PhiSizes:=function(X)
 local a,Y,Z; a:=[Size(X)]; Y:=X;
 while Size(Y)>1 do Z:=FrattiniSubgroup(Y); Add(a,Size(Z)); Y:=Z; od;
 return a;
end;;
ModuleSig:=function(X,c)
 local ans,Y,P,fix,dim,fdim;
 ans:=[]; Y:=X;
 while Size(Y)>1 do
  P:=FrattiniSubgroup(Y);
  fix:=Filtered(Elements(Y),x -> (x^c)*x^-1 in P);
  dim:=LogInt(Index(Y,P),2); fdim:=LogInt(Length(fix)/Size(P),2);
  Add(ans,[dim,fdim,(dim-fdim)/2]); Y:=P;
 od;
 return ans;
end;;
for gi in ids do
 G:=SmallGroup(gi[1],gi[2]); nc:=[];;na:=[];;
 for H in NormalSubgroups(G) do
  if Index(G,H)=12 then q:=IdGroup(FactorGroup(G,H));
   if q=idC then Add(nc,H);fi; if q=idA then Add(na,H);fi;
  fi;
 od;
 for K in nc do for L in na do
  if LogInt(Index(K,FrattiniSubgroup(K)),2)=LogInt(Index(L,FrattiniSubgroup(L)),2) then
   M:=ClosureGroup(K,L);; c:=First(Elements(SylowSubgroup(G,3)),x->Order(x)=3);;
   Print("PAIR G=",gi," K=",IdGroup(K)," ",StructureDescription(K),
    " L=",IdGroup(L)," ",StructureDescription(L),"\n");
   Print("  PhiSeriesK=",PhiSizes(K)," PhiSeriesL=",PhiSizes(L),"\n");
   Print("  PCentralK=",List(PCentralSeries(K,2),Size),
    " PCentralL=",List(PCentralSeries(L,2),Size),"\n");
   Print("  LowerCentralK=",List(LowerCentralSeries(K),Size),
    " LowerCentralL=",List(LowerCentralSeries(L),Size),"\n");
   Print("  centerK=",Size(Centre(K))," centerL=",Size(Centre(L)),
    " expK=",Exponent(K)," expL=",Exponent(L),"\n");
   Print("  C3PhiSig [dim,fixed,triv?rem/2]: K=",ModuleSig(K,c),
    " L=",ModuleSig(L,c),"\n");
  fi;
 od;od;
od;
QUIT;
