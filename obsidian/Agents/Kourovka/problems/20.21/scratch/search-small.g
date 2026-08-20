Print("GAP ", GAPInfo.Version, "\n");
targetC := IdGroup(CyclicGroup(12));
targetA := IdGroup(AlternatingGroup(4));
Print("target quotient IDs: C12=", targetC, ", A4=", targetA, "\n");
tested := 0;
withBoth := 0;
found := 0;
for n in [12,24..240] do
  if NumberSmallGroups(n) <> fail then
    Print("ORDER ", n, " GROUPS ", NumberSmallGroups(n), "\n");
    for i in [1..NumberSmallGroups(n)] do
      G := SmallGroup(n,i);
      tested := tested + 1;
      nc := [];; na := [];;
      for N in NormalSubgroups(G) do
        if Index(G,N)=12 then
          qid := IdGroup(FactorGroup(G,N));
          if qid=targetC then Add(nc,N); fi;
          if qid=targetA then Add(na,N); fi;
        fi;
      od;
      if Length(nc)>0 and Length(na)>0 then
        withBoth := withBoth+1;
        hit := false;
        for K in nc do for L in na do
          if IdGroup(K)=IdGroup(L) then
            Print("HIT SmallGroup(",n,",",i,") kernels ",IdGroup(K),"\n");
            found := found+1; hit:=true;
          fi;
        od; od;
        if not hit then
          Print("NEARMISS SmallGroup(",n,",",i,") C-kernels ",List(nc,IdGroup)," A-kernels ",List(na,IdGroup),"\n");
        fi;
      fi;
    od;
  fi;
od;
Print("SUMMARY tested=",tested," with_both_quotients=",withBoth," hits=",found,"\n");
QUIT;
