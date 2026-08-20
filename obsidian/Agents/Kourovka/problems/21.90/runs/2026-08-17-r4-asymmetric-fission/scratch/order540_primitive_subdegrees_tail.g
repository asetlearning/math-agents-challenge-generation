# Tail of the exact installed-library gate after the all-index run hit its 45 s cap.
deg:=540;;
Print("GAP=",GAPInfo.Version," primitive_groups_degree_540=",
      NrPrimitiveGroups(deg)," indices=[9,10]\n");
for i in [9,10] do
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
