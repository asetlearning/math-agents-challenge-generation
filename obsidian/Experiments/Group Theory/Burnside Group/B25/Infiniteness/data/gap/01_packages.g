for pkg in ["anupq","nq","lpres","ace","kbmag"] do
  Print("PKG ", pkg, " : ", LoadPackage(pkg), "\n");
od;
Print("GAP version: ", GAPInfo.Version, "\n");
QUIT;
