T := GL(3,2);
classes := ConjugacyClassesSubgroups(T);
order21 := Filtered(classes, c -> Size(Representative(c))=21);
Print("GAP_VERSION=", GAPInfo.Version, "\n");
Print("T_ID=", IdGroup(T), " T_SIZE=", Size(T), "\n");
Print("ORDER21_CONJUGACY_CLASSES=", Length(order21), "\n");
for c in order21 do
  P := Representative(c);
  Print("P_ID=", IdGroup(P), " P_DESC=", StructureDescription(P),
        " CLASS_SIZE=", Size(c), " NORMALIZER_SIZE=", Size(Normalizer(T,P)),
        " INDEX=", Index(T,P), "\n");
od;
Print("RUN_COMPLETE=true\n");
QUIT;
