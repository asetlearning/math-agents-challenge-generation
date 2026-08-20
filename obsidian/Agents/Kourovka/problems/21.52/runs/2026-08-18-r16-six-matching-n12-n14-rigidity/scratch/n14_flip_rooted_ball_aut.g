# Exact rooted radius-two ball certificate in the perfect-matching flip graph K_14.
if LoadPackage("grape") <> true then Error("GRAPE unavailable"); fi;
n := 14;; m := 7;;
G := SymmetricGroup(n);
base := List([1..m], i -> [2*i-1,2*i]);
H := Stabilizer(G,base,OnSetsSets);

s1rep := [[1,3],[2,4],[5,6],[7,8],[9,10],[11,12],[13,14]];
s2arep := [[1,3],[2,4],[5,7],[6,8],[9,10],[11,12],[13,14]];
s2brep := [[1,3],[2,5],[4,6],[7,8],[9,10],[11,12],[13,14]];
s1 := Orbit(H,s1rep,OnSetsSets);
s2a := Orbit(H,s2arep,OnSetsSets);
s2b := Orbit(H,s2brep,OnSetsSets);
vertices := Concatenation([[base],s1,s2a,s2b]);
if Length(Set(vertices)) <> 743 then Error("ball representatives/orbits overlap"); fi;

acthom := ActionHomomorphism(H,vertices,OnSetsSets);
nat := Image(acthom);
ker := Kernel(acthom);
rel := function(x,y) return Length(Intersection(x,y))=m-2; end;
gamma := Graph(H,vertices,OnSetsSets,rel,true);
if gamma.group <> nat then Error("natural rooted-ball action mismatch"); fi;
colours := [[1], [2..1+Length(s1)],
            [2+Length(s1)..1+Length(s1)+Length(s2a)],
            [2+Length(s1)+Length(s2a)..gamma.order]];
aut := AutGroupGraph(gamma,colours);

Print("sphere_sizes=1,",Length(s1),",",Length(s2a),",",Length(s2b)," total=",gamma.order,"\n");
Print("root_degree=",VertexDegree(gamma,1),"\n");
Print("natural_H_order=",Size(H)," natural_ball_kernel=",Size(ker)," natural_ball_image_order=",Size(nat),"\n");
Print("natural_is_subgroup_of_rooted_ball_aut=",IsSubgroup(aut,nat),"\n");
Print("rooted_ball_aut_order=",Size(aut),"\n");
Print("natural_equals_rooted_ball_aut=",nat=aut,"\n");
QUIT;
