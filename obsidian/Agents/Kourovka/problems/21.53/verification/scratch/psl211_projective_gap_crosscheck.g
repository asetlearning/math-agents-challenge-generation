# Independent projective-line representation of PSL(2,11).
# Points 1..11 represent x=0..10 and point 12 represents infinity.
# u:x|->x+1 and s:x|->-1/x come from determinant-one matrices.
u := (1,2,3,4,5,6,7,8,9,10,11);;
s := (1,12)(2,11)(3,6)(4,8)(5,9)(7,10);;
G := Group([u,s]);;
classes := ConjugacyClasses(G);;
classData := List(classes, c -> [Order(Representative(c)), Size(c)]);;
involutionClasses := Filtered(classes, c -> Order(Representative(c)) = 2);;

if Size(G) <> 660 then Error("wrong order"); fi;
if IsAbelian(G) then Error("unexpectedly abelian"); fi;
if not IsSimpleGroup(G) then Error("not simple"); fi;
if Size(Centre(G)) <> 1 then Error("projective group has nontrivial centre"); fi;
if Length(classes) <> 8 then Error("wrong conjugacy-class count"); fi;
if Length(involutionClasses) <> 1 or Size(involutionClasses[1]) <> 55 then
  Error("wrong involution classes");
fi;

Print("PSL211_PROJECTIVE_GAP_OK\n");
Print("GAP_VERSION=", GAPInfo.Version, "\n");
Print("ORDER=", Size(G), "\n");
Print("IS_ABELIAN=", IsAbelian(G), "\n");
Print("IS_SIMPLE=", IsSimpleGroup(G), "\n");
Print("CENTRE_ORDER=", Size(Centre(G)), "\n");
Print("CLASS_ORDER_SIZE=", classData, "\n");
Print("INVOLUTION_CLASS_COUNT=", Length(involutionClasses), "\n");
Print("INVOLUTION_CLASS_SIZE=", Size(involutionClasses[1]), "\n");
QUIT;
