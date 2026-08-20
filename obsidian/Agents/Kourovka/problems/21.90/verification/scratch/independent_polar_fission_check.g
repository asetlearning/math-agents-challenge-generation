LoadPackage("grape");;

# Build projective representatives and the nonsquare-type perpendicularity graph.
P:=[];;
for a in Tuples([0..4],5) do
  j:=PositionProperty(a,z->z<>0);
  if j<>fail and a[j]=1 then Add(P,a); fi;
od;
q:=a->(a[1]*a[2]+a[3]*a[4]+a[5]^2) mod 5;;
b:=function(a,c) return (a[1]*c[2]+a[2]*c[1]+a[3]*c[4]+a[4]*c[3]+2*a[5]*c[5]) mod 5; end;;
V:=Filtered(P,a->q(a) in [2,3]);;
polar:=Graph(Group(()),V,function(a,g)return a;end,function(a,c)return a<>c and b(a,c)=0;end,true);;
G:=AutGroupGraph(polar);; D:=DerivedSubgroup(G);;
Print("vertices=",Length(V)," degree=",VertexDegree(polar,1)," aut=",Size(G)," derived=",Size(D),"\n");

# For a transitive group K, form each undirected orbital once. Search all unions
# using the coefficient equations for A1*A3 directly on stabilizer-orbit reps.
Check:=function(K,label)
  local S,O,R,E,o,y,Z,N,c,ctrl,coef,deg,ans,walk;
  if Length(Orbit(K,1))<>300 then return 0; fi;
  S:=Stabilizer(K,1); O:=Orbits(S,[2..300]); E:=[];
  for o in O do
    y:=o[1]; Z:=EdgeOrbitsGraph(K,[1,y],300); N:=Set(Adjacency(Z,1));
    if Intersection(N,Adjacency(polar,1))=[] and Length(N)<=39 and
       not N in List(E,e->e[1]) then Add(E,[N,Z]); fi;
  od;
  R:=List(O,o->o[1]); deg:=List(E,e->Length(e[1]));
  ctrl:=List(R,y->y in Adjacency(polar,1));
  coef:=List(R,y->List(E,e->Length(Intersection(e[1],Adjacency(polar,y)))));
  ans:=0;
  walk:=function(i,sum,v)
    local nv,r,target;
    if sum>39 then return; fi;
    if i>Length(E) then
      if sum<>39 then return; fi;
      for r in [1..Length(R)] do
        if ctrl[r] then target:=9;
        elif R[r] in Union(List(Filtered([1..Length(E)],z->v[z]=1),z->E[z][1])) then target:=0;
        else target:=10; fi;
        if Sum([1..Length(E)],z->v[z]*coef[r][z])<>target then return; fi;
      od;
      ans:=ans+1; return;
    fi;
    v[i]:=0; walk(i+1,sum,v);
    v[i]:=1; walk(i+1,sum+deg[i],v);
    v[i]:=0;
  end;
  # Avoid exponential blow-up: reject partial vectors as soon as any coefficient
  # exceeds 10; this does not discard a nonnegative solution.
  walk:=function(i,sum,v)
    local nv,r,target,U;
    if sum>39 or ForAny([1..Length(R)],r->Sum([1..i-1],z->v[z]*coef[r][z])>10) then return; fi;
    if i>Length(E) then
      if sum<>39 then return; fi;
      U:=Union(List(Filtered([1..Length(E)],z->v[z]=1),z->E[z][1]));
      for r in [1..Length(R)] do
        if ctrl[r] then target:=9; elif R[r] in U then target:=0; else target:=10; fi;
        if Sum([1..Length(E)],z->v[z]*coef[r][z])<>target then return; fi;
      od;
      ans:=ans+1; return;
    fi;
    v[i]:=0; walk(i+1,sum,v); v[i]:=1; walk(i+1,sum+deg[i],v); v[i]:=0;
  end;
  walk(1,0,ListWithIdenticalEntries(Length(E),0));
  Print(label," order=",Size(K)," orbitals=",Length(E)," solutions=",ans,"\n");
  return ans;
end;;

T:=TableOfMarks("S4(5)");; U:=UnderlyingGroup(T);; f:=IsomorphismGroups(U,D);;
hits:=0;; trans:=0;; halves:=[];;
for i in [1..Length(OrdersTom(T))] do
  if OrdersTom(T)[i] mod 150=0 then
    K:=Image(f,RepresentativeTom(T,i));; os:=SortedList(List(Orbits(K,[1..300]),Length));
    if os=[300] then trans:=trans+1; hits:=hits+Check(K,Concatenation("D",String(i)));
    elif os=[150,150] then Add(halves,[i,K]); fi;
  fi;
od;
outer:=0;;
for p in halves do
  N:=Normalizer(G,p[2]);; hom:=NaturalHomomorphismByNormalSubgroup(N,p[2]);;
  Q:=Image(hom);; QD:=Image(hom,Intersection(N,D));;
  for e in Elements(Q) do
    if not e in QD and Order(e)=2 then
      K:=ClosureGroup(p[2],PreImagesRepresentative(hom,e));;
      if Length(Orbit(K,1))=300 then outer:=outer+1; hits:=hits+Check(K,Concatenation("O",String(p[1]))); fi;
    fi;
  od;
od;
Print("transitive_in_D=",trans," half_classes=",Length(halves)," outer_extensions=",outer," total_solutions=",hits,"\n");
QUIT;
