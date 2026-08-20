# Independent deterministic reconstruction/verifier for the six abstract
# parent IDs reported by the full C4xC2/[32,27] full-dual screen.
# This does not enumerate H^2(Q,A).  It reconstructs every marked kernel
# directly inside each canonical SmallGroup and checks the requested group
# properties by separate element/character/subgroup algorithms.

if not IsBound(targetids) then
  targetids:=[53357,53358,53373,53374,53384,53385];
fi;

CoordC4C2V := function(x,a4,a2)
  local i,j;
  for i in [0..3] do
    for j in [0..1] do
      if x=a4^i*a2^j then return [i,j]; fi;
    od;
  od;
  Error("no C4xC2 coordinates");
end;

SubgroupImageActionV := function(S,a) return Image(a,S); end;

MinimalC4C2GeneratorsV := function(H,N)
  local hpcgs,pairs,x,y;
  hpcgs:=Pcgs(H); pairs:=[];
  for x in Elements(N) do
    if Order(x)=4 then
      for y in Elements(N) do
        if Order(y)=2 and not y in Subgroup(N,[x]) and
           Subgroup(N,[x,y])=N then
          Add(pairs,[Concatenation(ExponentsOfPcElement(hpcgs,x),
                                  ExponentsOfPcElement(hpcgs,y)),x,y]);
        fi;
      od;
    fi;
  od;
  Sort(pairs,function(p,q) return p[1]<q[1]; end);
  if Length(pairs)=0 then Error("no two-generator C4xC2 basis"); fi;
  return [pairs[1][2],pairs[1][3]];
end;

PowerRationalExactV := function(G)
  local cc,x,o,k;
  for cc in ConjugacyClasses(G) do
    x:=Representative(cc); o:=Order(x);
    for k in [1..o] do
      if GcdInt(k,o)=1 and not IsConjugate(G,x,x^k) then
        return [false,x,k];
      fi;
    od;
  od;
  return [true,fail,fail];
end;

SMPByNormalClosuresV := function(G)
  local ccs,reps,closures,i,j;
  ccs:=ConjugacyClasses(G); reps:=List(ccs,Representative);
  closures:=List(reps,x->NormalClosure(G,Subgroup(G,[x])));
  for i in [1..Length(reps)] do
    for j in [1..i-1] do
      if closures[i]=closures[j] then return [false,i,j,closures[i]]; fi;
    od;
  od;
  return [true,Length(reps),Length(closures)];
end;

DeMeyerWitnessesV := function(G)
  local D,d,out,B,b,qinv;
  D:=DerivedSubgroup(G);
  d:=Length(AbelianInvariants(G/D)); out:=[];
  for B in NormalSubgroups(G) do
    if IsSubgroup(D,B) and IsSubgroup(Centre(D),B) then
      b:=LogInt(Size(B),2);
      if b<=d and (d-b) mod 2=0 then
        qinv:=AbelianInvariants(FactorGroup(D,B));
        if Length(qinv)>0 and Length(qinv) mod 2=0 and
           ForAll(qinv,n->n=2) then Add(out,[B,b,qinv]); fi;
      fi;
    fi;
  od;
  return out;
end;

# Reconstruct the prescribed action without reading the cohomology screen.
Astd:=SmallGroup(8,2); aelts:=Elements(Astd);
a4:=First(aelts,x->Order(x)=4); asub4:=Subgroup(Astd,[a4]);
a2:=First(aelts,x->Order(x)=2 and not x in asub4);
accs:=ConjugacyClasses(Astd); areps:=List(accs,Representative);
achars:=Irr(Astd); acharvals:=List(achars,chi->List(chi)); an:=Length(achars);
transperms:=[];
for k in [1..an] do
  imgs:=[];
  for i in [1..an] do
    vals:=List([1..an],j->acharvals[i][j]*acharvals[k][j]);
    Add(imgs,Position(acharvals,vals));
  od;
  Add(transperms,PermList(imgs));
od;
Trans:=Group(transperms);
AutAstd:=AutomorphismGroup(Astd); autagens:=GeneratorsOfGroup(AutAstd);
autperms:=[];
for aut in autagens do
  imgs:=[]; ainv:=InverseGeneralMapping(aut);
  for i in [1..an] do
    vals:=List(areps,x->acharvals[i][Position(areps,Image(ainv,x))]);
    Add(imgs,Position(acharvals,vals));
  od;
  Add(autperms,PermList(imgs));
od;
Lin:=Group(autperms);
autpermhom:=GroupHomomorphismByImages(AutAstd,Lin,autagens,autperms);
Hol:=Group(Concatenation(GeneratorsOfGroup(Trans),autperms));
qclasses:=Filtered(ConjugacyClassesSubgroups(Hol),cc->
  Size(Representative(cc))=32 and IdGroup(Representative(cc))=[32,27] and
  Size(Intersection(Representative(cc),Trans))=8);
if Length(qclasses)<>1 then Error("prescribed action is not unique"); fi;
S:=Representative(qclasses[1]); siso:=IsomorphismPcpGroup(S);
Qstd:=Image(siso); qgens:=Igs(Qstd); rhoimgs:=[];
for qg in qgens do
  sg:=PreImagesRepresentative(siso,qg); lambdaidx:=1^sg;
  lin:=sg*transperms[lambdaidx]^-1;
  Add(rhoimgs,PreImagesRepresentative(autpermhom,lin));
od;
rhoGroup:=Group(rhoimgs);
rhohom:=GroupHomomorphismByImages(Qstd,rhoGroup,qgens,rhoimgs);
if not IsGroupHomomorphism(rhohom) then Error("prescribed action hom failed"); fi;
AutQstd:=AutomorphismGroup(Qstd);
autqelts:=Elements(AutQstd); autaelts:=Elements(AutAstd);
prescribedcoords:=List(rhoimgs,r->[
  CoordC4C2V(Image(r,a4),a4,a2),CoordC4C2V(Image(r,a2),a4,a2)]);

ActionEquivalenceV := function(H,N)
  local nat,Q0,qiso,niso,thetaimgs,qg,q0,h,imgs,theta,rawcoords,
        ai,alpha,rhotrans,bi,beta,ok,j,a;
  nat:=NaturalHomomorphismByNormalSubgroup(H,N); Q0:=Image(nat);
  qiso:=IsomorphismGroups(Q0,Qstd); niso:=IsomorphismGroups(N,Astd);
  if qiso=fail or niso=fail then return fail; fi;
  thetaimgs:=[];
  for qg in qgens do
    q0:=PreImagesRepresentative(qiso,qg);
    h:=PreImagesRepresentative(nat,q0);
    imgs:=List([a4,a2],a->Image(niso,PreImagesRepresentative(niso,a)^h));
    theta:=GroupHomomorphismByImages(Astd,Astd,[a4,a2],imgs);
    if not IsGroupHomomorphism(theta) then Error("candidate action map failed"); fi;
    Add(thetaimgs,theta);
  od;
  rawcoords:=List(thetaimgs,t->[
    CoordC4C2V(Image(t,a4),a4,a2),CoordC4C2V(Image(t,a2),a4,a2)]);
  for ai in [1..Length(autqelts)] do
    alpha:=autqelts[ai];
    rhotrans:=List(qgens,q->Image(rhohom,Image(alpha,q)));
    for bi in [1..Length(autaelts)] do
      beta:=autaelts[bi]; ok:=true;
      for j in [1..Length(qgens)] do
        for a in [a4,a2] do
          if Image(beta,Image(thetaimgs[j],a))<>
             Image(rhotrans[j],Image(beta,a)) then ok:=false; break; fi;
        od;
        if not ok then break; fi;
      od;
      if ok then return rec(qiso:=qiso,niso:=niso,rawcoords:=rawcoords,
                            autqindex:=ai,autaindex:=bi); fi;
    od;
  od;
  return fail;
end;

Print("GAP_VERSION=",GAPInfo.Version,
      " PRESCRIBED_A=",StructureDescription(Astd),
      " PRESCRIBED_Q_ID=",IdGroup(Qstd),
      " DUAL_INTERSECTION_ORDER=",Size(Intersection(S,Trans)),
      " AUT_Q_ORDER=",Size(AutQstd)," AUT_A_ORDER=",Size(AutAstd),"\n");
Print("PRESCRIBED_ACTION_IMAGES_A4_A2=",prescribedcoords,"\n");

for hid in targetids do
  H:=SmallGroup(256,hid); hpcgs:=Pcgs(H); D:=DerivedSubgroup(H);
  kerncands:=Filtered(NormalSubgroups(H),N->
    Size(N)=8 and AbelianInvariants(N)=[2,4] and
    IdGroup(FactorGroup(H,N))=[32,27]);
  matches:=[];
  for N in kerncands do
    ae:=ActionEquivalenceV(H,N);
    if ae<>fail then Add(matches,[N,ae]); fi;
  od;
  AutH:=AutomorphismGroup(H); markedorbits:=[];
  for m in matches do
    orbitpos:=fail;
    if Length(markedorbits)>0 then
      orbitpos:=First([1..Length(markedorbits)],j->
        RepresentativeAction(AutH,markedorbits[j][1],m[1],
          SubgroupImageActionV)<>fail);
    fi;
    if orbitpos=fail then Add(markedorbits,m); fi;
  od;

  powrat:=PowerRationalExactV(H); irr:=Irr(H);
  charrat:=ForAll(irr,chi->ForAll(chi,v->IsRat(v)));
  smp:=SMPByNormalClosuresV(H); demw:=DeMeyerWitnessesV(H);
  nclosures:=fail; if smp[1] then nclosures:=smp[3]; fi;
  Print("PARENT_ID=",hid," STRUCTURE=",StructureDescription(H),
        " CLASS=",NilpotencyClassOfGroup(H),
        " D_ORDER=",Size(D)," D_INVARIANTS=",AbelianInvariants(D),
        " ABELIANIZATION=",AbelianInvariants(H/D),
        " CENTER_INVARIANTS=",AbelianInvariants(Centre(H)),"\n");
  Print("KERNEL_CANDIDATES=",Length(kerncands),
        " ACTION_MATCHES=",Length(matches),
        " MARKED_KERNEL_AUT_ORBITS=",Length(markedorbits),"\n");
  if Length(markedorbits)>0 then
    for oi in [1..Length(markedorbits)] do
      N:=markedorbits[oi][1]; ae:=markedorbits[oi][2];
      ngen:=MinimalC4C2GeneratorsV(H,N);
      Print("MARKED_KERNEL_ORBIT=",oi,
            " KERNEL_GENERATOR_EXPONENTS=",
            List(ngen,x->ExponentsOfPcElement(hpcgs,x)),
            " QUOTIENT_ID=",IdGroup(FactorGroup(H,N)),
            " RAW_ACTION_IMAGES_A4_A2=",ae.rawcoords,
            " ACTION_EQUIVALENCE_AUT_Q_INDEX=",ae.autqindex,
            " AUT_A_INDEX=",ae.autaindex,"\n");
    od;
  fi;
  Print("POWER_RATIONAL_EXACT=",powrat[1],
        " IRREDUCIBLE_CHARACTERS_RATIONAL_VALUED=",charrat,
        " CHARACTER_COUNT=",Length(irr),
        " EXACT_SMP=",smp[1]," CONJUGACY_CLASSES=",Length(ConjugacyClasses(H)),
        " DISTINCT_NORMAL_CLOSURES=",nclosures,"\n");
  Print("DEMEYER_WITNESS_COUNT=",Length(demw));
  if Length(demw)>0 then
    B:=demw[1][1];
    Print(" FIRST_B_ORDER=",Size(B)," FIRST_B_EXPONENTS=",
          List(Pcgs(B),x->ExponentsOfPcElement(hpcgs,x)),
          " FIRST_B_LOG2=",demw[1][2],
          " FIRST_D_MOD_B_INVARIANTS=",demw[1][3]);
  fi;
  Print("\nPARENT_ALL_REQUESTED_CHECKS=",
        Length(markedorbits)>0 and powrat[1] and charrat and smp[1] and
        Length(demw)>0,"\n");
od;
