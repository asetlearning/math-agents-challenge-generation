---
title: "Scope audit — Kourovka 20.115"
problem: "20.115"
audit_type: source-fidelity
scope_id: 20.115/nonzero-character-order-divisibility
scope_record: Agents/Kourovka/scopes/20.115-nonzero-character-order-divisibility.json
assignment_revision: 1
source_pdf_page: 161
source_transcription_checked: yes
result: PASS
active_assignment_answered: no
audited_record_modified: no
author: operator
tags:
  - agent/validator
  - user/operator
  - domain/group-theory
  - topic/kourovka
  - topic/character-tables
  - project/kourovka
  - status/draft
---

# Scope audit — Kourovka 20.115

## Result

**PASS.** Revision 1 faithfully and completely records the universal question,
both source-supplied contextual results, the admissibility conditions, the target
conclusion, and the logical requirements for a proof or counterexample. No
correction to the canonical scope is required.

This is a source-fidelity audit only. It does not assess the truth or current
literature status of the assertion, search for examples, or answer the active
assignment. Accordingly, `active_assignment_answered: no` is mandatory. The
canonical scope, board, and roster were not edited.

## Independently read rendered statement

I rendered and visually inspected the configured local Kourovka PDF page 161. With
line breaks normalized but mathematical typography retained, Problem 20.115 says:

> Let \(\chi\) be a complex irreducible character of a finite group \(G\). If
> \(\chi(x)\ne 0\) for some \(x\in G\), must the order \(o(x)\) of \(x\) divide
> \(|G|/\chi(1)\)?
>
> This is known to be true if \(G\) is solvable, and it is known that
> \((o(x)\chi(1))^4\) divides \(|G|^5\) for arbitrary \(G\).

The proposer is T. Wilde. The statement is unstarred and contains no other part,
exception, parameter range, editor answer, or later clause on the rendered page.

## Quantifier and object audit

| source datum | canonical treatment | audit |
|---|---|---|
| “Let \(\chi\) be … of a finite group \(G\)” | Every finite \(G\) and every complex irreducible character \(\chi\) of \(G\) | PASS |
| “for some \(x\in G\)” in the conditional question | Every choice of \(x\in G\) satisfying \(\chi(x)\ne0\) | PASS |
| “complex irreducible character” | An ordinary irreducible complex character, not a Brauer/modular or reducible character | PASS |
| “the order \(o(x)\) of \(x\)” | The exact element order of the chosen member \(x\in G\) | PASS |
| \(\chi(x)\ne0\) | The exact complex character value is nonzero | PASS |
| “must … divide” | The implication \(\chi(x)\ne0\Rightarrow o(x)\mid |G|/\chi(1)\) | PASS |

The source's word “some” introduces the element to which both the hypothesis and
the requested conclusion refer. Because \(G\), \(\chi\), and that choice of \(x\)
are arbitrary, the formal assertion is the universal implication over admissible
triples used in the JSON. It is not the much weaker claim that each character only
has to possess one favourable nonzero class.

“Complex irreducible character” has its standard ordinary-character meaning here.
The source introduces no prime or modular setting, and it imposes no faithfulness,
nonlinearity, nonidentity condition on \(x\), or nonsolvability hypothesis on
\(G\). The canonical constraints add none of those conditions.

## Divisibility normalization

Put \(m=o(x)\), \(d=\chi(1)\), and \(n=|G|\). For an ordinary irreducible complex
character of a finite group, \(d\) is a positive integer and \(d\mid n\). Hence

\[
m\mid n/d \quad\Longleftrightarrow\quad md\mid n.
\]

Thus the canonical form \(o(x)\chi(1)\mid |G|\) is exactly equivalent to the
source's \(o(x)\mid |G|/\chi(1)\). It does not strengthen the target and it avoids
any ambiguity about divisibility of a displayed quotient.

## Source clauses and contextual bounds

| clause id | rendered source content | canonical handling | audit |
|---|---|---|---|
| `c-question` | The universal nonzero-value implication | Active target | PASS |
| `c-solvable-context` | The same assertion is known when \(G\) is solvable | Context only; a proof restricted to solvable groups does not answer the active universal question | PASS |
| `c-general-bound-context` | Under the same standing \((G,\chi,x)\) and nonzero-value setup, \((o(x)\chi(1))^4\mid |G|^5\) is known for arbitrary \(G\) | Weaker context only | PASS |

The last formula has exponent four on the entire product
\(o(x)\chi(1)\), and exponent five on \(|G|\). The JSON records both exponents
correctly. “For arbitrary \(G\)” removes the solvability restriction; it does not
discard the preceding ordinary-character, membership, or nonzero-value setup.
Neither contextual result is a second active target, and neither by itself settles
the universal first-power divisibility question.

## Constraint-and-conclusion audit

| constraint id | required content | audit |
|---|---|---|
| `20.115-forall-G-chi-x` | Universal implication over all admissible triples \((G,\chi,x)\) | PASS |
| `20.115-G-finite` | \(G\) is finite | PASS |
| `20.115-chi-complex-irreducible` | \(\chi\) is an ordinary irreducible complex character of \(G\) | PASS |
| `20.115-x-in-G` | \(x\in G\), with \(o(x)\) its exact element order | PASS |
| `20.115-character-value-nonzero` | The exact value \(\chi(x)\) is nonzero | PASS |
| `20.115-order-degree-divisibility` | \(o(x)\mid |G|/\chi(1)\), equivalently \(o(x)\chi(1)\mid |G|\) | PASS |

All five admissibility conditions and the sole target-conclusion row are present,
required, assigned the correct roles, and linked to the active question clause.

## Exclusion audit

| revision-1 exclusion | source-fidelity assessment |
|---|---|
| Brauer or modular characters | PASS: the source asks about ordinary complex irreducible characters. |
| Rows with \(\chi(x)=0\) | PASS: exact nonvanishing is the antecedent of the source implication. |
| Reducible characters | PASS: irreducibility is explicit. |
| The already-known solvable restriction | PASS: resolving only that restriction repeats contextual knowledge and does not answer the arbitrary finite-group target. Solvable groups remain included in the universal statement itself. |
| The weaker fourth-power/fifth-power divisibility | PASS: it is source-supplied context, not the requested first-power conclusion. |
| A bounded character-table screen presented as a universal proof | PASS as a logical adequacy boundary forced by the universal quantifier; it is methodological rather than an additional printed source exclusion. |

No exclusion removes an admissible counterexample or weakens the universal proof
obligation.

## Success criteria and certificate

The proof criterion requires the implication for every finite group, every
ordinary irreducible complex character, and every element with nonzero value. It
therefore matches the universal target.

The counterexample criterion requires one reconstructible admissible triple and
failure of \(o(x)\chi(1)\mid |G|\). By the equivalence above, that is exactly one
counterexample to the source question. Read together with the certificate field,
the finite branch supplies:

- a reconstructible finite group or an exact identifier for its ordinary
  character table;
- an exact class/representative and exact element order;
- an ordinary irreducible row, its degree, and an exact cyclotomic value proving
  \(\chi(x)\ne0\), rather than a floating-point approximation;
- exact integer data showing \(o(x)\chi(1)\nmid |G|\).

Those data cover every admissibility and failed-conclusion row. The word “or” in
the certificate cleanly separates that finite counterexample package from the
alternative line-by-line universal proof. The two listed partial-progress outcomes
are correctly labelled as partial: neither a bounded family screen nor a reduction
to named remaining families is itself a universal proof or a counterexample.

## Non-substantive linked-note typography

The scope's linked Research transcription flattens the displayed bound as
`(o(x)chi(1))4 divides 5 |G|`. The rendered source and the canonical JSON instead
carry the unambiguous and correct formula
\((o(x)\chi(1))^4\mid |G|^5\). This typography loss in the noncanonical Research
note does not alter the canonical scope and does not require a scope revision.

## Evidence boundary

The configured PDF was rendered at 240 dpi and page 161 was inspected visually.
Plain-text extraction was used only for navigation and compared against the image,
especially \(\chi(x)\ne0\), \(x\in G\), \(o(x)\), \(\chi(1)\), the quotient, and
the superscripts four and five. No web search, literature audit, computation, or
problem-solving step was performed.
