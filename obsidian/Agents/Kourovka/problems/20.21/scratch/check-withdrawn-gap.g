Print("GAP ",GAPInfo.Version,"\n");
orders := [4,8,12,16,24,36,48,60,72,84,96,108,120,132,144];
idC4 := IdGroup(CyclicGroup(4));;
idV4 := IdGroup(ElementaryAbelianGroup(4));;
total := 0;; pairs := 0;;
for n in orders do
  for i in [1..NumberSmallGroups(n)] do
    Q := SmallGroup(n,i); total := total+1;
    c := [];; v := [];;
    for H in NormalSubgroups(Q) do
      if Index(Q,H)=4 then
        qid := IdGroup(FactorGroup(Q,H));
        if qid=idC4 then Add(c,H); fi;
        if qid=idV4 then Add(v,H); fi;
      fi;
    od;
    for H1 in c do for H2 in v do
      if H1<>H2 then
        pairs:=pairs+1;
        Print("PAIR SmallGroup(",n,",",i,") kernel-order=",Order(H1),
              " H1-char=",IsCharacteristicSubgroup(Q,H1),
              " H2-char=",IsCharacteristicSubgroup(Q,H2),"\n");
      fi;
    od; od;
  od;
od;
Print("SUMMARY groups=",total," pairs=",pairs,"\n");
QUIT;
