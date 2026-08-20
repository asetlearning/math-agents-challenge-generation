LoadPackage("grape");

pts := [];
for x1 in [0..4] do for x2 in [0..4] do for x3 in [0..4] do
for x4 in [0..4] do for x5 in [0..4] do
  x := [x1,x2,x3,x4,x5];
  pos := First([1..5],i->x[i]<>0);
  if pos<>fail and x[pos]=1 then Add(pts,x); fi;
od; od; od; od; od;
Q := x -> (x[1]*x[2]+x[3]*x[4]+x[5]^2) mod 5;
B := function(x,y)
  return (x[1]*y[2]+x[2]*y[1]+x[3]*y[4]+x[4]*y[3]+2*x[5]*y[5]) mod 5;
end;
types := List([0..4],q->Filtered(pts,x->Q(x)=q));
Print("projective_points=",Length(pts)," Q_counts=",List(types,Length),"\n");

# Multiplication by a projective scalar changes Q by a square, so Q=1 and 4
# form one intrinsic type and Q=2 and 3 the other.
for chosen in [Concatenation(types[2],types[5]),Concatenation(types[3],types[4])] do
  adj := List(chosen,x->Filtered([1..Length(chosen)],j->B(x,chosen[j])=0));
  degs := Set(List(adj,Length));
  commonAdj := Set(List(Combinations([1..Length(chosen)],2),ij->Length(Intersection(adj[ij[1]],adj[ij[2]]))));
  Print("type_size=",Length(chosen)," degrees=",degs," common_counts=",commonAdj,"\n");
od;

chosen := Concatenation(types[3],types[4]);
gamma := Graph(Group(()),chosen,function(x,g) return x; end,function(x,y) return x<>y and B(x,y)=0; end,true);
aut := AutGroupGraph(gamma);
stab := Stabilizer(aut,1);
Print("minus_perp aut_order=",Size(aut)," vertex_orbit=",Length(Orbit(aut,1)),
      " stabilizer_orbit_sizes=",SortedList(List(Orbits(stab,[1..300]),Length)),"\n");
der := DerivedSubgroup(aut);
if Length(Orbit(der,1))=300 then
  Print("derived_order=",Size(der)," stabilizer_orbit_sizes=",
        SortedList(List(Orbits(Stabilizer(der,1),[1..300]),Length)),"\n");
else
  Print("derived_order=",Size(der)," vertex_orbit_sizes=",SortedList(List(Orbits(der,[1..300]),Length)),"\n");
fi;
tm := Runtime();

TestTransitiveGroup := function(h,label)
  local st,orbs,bases,o,y,og,nbr,d,z,hit,tested,linearpass,suffix,CheckComb,Search,
        reps,controller,crossmat,suffixcross,ci,bi,row,expected,newcross,newcomb,jj,ExpectedCross;
  if Length(Orbit(h,1))<>300 then return 0; fi;
  st:=Stabilizer(h,1); orbs:=Orbits(st,[2..300]); bases:=[];
  for o in orbs do
    y:=o[1]; og:=EdgeOrbitsGraph(h,[1,y],300); nbr:=Adjacency(og,1); d:=Length(nbr);
    if d<=39 and Intersection(nbr,Adjacency(gamma,1))=[] and
       ForAll(bases,z->Adjacency(z[2],1)<>nbr) then Add(bases,[[1,y],og,d]); fi;
  od;
  Print("TRANSITIVE label=",label," order=",Size(h)," base_degrees=",List(bases,z->z[3]),"\n");
  reps:=List(orbs,o->o[1]); controller:=[];
  for y in reps do
    if y in Adjacency(gamma,1) then Add(controller,-1);
    else Add(controller,First([1..Length(bases)],bi->y in Adjacency(bases[bi][2],1))); fi;
    if controller[Length(controller)]=fail then controller[Length(controller)]:=0; fi;
  od;
  crossmat:=List(reps,y->List([1..Length(bases)],bi->
    Length(Intersection(Adjacency(bases[bi][2],1),Adjacency(gamma,y)))));
  ExpectedCross:=function(ci,comb)
    if controller[ci]=-1 then return 9; fi;
    if controller[ci] in comb then return 0; fi;
    return 10;
  end;
  hit:=0; tested:=0; linearpass:=0;
  CheckComb:=function(comb)
    local nx,ny,common,expectedCommon,jj;
    tested:=tested+1;
    nx:=Set(Concatenation(List(comb,jj->Adjacency(bases[jj][2],1))));
    if Length(nx)<>39 then return; fi;
    linearpass:=linearpass+1;
    for y in reps do
      ny:=Set(Concatenation(List(comb,jj->Adjacency(bases[jj][2],y))));
      common:=Length(Intersection(nx,ny));
      if y in nx then expectedCommon:=13;
      elif y in Adjacency(gamma,1) then expectedCommon:=0;
      else expectedCommon:=5; fi;
      if common<>expectedCommon then return; fi;
    od;
    hit:=hit+1; Print("TARGET_HIT label=",label," base_indices=",comb,"\n");
  end;
  suffix:=ListWithIdenticalEntries(Length(bases)+1,0);
  for y in Reversed([1..Length(bases)]) do suffix[y]:=suffix[y+1]+bases[y][3]; od;
  suffixcross:=List([1..Length(reps)],ci->ListWithIdenticalEntries(Length(bases)+1,0));
  for ci in [1..Length(reps)] do
    for bi in Reversed([1..Length(bases)]) do suffixcross[ci][bi]:=suffixcross[ci][bi+1]+crossmat[ci][bi]; od;
  od;
  Search:=function(pos,total,comb,cross)
    if ForAny(cross,z->z>10) then return; fi;
    for ci in [1..Length(reps)] do
      if controller[ci] in comb and cross[ci]<>0 then return; fi;
      if controller[ci]=-1 then expected:=9;
      elif controller[ci]=0 or (controller[ci]<pos and not controller[ci] in comb) then expected:=10;
      else expected:=fail; fi;
      if expected<>fail and (cross[ci]>expected or cross[ci]+suffixcross[ci][pos]<expected) then return; fi;
    od;
    if total=39 then
      if ForAll([1..Length(reps)],ci->cross[ci]=ExpectedCross(ci,comb)) then CheckComb(comb); fi;
      return;
    fi;
    if pos>Length(bases) or total>39 or total+suffix[pos]<39 then return; fi;
    Search(pos+1,total,comb,cross);
    if total+bases[pos][3]<=39 then
      newcross:=List([1..Length(reps)],ci->cross[ci]+crossmat[ci][pos]);
      Search(pos+1,total+bases[pos][3],Concatenation(comb,[pos]),newcross);
    fi;
  end;
  Search(1,0,[],ListWithIdenticalEntries(Length(reps),0));
  Print("TRANSITIVE_DONE label=",label," linear_unions_tested=",tested," quadratic_passes=",linearpass," hits=",hit,"\n");
  return hit;
end;

tom:=TableOfMarks("S4(5)"); u:=UnderlyingGroup(tom); iso:=IsomorphismGroups(u,der);
Print("tom_classes=",Length(OrdersTom(tom))," iso_fail=",iso=fail,"\n");
transcount:=0; hitcount:=0; twoorbit:=[];
for idx in [1..Length(OrdersTom(tom))] do
  if Size(der) mod OrdersTom(tom)[idx]=0 and OrdersTom(tom)[idx] mod 150=0 then
    h:=Image(iso,RepresentativeTom(tom,idx));
    os:=SortedList(List(Orbits(h,[1..300]),Length));
    if os=[300] then
      transcount:=transcount+1; hitcount:=hitcount+TestTransitiveGroup(h,Concatenation("D:",String(idx)));
    elif os=[150,150] then Add(twoorbit,[idx,h]); fi;
  fi;
od;
Print("derived_transitive_classes=",transcount," derived_target_hits=",hitcount,
      " two_150_classes=",Length(twoorbit)," runtime_ms=",Runtime()-tm,"\n");
outertested:=0; outertrans:=0; outerhits:=0;
for pair in twoorbit do
  idx:=pair[1]; h0:=pair[2]; nrm:=Normalizer(aut,h0);
  hom:=NaturalHomomorphismByNormalSubgroup(nrm,h0); quo:=Image(hom);
  dquo:=Image(hom,Intersection(nrm,der));
  outerels:=Filtered(Elements(quo),qel->not qel in dquo and Order(qel)=2);
  Print("OUTER_BASE D:",idx," h0_order=",Size(h0)," normalizer_order=",Size(nrm),
        " quotient_order=",Size(quo)," outer_involutions=",Length(outerels),"\n");
  for qel in outerels do
    outertested:=outertested+1; lift:=PreImagesRepresentative(hom,qel);
    h:=Group(Concatenation(GeneratorsOfGroup(h0),[lift]));
    if Length(Orbit(h,1))=300 then
      outertrans:=outertrans+1;
      outerhits:=outerhits+TestTransitiveGroup(h,Concatenation("OUT:",String(idx),":",String(outertested)));
    fi;
  od;
od;
Print("outer_extensions_tested=",outertested," outer_transitive=",outertrans,
      " outer_target_hits=",outerhits," total_vertex_transitive_hits=",hitcount+outerhits,
      " total_runtime_ms=",Runtime()-tm,"\n");
QUIT;
