# Independent permutation-domain verification of the custom BFS compatible-
# pair orbit count on H^2(Q,C4xC2).

Read("Agents/Kourovka/problems/12.15/scratch/pilot_c4c2_q49_compatible_orbits.g");

h2perms49:=[];
for rows49 in actionrows49 do
  pimgs49:=List(coeffs49,v49->
    MixedIndexQ49(ApplyFactorMapQ49(v49,rows49),coh49.factor.rels));
  Add(h2perms49,PermList(pimgs49));
od;
h2act49:=Group(h2perms49);
h2orbits49:=Orbits(h2act49,[1..Length(coeffs49)]);
h2sizes49:=List(h2orbits49,Length);
Print("H2_PERMUTATION_ACTION_ORDER=",Size(h2act49),
      " H2_PERMUTATION_ORBITS=",Length(h2orbits49),
      " H2_PERMUTATION_ORBIT_SIZE_DISTRIBUTION=",Collected(h2sizes49),
      " H2_PERMUTATION_COVERAGE=",Sum(h2sizes49),"\n");
Print("BFS_PERMUTATION_ORBIT_COUNT_AGREE=",
      Length(h2orbits49)=Length(orbitreps49),
      " BFS_PERMUTATION_DISTRIBUTIONS_AGREE=",
      Collected(h2sizes49)=Collected(orbitsizes49),"\n");
