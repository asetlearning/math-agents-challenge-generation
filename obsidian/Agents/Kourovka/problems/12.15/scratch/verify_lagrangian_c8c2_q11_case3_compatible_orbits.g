# Independent permutation-domain check of the custom compatible-pair BFS.

Read("Agents/Kourovka/problems/12.15/scratch/pilot_lagrangian_c8c2_q11_case3_compatible_orbits.g");
h2permslag:=[];
for rowslag in actionrowslag do
  pimgslag:=List(coeffslag,v->
    MixedIndexLagComp(ApplyFactorMapLagComp(v,rowslag),lagrec.coh.factor.rels));
  Add(h2permslag,PermList(pimgslag));
od;
h2actlag:=Group(h2permslag);
h2orbitslag:=Orbits(h2actlag,[1..Length(coeffslag)]);
h2sizeslag:=List(h2orbitslag,Length);
Print("H2_PERMUTATION_ACTION_ORDER=",Size(h2actlag),
      " H2_PERMUTATION_ORBITS=",Length(h2orbitslag),
      " H2_PERMUTATION_ORBIT_SIZE_DISTRIBUTION=",Collected(h2sizeslag),
      " H2_PERMUTATION_COVERAGE=",Sum(h2sizeslag),"\n");
Print("BFS_PERMUTATION_ORBIT_COUNT_AGREE=",
      Length(h2orbitslag)=Length(orbitrepslag),
      " BFS_PERMUTATION_DISTRIBUTIONS_AGREE=",
      Collected(h2sizeslag)=Collected(orbitsizeslag),"\n");
