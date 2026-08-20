# Explicit certificate that no nonidentity element of the distinguished
# A=C4xC2 is alpha-regular for the unique Q=[32,49] affine embedding.

Read("Agents/Kourovka/problems/12.15/scratch/pilot_c4c2_q49_full_action_cohomology.g");

Print("Q49_ALPHA_REGULAR_EXCLUSION Q_ID=",IdGroup(S49),
      " A_NONIDENTITY_ELEMENTS=",Length(areps49)-1,"\n");
for aidx49 in [2..Length(areps49)] do
  killer49:=fail;
  for se49 in Elements(S49) do
    lambdaidx49:=1^se49;
    lin49:=se49*transperms49[lambdaidx49]^-1;
    fixes49:=ForAll([1..Length(areps49)],i49->
      acharvals49[i49^lin49][aidx49]=acharvals49[i49][aidx49]);
    if fixes49 and acharvals49[lambdaidx49][aidx49]<>1 then
      killer49:=[se49,lambdaidx49,acharvals49[lambdaidx49][aidx49]];
      break;
    fi;
  od;
  if killer49=fail then Error("unexpected alpha-regular element"); fi;
  Print("A_COORD=",CoordC4C2Q49(areps49[aidx49],a4q49,a2q49),
        " A_ORDER=",Order(areps49[aidx49]),
        " KILLER_Q_PCP_EXP=",
          ExponentsByPcp(upcp49,Image(siso49,killer49[1])),
        " LINEARLY_FIXES_A=true",
        " TRANSLATION_CHARACTER_INDEX=",killer49[2],
        " TRANSLATION_VALUE=",killer49[3],"\n");
od;
Print("ALPHA_REGULAR_NONIDENTITY_COUNT=0\n");
