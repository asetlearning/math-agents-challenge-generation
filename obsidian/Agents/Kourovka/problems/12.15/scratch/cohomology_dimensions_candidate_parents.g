# Compute only H^2(H,C2) dimensions for the parent candidates observed in
# the capped high-ID order-256 pilot.  This does not enumerate extensions.

Print("GAP_VERSION=", GAPInfo.Version, "\n");
for id in [53342,53343,53355,53356,53357,53358,53359] do
  H := SmallGroup(256,id);
  mats := List(Pcgs(H), x -> IdentityMat(1,GF(2)));
  modu := GModuleByMats(mats,GF(2));
  coh := TwoCohomology(H,modu);
  Print("PARENT_ID=", id,
        " H2_DIM=", Dimension(Image(coh.cohom)),
        " H2_SIZE=", Size(Image(coh.cohom)), "\n");
od;
QUIT;
