LoadPackage("grape");

SRGParams := function(g)
  local V,k,adj,lams,mus,x,y,c;
  V := [1..OrderGraph(g)];
  k := Length(Adjacency(g,1));
  if not ForAll(V,x->Length(Adjacency(g,x))=k) then return fail; fi;
  lams := []; mus := [];
  for x in V do
    adj := Adjacency(g,x);
    for y in [x+1..OrderGraph(g)] do
      c := Length(Intersection(adj,Adjacency(g,y)));
      if y in adj then AddSet(lams,c); else AddSet(mus,c); fi;
    od;
  od;
  if Length(lams)=1 and Length(mus)=1 then
    return [OrderGraph(g),k,lams[1],mus[1]];
  fi;
  return ["notSRG",k,lams,mus];
end;

Report := function(name,g)
  Print(name," vertices=",OrderGraph(g)," distance_regular=",IsDistanceRegular(g),
        " G2=",SRGParams(DistanceGraph(g,[2])),
        " G3=",SRGParams(DistanceGraph(g,[3])),"\n");
end;

for q in [2..7] do Report(Concatenation("H(3,",String(q),")"),HammingGraph(3,q)); od;
for n in [6..10] do Report(Concatenation("J(",String(n),",3)"),JohnsonGraph(n,3)); od;

# Odd graph O_4 = Kneser graph KG(7,3).
V := Combinations([1..7],3);
g := Graph(Group(()),V,function(x,z) return x; end,
           function(x,y) return IsEmpty(Intersection(x,y)); end,true);
Report("Odd graph O4=KG(7,3)",g);

# Halved 7-cube: even subsets of a 7-set, adjacent when symmetric difference has size 2.
V := Filtered(Combinations([1..7]),x->IsEvenInt(Length(x)));
g := Graph(Group(()),V,function(x,z) return x; end,
           function(x,y) return Length(Difference(Union(x,y),Intersection(x,y)))=2; end,true);
Report("halved 7-cube",g);

QUIT;
