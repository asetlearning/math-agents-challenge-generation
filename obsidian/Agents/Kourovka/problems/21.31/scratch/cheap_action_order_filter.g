hids := [17,19,27,29,38];;
Print("GAP_VERSION=",GAPInfo.Version,"\n");
for hid in hids do
  H := SmallGroup(252,hid);;
  qorders := Set(List(NormalSubgroups(H),L->Index(H,L)));;
  possiblePairs := 0;; zeroPairs := [];;
  for mid in [1..46] do
    M := SmallGroup(252,mid);; ao := Size(AutomorphismGroup(M));;
    poss := Filtered(qorders,x->x>1 and IsInt(ao/x));;
    if Length(poss)=0 and mid<>hid then Add(zeroPairs,mid);
    else possiblePairs:=possiblePairs+1; fi;
  od;
  Print("H_ID=",IdGroup(H)," QUOTIENT_ORDERS=",qorders,
        " DIVISIBILITY_SURVIVORS=",possiblePairs,
        " ZERO_M_IDS=",zeroPairs,"\n");
od;
QUIT;
