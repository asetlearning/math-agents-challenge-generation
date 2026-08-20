pairs := [ [2,2], [9,5], [11,5], [17,1], [19,2], [27,3], [29,4], [38,5], [40,5] ];
Print("GAP_VERSION=", GAPInfo.Version, "\n");
Print("SMALLGRP_VERSION=", InstalledPackageVersion("smallgrp"), "\n");
surviving := [];
eliminated := [];
for pair in pairs do
  H := SmallGroup(252, pair[1]);
  candidates := Filtered(NormalSubgroups(H), K ->
    IdGroup(K) = [12,pair[2]] and IdGroup(FactorGroup(H,K)) = [21,1]);
  passing := 0;
  ordersKC := [];
  for K in candidates do
    C := Centralizer(H,K);
    KC := ClosureGroup(K,C);
    Add(ordersKC, Size(KC));
    if KC = H then passing := passing + 1; fi;
  od;
  Print("PAIR=", [IdGroup(H),[12,pair[2]]],
        " CANDIDATE_K=", Length(candidates),
        " KC_ORDERS=", ordersKC,
        " PASSING_K=", passing, "\n");
  if passing = 0 then Add(eliminated, [252,pair[1]]);
  else Add(surviving, [252,pair[1]]); fi;
od;
Print("ELIMINATED_H=", eliminated, "\n");
Print("SURVIVING_H=", surviving, "\n");
QUIT;
