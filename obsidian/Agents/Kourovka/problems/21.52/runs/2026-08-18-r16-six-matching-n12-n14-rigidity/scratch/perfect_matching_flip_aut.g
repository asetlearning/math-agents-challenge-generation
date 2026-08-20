# Exact GRAPE/nauty certificate for the perfect-matching four-point flip graph.
# Usage: gap -q -c 'n:=12;; Read("perfect_matching_flip_aut.g");'

if LoadPackage("grape") <> true then
  Error("GRAPE unavailable");
fi;

if not IsBound(n) then
  Error("set global n to 12 or 14 before reading this file");
fi;
if not n in [12,14] then
  Error("n must be 12 or 14");
fi;
m := n/2;

G := SymmetricGroup(n);
base := List([1..m], i -> [2*i-1,2*i]);
vertices := Orbit(G,base,OnSetsSets);
acthom := ActionHomomorphism(G,vertices,OnSetsSets);
nat := Image(acthom);
ker := Kernel(acthom);

rel := function(x,y)
  return Length(Intersection(x,y)) = m-2;
end;

gamma := Graph(G,vertices,OnSetsSets,rel,true);
if gamma.group <> nat then
  Error("GRAPE induced action differs from independently formed natural action");
fi;
if not IsSimpleGraph(gamma) then
  Error("flip graph is not simple");
fi;

degree := VertexDegree(gamma,1);
edge_count := gamma.order * degree / 2;
aut := AutGroupGraph(gamma);

Print("n=",n,"\n");
Print("vertices=",gamma.order," expected=",Product([1,3..n-1]),"\n");
Print("degree=",degree," expected=",2*Binomial(m,2)," edges=",edge_count,"\n");
Print("natural_kernel_size=",Size(ker)," natural_order=",Size(nat)," expected=",Factorial(n),"\n");
Print("natural_is_subgroup_of_full=",IsSubgroup(aut,nat),"\n");
Print("full_aut_order=",Size(aut),"\n");
Print("natural_equals_full=",nat=aut,"\n");
Print("full_is_transitive=",IsTransitive(aut,[1..gamma.order]),"\n");

QUIT;
