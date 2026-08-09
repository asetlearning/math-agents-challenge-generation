# Epimorphism F -> R(2,5), word evaluator, and class-12-vs-13 verification
LoadPackage("anupq");;
F := FreeGroup("a","b");;
phi := PqEpimorphism(F : Prime := 5, Exponent := 5);;
Q := Image(phi);;
Print("Image size = 5^", LogInt(Size(Q),5), "\n");
ia := Image(phi, F.1);;
ib := Image(phi, F.2);;
one := One(Q);;

# word -> R(2,5) evaluator over alphabet a,b,A,B
EvalWord := function(str)
  local g, c;
  g := one;
  for c in str do
    if c = 'a' then g := g*ia;
    elif c = 'b' then g := g*ib;
    elif c = 'A' then g := g*ia^-1;
    elif c = 'B' then g := g*ib^-1;
    fi;
  od;
  return g;
end;;

Print("[a,b] nontrivial in R(2,5): ", Comm(ia,ib) <> one, "\n");
Print("EvalWord ABab ([a,b]) nontrivial: ", EvalWord("ABab") <> one, "\n");
Print("EvalWord a^5 trivial: ", EvalWord("aaaaa") = one, "\n");

# Exhaustive left-normed commutator scan: layer-by-layer.
# level k: images of all left-normed [x1,...,xk], xi in {a,b}
gens := [ia, ib];;
level := [ia, ib];;
for k in [2..14] do
  nlevel := [];
  for g in level do
    for x in gens do
      Add(nlevel, Comm(g, x));
    od;
  od;
  level := nlevel;
  Print("weight ", k, ": #left-normed = ", Length(level),
        ", #nontrivial = ", Number(level, g -> g <> one), "\n");
  if ForAll(level, g -> g = one) then
    Print("ALL left-normed commutators of weight ", k, " are trivial => class < ", k, " (gamma_", k, " = 1 mod higher, and since previous layer generated, class = ", k-1, ")\n");
    break;
  fi;
od;

# direct gamma_13 via CommutatorSubgroup
lcs := LowerCentralSeries(Q);;
Print("Length(lcs) = ", Length(lcs), ", last term trivial: ", Size(lcs[Length(lcs)]) = 1, "\n");
g12 := lcs[12];;
Print("Size(gamma_12) = 5^", LogInt(Size(g12),5), "\n");
c13 := CommutatorSubgroup(g12, Q);;
Print("Size([gamma_12, Q]) = ", Size(c13), " (1 means class 12 exactly)\n");

# exhibit a surviving weight-12 left-normed commutator
level := [ia, ib];;
words := ["a","b"];;
found := false;;
for k in [2..12] do
  nlevel := []; nwords := [];
  for i in [1..Length(level)] do
    for j in [1..2] do
      Add(nlevel, Comm(level[i], gens[j]));
      Add(nwords, Concatenation(words[i], ["a","b"][j]));
    od;
  od;
  level := nlevel; words := nwords;
od;
for i in [1..Length(level)] do
  if level[i] <> one then
    Print("surviving weight-12 left-normed commutator [", words[i], "] (letters = entry sequence) is NONTRIVIAL in R(2,5)\n");
    found := true;
    break;
  fi;
od;
if not found then Print("NO weight-12 left-normed commutator survives (unexpected)\n"); fi;
QUIT;
