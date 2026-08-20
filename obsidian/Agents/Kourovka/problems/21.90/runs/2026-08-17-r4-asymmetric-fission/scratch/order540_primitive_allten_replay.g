# Deterministic leased replay of the complete installed degree-540 primitive
# group layer. DO NOT RUN WITHOUT A LIVE HEAVY-COMPUTE LEASE.
outpath:="Agents/Kourovka/problems/21.90/runs/2026-08-17-r4-asymmetric-fission/scratch/order540_primitive_allten_replay.out";;
LogTo(outpath);

deg:=540;;
infos:=PackageInfo("primgrp");;
if Length(infos)=0 then Error("PrimGrp package metadata absent"); fi;
n:=NrPrimitiveGroups(deg);;
if n<>10 then Error("installed degree-540 primitive-group count changed"); fi;
Print("GAP=",GAPInfo.Version," PrimGrp=",infos[1].Version,
      " degree=",deg," count=",n,"\n");

length77count:=0;; selfpairedcount:=0;; eligiblecount:=0;;

# The first eight catalogue groups are small enough for exact stabilizer orbits.
for i in [1..8] do
  g:=PrimitiveGroup(deg,i);;
  h:=Stabilizer(g,1);;
  os:=Orbits(h,[1..deg]);;
  lens:=SortedList(List(os,Length));;
  if Sum(lens)<>deg then Error("subdegrees do not sum to 540"); fi;
  Print("index=",i," order=",Size(g)," subdegrees=",lens,"\n");

  for o in Filtered(os,z->Length(z)=77) do
    length77count:=length77count+1;
    b:=Minimum(o);;
    t:=RepresentativeAction(g,1,b);;
    if t=fail then Error("transitive group lacked a transporter"); fi;
    pairedpoint:=1^(t^-1);;
    selfpaired:=pairedpoint in o;
    Print("  length77 representative=",b,
          " paired_representative=",pairedpoint,
          " self_paired=",selfpaired,"\n");

    if selfpaired then
      selfpairedcount:=selfpairedcount+1;
      orbital:=Orbit(g,[1,b],OnTuples);;
      adj:=List([1..deg],z->[]);;
      for pair in orbital do Add(adj[pair[1]],pair[2]); od;
      for z in adj do Sort(z); od;
      degreevalues:=Set(List(adj,Length));;
      symmetric:=ForAll([1..deg],
        u->ForAll(adj[u],v->u in adj[v]));;
      lambdavalues:=[];; muvalues:=[];;
      for u in [1..deg] do
        for v in [u+1..deg] do
          cn:=Length(Intersection(adj[u],adj[v]));;
          if v in adj[u] then AddSet(lambdavalues,cn);
          else AddSet(muvalues,cn); fi;
        od;
      od;
      eligible:=symmetric and degreevalues=[77]
                and lambdavalues=[4] and muvalues=[12];;
      if eligible then eligiblecount:=eligiblecount+1; fi;
      Print("  orbital_size=",Length(orbital),
            " symmetric=",symmetric,
            " degrees=",degreevalues,
            " adjacent_common=",lambdavalues,
            " nonadjacent_common=",muvalues,
            " is_srg_540_77_4_12=",eligible,"\n");
    fi;
  od;
od;

# Exact natural-group recognition avoids the expensive stabilizer calculation.
# Natural A_540 and S_540 are 2-transitive, hence have subdegrees [1,539].
for i in [9,10] do
  g:=PrimitiveGroup(deg,i);;
  alt:=IsNaturalAlternatingGroup(g);;
  sym:=IsNaturalSymmetricGroup(g);;
  if (i=9 and not alt) or (i=9 and sym)
     or (i=10 and alt) or (i=10 and not sym) then
    Error("catalogue tail no longer has natural A_540,S_540 ordering");
  fi;
  Print("index=",i," natural_alt=",alt," natural_sym=",sym,
        " subdegrees=[ 1, 539 ]\n");
od;

Print("length77_suborbits=",length77count,
      " self_paired_length77=",selfpairedcount,
      " eligible_srg_orbitals=",eligiblecount,"\n");
LogTo();
QUIT;
