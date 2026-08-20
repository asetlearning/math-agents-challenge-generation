Print("GAP_VERSION=", GAPInfo.Version, "\n");
Print("NUMBER_SMALL_GROUPS_252=", NumberSmallGroups(252), "\n");
target := SmallGroup(21,1);
Print("TARGET_21_ID=", IdGroup(target),
      " TARGET_21_STRUCTURE=", StructureDescription(target), "\n");
countGroups := 0;
countPairs := 0;
for i in [1..NumberSmallGroups(252)] do
  H := SmallGroup(252,i);
  matches := Filtered(NormalSubgroups(H),
             K -> Size(K)=12 and IdGroup(FactorGroup(H,K))=IdGroup(target));
  if Length(matches)>0 then
    countGroups := countGroups+1;
    countPairs := countPairs+Length(matches);
    Print("H_id=", IdGroup(H),
          " H_structure=", StructureDescription(H),
          " matching_normal_K=", Length(matches),
          " K_ids=", List(matches, IdGroup), "\n");
  fi;
od;
Print("MATCHING_H_GROUPS=", countGroups, "\n");
Print("MATCHING_HK_PAIRS=", countPairs, "\n");
QUIT;
