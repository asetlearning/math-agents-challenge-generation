NO_QUIT := true;
LoadPackage("grape");
Read("Agents/Kourovka/problems/21.90/scratch/hoffman_singleton_local.g");

D := DerivedSubgroup(aut);
orbs := Orbits(D,cocs,OnSets);
Print("derived_order=",Size(D)," coclique_orbit_sizes=",List(orbs,Length)," vertex_orbit_sizes=",List(Orbits(D,[1..50]),Length),"\n");
stab := Stabilizer(D,1);
fixed := Filtered(cocs,S->ForAll(GeneratorsOfGroup(stab),g->OnSets(S,g)=S));
Print("cocliques fixed by vertex-1 stabilizer=",Length(fixed),"\n");

SRGParams := function(g)
  local V,k,adj,lams,mus,x,y,c;
  V:=[1..OrderGraph(g)]; k:=Length(Adjacency(g,1)); lams:=[]; mus:=[];
  if not ForAll(V,x->Length(Adjacency(g,x))=k) then return fail; fi;
  for x in V do adj:=Adjacency(g,x); for y in [x+1..OrderGraph(g)] do
    c:=Length(Intersection(adj,Adjacency(g,y)));
    if y in adj then AddSet(lams,c); else AddSet(mus,c); fi;
  od; od;
  if Length(lams)=1 and Length(mus)=1 then return [OrderGraph(g),k,lams[1],mus[1]]; fi;
  return ["notSRG",k,lams,mus];
end;

for C1 in fixed do
  assign := [];
  for x in [1..50] do
    g := RepresentativeAction(D,1,x);
    assign[x] := OnSets(C1,g);
  od;
  symmetric := ForAll([1..50],x->ForAll([1..50],y->((y in assign[x])=(x in assign[y]))));
  intsets := [];
  for x in [1..50] do for y in [x+1..50] do AddSet(intsets,Length(Intersection(assign[x],assign[y]))); od; od;
  Print("C1=",C1," contains1=",1 in C1," symmetric=",symmetric," assignment_intersections=",intsets);
  if symmetric and ForAll(assign,x->Length(x)=15) then
    G := Graph(Group(()),[1..50],function(x,z)return x;end,function(x,y)return x<>y and y in assign[x];end,true);
    Print(" degree=",VertexDegree(G,1)," DR=",IsDistanceRegular(G)," G2=",SRGParams(DistanceGraph(G,[2]))," G3=",SRGParams(DistanceGraph(G,[3]))," G3_is_HS=",IsIsomorphicGraph(DistanceGraph(G,[3]),H));
  fi;
  Print("\n");
od;
QUIT;
