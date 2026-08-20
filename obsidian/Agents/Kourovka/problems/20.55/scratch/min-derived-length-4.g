LoadPackage("smallgrp");
Print("GAP_VERSION=", GAPInfo.Version, "\n");
Print("SMALLGRP_VERSION=", InstalledPackageVersion("smallgrp"), "\n");
FindFirstDL4 := function()
  local n, ids;
  for n in [1..255] do
    if NumberSmallGroups(n) <> fail then
      ids := IdsOfAllSmallGroups(Size, n, IsSolvableGroup, true, DerivedLength, 4);
      if Length(ids) > 0 then
        Print("FIRST_ORDER=", n, " COUNT=", Length(ids), " IDS=", ids, "\n");
        return;
      fi;
    fi;
  od;
  Print("NONE_THROUGH=255\n");
end;
FindFirstDL4();
QUIT;
