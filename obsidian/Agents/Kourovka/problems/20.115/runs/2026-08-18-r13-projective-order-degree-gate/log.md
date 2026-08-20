---
author: operator
tags:
  - agent/problem
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/character-theory
  - project/kourovka
  - status/draft
problem: "20.115"
scope_id: 20.115/nonzero-character-order-divisibility
assignment_revision: 1
direction: proof
cycle: 13
strategy: PROJECTIVE-ORDER-DEGREE-GATE
---

# Cycle 13 log: projective order-degree gate

## 2026-08-18T05:30:10Z — work start

Detailed cumulative active time at entry: `02:26:38`. This increment is capped at
45 new active minutes. The context is fresh: the preceding unreviewed Fitting
argument and table screens are not premises and were not inspected.

## 2026-08-18T05:37:36Z — source and staleness gate

- Read the source PDF through `_meta/agents/Kourovka/paths.env`, extracted printed
  page 161, and visually inspected a 160 dpi rendering of that page.
- Correct transcription: Let `chi` be a complex irreducible character of a finite
  group `G`. If `chi(x) != 0` for some `x in G`, must the exact order `o(x)` divide
  `|G|/chi(1)`? Equivalently, must `o(x)chi(1)` divide `|G|`?
- Context outside the active clause: the source says this holds for solvable `G`
  and that `(o(x)chi(1))^4` divides `|G|^5` for arbitrary `G`.
- `source_transcription_checked: yes`; `active_scope_checked: yes`.
- The corpus row has `answered:false`, `has_editor_comment:false`, and
  `has_later_comment:false`. Its metadata says page 162, whereas the rendered PDF
  itself labels the page 161 and the canonical scope uses 161; the mathematical
  transcription agrees with the canonical scope.
- `external_staleness_check: deferred_to_lead_or_human_for_discovery_blind_run`.
  No open-web search was performed.

### Clause and six-row admissibility matrix

| row | source condition | active use |
|---|---|---|
| `20.115-forall-G-chi-x` | every admissible triple `(G,chi,x)` | the desired assertion is universal |
| `20.115-G-finite` | `G` is finite | must be retained throughout |
| `20.115-chi-complex-irreducible` | ordinary complex irreducible `chi` | projective characters are only an auxiliary vehicle |
| `20.115-x-in-G` | `x in G`, with exact element order | no order bound or projective order may replace `o(x)` |
| `20.115-character-value-nonzero` | exact `chi(x) != 0` | numerical approximations are inadmissible |
| `20.115-order-degree-divisibility` | `o(x)chi(1) | |G|` | exact target conclusion |

The solvable-case and fourth-power clauses are contextual and outside the active
scope. The projective lemma includes the trivial factor set, so a universal proof
of it would already prove the exact source assertion.

## Strategy portfolio

1. **Theoretical / dictionary audit (first):** realize a finite-order cocycle by a
   finite central extension, prove the correspondence of irreducibility and
   nonvanishing, and compute the exact order of a lift. Test whether the proposed
   lemma is genuinely stronger than, equivalent to, or merely conditional on the
   source assertion.
2. **Structured counterexample:** if the lift formula exposes slack, seek one
   designed central extension (not a catalogue) whose faithful central-character
   row has a nonzero value and violates the quotient order-degree divisibility.
3. **Small-case probe:** only if theory leaves a concrete candidate, inspect that
   single motivated central extension. A negative finite check would establish no
   universal claim.
4. **Certificate plan:** a projective refutation must specify normalized factor
   set, matrices or an ordinary central-extension character, exact quotient
   element order, exact nonzero trace, and failed divisibility. Then separately
   test whether an ordinary lift violates all six source rows.

Kill criterion: stop the proposed bridge if the exact lift-order/kernel ratio
cannot cancel, or if the lemma reduces tautologically to the unresolved source
statement without a stronger hypothesis. A promising explicit certificate is not
silently abandoned at the cap.

## 2026-08-18T05:46:28Z — exact central-extension audit

Let `f:H x H -> mu_m` be a normalized finite-valued factor set and let
`rho(g)rho(k)=f(g,k)rho(gk)`. Define

`E_f = mu_m x H`, with `(z,g)(w,k)=(zw f(g,k),gk)`.

Then `rho_tilde(z,g)=z rho(g)` is an ordinary irreducible representation exactly
when `rho` is projectively irreducible, and
`chi_tilde(z,g)=z alpha(g)`. Thus nonvanishing is independent of the chosen lift.
Conversely, a central extension with an irreducible character over a central
linear character gives this construction after a section is chosen. Quotienting
the central kernel by the kernel of its scalar character leaves the **effective
scalar kernel**, which is cyclic because it embeds in the finite subgroups of
`C^*`.

For a central extension `1 -> Z -> E -> H -> 1` with effective cyclic scalar
kernel `|Z|=m`, take `h in H`, `n=o(h)`, and a lift `y`. Put `c=y^n in Z`. For
every `z in Z`, the exact formulas are

`o(zy) = n o(z^n c)` and `chi_tilde(zy)=lambda(z)chi_tilde(y)`.

The order formula is exact: any exponent killing `zy` must first be a multiple
of the exact quotient order `n`, and `(zy)^(nt)=(z^n c)^t`.

If the ordinary source divisibility is available for `E`, it yields only

`n alpha(1) | (m/r)|H|`, where `r=o(z^n c)`.

Full cancellation is possible exactly when some lift has order `nm`, equivalently
some `z^n c` generates `Z`. Prime by prime this happens iff, for every
`p | gcd(n,m)`, the projection of `c` to the Sylow `p`-subgroup of `Z` is a
generator. For `p` not dividing `n`, the `n`th-power map is an automorphism; for
`p | n`, multiplying by an `n`th power cannot change whether the exponent is a
unit modulo `p`. This criterion is invariant under changing the lift.

Two immediate consequences:

1. The universal projective assertion contains the active ordinary assertion as
   the special case `f=1`; proving it universally is not an independent bridge.
2. Applying the ordinary assertion to an arbitrary central extension is
   insufficient unless the effective scalar-kernel factor is cancelled. Exact
   nonvanishing does **not** itself force the full-order-lift criterion.

### Reconstructible non-counterexample showing the lift obstruction

Take
`E=D_8 x C_2=<r,s,c | r^4=s^2=c^2=1, srs=r^-1, [c,r]=[c,s]=1>` and
`Z=<r^2>`. Let the degree-two irreducible representation send `r` to a quarter
rotation, `s` to a reflection, and the external `c` to `I`. Then `r^2` acts as
`-I`, so the effective scalar kernel is `Z`; `H=E/Z` is `C_2^3`. For
`h=cZ`, every lift has order two, while the associated projective trace is `2`.
Thus `alpha(h)!=0` does not force a lift of order `o(h)|Z|=4`. The projective
divisibility itself still holds (`2*2 | 8`), so this is explicitly **not** a
counterexample to either the projective lemma or the source problem.

### Conditional least-counterexample gate

Suppose `G` is least by order among ordinary source counterexamples, `1!=N normal
G`, `H=G/N`, `h=xN`, and a Clifford reduction has independently established

- `chi(1)=a alpha(1)` and `alpha(h)!=0`;
- `t=o(x)/o(h)` and `t a | |N|`;
- `alpha` has an effective cyclic scalar extension `E` of `H` with kernel `Z`,
  `|Z|<|N|`, and the full-order-lift criterion at `h`.

Then `|E|=|Z||H|<|G|`; minimality applies to the ordinary irreducible lift in
`E`, full lift order cancels `|Z|`, and gives `o(h)alpha(1)| |H|`. Multiplying
by `t a | |N|` gives the exact source conclusion
`o(x)chi(1)| |G|`, a contradiction. These hypotheses are therefore sufficient
for the projective step of a least-counterexample reduction. They have not been
derived in this clean context; in particular, neither the scalar-kernel size nor
the full-order-lift condition may be silently assumed.

## Bounded sanity probes (not premises and not universal evidence)

GAP 4.12.1 was available. Four theoretically motivated Schur-cover tables were
inspected only as sanity checks, with no table catalogue enumeration: `2.S4`,
`2.S5`, `2.A7`, and `6.A7`. The displayed faithful rows of the first three gave
no visible projective quotient violation. A direct exact scan of all 40 rows and
40 lift classes of `6.A7`, using its stored fusion to `A7`, printed `hits=0`.
This fixed bounded output proves nothing about the universal assertion and is not
used in the structural partial result. No further table was opened.

Representative executed GAP command for the last probe:

```gap
t:=CharacterTable("6.A7");; q:=CharacterTable("A7");;
f:=GetFusionMap(t,q);; oq:=OrdersClassRepresentatives(q);;
for i in [1..Length(Irr(t))] do
  for j in [1..Length(f)] do
    if Irr(t)[i][j]<>0*Irr(t)[i][j]
       and Size(q) mod (Irr(t)[i][1]*oq[f[j]])<>0 then
      Add(hits,[i,j]);
    fi;
  od;
od;
Print("hits=",Length(hits),"\n");
```

Observed output: `hits=0`.

## 2026-08-18T05:50:33Z — early strategy stop and handoff

- Self-check: exact active scope and all six rows remain unchanged. No ordinary
  source candidate has been produced. The universal projective assertion is not
  independently accessible because it includes the source assertion at the
  trivial factor set. The exact central-extension transfer lemma is checkable;
  its scalar-kernel, lift-order, and kernel-side conditions identify the remaining
  bottleneck.
- Outcome: `PARTIAL_RESULT`; `active_assignment_answered:no`.
- Named strategy status: `PROJECTIVE-ORDER-DEGREE-GATE` is exhausted as a
  standalone universal bridge. A refinement is live only if the intended
  least-counterexample structure proves all three explicit hypotheses in
  `findings.md`; that scheduling choice was sent to Lead and MathExpert.
- Sent the exact mathematical partial to Validator for independent reconstruction.
- Active interval charged: `00:20:23` (`05:30:10Z`--`05:50:33Z`).
- Detailed cumulative active time: `02:47:01`.
- State after handoff: `awaiting_lead`.
