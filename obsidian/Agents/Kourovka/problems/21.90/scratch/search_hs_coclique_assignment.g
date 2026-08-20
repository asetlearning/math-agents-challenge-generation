NO_QUIT := true;
LoadPackage("grape");
Read("Agents/Kourovka/problems/21.90/scratch/hoffman_singleton_local.g");

# Disjointness graph on the 100 maximum cocliques.
K := Graph(Group(()),[1..Length(cocs)],function(x,z)return x;end,
           function(i,j)return i<>j and IsEmpty(Intersection(cocs[i],cocs[j]));end,true);
comps := ConnectedComponents(K);
Print("disjointness_graph degree=",VertexDegree(K,1)," component_sizes=",List(comps,Length),"\n");

tested := 0; solutions := []; maxinc := 0; histogram := [];
for comp in comps do
  KC := Graph(Group(()),[1..50],function(x,z)return x;end,
              function(i,j)return i<>j and IsEmpty(Intersection(cocs[comp[i]],cocs[comp[j]]));end,true);
  iso := GraphIsomorphism(H,KC);
  isovalid := IsPerm(iso) and ForAll([1..50],x->Set(List(Adjacency(H,x),y->y^iso))=Set(Adjacency(KC,x^iso)));
  Print("component isomorphic_to_H=",IsPerm(iso)," explicit_iso_check=",isovalid,"\n");
  if IsPerm(iso) then
    for aa in aut do
      tested := tested+1;
      inc := Number([1..50],x->x in cocs[comp[(x^aa)^iso]]);
      maxinc := Maximum(maxinc,inc);
      if not IsBound(histogram[inc+1]) then histogram[inc+1]:=0; fi;
      histogram[inc+1]:=histogram[inc+1]+1;
      if inc=50 then
        Add(solutions,List([1..50],x->comp[(x^aa)^iso]));
      fi;
    od;
  fi;
od;
Print("isomorphisms_tested=",tested," incidence_compatible_solutions=",Length(solutions),"\n");
Print("maximum_incidence_conditions_met=",maxinc," histogram(index=count+1)=",histogram,"\n");
if not IsEmpty(solutions) then Print("first_solution=",solutions[1],"\n"); fi;
QUIT;
