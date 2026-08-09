# End-to-end re-verification of the exact strings in candidates.txt
LoadPackage("anupq");;
F := FreeGroup("a","b");;
phi := PqEpimorphism(F : Prime := 5, Exponent := 5);;
Q := Image(phi);;
ia := Image(phi, F.1);; ib := Image(phi, F.2);; oneQ := One(Q);;
EvalWord := function(str)
  local g, c;
  g := oneQ;
  for c in str do
    if c = 'a' then g := g*ia; elif c = 'b' then g := g*ib;
    elif c = 'A' then g := g*ia^-1; elif c = 'B' then g := g*ib^-1; fi;
  od;
  return g;
end;;
lines := ReadAsFunction; # placeholder
input := InputTextFile("candidates.txt");;
nok := 0;; nbad := 0;;
line := ReadLine(input);;
while line <> fail do
  parts := SplitString(Chomp(line), "\t");
  if Length(parts) = 3 then
    w := parts[3];
    ea := Number(w, c -> c='a') - Number(w, c -> c='A');
    eb := Number(w, c -> c='b') - Number(w, c -> c='B');
    triv := EvalWord(w) = oneQ;
    if ea = 0 and eb = 0 and triv and Length(w) = Int(parts[2]) then
      nok := nok + 1;
    else
      nbad := nbad + 1;
      Print("BAD: ", parts[1], " abel=[",ea,",",eb,"] trivial=",triv,"\n");
    fi;
  fi;
  line := ReadLine(input);
od;
CloseStream(input);;
Print("candidates.txt verification: ", nok, " OK, ", nbad, " BAD\n");
QUIT;
