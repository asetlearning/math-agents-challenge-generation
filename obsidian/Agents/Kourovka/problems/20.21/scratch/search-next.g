Print("GAP ", GAPInfo.Version, "\n");
targetC := IdGroup(CyclicGroup(12));; targetA := IdGroup(AlternatingGroup(4));;
tested:=0;; withBoth:=0;; found:=0;;
for n in [288,300,312,324,336,348,360] do
  Print("ORDER ",n," GROUPS ",NumberSmallGroups(n),"\n");
  for i in [1..NumberSmallGroups(n)] do
    G:=SmallGroup(n,i); tested:=tested+1; nc:=[];; na:=[];;
    for N in NormalSubgroups(G) do
      if Index(G,N)=12 then
        qid:=IdGroup(FactorGroup(G,N));
        if qid=targetC then Add(nc,N); fi; if qid=targetA then Add(na,N); fi;
      fi;
    od;
    if Length(nc)>0 and Length(na)>0 then
      withBoth:=withBoth+1;
      for K in nc do for L in na do
        if IdGroup(K)=IdGroup(L) then
          found:=found+1; Print("HIT SmallGroup(",n,",",i,") kernel=",IdGroup(K),"\n");
        fi;
      od; od;
    fi;
  od;
od;
Print("SUMMARY tested=",tested," with_both=",withBoth," hits=",found,"\n");
QUIT;
