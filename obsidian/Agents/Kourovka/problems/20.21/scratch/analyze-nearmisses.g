ids := [[48,31],[96,69],[96,73],[96,74],[96,196],[144,34],[144,129],[144,155],
[192,188],[192,191],[192,192],[192,193],[192,200],[192,203],[192,204],
[192,993],[192,994],[192,995],[192,996],[192,997],[192,998],[192,999],
[192,1010],[192,1011],[192,1012],[192,1013],[192,1496],[192,1505],
[240,110],[240,152],[240,193]];
idC := IdGroup(CyclicGroup(12));; idA := IdGroup(AlternatingGroup(4));;
sameab := 0;; totalpairs := 0;;
for gi in ids do
  G:=SmallGroup(gi[1],gi[2]); nc:=[];; na:=[];;
  for H in NormalSubgroups(G) do
    if Index(G,H)=12 then
      q:=IdGroup(FactorGroup(G,H));
      if q=idC then Add(nc,H); fi; if q=idA then Add(na,H); fi;
    fi;
  od;
  for K in nc do for L in na do
    totalpairs:=totalpairs+1; if AbelianInvariants(K)=AbelianInvariants(L) then sameab:=sameab+1; fi;
    N:=Intersection(K,L); Q:=FactorGroup(G,N);
    Print("G=",gi," K=",IdGroup(K)," L=",IdGroup(L)," |N|=",Order(N),
      " |G/N|=",Order(Q)," Q=",IdGroup(Q),
      " Kab=",AbelianInvariants(K)," Lab=",AbelianInvariants(L),
      " Kder=",Size(DerivedSubgroup(K))," Lder=",Size(DerivedSubgroup(L)),"\n");
  od; od;
od;
Print("SUMMARY pairs=",totalpairs," same_abelianization=",sameab,"\n");
QUIT;
