# Exact GRAPE/nauty certificate for six-matchings of K_13 adjacent when five
# edges are common.

if LoadPackage("grape") <> true then Error("GRAPE unavailable"); fi;
n := 13;
k := 6;
G := SymmetricGroup(n);
base := List([1..k], i -> [2*i-1,2*i]);
vertices := Orbit(G,base,OnSetsSets);
acthom := ActionHomomorphism(G,vertices,OnSetsSets);
nat := Image(acthom);
ker := Kernel(acthom);
rel := function(x,y) return Length(Intersection(x,y)) = k-1; end;
gamma := Graph(G,vertices,OnSetsSets,rel,true);
if gamma.group <> nat then Error("natural action mismatch"); fi;
if not IsSimpleGraph(gamma) then Error("not simple"); fi;
degree := VertexDegree(gamma,1);
aut := AutGroupGraph(gamma);
Print("n=13 k=6\n");
Print("vertices=",gamma.order," expected=135135\n");
Print("degree=",degree," expected=12 edges=",gamma.order*degree/2,"\n");
Print("natural_kernel_size=",Size(ker)," natural_order=",Size(nat)," expected=",Factorial(n),"\n");
Print("natural_is_subgroup_of_full=",IsSubgroup(aut,nat),"\n");
Print("full_aut_order=",Size(aut),"\n");
Print("natural_equals_full=",nat=aut,"\n");
Print("full_is_transitive=",IsTransitive(aut,[1..gamma.order]),"\n");
QUIT;
