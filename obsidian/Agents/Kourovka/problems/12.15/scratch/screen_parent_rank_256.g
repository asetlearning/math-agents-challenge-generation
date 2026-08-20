# Exhaustive rank-sector screen for order-256 quotients H of a hypothetical
# minimum order-512 counterexample.  Required global: dtarget in [3,4,5].
# Every pre-SMP filter is a proved necessary parent condition.  Exact SMP is
# then tested, followed by the exact H^2(H,C2) nondegeneracy screen.

if not IsBound(dtarget) or not dtarget in [3,4,5] then
  Error("bind dtarget to 3, 4, or 5");
fi;

HasSMPExactRank := function(G)
  local irr,signatures,sig,i,j;
  irr:=Irr(G);
  signatures:=[];
  for i in [1..NrConjugacyClasses(G)] do
    sig:=[];
    for j in [1..Length(irr)] do
      Add(sig,irr[j][i]=irr[j][1]);
    od;
    if sig in signatures then return false; fi;
    Add(signatures,sig);
  od;
  return true;
end;

PassesRationalRank := function(G)
  local cc,x,ox;
  for cc in ConjugacyClasses(G) do
    x:=Representative(cc); ox:=Order(x);
    if not IsConjugate(G,x,x^-1) then return false; fi;
    if ox>=8 and not IsConjugate(G,x,x^3) then return false; fi;
  od;
  return true;
end;

HasDeMeyerWitnessRank := function(G,D,d)
  local B,b,qinv;
  for B in NormalSubgroups(G) do
    if IsSubgroup(D,B) and IsSubgroup(Centre(D),B) then
      b:=LogInt(Size(B),2);
      if b<=d and (d-b) mod 2=0 then
        qinv:=AbelianInvariants(FactorGroup(D,B));
        if Length(qinv)>0 and Length(qinv) mod 2=0 and
           ForAll(qinv,n->n=2) then
          return [Position(NormalSubgroups(G),B),b,Length(qinv)];
        fi;
      fi;
    fi;
  od;
  return fail;
end;

rankids:=[];
for pctarget in [3..7] do
  Append(rankids,List(IdsOfAllSmallGroups(Size,256,RankPGroup,dtarget,
                    PClassPGroup,pctarget),pair->pair[2]));
od;
Sort(rankids);
rankidstotal:=Length(rankids);
if not IsBound(rankstartpos) then rankstartpos:=1; fi;
if not IsBound(rankendpos) then rankendpos:=rankidstotal; fi;
if rankstartpos<1 or rankendpos>rankidstotal or rankstartpos>rankendpos then
  Error("invalid inclusive rank-list position range");
fi;
rankids:=rankids{[rankstartpos..rankendpos]};

stage_metabelian:=0;
stage_exactderived:=0;
stage_class_exp_center:=0;
stage_rational:=0;
stage_smp:=0;
parentidsrank:=[];
Print("GAP_VERSION=",GAPInfo.Version," ORDER=256 RANK=",dtarget,
      " PRECOMPUTED_PCLASS_GE3_TOTAL=",rankidstotal,
      " POSITION_RANGE=",[rankstartpos,rankendpos],
      " IDS_IN_RUN=",Length(rankids),"\n");

rankposlocal:=0;
for idrank in rankids do
  rankposlocal:=rankposlocal+1;
  rankgrp:=SmallGroup(256,idrank);
  rankder:=DerivedSubgroup(rankgrp);
  if IsAbelian(rankder) then
    stage_metabelian:=stage_metabelian+1;
    if Size(rankder)=2^(8-dtarget) and
       ForAll(AbelianInvariants(rankgrp/rankder),n->n=2) and
       Exponent(rankder)<=8 then
      stage_exactderived:=stage_exactderived+1;
      rankclass:=NilpotencyClassOfGroup(rankgrp);
      rankcenter:=Centre(rankgrp);
      if rankclass>=3 and Exponent(rankgrp)<=16 and
         Exponent(rankcenter)=2 then
        stage_class_exp_center:=stage_class_exp_center+1;
        if PassesRationalRank(rankgrp) then
          stage_rational:=stage_rational+1;
          if HasSMPExactRank(rankgrp) then
            stage_smp:=stage_smp+1;
            rankwit:=HasDeMeyerWitnessRank(rankgrp,rankder,dtarget);
            Print("EXACT_SMP_STRUCTURAL_ID=",idrank,
                  " CLASS=",rankclass,
                  " DERIVED_INV=",AbelianInvariants(rankder),
                  " CENTER_INV=",AbelianInvariants(rankcenter),
                  " DEMEYER_WITNESS=",rankwit,"\n");
            if rankwit<>fail then Add(parentidsrank,idrank); fi;
          fi;
        fi;
      fi;
    fi;
  fi;
  if rankposlocal mod 250=0 then
    Print("CHECKPOINT_POSITION=",rankstartpos+rankposlocal-1,
          " ID=",idrank,
          " RATIONAL=",stage_rational,
          " EXACT_SMP=",stage_smp,
          " PARENTS=",Length(parentidsrank),"\n");
  fi;
od;

Print("RANK=",dtarget,
      " METABELIAN=",stage_metabelian,
      " EXACT_DERIVED_AND_AB=",stage_exactderived,
      " CLASS_EXP_CENTER=",stage_class_exp_center,
      " RATIONAL=",stage_rational,
      " EXACT_SMP=",stage_smp,
      " PARENT_IDS=",parentidsrank,"\n");

noquit:=true; requirederived:=true; stopafterfirst:=true;
for idrank in parentidsrank do
  ordtarget:=256; idtarget:=idrank;
  Read("Agents/Kourovka/problems/12.15/scratch/screen_nondegenerate_c2_cocycles.g");
od;
QUIT;
