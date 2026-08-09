# Kernel-candidate search: short balanced commutator-tree words of LCS-weight 13/14.
# Such words lie in gamma_w(F), w >= 13 > class(R(2,5)) = 12, hence die in R(2,5).
LoadPackage("anupq");;
F := FreeGroup("a","b");;
a := F.1;; b := F.2;;
phi := PqEpimorphism(F : Prime := 5, Exponent := 5);;
Q := Image(phi);;
oneQ := One(Q);;
Print("R(2,5) size = 5^", LogInt(Size(Q),5), "\n");

WordString := function(w)
  local rep, s, x;
  rep := LetterRepAssocWord(UnderlyingElement(w));
  s := "";
  for x in rep do
    if x = 1 then Add(s,'a');
    elif x = -1 then Add(s,'A');
    elif x = 2 then Add(s,'b');
    elif x = -2 then Add(s,'B');
    fi;
  od;
  return s;
end;;

leaves := [a, b, a^-1, b^-1];;

# random near-balanced commutator tree of total leaf-weight w
RandTree := function(w)
  local w1, u, v, tries, lo, hi;
  if w = 1 then return Random(leaves); fi;
  tries := 0;
  repeat
    lo := Maximum(1, QuoInt(w,2) - Random([0,0,0,1,1,2]));
    w1 := Minimum(w-1, lo);
    u := RandTree(w1);
    v := RandTree(w - w1);
    tries := tries + 1;
  until Comm(u,v) <> One(F) or tries > 20;
  return Comm(u,v);
end;;

results := rec(w13 := [], w14 := []);;
seen := NewDictionary("", true);;

for pair in [ [13, "w13"], [14, "w14"] ] do
  w := pair[1];
  for trial in [1..6000] do
    c := RandTree(w);
    if c = One(F) then continue; fi;
    s := WordString(c);
    si := WordString(c^-1);
    if si < s then s := si; c := c^-1; fi;
    if LookupDictionary(seen, s) <> fail then continue; fi;
    AddDictionary(seen, s, true);
    Add(results.(pair[2]), rec(len := Length(s), str := s, wt := w, elt := c));
  od;
  Sort(results.(pair[2]), function(x,y) return x.len < y.len; end);
  Print("weight ", w, ": ", Length(results.(pair[2])), " distinct candidates, shortest length ", results.(pair[2])[1].len, "\n");
od;

# verify top candidates: exponent sums zero (abelianization) and trivial in R(2,5)
Verify := function(r)
  local ea, eb, im;
  ea := ExponentSumWord(UnderlyingElement(r.elt), UnderlyingElement(a));
  eb := ExponentSumWord(UnderlyingElement(r.elt), UnderlyingElement(b));
  im := Image(phi, r.elt);
  return rec(abel := [ea, eb], inR := (im = oneQ));
end;;

Print("\n=== TOP CANDIDATES (weight 14 first, then weight 13) ===\n");
count := 0;;
for r in results.w14{[1..Minimum(12, Length(results.w14))]} do
  v := Verify(r);
  count := count + 1;
  Print("W14-", count, " len=", r.len, " abel=", v.abel, " trivial_in_R=", v.inR, "\n  ", r.str, "\n");
od;
count := 0;;
for r in results.w13{[1..Minimum(8, Length(results.w13))]} do
  v := Verify(r);
  count := count + 1;
  Print("W13-", count, " len=", r.len, " abel=", v.abel, " trivial_in_R=", v.inR, "\n  ", r.str, "\n");
od;

# negative control: a weight-12 balanced commutator that is NONtrivial in R(2,5)
# (shows the pipeline does not trivially kill everything of this shape)
ctrl := fail;;
for trial in [1..2000] do
  c := RandTree(12);
  if c <> One(F) and Image(phi, c) <> oneQ then ctrl := c; break; fi;
od;
if ctrl <> fail then
  Print("\nCONTROL weight-12 balanced commutator NONTRIVIAL in R(2,5): len=",
        Length(WordString(ctrl)), "\n  ", WordString(ctrl), "\n");
else
  Print("\nCONTROL: no nontrivial weight-12 balanced commutator found in 2000 trials\n");
fi;
QUIT;
