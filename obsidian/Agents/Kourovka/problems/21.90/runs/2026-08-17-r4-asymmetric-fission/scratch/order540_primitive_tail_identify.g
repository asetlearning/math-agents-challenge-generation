# Identify the two installed degree-540 groups whose full stabilizer-orbit
# computation exceeded the 55 s cheap cap.
for i in [9,10] do
  g:=PrimitiveGroup(540,i);;
  Print("index=",i,
        " generators=",Length(GeneratorsOfGroup(g)),
        " moved_points=",NrMovedPoints(g),
        " onan_scott=",ONanScottType(g),
        " natural_alt=",IsNaturalAlternatingGroup(g),
        " natural_sym=",IsNaturalSymmetricGroup(g),"\n");
od;
QUIT;
