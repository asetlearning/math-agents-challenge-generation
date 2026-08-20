Print("GAP ",GAPInfo.Version,"\n");
ids := [[48,31],[96,69],[96,73],[96,74],[96,196],
[192,188],[192,191],[192,192],[192,193],[192,200],[192,203],[192,204],
[192,993],[192,994],[192,995],[192,996],[192,997],[192,998],[192,999],
[192,1010],[192,1011],[192,1012],[192,1013],[192,1496],[192,1505]];
idC:=IdGroup(CyclicGroup(12));; idA:=IdGroup(AlternatingGroup(4));;
pairs:=0;; equald:=0;;
for gi in ids do
  G:=SmallGroup(gi[1],gi[2]); nc:=[];; na:=[];;
  for H in NormalSubgroups(G) do
    if Index(G,H)=12 then
      qid:=IdGroup(FactorGroup(G,H));
      if qid=idC then Add(nc,H); fi; if qid=idA then Add(na,H); fi;
    fi;
  od;
  for K in nc do for L in na do
    M:=ClosureGroup(K,L);
    if Index(G,M)=3 and IsPGroup(M) then
      pairs:=pairs+1;
      pK:=FrattiniSubgroup(K);; pL:=FrattiniSubgroup(L);;
      dK:=LogInt(Index(K,pK),2);; dL:=LogInt(Index(L,pL),2);;
      pM:=FrattiniSubgroup(M);;
      eK:=LogInt(Index(Intersection(K,pM),pK),2);;
      eL:=LogInt(Index(pM,pL),2);;
      if dK=dL then equald:=equald+1; fi;
      if eL=eK+1 then
        Print("CORRECTION G=",gi," K=",IdGroup(K)," L=",IdGroup(L),
          " der=",[Size(DerivedSubgroup(K)),Size(DerivedSubgroup(L))],
          " squares=",[Size(Subgroup(K,List(Elements(K),x->x^2))),Size(Subgroup(L,List(Elements(L),x->x^2)))],"\n");
      fi;
      Print("PAIR G=",gi," K=",IdGroup(K)," L=",IdGroup(L),
        " M=",IdGroup(M)," dK=",dK," dL=",dL,
        " eK=",eK," eL=",eL," equal=",dK=dL,"\n");
    fi;
  od; od;
od;
Print("SUMMARY minimal_shape_pairs=",pairs," equal_d=",equald,"\n");
QUIT;
