# Capped diagnosis of the raw-pcp conjugacy slowdown first seen after orbit 312.

Read("Agents/Kourovka/problems/12.15/scratch/pilot_c4c2_q49_compatible_orbits.g");

PowerRationalDiagnosticQ49 := function(G)
  local cc,x,o,k;
  for cc in ConjugacyClasses(G) do
    x:=Representative(cc); o:=Order(x);
    for k in [1..o] do
      if GcdInt(k,o)=1 and not IsConjugate(G,x,x^k) then
        return [false,ExponentsOfPcElement(Pcgs(G),x),k];
      fi;
    od;
  od;
  return [true,fail,fail];
end;

opos49:=313; coeff49:=orbitreps49[opos49];
coc49:=IntVector(coeff49*coh49.factor.prei);
tails49:=TailVectorModQ49(coc49);
t49:=Runtime(); parent49:=ExtensionC4C2Q49(C49rec,tails49,actioncoords49);
Print("ORBIT=",opos49," COEFF=",coeff49," CONSTRUCT_MS=",Runtime()-t49,
      " ORDER=",Size(parent49)," KERNEL_ORDER=",Size(parent49!.markedmoduleQ49),"\n");
t49:=Runtime(); hid49:=IdGroup(parent49)[2];
Print("H_ID=",hid49," IDGROUP_MS=",Runtime()-t49,"\n");
can49:=SmallGroup(256,hid49); t49:=Runtime();
powcan49:=PowerRationalDiagnosticQ49(can49);
Print("CANONICAL_POWER_RESULT=",powcan49,
      " CANONICAL_POWER_MS=",Runtime()-t49,"\n");
t49:=Runtime(); powraw49:=PowerRationalDiagnosticQ49(parent49);
Print("RAW_POWER_RESULT=",powraw49," RAW_POWER_MS=",Runtime()-t49,"\n");
