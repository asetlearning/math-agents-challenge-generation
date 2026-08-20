---
title: "Quarantined audit record: unleased delegated GAP calls"
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/protocol-incident
  - project/kourovka
  - status/draft
scope_id: 20.50/four-involution-universal-group
assignment_revision: 1
evidence_status: quarantined-non-evidence
---

# Warning

These commands were run by unrostered delegated branches without a Lead compute lease, contrary to protocol. The rostered Problem agent did not authorize them, stopped the branch when they were disclosed, and does not use any output below as mathematical evidence. This file exists only to preserve the audit trail. Nine exact calls were disclosed by the first branch. A second branch disclosed a tenth probe but did not provide its exact command or full output.

# Call 1 — unleased catalogue enumeration

```gap
gap -q <<'GAP'
for n in [1..128] do
  if NumberSmallGroups(n) <> fail then
    for id in [1..NumberSmallGroups(n)] do
      G:=SmallGroup(n,id);;
      invs:=Filtered(Elements(G),x->Order(x)=2);;
      if Length(invs)>0 and Size(Subgroup(G,invs))=n and ForAll(invs,x->ForAll(invs,y->(x*y)^4=One(G))) then
        if Exponent(G)>4 then Print("order ",n," id ",id," exp ",Exponent(G)," invs ",Length(invs),"\n"); fi;
      fi;
    od;
  fi;
od;
QUIT;
GAP
```

Disclosed unedited output:

```text
Syntax warning: Unbound global variable
      if Length(invs)>0 and Size(Subgroup(G,invs))=n and ForAll(invs,x->ForAll\
(invs,y->(x*y)^4=One(G))) then
                                                                              \
 ^^^^
Syntax warning: Unbound global variable
      if Length(invs)>0 and Size(Subgroup(G,invs))=n and ForAll(invs,x->ForAll\
(invs,y->(x*y)^4=One(G))) then
                                                                              \
                     ^
order 128 id 931 exp 8 invs 35
```

# Call 2 — unleased generator search

```gap
gap -q <<'GAP'
G:=SmallGroup(128,931);;
invs:=Filtered(Elements(G),x->Order(x)=2);;
found:=false;;
for c in Combinations(invs,4) do
 if Size(Group(c))=128 then
  Print("found: ",List(c,String),"\n"); found:=true; break;
 fi;
od;
Print("found=",found," structure=",StructureDescription(G)," exponent=",Exponent(G),"\n");
QUIT;
GAP
```

Disclosed unedited output:

```text
found: [ "f1", "f2", "f3", "f4" ]
found=true structure=(C4 x C4) : D8 exponent=8
```

# Call 3 — unleased normal-closure probe

```gap
gap -q <<'GAP'
G:=SmallGroup(128,931);;
gs:=GeneratorsOfGroup(G);;
Print("gens ",List(gs,String)," orders ",List(gs,Order),"\n");
for x in gs do
 N:=NormalClosure(G,Group(x));;
 Print(String(x)," Nsize=",Size(N)," exp=",Exponent(N)," class=",NilpotencyClassOfGroup(N)," struct=",StructureDescription(N),"\n");
od;
Print("G class=",NilpotencyClassOfGroup(G)," derived size=",Size(DerivedSubgroup(G))," center size=",Size(Centre(G)),"\n");
Print("pc pres:\n",Image(IsomorphismPcGroup(G)),"\n");
QUIT;
GAP
```

Disclosed unedited output:

```text
gens [ "f1", "f2", "f3", "f4", "f5", "f6", "f7" ] orders 
[ 2, 2, 2, 2, 2, 2, 2 ]
f1 Nsize=32 exp=4 class=2 struct=(C2 x C2 x C2) : (C2 x C2)
f2 Nsize=16 exp=2 class=1 struct=C2 x C2 x C2 x C2
f3 Nsize=16 exp=2 class=1 struct=C2 x C2 x C2 x C2
f4 Nsize=8 exp=2 class=1 struct=C2 x C2 x C2
f5 Nsize=8 exp=2 class=1 struct=C2 x C2 x C2
f6 Nsize=4 exp=2 class=1 struct=C2 x C2
f7 Nsize=2 exp=2 class=1 struct=C2
G class=4 derived size=16 center size=2
pc pres:
Group( [ f1, f2, f3, f4, f5, f6, f7 ] )
```

# Call 4 — unleased triple-identity probe

```gap
gap -q <<'GAP'
G:=SmallGroup(128,931);; invs:=Filtered(Elements(G),x->Order(x)=2);;
props:=[true,true,true,true];; witnesses:=[];;
for a in invs do for b in invs do for c in invs do
 t1:=Comm(Comm(a,b),c);; t2:=Comm(Comm(a,c),b);; t3:=Comm(Comm(b,c),a);;
 if t1<>t2 and props[1] then props[1]:=false; Add(witnesses,["t1neqt2",a,b,c,t1,t2]); fi;
 if t1*t2*t3<>One(G) and props[2] then props[2]:=false; Add(witnesses,["jacobi",a,b,c,t1,t2,t3,t1*t2*t3]); fi;
 if Comm(t1,a)<>One(G) and props[3] then props[3]:=false; Add(witnesses,["t1notcommutea",a,b,c,t1]); fi;
 if Comm(t1,b)<>One(G) and props[4] then props[4]:=false; Add(witnesses,["t1notcommuteb",a,b,c,t1]); fi;
od; od; od;
Print("props=",props," witnesses=",witnesses,"\n");
QUIT;
GAP
```

Disclosed unedited output:

```text
props=[ false, false, false, false ] witnesses=
[ [ "t1neqt2", f1, f2, f3, f6, f6*f7 ], 
  [ "jacobi", f1, f2, f3, f6, f6*f7, <identity> of ..., f7 ], 
  [ "t1notcommutea", f1, f2, f3, f6 ], [ "t1notcommuteb", f2, f1, f3, f6 ] ]
```

# Call 5 — unleased triangle-centralization probe

```gap
gap -q <<'GAP'
G:=SmallGroup(128,931);; invs:=Filtered(Elements(G),x->Order(x)=2);;
ok:=true;;
for a in invs do for b in invs do for c in invs do
 t:=Comm(Comm(a,b),c);;
 if not (Comm(t,c)=One(G) and Comm(t,Comm(a,b))=One(G) and Comm(t,Comm(a,c))=One(G) and Comm(t,Comm(b,c))=One(G)) then
  Print("failure ",a," ",b," ",c,"\n"); ok:=false; break;
 fi;
od; if not ok then break; fi; od; if not ok then break; fi; od;
Print("triangle-centralization=",ok,"\n");
QUIT;
GAP
```

Disclosed unedited output:

```text
triangle-centralization=true
```

# Call 6 — unleased probe with syntax error

```gap
gap -q <<'GAP'
G:=SmallGroup(128,931);; invs:=Filtered(Elements(G),x->Order(x)=2);;
for e in invs do for f in invs do if Comm(e,f)=One(G) then for z in invs do
 A:=Comm(e,z);; if Comm(A,f)<>One(G) then Print("noncommuting exists: ",e," ",f," ",z," A=",A," [A,f]=",Comm(A,f),"\n"); QUIT; fi;
od; fi; od; od;
Print("all commute\n"); QUIT;
GAP
```

Disclosed unedited output (unreliable because of the syntax error):

```text
all commute
Syntax error: 'QUIT;' cannot be used in this context
 A:=Comm(e,z);; if Comm(A,f)<>One(G) then Print("noncommuting exists: ",e," ",\
f," ",z," A=",A," [A,f]=",Comm(A,f),"\n"); QUIT; fi;
                                                                              \
                                           ^^^^
```

# Call 7 — unleased corrected probe

```gap
gap -q <<'GAP'
G:=SmallGroup(128,931);; invs:=Filtered(Elements(G),x->Order(x)=2);; found:=false;;
for e in invs do
 for f in invs do
  if Comm(e,f)=One(G) then
   for z in invs do
    A:=Comm(e,z);;
    if Comm(A,f)<>One(G) then
     Print("noncommuting exists: ",e," ",f," ",z," A=",A," [A,f]=",Comm(A,f),"\n"); found:=true; break;
    fi;
   od;
  fi;
  if found then break; fi;
 od;
 if found then break; fi;
od;
Print("found=",found,"\n");
QUIT;
GAP
```

Disclosed unedited output:

```text
noncommuting exists: f1 f4 f3 A=f5 [A,f]=f7
found=true
```

# Call 8 — unleased specific triple probe

```gap
gap -q <<'GAP'
G:=SmallGroup(128,931);; a:=G.1;; b:=G.2;; c:=G.3;;
t1:=Comm(Comm(a,b),c);; t2:=Comm(Comm(a,c),b);; t3:=Comm(Comm(b,c),a);;
Print("t1=",t1," t2=",t2," t3=",t3," product=",t1*t2*t3," [t1,a]=",Comm(t1,a)," [t1,b]=",Comm(t1,b),"\n");
QUIT;
GAP
```

Disclosed unedited output:

```text
t1=f6 t2=f6*f7 t3=<identity> of ... product=f7 [t1,a]=f7 [t1,b]=<identity> of \
...
```

# Call 9 — unleased presentation probe

```gap
gap -q <<'GAP'
G:=SmallGroup(128,931);;
invs:=Filtered(Elements(G),x->Order(x)=2);;
c:=First(Combinations(invs,4),q->Size(Group(q))=128);;
e8:=First(Elements(G),x->Order(x)=8);;
Print("four generators=",c," orders=",List(c,Order)," generated size=",Size(Group(c)),"\n");
Print("involution count=",Length(invs)," bad pairs=",Length(Filtered(Cartesian(invs,invs),q->(q[1]*q[2])^4<>One(G))),"\n");
Print("element order 8=",e8," exponent=",Exponent(G)," class=",NilpotencyClassOfGroup(G)," derived size=",Size(DerivedSubgroup(G))," center size=",Size(Centre(G))," structure=",StructureDescription(G),"\n");
iso:=IsomorphismFpGroupByGenerators(G,c);;
F:=Image(iso);;
Print("fp generators=",GeneratorsOfGroup(F),"\nfp relators=",RelatorsOfFpGroup(F),"\n");
Print("order8 word image=",Image(iso,e8),"\n");
QUIT;
GAP
```

Only this disclosed prefix/suffix is available; the enormous relator line was tool-truncated and is not reconstructible:

```text
four generators=[ f1, f2, f3, f4 ] orders=[ 2, 2, 2, 2 ] generated size=128
involution count=35 bad pairs=0
element order 8=f1*f2*f3 exponent=8 class=4 derived size=16 center size=
2 structure=(C4 x C4) : D8
fp generators=[ F1, F2, F3, F4 ]
fp relators=[ F1^-2, F2^-2, ... ]
...
order8 word image=F1*F2*F3
```

# Call 10 — second branch, exact command unavailable

The second branch disclosed only that it had made a bounded GAP 4.12.1 check of a three-generator presentation, reporting order 128 and `IdGroup [128,928]`. It did not supply the exact command or full output. Under the “never report an output you did not observe” rule, nothing further can be reconstructed or asserted. This tenth call is recorded solely as an incident with missing evidence.
