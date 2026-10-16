---
title: Artefacts
module: intelligent-agents
nav_order: 1
permalink: /modules/intelligent-agents/artefacts/
summary: >-
  Code, designs, diagrams and written work produced during the module, each
  mapped to the learning outcomes it evidences.
---

Code, designs and results. Full write-ups are in the [evidence appendix](../evidence/).

## Agent-based system

<p class="meta"><span class="badge badge--completed">completed</span> <span class="muted">Individual project · Evidences LO2, LO3</span></p>

### ScholarPlan — implementation and presentation

- **Code:** [github.com/aabouraya/scholar_plan](https://github.com/aabouraya/scholar_plan/tree/c66190e),
  commit `c66190e`, as presented.
- **Presentation:** [slide deck](https://docs.google.com/presentation/d/1cRRCG0g3pqrjCc7xxqDpI_tBM-J0sCwP/edit?usp=sharing)
  (demo on slide 6).
- **Full write-up:** [ScholarPlan implementation](../evidence/scholarplan-implementation/)

```bash
uv run scholarplan "How does the attention mechanism in Transformers work?"
uv run scholarplan search runs/<timestamp> "why scale the dot product"   # offline, no LLM
```

<figure>
  <a href="{{ '/assets/img/intelligent-agents/scholarplan-implementation.png' | relative_url }}"><img src="{{ '/assets/img/intelligent-agents/scholarplan-implementation.png' | relative_url }}" alt="Implementation architecture: a Controller above a shared SQLite blackboard. The deliberative Planner sits on one side; the reactive Retriever, Processor, Critic and Archivist on the other. Agents connect only to the blackboard."></a>
  <figcaption>The implemented architecture, from the presentation. Agents never call each other; every agent reads and writes only the blackboard.</figcaption>
</figure>

| Agent | Kind | What it does |
| --- | --- | --- |
| Planner | deliberative, GPT-5-mini | Runs a ReAct loop. Each step writes a Thought and one Action (`search`, `abandon` or `finish`), and must address any Critic feedback first. Writes the final synthesis. |
| Retriever | reactive, no LLM | Searches the three APIs for a pending subtask, removes duplicates by DOI, arXiv ID or title, and records where each paper came from. |
| Processor | reactive, GPT-5-mini | Ranks sources with local MiniLM embeddings and summarises the top 3 into at most 4 claims each. |
| Critic | reactive, Llama-3.3-70B | Checks every claim against the source abstract. A summary passes only if all its claims are supported; otherwise it writes feedback for the Planner. |
| Archivist | reactive, no LLM | Exports the report, BibTeX, a vector index and the full trace. |

#### Structure: classes and blackboard tables

<figure>
  <a href="{{ '/assets/img/intelligent-agents/scholarplan-class-diagram.png' | relative_url }}"><img src="{{ '/assets/img/intelligent-agents/scholarplan-class-diagram.png' | relative_url }}" alt="UML class diagram: the Planner, Retriever, Processor, Critic and Archivist classes implement an Agent protocol with can_act and act. The controller creates the Blackboard and asks who can act. Each agent reads and writes the Blackboard class, and uses supporting modules: llm, sources, citations, index, embeddings and http_cache."></a>
  <figcaption>Class diagram. Every agent implements the same two-method <code>Agent</code> protocol, so the controller never needs to know which agent it is running.</figcaption>
</figure>

<figure>
  <a href="{{ '/assets/img/intelligent-agents/scholarplan-erd.png' | relative_url }}"><img src="{{ '/assets/img/intelligent-agents/scholarplan-erd.png' | relative_url }}" alt="Entity-relationship diagram of the eight blackboard tables. A subtask finds many sources and groups many summaries; a source is summarised in many summaries; a summary contains many claims; feedback is about a subtask or a summary. The run, thoughts and synthesis tables stand alone."></a>
  <figcaption>Entity-relationship diagram of the blackboard. The status columns are the triggers: a new row status is what tells the next agent it can act.</figcaption>
</figure>

| Agent | Writes to |
| --- | --- |
| Planner | `thoughts`, `subtasks` (new or abandoned), `synthesis`, `feedback` (when a query is refused) |
| Retriever | `subtasks` (claims a pending one, marks it done), `sources`, `feedback` |
| Processor | `sources` (relevance, status), `summaries` and their `claims`, `subtasks`, `feedback` |
| Critic | `claims` (verdicts), `summaries` (verified or rejected), `synthesis` (verdict), `feedback` |
| Archivist | nothing; it reads the blackboard and writes the output files to disk |
| Controller | `run`, `thoughts` (observations) |

#### What changed from the design

| The design said | What was built | Why |
| --- | --- | --- |
| The Llama Critic can run locally via Ollama (§3) | Azure only | It needs about 40 GB of memory; the laptop has 32 GB |
| The Critic is unit-tested against MiniCheck (§4, §6) | Unit tests use a fake model; MiniCheck is a second opinion | MiniCheck answers only yes or no, and the Planner needs the Critic's written reason to re-plan |
| About 50 hand-labelled claims for the Critic | 13 claims | A smaller set was built; it is listed as a limitation |
| GPT-5-nano as a fallback model | No fallback | Azure for Students has no GPT-5-nano quota |
| Full text where open access, abstracts as fallback (§2.2) | Abstracts only | Abstracts are always available from the APIs; full text often is not |
| Low-temperature sampling (§5) | Strict JSON schemas for GPT-5-mini; temperature 0 for Llama | GPT-5-mini accepts only its default temperature |

#### Results

| Level | Result |
| --- | --- |
| Unit and component (fake LLMs, saved API responses) | 67 passed |
| Integration (live APIs and models) | 3 passed |
| Critic on 13 hand-labelled claims | 13 of 13 correct; no unsupported claim accepted |
| Critic against MiniCheck, a second independent checker | Agreed on all 192 claims checked |
| End to end, 4 fixed research questions | 4 of 4 finished, no API errors, 99% of claims passed, about $0.03 per run |

<figure>
  <a href="{{ '/assets/img/intelligent-agents/scholarplan-eval-run.png' | relative_url }}"><img src="{{ '/assets/img/intelligent-agents/scholarplan-eval-run.png' | relative_url }}" alt="Terminal output of the end-to-end evaluation on 4 questions, 3 October 2026: recall retrieved 20%, recall cited 15%, claim pass rate 99%, 3.0 steps, $0.030 per run."></a>
  <figcaption>The end-to-end evaluation run on 3 October 2026.</figcaption>
</figure>

#### Limitations

| Limitation | Evidence |
| --- | --- |
| Recall of well-known papers is low and unstable | 25%, 55%, 50% and 20% across four saved runs, one run per setting |
| The Critic checks support, not coverage | A fully verified review can still miss the key papers |
| Abstracts only | A claim can be true of a paper but not checkable from its abstract |
| Small labelled set | 13 claims; only one real claim was rejected |

#### Legal, social, ethical and professional considerations

| Issue | How ScholarPlan handles it |
| --- | --- |
| Citing every claim | Only claims the Critic supports reach the report, each with its source; the trace records which database each paper came from, and when |
| Fair use of APIs | Rate limits respected, with throttling, `Retry-After` retries and caching; arXiv's open-access interoperability acknowledged |
| Secrets | API keys in a git-ignored `.env` with restricted permissions, never written to the cache |
| Cost | A 20-step budget and per-call cost tracking keep runs within a one-off student credit |
| Use of AI tools | Claude Code helped write, test and document the code, and the repository says so; the design decisions were mine |

## Design and modelling

<p class="meta"><span class="badge badge--completed">completed</span> <span class="muted">Team project · Evidences LO1, LO2, LO3</span></p>

### ScholarPlan — team design proposal

- **Full proposal, verbatim:** [ScholarPlan team design proposal](../evidence/team-proposal/) (Group A, September 2026)
- **Who did what:** [Team](../team/#team-output) · **Tutor feedback:** [evidence appendix](../evidence/tutor-feedback/)

| The brief asks the agents to… | ScholarPlan agent | Where in the proposal |
| --- | --- | --- |
| Plan the work | Planner (deliberative, ReAct loop) | §3, §5 |
| Find documents or online content | Retriever (arXiv, OpenAlex, Crossref) | §2.1, §6 |
| Process or reason over the data | Processor and Critic (claim-level verification) | §3, §5 |
| Do something meaningful with the result | Archivist (report, BibTeX, vector index, trace) | §2.1, §7 |

<figure>
  <a href="{{ '/assets/img/intelligent-agents/scholarplan-architecture.png' | relative_url }}"><img src="{{ '/assets/img/intelligent-agents/scholarplan-architecture.png' | relative_url }}" alt="Architecture diagram: the Planner, Retriever, Processor, Critic and Archivist each connect only to a central shared blackboard."></a>
  <figcaption><strong>Figure 1.</strong> Architectural view: five role-specialised agents coordinating through the shared blackboard.</figcaption>
</figure>

<figure>
  <a href="{{ '/assets/img/intelligent-agents/scholarplan-activity.png' | relative_url }}"><img src="{{ '/assets/img/intelligent-agents/scholarplan-activity.png' | relative_url }}" alt="UML activity diagram in swimlanes for User, Planner, Retriever, Processor, Critic and Archivist, with a dashed re-planning loop from Critic rejection back to the Planner."></a>
  <figcaption><strong>Figure 2.</strong> Activity view: end-to-end flow by agent, with the Critic-rejection re-planning loop dashed.</figcaption>
</figure>

<figure>
  <a href="{{ '/assets/img/intelligent-agents/scholarplan-sequence.png' | relative_url }}"><img src="{{ '/assets/img/intelligent-agents/scholarplan-sequence.png' | relative_url }}" alt="UML sequence diagram of the agents reading and writing the blackboard, with a loop over subtasks and the Archivist writing to disk at the end."></a>
  <figcaption><strong>Figure 3.</strong> Sequence view: agents interacting through the blackboard; only the Archivist writes to disk.</figcaption>
</figure>

## Formative activities

### Week 6 — Creating agent dialogues in KQML and KIF

<p class="meta"><span class="badge badge--completed">completed</span> <span class="muted">Evidences LO1, LO2</span></p>

**The brief.** Alice (procurement) asks Bob (stock control) how many 50 inch
televisions are in stock, and how many HDMI ports they have.

#### The shared ontology

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
| Bob's remit | Answers both questions | Strictly, HDMI ports are a product specification, not a stock level. A stricter Bob would reply `sorry` or forward the question to a catalogue agent: an agent can only answer within its ontology and competence. |

### Constituency-based parse trees

<p class="meta"><span class="badge badge--completed">completed</span> <span class="muted">Evidences LO2</span></p>

**The brief.** Draw a constituency-based parse tree for three phrases.

| Tag | Meaning | Tag | Meaning |
| --- | --- | --- | --- |
| `S` | sentence | `NN` | noun |
| `NP` | noun phrase | `NNS` | plural noun |
| `VP` | verb phrase | `VBD` | past-tense verb |
| `PP` | prepositional phrase | `VBZ` | third-person verb |
| `DT` | determiner | `IN` | preposition |

#### 1. The government raised interest rates.

```
S
├── NP
│   ├── DT   The
│   └── NN   government
└── VP
    ├── VBD  raised
    └── NP
        ├── NN   interest
        └── NNS  rates
```


#### 2. The internet gives everyone a voice.

```
S
├── NP
│   ├── DT   The
│   └── NN   internet
└── VP
    ├── VBZ  gives
    ├── NP
    │   └── NN   everyone
    └── NP
        ├── DT   a
        └── NN   voice
```


#### 3. The man saw the dog with the telescope.

**Reading A — the man used the telescope** (PP attached to the VP).

```
S
├── NP
│   ├── DT   The
│   └── NN   man
└── VP
    ├── VBD  saw
    ├── NP
    │   ├── DT   the
    │   └── NN   dog
    └── PP
        ├── IN   with
        └── NP
            ├── DT   the
            └── NN   telescope
```

**Reading B — the dog had the telescope** (PP attached to the object NP).

```
S
├── NP
│   ├── DT   The
│   └── NN   man
└── VP
    ├── VBD  saw
    └── NP
        ├── NP
        │   ├── DT   the
        │   └── NN   dog
        └── PP
            ├── IN   with
            └── NP
                ├── DT   the
                └── NN   telescope
```

| Sentence | Structure | Why it matters |
| --- | --- | --- |
| 1 | *interest rates* is one NP, a noun compound | Read as two separate objects, the sentence says something the writer did not mean |
| 2 | *gives* is ditransitive: the VP takes two NPs, the recipient and the thing given | The verb decides how many arguments the phrase needs |
| 3 | The PP attaches to the VP (A) or inside the object NP (B) | Syntax alone cannot settle it; it needs world knowledge. It is the same failure as an agent that parses an instruction correctly and grounds it to the wrong referent |
