---
title: Artefacts
module: intelligent-agents
nav_order: 3
permalink: /modules/intelligent-agents/artefacts/
summary: >-
  Code, designs, diagrams and written work produced during the module, each
  mapped to the learning outcomes it evidences.
---

Source code for this module lives under
[`artefacts/intelligent-agents/`](https://github.com/aabouraya/msc-ai-portfolio/tree/master/artefacts/intelligent-agents)
in this repository. Each artefact below states what it is, what it demonstrates,
and how to run it where that applies.

## Agent-based system

<p class="meta"><span class="badge badge--not-started">not started</span> <span class="muted">Evidences LO2, LO3</span></p>

<div class="todo" markdown="1">
For the implementation, cover: the problem it addresses, the agent architecture
chosen and *why that one* over the alternatives, how to run it, what the results
were, and its limitations. The critical evaluation is what LO2 asks for — a
working program on its own does not evidence it.

Note the legal, social, ethical and professional considerations here too; LO3
explicitly requires them.
</div>

## Design and modelling

<p class="meta"><span class="badge badge--not-started">not started</span> <span class="muted">Evidences LO1, LO3</span></p>

<div class="todo" markdown="1">
Architecture diagrams, agent interaction models, state or sequence diagrams.
Commit images to `assets/img/intelligent-agents/` and embed them with:

`![Description]({{ '/assets/img/intelligent-agents/diagram.png' | relative_url }})`
</div>

## Formative activities

Weekly formative exercises. They were not assessed, but they show the working
rather than only the conclusion.

### Week 6 — Creating agent dialogues in KQML and KIF

<p class="meta"><span class="badge badge--completed">completed</span> <span class="muted">Evidences LO1, LO2</span></p>

**The brief.** Write a dialogue in KQML and KIF between two agents. Alice procures
stock; Bob controls stock levels for a warehouse. Alice must ask Bob how many
50 inch televisions are available, and how many HDMI slots those televisions
have.

#### The shared ontology

Both agents have to read the same symbols the same way, so the vocabulary is
declared before any message is sent.

```
;; Ontology: warehouse-stock
;;
;; Relations
;;   (stock-level ?product ?units)   ; units of ?product currently held
;;   (hdmi-ports  ?product ?count)   ; HDMI ports fitted to ?product
;;
;; Individual
;;   tv-50-inch                      ; 50 inch television
```

#### The dialogue

**1 — Alice asks how many 50 inch televisions are in stock.**

```
(ask-one
  :sender     alice
  :receiver   bob
  :language   KIF
  :ontology   warehouse-stock
  :reply-with stock-q1
  :content    (stock-level tv-50-inch ?units))
```

**2 — Bob answers.**

```
(tell
  :sender      bob
  :receiver    alice
  :language    KIF
  :ontology    warehouse-stock
  :in-reply-to stock-q1
  :content     (stock-level tv-50-inch 25))
```

**3 — Alice asks how many HDMI ports they have.**

```
(ask-one
  :sender     alice
  :receiver   bob
  :language   KIF
  :ontology   warehouse-stock
  :reply-with spec-q1
  :content    (hdmi-ports tv-50-inch ?count))
```

**4 — Bob answers.**

```
(tell
  :sender      bob
  :receiver    alice
  :language    KIF
  :ontology    warehouse-stock
  :in-reply-to spec-q1
  :content     (hdmi-ports tv-50-inch 4))
```

#### Why these choices

| Element | Choice | Reason |
| --- | --- | --- |
| Alice's messages | `ask-one` | Each question has a single scalar answer. `ask-all` or `stream-all` would ask for every solution, which is wrong for one quantity. |
| Bob's messages | `tell` | Bob asserts a fact he holds into Alice's knowledge base. He is answering, not requesting or committing to an action. |
| `:language` | `KIF` | Declares that `:content` is KIF, so the receiver knows how to parse it. KQML is the envelope; KIF is what is inside it. |
| `:ontology` | `warehouse-stock` | Without a named ontology, `stock-level` is just a symbol. This is what makes the exchange meaningful rather than merely well-formed. |
| `:reply-with` / `:in-reply-to` | `stock-q1`, `spec-q1` | Pairs each answer with its question, so two open queries cannot be confused. |
| Variables | `?units`, `?count` | The unbound variable *is* the question — Bob replies by binding it. |

#### One observation

The brief gives Bob a narrow remit: he controls stock **levels**. Asking him how
many HDMI ports a television has steps outside that remit, since it is a product
specification rather than an inventory fact. A stricter design would have Bob
answer the second question with `sorry`, or forward it to a catalogue agent. The
dialogue above assumes Bob's knowledge base covers both, which is the simpler
reading of the exercise — but the ambiguity is itself the point: an agent can
only answer within the ontology and competence it has been given.

#### What this demonstrates

- **LO1** — why agent-based computing suits this problem: two autonomous parties
  with separate knowledge, cooperating through messages rather than shared memory
  or direct function calls.
- **LO2** — KQML and KIF as the speech-act model of agent communication:
  performatives carry intent, content carries the claim, and the ontology makes
  the two mutually intelligible.

<div class="todo" markdown="1">
Add the remaining weekly formative activities as `### Week N — …` sections above,
each with its badge and the outcomes it evidences. If they grow past a handful,
move them to a page of their own.
</div>
