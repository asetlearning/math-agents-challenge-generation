# Exact installed-library gate for degree-540 primitive groups.
deg:=540;;
n:=NrPrimitiveGroups(deg);;
Print("GAP=",GAPInfo.Version," primitive_groups_degree_540=",n,"\n");
for i in [1..n] do
  g:=PrimitiveGroup(deg,i);;
  h:=Stabilizer(g,1);;
  os:=Orbits(h,[1..deg]);;
  lens:=List(os,Length);;
  Print("index=",i," order=",Size(g)," subdegrees=",lens,"\n");
  for o in Filtered(os,z->Length(z)=77) do
    b:=o[1];;
    t:=RepresentativeAction(g,1,b);;
    if t=fail then
      Error("transitive primitive group lacked a transporter");
    fi;
    pairedpoint:=1^(t^-1);;
    Print("  length77 representative=",b,
          " paired_representative=",pairedpoint,
          " self_paired=",pairedpoint in o,"\n");
  od;
od;
QUIT;
