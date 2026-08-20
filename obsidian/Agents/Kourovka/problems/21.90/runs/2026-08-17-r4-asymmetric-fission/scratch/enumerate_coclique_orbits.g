LoadPackage("grape");

# Construct the reviewed standard srg(300,65,10,15): nonsquare-type
# projective points for Q=x1*x2+x3*x4+x5^2 over GF(5), adjacent when
# perpendicular under the polar form.
pts := [];
for x1 in [0..4] do for x2 in [0..4] do for x3 in [0..4] do
for x4 in [0..4] do for x5 in [0..4] do
  x := [x1,x2,x3,x4,x5];
  pos := First([1..5],i->x[i]<>0);
  if pos<>fail and x[pos]=1 then Add(pts,x); fi;
od; od; od; od; od;

Q := x -> (x[1]*x[2]+x[3]*x[4]+x[5]^2) mod 5;
Polar := function(x,y)
  return (x[1]*y[2]+x[2]*y[1]+x[3]*y[4]+x[4]*y[3]
          +2*x[5]*y[5]) mod 5;
end;

types := List([0..4],q->Filtered(pts,x->Q(x)=q));
chosen := Concatenation(types[3],types[4]); # Q-values 2 and 3
Bgraph := Graph(Group(()),chosen,function(x,g) return x; end,
  function(x,y) return x<>y and Polar(x,y)=0; end,true);

degrees := Set(List([1..Bgraph.order],u->Length(Adjacency(Bgraph,u))));
common := Set(List(Combinations([1..Bgraph.order],2),uv->
  Length(Intersection(Adjacency(Bgraph,uv[1]),Adjacency(Bgraph,uv[2])))));
Print("vertices=",Bgraph.order," degrees=",degrees," common_counts=",common,"\n");
if Bgraph.order<>300 or degrees<>[65] or common<>[10,15] then
  Error("standard constituent check failed");
fi;

aut := AutGroupGraph(Bgraph);
Print("aut_order=",Size(aut)," vertex_orbit=",Length(Orbit(aut,1)),"\n");
Kgraph := NewGroupGraph(aut,ComplementGraph(Bgraph));

start := Runtime();
# alls=2 requests exactly one representative of every Aut(B)-orbit;
# maximal=false because the Hoffman bound already proves size 40 is maximum.
reps := CompleteSubgraphsOfGivenSize(Kgraph,40,2,false);
Print("orbit_representatives=",Length(reps)," runtime_ms=",Runtime()-start,"\n");

if Length(reps)=0 then
  witness39 := CompleteSubgraphsOfGivenSize(Kgraph,39,0,false);
  Print("size39_witness_count=",Length(witness39),
        " witness=",witness39," runtime_ms=",Runtime()-start,"\n");
  maxc := MaximumClique(Kgraph);
  Print("maximum_coclique_size=",Length(maxc)," witness=",maxc,
        " runtime_ms=",Runtime()-start,"\n");
  direct_start := Runtime();
  Ktrivial := NewGroupGraph(Group(()),ComplementGraph(Bgraph));
  direct40 := CompleteSubgraphsOfGivenSize(Ktrivial,40,0,false);
  Print("trivial_group_size40_count=",Length(direct40),
        " runtime_ms=",Runtime()-direct_start,"\n");
fi;

total := 0;
for i in [1..Length(reps)] do
  stab := Stabilizer(aut,Set(reps[i]),OnSets);
  osize := Size(aut)/Size(stab);
  total := total+osize;
  Print("ORBIT ",i," stabilizer=",Size(stab)," orbit_size=",osize,
        " representative=",reps[i],"\n");
od;
Print("total_cocliques=",total," total_runtime_ms=",Runtime()-start,"\n");
QUIT;
