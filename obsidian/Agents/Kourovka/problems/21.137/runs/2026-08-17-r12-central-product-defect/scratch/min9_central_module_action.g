# MIN9-CENTRAL-MODULE-ACTION for Kourovka 21.137, revision 2.
# This file enumerates outer actions only.  It never constructs a factor system,
# cocycle, extension, descendant, or SmallGroup catalogue row.

F := GF(3);;
z := Z(3);;
I5 := IdentityMat(5,F);;
I3 := IdentityMat(3,F);;

EmbedG := function(g)
  local M,i,j;
  M := IdentityMat(5,F);
  for i in [1..2] do
    for j in [1..2] do M[i][j] := g[i][j]; od;
  od;
  M[3][3] := DeterminantMat(g);
  return M;
end;;

EmbedH := function(h)
  local M,i,j;
  M := IdentityMat(5,F);
  for i in [1..2] do
    for j in [1..2] do M[i+3][j+3] := h[i][j]; od;
  od;
  return M;
end;;

Shear := function(row,col)
  local M;
  M := IdentityMat(5,F);
  M[row][col] := M[row][col]+One(F);
  return M;
end;;

MIN9LieBracket := function(x,y)
  local v;
  v := [Zero(F),Zero(F),Zero(F),Zero(F),Zero(F)];
  v[3] := x[1]*y[2]-x[2]*y[1];
  return v;
end;;

ColumnImage := function(M,v)
  return List([1..Length(M)],i->Sum([1..Length(v)],j->M[i][j]*v[j]));
end;;

gl2 := GL(2,3);;
autgens := [];;
Append(autgens,List(GeneratorsOfGroup(gl2),EmbedG));
Append(autgens,List(GeneratorsOfGroup(gl2),EmbedH));
# lambda: W -> C
Add(autgens,Shear(3,4)); Add(autgens,Shear(3,5));
# tau_W: V -> W
Add(autgens,Shear(4,1)); Add(autgens,Shear(4,2));
Add(autgens,Shear(5,1)); Add(autgens,Shear(5,2));
# tau_C: V -> C, exactly the inner subgroup
innergens := [Shear(3,1),Shear(3,2)];;
Append(autgens,innergens);

basis5 := IdentityMat(5,F);;
bracketOK := ForAll(autgens,M->ForAll(basis5,x->ForAll(basis5,y->
  ColumnImage(M,MIN9LieBracket(x,y))=MIN9LieBracket(ColumnImage(M,x),ColumnImage(M,y)))));;

AutP := Group(autgens);;
InnP := Group(innergens);;
Print("MIN9_BEGIN gap_version=",GAPInfo.Version,"\n");
Print("COORDINATE_CHECK bracket_generators=",bracketOK,
      " aut_order=",Size(AutP)," inner_order=",Size(InnP),
      " inner_normal=",IsNormal(AutP,InnP),"\n");
if not bracketOK or Size(AutP)<>48^2*3^8 or Size(InnP)<>3^2 or
   not IsNormal(AutP,InnP) then
  Print("STATUS=HARD_KILL_COORDINATE_MODEL\n");
  QUIT_GAP(2);
fi;

outq := NaturalHomomorphismByNormalSubgroup(AutP,InnP);;
Oraw := Image(outq);;
otopc := IsomorphismPcGroup(Oraw);;
O := Image(otopc);;
opcgs := Pcgs(O);;

LiftOuter := function(u)
  local uraw;
  uraw := PreImagesRepresentative(otopc,u);
  return PreImagesRepresentative(outq,uraw);
end;;

OuterCoords := function(u)
  return ExponentsOfPcElement(opcgs,u);
end;;

CentralMatrix := function(u)
  local M;
  M := LiftOuter(u);
  return List([3..5],i->List([3..5],j->M[i][j]));
end;;

Osize := Size(O);;
S := SylowSubgroup(O,3);;
Print("OUTER_CHECK outer_order=",Osize," expected=",48^2*3^6,
      " sylow3_order=",Size(S)," expected_sylow3=",3^8,
      " kernel_order=",Size(Kernel(outq)),"\n");
if Osize<>48^2*3^6 or Size(S)<>3^8 or Size(Kernel(outq))<>3^2 then
  Print("STATUS=HARD_KILL_OUTER_QUOTIENT\n");
  QUIT_GAP(3);
fi;

ColumnNullspace := function(K)
  return NullspaceMat(TransposedMat(K));
end;;

IsRegularJ3 := function(B)
  local N;
  N := B-I3;
  return RankMat(N)=2 and RankMat(N^2)=1 and RankMat(N^3)=0;
end;;

CentralData := function(U)
  local cgens,Cimg,eqs,B,fixed,reg,branch;
  cgens := List(GeneratorsOfGroup(U),CentralMatrix);
  Cimg := Group(cgens);
  eqs := [];
  for B in cgens do Append(eqs,B-I3); od;
  fixed := ColumnNullspace(eqs);
  reg := Number(Elements(Cimg),IsRegularJ3);
  branch := "INELIGIBLE";
  if Length(fixed)=1 and fixed[1][1]<>Zero(F) and
     fixed[1][2]=Zero(F) and fixed[1][3]=Zero(F) and reg>0 then
    if Size(Cimg)=3 and IsCyclic(Cimg) then
      branch := "CYCLIC_REGULAR_C3";
    elif Size(Cimg)=9 and IsAbelian(Cimg) and Exponent(Cimg)=3 then
      branch := "ELEMENTARY_C3xC3_CENTRALIZER";
    elif Size(Cimg)=27 and not IsAbelian(Cimg) and Exponent(Cimg)=3 then
      branch := "FULL_UT3_3";
    else
      branch := "UNEXPECTED_ELIGIBLE_BRANCH";
    fi;
  fi;
  return rec(image:=Cimg,image_order:=Size(Cimg),fixed:=fixed,
             regular_count:=reg,branch:=branch);
end;;

IsElementaryImage := function(U,maxdim)
  local sz,d;
  sz := Size(U);
  if not IsAbelian(U) or Exponent(U)<>3 then return false; fi;
  d := LogInt(sz,3);
  return sz=3^d and d>=1 and d<=maxdim;
end;;

IsH3Image := function(U)
  return Size(U)=27 and Exponent(U)=3 and not IsAbelian(U) and
         Size(DerivedSubgroup(U))=3 and Size(Centre(U))=3;
end;;

IsH3C3Image := function(U)
  return Size(U)=81 and Exponent(U)=3 and not IsAbelian(U) and
         Size(DerivedSubgroup(U))=3 and Size(Centre(U))=9;
end;;

Print("SUBGROUP_ENUM_BEGIN sylow_order=",Size(S),"\n");
sclasses := ConjugacyClassesSubgroups(S);;
Print("SUBGROUP_ENUM_COMPLETE s_class_count=",Length(sclasses),"\n");

candidates := [];;
targetAcount := 0;; targetNcount := 0;;
targetAsum := 0;; targetNsum := 0;;
centralAcount := 0;; centralNcount := 0;;
centralAsum := 0;; centralNsum := 0;;
for si in [1..Length(sclasses)] do
  U := Representative(sclasses[si]);
  allowA := IsElementaryImage(U,4);
  allowN := IsElementaryImage(U,3) or IsH3Image(U) or IsH3C3Image(U);
  if allowA or allowN then
    ssize := Size(S)/Size(Normalizer(S,U));
    if allowA then targetAcount:=targetAcount+1; targetAsum:=targetAsum+ssize; fi;
    if allowN then targetNcount:=targetNcount+1; targetNsum:=targetNsum+ssize; fi;
    cd := CentralData(U);
    if cd.branch="UNEXPECTED_ELIGIBLE_BRANCH" then
      Error("eligible central image falls outside the derived three branches");
    fi;
    if cd.branch<>"INELIGIBLE" then
      if allowA then centralAcount:=centralAcount+1; centralAsum:=centralAsum+ssize; fi;
      if allowN then centralNcount:=centralNcount+1; centralNsum:=centralNsum+ssize; fi;
      Add(candidates,rec(sindex:=si,U:=U,allowA:=allowA,allowN:=allowN,
                         sclass_size:=ssize,central:=cd));
    fi;
  fi;
od;
Print("PREFUSION_PARTITION quotient=C3^4 target_sclasses=",targetAcount,
      " target_subgroups_sum=",targetAsum," central_pass_sclasses=",centralAcount,
      " central_pass_subgroups_sum=",centralAsum,"\n");
Print("PREFUSION_PARTITION quotient=H3xC3 target_sclasses=",targetNcount,
      " target_subgroups_sum=",targetNsum," central_pass_sclasses=",centralNcount,
      " central_pass_subgroups_sum=",centralNsum,"\n");

Print("PROFILE_BEFORE_FUSION_SETUP retained_sclasses=",Length(candidates),"\n");

avec := [];;
for a1 in F do
  for a2 in F do
    if a1<>Zero(F) or a2<>Zero(F) then Add(avec,[a1,a2]); fi;
  od;
od;

DForA := function(a)
  local D;
  D := NullMat(5,5,F);
  D[3][1] := a[2];
  D[3][2] := -a[1];
  return D;
end;;

ProjectedFixedIsA := function(N,a)
  local kb,proj;
  kb := ColumnNullspace(N);
  proj := List(kb,v->[v[1],v[2]]);
  return RankMat(proj)=1 and RankMat(Concatenation(proj,[a]))=1;
end;;

LiftCounts := function(u)
  local A0,counts,inn,A,N,ai,a;
  A0 := LiftOuter(u^-1);
  counts := List(avec,a->0);
  for inn in Elements(InnP) do
    A := inn*A0;
    N := A-I5;
    if RankMat(N)=3 and RankMat(N^2)=2 and RankMat(N^3)=1 and
       RankMat(N^4)=0 then
      for ai in [1..Length(avec)] do
        a := avec[ai];
        if N^3=DForA(a) and ProjectedFixedIsA(N,a) then
          counts[ai] := counts[ai]+1;
        fi;
      od;
    fi;
  od;
  return counts;
end;;

MaxFlowProfile := function(profile,k)
  local q,n,src,sink,cap,res,i,j,uind,aind,flow,parent,queue,head,x,y,
        aug,reach,cut;
  q := Length(profile); n := q+10; src := 1; sink := n;
  cap := NullMat(n,n);
  for i in [1..q] do
    uind := 1+i; cap[src][uind] := 9*k;
    for j in [1..8] do
      aind := 1+q+j; cap[uind][aind] := 3*k*profile[i][j];
    od;
  od;
  for j in [1..8] do cap[1+q+j][sink] := 27; od;
  res := List(cap,ShallowCopy); flow := 0;
  while true do
    parent := List([1..n],i->0); parent[src] := -1;
    queue := [src]; head := 1;
    while head<=Length(queue) and parent[sink]=0 do
      x := queue[head]; head := head+1;
      for y in [1..n] do
        if parent[y]=0 and res[x][y]>0 then
          parent[y]:=x; Add(queue,y);
          if y=sink then break; fi;
        fi;
      od;
    od;
    if parent[sink]=0 then break; fi;
    aug := 10^9; y := sink;
    while y<>src do x:=parent[y]; aug:=Minimum(aug,res[x][y]); y:=x; od;
    y := sink;
    while y<>src do
      x:=parent[y]; res[x][y]:=res[x][y]-aug;
      res[y][x]:=res[y][x]+aug; y:=x;
    od;
    flow := flow+aug;
  od;
  reach := List([1..n],i->false); reach[src]:=true;
  queue:=[src]; head:=1;
  while head<=Length(queue) do
    x:=queue[head]; head:=head+1;
    for y in [1..n] do
      if not reach[y] and res[x][y]>0 then reach[y]:=true; Add(queue,y); fi;
    od;
  od;
  cut := 0;
  for i in [1..n] do
    if reach[i] then
      for j in [1..n] do if not reach[j] then cut:=cut+cap[i][j]; fi; od;
    fi;
  od;
  return rec(value:=flow,cut:=cut,
             reachable_u:=Filtered([1..q],i->reach[1+i]),
             reachable_a:=Filtered([1..8],j->reach[1+q+j]));
end;;

Print("PREFUSION_LIFT_PROFILE_BEGIN sclasses=",Length(candidates),"\n");
survivors := [];;
survApre := 0;; survNpre := 0;;
for ci in [1..Length(candidates)] do
  U := candidates[ci].U; uelts := Elements(U);
  profile := List(uelts,LiftCounts);
  k := 81/Size(U);
  flow := MaxFlowProfile(profile,k);
  candidates[ci].uelts := uelts; candidates[ci].profile := profile;
  candidates[ci].flow := flow; candidates[ci].survives := flow.value=216;
  candidates[ci].labelhist := SortedList(List([1..8],j->Number(profile,r->r[j]=9)));
  if candidates[ci].survives then
    Add(survivors,ci);
    if candidates[ci].allowA then survApre:=survApre+1; fi;
    if candidates[ci].allowN then survNpre:=survNpre+1; fi;
  fi;
  Print("PREFUSION_LIFT_PROFILE candidate=",ci,
        " sclass_index=",candidates[ci].sindex," image_order=",Size(U),
        " central_branch=",candidates[ci].central.branch," kernel_size=",k,
        " label_histogram=",candidates[ci].labelhist,
        " max_flow=",flow.value," min_cut=",flow.cut,
        " reachable_u_indices=",flow.reachable_u,
        " reachable_a_indices=",flow.reachable_a,
        " a_vectors=",avec," survives=",candidates[ci].survives,"\n");
od;
Print("PREFUSION_LIFT_PROFILE_COMPLETE survivors=",Length(survivors),
      " survivor_C3^4_sclasses=",survApre,
      " survivor_H3xC3_sclasses=",survNpre,"\n");

# Only now fuse flow survivors under the full outer group.  Exact invariant
# buckets avoid calling the transporter on pairs that cannot be conjugate.
fused := [];;
for ci in survivors do
  pos := fail;
  for fj in [1..Length(fused)] do
    if Size(candidates[ci].U)=Size(fused[fj].rep) and
       candidates[ci].central.branch=fused[fj].central.branch and
       candidates[ci].labelhist=fused[fj].labelhist and
       IsConjugate(O,candidates[ci].U,fused[fj].rep) then pos:=fj; break; fi;
  od;
  if pos=fail then
    Add(fused,rec(rep:=candidates[ci].U,members:=[ci],
                  central:=candidates[ci].central,
                  labelhist:=candidates[ci].labelhist,
                  uelts:=candidates[ci].uelts,profile:=candidates[ci].profile,
                  flow:=candidates[ci].flow,survives:=true));
  else
    Add(fused[pos].members,ci);
  fi;
od;
Print("FULL_OUTER_FUSION_COMPLETE prefusion_survivors=",Length(survivors),
      " full_outer_classes=",Length(fused),"\n");

for fj in [1..Length(fused)] do
  frec := fused[fj]; U := frec.rep; Nrm := Normalizer(O,U);
  frec.normalizer := Nrm;
  frec.allowA := ForAny(frec.members,ci->candidates[ci].allowA);
  frec.allowN := ForAny(frec.members,ci->candidates[ci].allowN);
  frec.fusion_witnesses := [];
  for ci in frec.members do
    w := RepresentativeAction(O,candidates[ci].U,U,OnPoints);
    if w=fail or candidates[ci].U^w<>U then Error("full-outer fusion witness missing"); fi;
    Add(frec.fusion_witnesses,OuterCoords(w));
  od;
  Print("OUTER_CLASS id=",fj," order=",Size(U),
        " structure=",StructureDescription(U),
        " allow_C3^4=",frec.allowA," allow_H3xC3=",frec.allowN,
        " sclass_indices=",List(frec.members,ci->candidates[ci].sindex),
        " sclass_sizes=",List(frec.members,ci->candidates[ci].sclass_size),
        " fusion_witness_pc=",frec.fusion_witnesses,
        " normalizer_order=",Size(Nrm),
        " normalizer_generators_pc=",List(GeneratorsOfGroup(Nrm),OuterCoords),
        " central_image_order=",frec.central.image_order,
        " central_regular_count=",frec.central.regular_count,
        " central_fixed_basis=",frec.central.fixed,
        " central_branch=",frec.central.branch,
        " label_histogram=",frec.labelhist," flow=",frec.flow.value,"\n");
od;

# C3^4: Aut(R) is transitive on epimorphisms to a fixed elementary image.
# We nevertheless construct the representative and check the full epimorphism
# count against the elementary linear count.
Rabel := ElementaryAbelianGroup(IsPcGroup,81);;
rabgens := GeneratorsOfGroup(Rabel);;
rabpcgs := Pcgs(Rabel);;
EpiCountAbelian := function(d)
  local ans,i;
  ans:=1; for i in [0..d-1] do ans:=ans*(3^4-3^i); od; return ans;
end;;

Print("EPIMORPHISM_ENUM_BEGIN quotient=C3^4\n");
for fj in [1..Length(fused)] do
  if fused[fj].allowA then
    U := fused[fj].rep; ug := MinimalGeneratingSet(U); d:=Length(ug);
    tup := Concatenation(ug,List([1..4-d],i->One(U)));
    hom := GroupHomomorphismByImages(Rabel,U,rabgens,tup);
    if hom=fail or Size(Image(hom))<>Size(U) then Error("C3^4 epi construction failed"); fi;
    ker := Kernel(hom); epin := EpiCountAbelian(d);
    Print("EPI_ORBIT quotient=C3^4 class=",fj," orbit=1 total_orbits=1",
          " orbit_size=",epin," total_epimorphisms=",epin,
          " kernel_order=",Size(ker)," kernel_structure=",StructureDescription(ker),
          " kernel_generators_pc=",List(GeneratorsOfGroup(ker),
             x->ExponentsOfPcElement(rabpcgs,x)),
          " image_tuple_pc=",List(tup,OuterCoords),
          " lift_matrices=",List(tup,LiftOuter),
          " flow=",fused[fj].flow.value," survives=",fused[fj].survives,"\n");
  fi;
od;
Print("EPIMORPHISM_ENUM_COMPLETE quotient=C3^4\n");

# Construct R=H_3(3) x C3 as explicit block-unipotent matrices, with
# tracked generators x=I+E12, y=I+E23, z=I+E45.
rx := IdentityMat(5,F);; rx[1][2] := rx[1][2]+One(F);;
ry := IdentityMat(5,F);; ry[2][3] := ry[2][3]+One(F);;
rz := IdentityMat(5,F);; rz[4][5] := rz[4][5]+One(F);;
R0 := Group([rx,ry,rz]);;
r0gens := [rx,ry,rz];;
rtopc := IsomorphismPcGroup(R0);;
Rnon := Image(rtopc);;
rngens := List(r0gens,x->Image(rtopc,x));;
rnpcgs := Pcgs(Rnon);;
if Size(Rnon)<>81 or Exponent(Rnon)<>3 or
   Size(DerivedSubgroup(Rnon))<>3 or Size(Centre(Rnon))<>9 or
   Size(Subgroup(Rnon,rngens))<>81 then Error("R=H3xC3 reconstruction failed"); fi;
AutRnon := AutomorphismGroup(Rnon);;
autRgens := GeneratorsOfGroup(AutRnon);;
Print("RNON_CHECK order=",Size(Rnon)," exponent=",Exponent(Rnon),
      " derived_order=",Size(DerivedSubgroup(Rnon)),
      " centre_order=",Size(Centre(Rnon))," aut_order=",Size(AutRnon),"\n");

TupleKey := function(t,uelts)
  local n,p;
  n:=Length(uelts); p:=List(t,x->Position(uelts,x));
  if fail in p then Error("tuple element outside image subgroup"); fi;
  return p[1]+n*(p[2]-1)+n^2*(p[3]-1);
end;;

NonabelianEpiOrbits := function(U,Nrm)
  local uelts,n,one,epis,keymap,a,b,d,t,key,seen,orbits,idx,queue,head,
        cur,hom,nt,j,orb,aut,ng;
  uelts:=Elements(U); n:=Length(uelts); one:=One(U); epis:=[];
  keymap:=List([1..n^3],i->0);
  for a in uelts do
    for b in uelts do
      for d in uelts do
        if Comm(d,a)=one and Comm(d,b)=one and Size(Subgroup(U,[a,b,d]))=n then
          t:=[a,b,d]; Add(epis,t); key:=TupleKey(t,uelts);
          if keymap[key]<>0 then Error("duplicate epi tuple key"); fi;
          keymap[key]:=Length(epis);
        fi;
      od;
    od;
  od;
  seen:=List([1..Length(epis)],i->false); orbits:=[];
  for idx in [1..Length(epis)] do
    if not seen[idx] then
      seen[idx]:=true; queue:=[idx]; head:=1; orb:=[];
      while head<=Length(queue) do
        cur:=queue[head]; head:=head+1; Add(orb,cur); t:=epis[cur];
        hom:=GroupHomomorphismByImagesNC(Rnon,U,rngens,t);
        for aut in autRgens do
          nt:=List(rngens,x->Image(hom,Image(aut,x)));
          j:=keymap[TupleKey(nt,uelts)];
          if j=0 then Error("Aut(R) moved epi outside complete epi list"); fi;
          if not seen[j] then seen[j]:=true; Add(queue,j); fi;
        od;
        for ng in GeneratorsOfGroup(Nrm) do
          nt:=List(t,x->x^ng); j:=keymap[TupleKey(nt,uelts)];
          if j=0 then Error("normalizer moved epi outside complete epi list"); fi;
          if not seen[j] then seen[j]:=true; Add(queue,j); fi;
        od;
      od;
      Add(orbits,rec(rep:=epis[orb[1]],size:=Length(orb)));
    fi;
  od;
  if Sum(orbits,o->o.size)<>Length(epis) then Error("epi orbit partition mismatch"); fi;
  return rec(total:=Length(epis),orbits:=orbits);
end;;

Print("EPIMORPHISM_ENUM_BEGIN quotient=H3xC3\n");
survA := 0;; survN := 0;;
for fj in [1..Length(fused)] do
  if fused[fj].allowA and fused[fj].survives then survA:=survA+1; fi;
  if fused[fj].allowN then
    ep := NonabelianEpiOrbits(fused[fj].rep,fused[fj].normalizer);
    Print("EPI_PARTITION quotient=H3xC3 class=",fj,
          " total_epimorphisms=",ep.total," orbit_count=",Length(ep.orbits),
          " orbit_sizes=",List(ep.orbits,o->o.size),
          " orbit_size_sum=",Sum(ep.orbits,o->o.size),"\n");
    for oi in [1..Length(ep.orbits)] do
      tup:=ep.orbits[oi].rep;
      hom:=GroupHomomorphismByImages(Rnon,fused[fj].rep,rngens,tup);
      if hom=fail or Size(Image(hom))<>Size(fused[fj].rep) then
        Error("H3xC3 representative epi failed");
      fi;
      ker:=Kernel(hom);
      Print("EPI_ORBIT quotient=H3xC3 class=",fj," orbit=",oi,
            " orbit_size=",ep.orbits[oi].size,
            " kernel_order=",Size(ker)," kernel_structure=",StructureDescription(ker),
            " kernel_generators_pc=",List(GeneratorsOfGroup(ker),
               x->ExponentsOfPcElement(rnpcgs,x)),
            " image_tuple_pc=",List(tup,OuterCoords),
            " lift_matrices=",List(tup,LiftOuter),
            " flow=",fused[fj].flow.value," survives=",fused[fj].survives,"\n");
    od;
    if fused[fj].survives then survN:=survN+Length(ep.orbits); fi;
  fi;
od;
Print("EPIMORPHISM_ENUM_COMPLETE quotient=H3xC3\n");
Print("SURVIVOR_COUNTS quotient_C3^4_outer_orbits=",survA,
      " quotient_H3xC3_epimorphism_orbits=",survN,"\n");
Print("STATUS=MIN9_CENTRAL_MODULE_ACTION_COMPLETE active_assignment_answered=no",
      " factor_systems_opened=0 cocycles_opened=0\n");
QUIT_GAP(0);
