LoadPackage("grape");
H := EdgeOrbitsGraph(Group([
 (1,19,47,48,5,38,12,13,22,44,40,34,20,32,33,42,4,18,11,10)(2,3,35,8,23,31,36,25,50,26,14,45,27,49,6,46,21,28,24,15)(7,29,41,39,30)(9,37,16,17,43),
 (1,32,19)(2,49,35)(3,6,18)(4,39,38,8,25,23)(5,21,29,7,44,46)(9,43,27,20,22,50)(11,36,45,13,37,28)(12,40,14,16,31,47)(15,48)(17,34,41,26,33,24)(30,42)
]),[[1,2]]);
Print("HS vertices=",OrderGraph(H)," degree=",VertexDegree(H,1)," DR=",IsDistanceRegular(H),"\n");
C := ComplementGraph(H);
cocReps := CompleteSubgraphsOfGivenSize(C,15);
aut := AutGroupGraph(H);
cocs := Set(Concatenation(List(cocReps,S->Orbit(aut,S,OnSets))));
Print("15-coclique orbit_representatives=",Length(cocReps)," aut_order=",Size(aut),"\n");
Print("15-cocliques=",Length(cocs)," incidence_count_vertex1=",Number(cocs,S->1 in S),"\n");
ints := [];
for i in [1..Length(cocs)] do for j in [i+1..Length(cocs)] do AddSet(ints,Length(Intersection(cocs[i],cocs[j]))); od; od;
Print("distinct pairwise intersections=",ints,"\n");
Print("cocliques containing vertex 1:\n");
for S in Filtered(cocs,S->1 in S) do Print(S,"\n"); od;
