---
title: Artefacts
module: intelligent-agents
nav_order: 3
permalink: /modules/intelligent-agents/artefacts/
summary: >-
  Code, designs, diagrams and written work produced during the module, each
  mapped to the learning outcomes it evidences.
---

Source files for this module live under
[`artefacts/intelligent-agents/`](https://github.com/aabouraya/msc-ai-portfolio/tree/master/artefacts/intelligent-agents)
in this repository. The ScholarPlan code has its own repository, linked below. Each artefact below states what it is, what it demonstrates,
and how to run it where that applies.

## Agent-based system

<p class="meta"><span class="badge badge--completed">completed</span> <span class="muted">Evidences LO2, LO3</span></p>

### ScholarPlan — implementation and presentation

**The brief.** Build the agent designed in the team project and present it. The
team proposal is in [Design and modelling](#scholarplan--team-design-proposal)
below. This part is my individual work.

**The evidence.**

- **Code:** [github.com/aabouraya/scholar_plan](https://github.com/aabouraya/scholar_plan/tree/c66190e),
  pinned to commit `c66190e`, the version presented. The repository includes the
  tests, evaluation runs, a development log and a remediation log.
- **Presentation:** [slide deck](https://github.com/aabouraya/msc-ai-portfolio/raw/master/artefacts/intelligent-agents/agent-system/ScholarPlan_IntelligentAgents_slides.pptx)
  (11 slides, 24 MB download). The submitted version was narrated; this copy has
  the narration removed to keep it small. Slide 6 holds the demo, a screen
  recording of a real run.

#### What it does

Given one research question, ScholarPlan plans its own searches, gathers papers
from OpenAlex, arXiv and Crossref, and summarises them into short claims. A
separate model checks every claim against its source, and the system writes a
cited literature review. A typical run takes 3 to 4 steps, about 2 minutes and
about $0.03.

```bash
uv run scholarplan "How does the attention mechanism in Transformers work?"
uv run scholarplan search runs/<timestamp> "why scale the dot product"   # offline, no LLM
```

Setup (Python 3.11, uv, and an Azure deployment of both models) is in the
[repository README](https://github.com/aabouraya/scholar_plan/blob/c66190e/README.md).

#### How it works

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

A controller runs one Planner step, then lets the reactive agents act until none
can, and repeats. It stops when the Planner finishes, when coverage is met (3
subtasks with at least 2 verified summaries each), or after 20 steps. The Critic
is a different model family from the Processor, so the two are less likely to
share blind spots.

#### Structure: classes and blackboard tables

The proposal showed behaviour (activity and sequence diagrams) but not
structure, which was the tutor's first improvement point. These two diagrams
were added to the repository afterwards, in commit
[`460fb65`](https://github.com/aabouraya/scholar_plan/tree/460fb65/diagrams)
(14 October 2026), and checked against the code.

<figure>
  <a href="{{ '/assets/img/intelligent-agents/scholarplan-class-diagram.png' | relative_url }}"><img src="{{ '/assets/img/intelligent-agents/scholarplan-class-diagram.png' | relative_url }}" alt="UML class diagram: the Planner, Retriever, Processor, Critic and Archivist classes implement an Agent protocol with can_act and act. The controller creates the Blackboard and asks who can act. Each agent reads and writes the Blackboard class, and uses supporting modules: llm, sources, citations, index, embeddings and http_cache."></a>
  <figcaption>Class diagram. Every agent implements the same two-method <code>Agent</code> protocol, so the controller never needs to know which agent it is running.</figcaption>
</figure>

<figure>
  <a href="{{ '/assets/img/intelligent-agents/scholarplan-erd.png' | relative_url }}"><img src="{{ '/assets/img/intelligent-agents/scholarplan-erd.png' | relative_url }}" alt="Entity-relationship diagram of the eight blackboard tables. A subtask finds many sources and groups many summaries; a source is summarised in many summaries; a summary contains many claims; feedback is about a subtask or a summary. The run, thoughts and synthesis tables stand alone."></a>
  <figcaption>Entity-relationship diagram of the blackboard. The status columns are the triggers: a new row status is what tells the next agent it can act.</figcaption>
</figure>

Neither diagram shows which agent writes which table. That is the permission
model the proposal took from the Gaia methodology (§4), so it is traced here
from the code:

| Agent | Writes to |
| --- | --- |
| Planner | `thoughts`, `subtasks` (new or abandoned), `synthesis`, `feedback` (when a query is refused) |
| Retriever | `subtasks` (claims a pending one, marks it done), `sources`, `feedback` |
| Processor | `sources` (relevance, status), `summaries` and their `claims`, `subtasks`, `feedback` |
| Critic | `claims` (verdicts), `summaries` (verified or rejected), `synthesis` (verdict), `feedback` |
| Archivist | nothing; it reads the blackboard and writes the output files to disk |
| Controller | `run`, `thoughts` (observations) |

Every agent can write `feedback`. That is the only way a reactive agent can
change what the Planner does next.

#### What changed from the design

Building it showed where the team design did not hold. Each change is recorded
in the [development log](https://github.com/aabouraya/scholar_plan/blob/c66190e/docs/development_log.md).

| The design said | What was built | Why |
| --- | --- | --- |
| The Llama Critic can run locally via Ollama (§3) | Azure only | It needs about 40 GB of memory; the laptop has 32 GB |
| The Critic is unit-tested against MiniCheck (§4, §6) | Unit tests use a fake model; MiniCheck is a second opinion | MiniCheck answers only yes or no, and the Planner needs the Critic's written reason to re-plan |
| About 50 hand-labelled claims for the Critic | 13 claims | A smaller set was built; it is listed as a limitation |
| GPT-5-nano as a fallback model | No fallback | Azure for Students has no GPT-5-nano quota |
| Full text where open access, abstracts as fallback (§2.2) | Abstracts only | Abstracts are always available from the APIs; full text often is not |
| Low-temperature sampling (§5) | Strict JSON schemas for GPT-5-mini; temperature 0 for Llama | GPT-5-mini accepts only its default temperature |

#### Results

It was built in four iterations, each ending with a test that had to pass before
the next began. Eleven problems found on the way are in the
[remediation log](https://github.com/aabouraya/scholar_plan/blob/c66190e/docs/remediation_log.md).
The final [test report](https://github.com/aabouraya/scholar_plan/blob/c66190e/docs/testing/test_report.md)
(3 October 2026) shows:

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

In one run the Critic rejected a summary and the first synthesis draft. The
Planner redrafted, and the second draft passed. That is the re-planning loop
working on real data rather than only under fault injection.

#### Limitations

- **Recall of well-known papers is low and unstable.** Across four saved runs it
  was 25%, 55%, 50% and 20%. The Planner picks different queries each run, and
  recent papers now outrank older landmark ones. With one run per setting, the
  evaluation cannot show whether the tuning between runs helped.
- **The Critic checks support, not coverage.** A review can be fully verified
  and still miss the key papers.
- **Abstracts only.** A claim can be true of the paper but not checkable from
  its abstract.
- **Small labelled set.** 13 claims, and only one real claim was rejected, so the
  test of rejections is thin.

#### Legal, social, ethical and professional considerations

- **Citing every claim.** Only claims the Critic supports reach the report, each
  with its source. The trace records which database each paper came from and
  when, so a reader can check any claim.
- **Using the APIs fairly.** Requests follow each API's rate limits, with
  throttling and retries that respect `Retry-After`, and are cached so the same
  call is not repeated. arXiv's open access interoperability is acknowledged in
  the README.
- **Secrets.** API keys live in a git-ignored `.env` with restricted
  permissions, and are never written to the cache.
- **Cost.** The 20-step budget and per-call cost tracking keep runs within the
  one-off student credit.
- **Use of AI tools.** Claude Code was used to help write, test and document the
  code, and the repository says so. The design decisions were mine.

#### What this demonstrates

- **LO2.** It applies agent techniques (ReAct planning, Reflexion-style
  re-planning, blackboard coordination) to a real problem with real uncertainty.
  It is evaluated honestly, including the results that did not improve.
- **LO3.** It uses software tools chosen by evidence, tested at four levels, and
  built with attention to provenance, fair API use, secrets and cost.

## Design and modelling

<p class="meta"><span class="badge badge--completed">completed</span> <span class="muted">Evidences LO1, LO2, LO3</span></p>

### ScholarPlan — team design proposal

**The brief.** The Development Team Project asked each team to act as software
consultants and design an LLM-powered planning agent for academic research and
information gathering. The agents had to find documents or online content,
process or reason over them, and do something useful with the result. One report
was submitted per team, due 7 September 2026, with a 1,000-word limit. It is worth
20% of the module mark.

Our team (Group A: Yasmin, Adel A. and me) proposed **ScholarPlan**. It is a
hybrid multi-agent system in which an LLM Planner breaks a research goal into
subtasks. Four specialised agents then retrieve, summarise, verify and archive
the evidence, coordinating only through a shared blackboard. The table shows how
each requirement in the brief is met.

| The brief asks the agents to… | ScholarPlan agent | Where in the proposal |
| --- | --- | --- |
| Plan the work | Planner (deliberative, ReAct loop) | §3, §5 |
| Find documents or online content | Retriever (arXiv, OpenAlex, Crossref) | §2.1, §6 |
| Process or reason over the data | Processor and Critic (claim-level verification) | §3, §5 |
| Do something meaningful with the result | Archivist (report, BibTeX, vector index, trace) | §2.1, §7 |

The proposal is reproduced verbatim below, including the figures as submitted.
Only the heading levels and line wrapping are changed so that it fits this page.
How the work was divided is recorded on the [Team](../team/) page.
The tutor's feedback on the proposal, with my response, is on the
[Feedback](../feedback/#team-design-proposal--tutor-feedback) page.

<div class="post" markdown="1">

#### 1. Introduction

Academic literature searching is repetitive yet error-prone when delegated to a
single large language model (LLM), because unaided LLMs plan unreliably and
fabricate citations (Ji *et al.*, 2023; Kambhampati *et al.*, 2024). This
proposal presents ScholarPlan, a multi-agent system in which an LLM Planner
decomposes a research goal, cooperating agents retrieve, summarise, and verify
evidence from open scholarly sources, and an Archivist stores the results
offline.

#### 2. System Requirements and Assumptions

##### 2.1 Requirements

- **Instruction-tuned LLMs for three roles.** The Planner and Processor must
  return schema-valid JSON (a subtask graph and a claim list) and are ranked on
  the Berkeley Function-Calling Leaderboard (BFCL, 2026); the Critic performs
  entailment classification and is ranked on LLM-AggreFact (Tang, Laban and
  Durrett, 2024).
- **Keyless scholarly APIs** (arXiv, OpenAlex, Crossref) that return stable
  identifiers (DOI, arXiv ID), so every claim is traceable to a source (Priem,
  Piwowar and Orr, 2022).
- **Local sentence embeddings** (Reimers and Gurevych, 2019) for deduplication,
  relevance ranking, and vector indexing at zero cost.
- **A bounded ReAct reasoning loop** (Yao *et al.*, 2023) capped at 20 steps per
  run, controlling both Azure credit and API rate limits.
- **Offline outputs:** a report, BibTeX bibliography, vector index, and
  execution trace, satisfying the retrieval, processing, and storage success
  criteria.

##### 2.2 Assumptions

- Sources are mainly English; full text exists only for open-access works, with
  abstracts as fallback.
- Single user, single run, single machine; no authentication, multi-tenancy, or
  distributed deployment.
- Free-tier quotas and the one-off Azure student credit suffice for
  demonstration scale.

#### 3. Design Decisions

- **Hybrid agent architecture.** A single deliberative LLM Planner reasons over
  the goal while role-specialised reactive agents (Retriever, Processor, Critic,
  Archivist) act only when their input appears. Hybrid layering combines
  deliberative goal-direction with reactive robustness (Wooldridge, 2009) and
  keeps retrieval, processing, and critique as separate failure surfaces, so an
  irrelevant source is never confused with an unsupported claim (Guo *et al.*,
  2024).
- **Blackboard coordination.** Agents never invoke one another; they read and
  write shared state (Figures 2 and 3). The blackboard model offers decoupled,
  opportunistic control among heterogeneous knowledge sources (Hayes-Roth, 1985)
  and has recently outperformed centralised orchestration for LLM agents in
  information discovery (Salemi *et al.*, 2025). Implementing it in SQLite3
  makes every intermediate artefact persistent and inspectable.
- **ReAct planning with Reflexion-style re-planning.** The Planner interleaves
  Thought, Action, and Observation (Yao *et al.*, 2023). A rejected summary
  produces a written Feedback record that the Planner reads before its next
  thought, then narrows the query, seeks another source, or abandons the claim,
  mirroring verbal self-reflection (Shinn *et al.*, 2023).
- **Independent verification.** The Critic, a separate model, tests whether each
  claim is entailed by its cited source, following the LLM-Modulo argument that
  LLM plans need an external verifier (Kambhampati *et al.*, 2024) and grounding
  outputs in retrieved text (Lewis *et al.*, 2020).
- **Benchmark-driven model selection.** GPT-5-mini serves the Planner and
  Processor: it scores 55.46% on BFCL V4, and Azure's $100 student credit funds
  well over a hundred runs at Global Standard prices (BFCL, 2026; Microsoft,
  2026), with GPT-5-nano as fallback. Llama-3.3-70B-Instruct (Dubey et al.,
  2024) serves as the Critic: it outscores gpt-4o-mini on LLM-AggreFact (Tang,
  Laban and Durrett, 2024), is not deprecated in Azure, and, being open-weight,
  can run locally via Ollama for reproducibility.
- **Plain-Python orchestration.** LangChain and LangGraph were rejected because
  their abstractions obscure the ReAct loop under assessment and add dependency
  churn.

<figure>
  <a href="{{ '/assets/img/intelligent-agents/scholarplan-architecture.png' | relative_url }}"><img src="{{ '/assets/img/intelligent-agents/scholarplan-architecture.png' | relative_url }}" alt="Architecture diagram: the Planner, Retriever, Processor, Critic and Archivist each connect only to a central shared blackboard."></a>
  <figcaption><strong>Figure 1.</strong> Architectural view: five role-specialised agents coordinating through the shared blackboard.</figcaption>
</figure>

#### 4. Development Approach

- **Scrum with weekly sprints** (Schwaber and Sutherland, 2020). LLM behaviour
  is empirically uncertain, so requirements emerge through experimentation;
  plan-driven methods presuppose stable, specifiable requirements (Sommerville,
  2016). Sprint reviews double as prompt-evaluation checkpoints.
- **Role-based agent-oriented analysis.** Following the Gaia methodology, each
  agent is specified as a role with responsibilities, permissions (blackboard
  read and write rights), and protocols (Wooldridge, Jennings and Kinny, 2000);
  the five roles map onto per-member work packages, supporting virtual teamwork.
- **Testing by agent type.** Deterministic agents (Retriever, Archivist) receive
  pytest unit tests; the Critic is unit-tested against bespoke-minicheck:7b; the
  Planner and Processor use an evaluation harness of fixed research questions
  with known relevant sources, measuring source recall and Critic pass rate.

<figure>
  <a href="{{ '/assets/img/intelligent-agents/scholarplan-activity.png' | relative_url }}"><img src="{{ '/assets/img/intelligent-agents/scholarplan-activity.png' | relative_url }}" alt="UML activity diagram in swimlanes for User, Planner, Retriever, Processor, Critic and Archivist, with a dashed re-planning loop from Critic rejection back to the Planner."></a>
  <figcaption><strong>Figure 2.</strong> Activity view: end-to-end flow by agent, with the Critic-rejection re-planning loop dashed.</figcaption>
</figure>

<figure>
  <a href="{{ '/assets/img/intelligent-agents/scholarplan-sequence.png' | relative_url }}"><img src="{{ '/assets/img/intelligent-agents/scholarplan-sequence.png' | relative_url }}" alt="UML sequence diagram of the agents reading and writing the blackboard, with a loop over subtasks and the Archivist writing to disk at the end."></a>
  <figcaption><strong>Figure 3.</strong> Sequence view: agents interacting through the blackboard; only the Archivist writes to disk.</figcaption>
</figure>

#### 5. Anticipated Challenges

- **Task decomposition.** LLM planners over- or under-decompose goals (Huang *et
  al.*, 2024). Mitigation: JSON-schema-constrained subtasks, one subtask issued
  per ReAct step, and a coverage threshold that terminates the loop, keeping
  plan validity under external control (Kambhampati *et al.*, 2024).
- **Unreliable or noisy online data.** Irrelevant context degrades LLM reasoning
  (Shi *et al.*, 2023). Mitigation: DOI deduplication, embedding-based relevance
  ranking (Reimers and Gurevych, 2019), and provenance captured at fetch time
  (Priem, Piwowar and Orr, 2022).
- **Hallucinated claims.** Summaries may assert content absent from the source
  (Ji *et al.*, 2023). Mitigation: claim-level entailment checking by the Critic
  (Tang, Laban and Durrett, 2024); unsupported summaries never reach the report.
- **Explainability of LLM decisions.** Mitigation: every Thought, Verdict, and
  Feedback is persisted to the blackboard and exported as a trace, making the
  reasoning chain auditable in the manner of chain-of-thought (Wei *et al.*,
  2022).
- **Agent cooperation and single point of failure.** The blackboard decouples
  agents but concentrates risk (Salemi *et al.*, 2025). Mitigation: SQLite
  transactions for atomic claims and the step budget to prevent runaway loops.
- **Cost and rate limits.** Azure credit is non-renewable, and arXiv permits one
  request every three seconds. Mitigation: the 20-step budget, source caching,
  and an early sprint measuring real per-run cost, since benchmark costs cannot
  simply be summed.
- **Non-deterministic behaviour.** Mitigation: the evaluation harness in Section
  4 and low-temperature sampling.

#### 6. Tools, Libraries, Models and Environments

- **Language and environment:** Python 3.11; uv for virtual environments and
  dependencies; VS Code; Git and GitHub for source control and code review.
- **Models:** GPT-5-mini (Planner, Processor; fallback GPT-5-nano) and
  Llama-3.3-70B-Instruct (Critic) on Azure for Students; bespoke-minicheck:7b
  via Ollama for testing; sentence-transformers for embeddings.
- **Data sources:** arXiv API, OpenAlex API, and Crossref REST API.
- **Storage:** sqlite3 (blackboard, metadata) and sqlite-vec (vector index).
- **Testing:** pytest and a bespoke evaluation harness.
- **Hosting:** Azure for Students ($100 credit) was selected over Hugging Face
  inference credits ($0.10 per month, too small for repeated evaluation) and
  Ollama (hardware the team cannot guarantee).

#### 7. Conclusion

ScholarPlan combines a deliberative ReAct planner, reactive specialists, and
blackboard coordination to meet the three success criteria within free-tier
constraints: retrieval by the Retriever, processing by the Processor and Critic,
storage by the Archivist. Its principal risks (decomposition quality, noisy data
and cost) are addressed through schema-constrained planning, independent
verification and a bounded step budget.

**References**

<div class="references" markdown="1">

Dubey, A. *et al.* (2024) ‘The Llama 3 herd of models’, *arXiv preprint*
arXiv:2407.21783. Available at: <https://arxiv.org/abs/2407.21783> (Accessed: 2
September 2026).

Guo, T., Chen, X., Wang, Y., Chang, R., Pei, S., Chawla, N.V., Wiest, O. and
Zhang, X. (2024) ‘Large language model based multi-agents: A survey of progress
and challenges’, in *Proceedings of the Thirty-Third International Joint
Conference on Artificial Intelligence (IJCAI-24)*. Jeju: IJCAI, pp. 8048–8057.
Available at: <https://doi.org/10.24963/ijcai.2024/890> (Accessed: 2 September
2026).

Hayes-Roth, B. (1985) ‘A blackboard architecture for control’, *Artificial
Intelligence*, 26(3), pp. 251–321. Available at:
<https://doi.org/10.1016/0004-3702(85)90063-3> (Accessed: 2 September 2026).

Huang, X., Liu, W., Chen, X., Wang, X., Wang, H., Lian, D., Wang, Y., Tang, R.
and Chen, E. (2024) ‘Understanding the planning of LLM agents: A survey’, *arXiv
preprint* arXiv:2402.02716. Available at: <https://arxiv.org/abs/2402.02716>
(Accessed: 2 September 2026).

Ji, Z., Lee, N., Frieske, R., Yu, T., Su, D., Xu, Y., Ishii, E., Bang, Y.J.,
Madotto, A. and Fung, P. (2023) ‘Survey of hallucination in natural language
generation’, *ACM Computing Surveys*, 55(12), Article 248, pp. 1–38. Available
at: <https://doi.org/10.1145/3571730> (Accessed: 2 September 2026).

Kambhampati, S., Valmeekam, K., Guan, L., Verma, M., Stechly, K., Bhambri, S.,
Saldyt, L. and Murthy, A. (2024) ‘Position: LLMs can’t plan, but can help
planning in LLM-Modulo frameworks’, in *Proceedings of the 41st International
Conference on Machine Learning (ICML 2024)*. Vienna: PMLR 235. Available at:
<https://arxiv.org/abs/2402.01817> (Accessed: 2 September 2026).

Lewis, P. *et al.* (2020) ‘Retrieval-augmented generation for
knowledge-intensive NLP tasks’, in *Advances in Neural Information Processing
Systems 33 (NeurIPS 2020)*, pp. 9459–9474. Available at:
<https://arxiv.org/abs/2005.11401> (Accessed: 2 September 2026).

Patil, S.G., Zhang, T., Wang, X. and Gonzalez, J.E. (2023) ‘Gorilla: Large
language model connected with massive APIs’, *arXiv preprint* arXiv:2305.15334.
Available at: <https://arxiv.org/abs/2305.15334> (Accessed: 2 September 2026).

Priem, J., Piwowar, H. and Orr, R. (2022) ‘OpenAlex: A fully-open index of
scholarly works, authors, venues, institutions, and concepts’, *arXiv preprint*
arXiv:2205.01833. Available at: <https://arxiv.org/abs/2205.01833> (Accessed: 2
September 2026).

Reimers, N. and Gurevych, I. (2019) ‘Sentence-BERT: Sentence embeddings using
Siamese BERT-networks’, in *Proceedings of the 2019 Conference on Empirical
Methods in Natural Language Processing and the 9th International Joint
Conference on Natural Language Processing (EMNLP-IJCNLP)*. Hong Kong:
Association for Computational Linguistics, pp. 3982–3992.

Salemi, A., Parmar, M., Goyal, P., Song, Y., Yoon, J., Zamani, H., Palangi, H.
and Pfister, T. (2025) ‘LLM-based multi-agent blackboard system for information
discovery in data science’, *arXiv preprint* arXiv:2510.01285. Available at:
<https://arxiv.org/abs/2510.01285> (Accessed: 2 September 2026).

Schwaber, K. and Sutherland, J. (2020) *The Scrum Guide*. Available at:
<https://scrumguides.org> (Accessed: 2 September 2026).

Shi, F., Chen, X., Misra, K., Scales, N., Dohan, D., Chi, E.H., Schärli, N. and
Zhou, D. (2023) ‘Large language models can be easily distracted by irrelevant
context’, in *Proceedings of the 40th International Conference on Machine
Learning (ICML 2023)*. Honolulu: PMLR 202, pp. 31210–31227.

Shinn, N., Cassano, F., Gopinath, A., Narasimhan, K. and Yao, S. (2023)
‘Reflexion: Language agents with verbal reinforcement learning’, in *Advances in
Neural Information Processing Systems 36 (NeurIPS 2023)*. Available at:
<https://arxiv.org/abs/2303.11366> (Accessed: 2 September 2026).

Sommerville, I. (2016) *Software Engineering*. 10th edn. Harlow: Pearson.

Tang, L., Laban, P. and Durrett, G. (2024) ‘MiniCheck: Efficient fact-checking
of LLMs on grounding documents’, in *Proceedings of the 2024 Conference on
Empirical Methods in Natural Language Processing (EMNLP 2024)*. Miami:
Association for Computational Linguistics. Available at:
<https://doi.org/10.18653/v1/2024.emnlp-main.499> (Accessed: 2 September 2026).

Wei, J., Wang, X., Schuurmans, D., Bosma, M., Ichter, B., Xia, F., Chi, E., Le,
Q.V. and Zhou, D. (2022) ‘Chain-of-thought prompting elicits reasoning in large
language models’, in *Advances in Neural Information Processing Systems 35
(NeurIPS 2022)*, pp. 24824–24837. Available at:
<https://arxiv.org/abs/2201.11903> (Accessed: 2 September 2026).

Wooldridge, M. (2009) *An Introduction to MultiAgent Systems*. 2nd edn.
Chichester: John Wiley & Sons.

Wooldridge, M., Jennings, N.R. and Kinny, D. (2000) ‘The Gaia methodology for
agent-oriented analysis and design’, *Autonomous Agents and Multi-Agent
Systems*, 3(3), pp. 285–312. Available at:
<https://doi.org/10.1023/A:1010071910869> (Accessed: 2 September 2026).

Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K. and Cao, Y.
(2023) ‘ReAct: Synergizing reasoning and acting in language models’, in
*Proceedings of the Eleventh International Conference on Learning
Representations (ICLR 2023)*. Available at: <https://arxiv.org/abs/2210.03629>
(Accessed: 2 September 2026).

Berkeley Function-Calling Leaderboard (2026) Berkeley Function-Calling
Leaderboard V4. Berkeley, CA: UC Berkeley Sky Computing Lab. Available at:
<https://gorilla.cs.berkeley.edu/leaderboard.html> (Accessed: 16 Aug 2026).

Microsoft (2026) Azure Retail Prices API. Available at:
<https://learn.microsoft.com/en-us/rest/api/cost-management/retail-prices/azure-retail-prices>
(Accessed: 16 August 2026).

</div>

</div>

#### What this demonstrates

- **LO1.** The proposal chooses an architecture and justifies it against the
  alternatives: hybrid deliberative and reactive agents over a single LLM, and
  blackboard coordination over direct calls or central orchestration.
- **LO2.** It addresses the known risks of LLM agents (unreliable planning,
  noisy data and hallucinated claims) with specific controls. These are
  schema-constrained subtasks, an independent Critic from a different model
  family, and a bounded step budget.
- **LO3.** It selects tools by evidence: models by benchmark and cost, keyless
  APIs for traceable provenance, and plain Python over LangChain so the ReAct
  loop stays inspectable.

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

### Constituency-based parse trees

<p class="meta"><span class="badge badge--completed">completed</span> <span class="muted">Evidences LO2</span></p>

**The brief.** Draw a constituency-based parse tree for three phrases: *The
government raised interest rates.* / *The internet gives everyone a voice.* /
*The man saw the dog with the telescope.*

Trees are written as indented plain text. It reads as a tree, diffs cleanly in
git, and needs no image toolchain or JavaScript — the same reason the KQML above
is a code block.

Tags: `S` sentence · `NP` noun phrase · `VP` verb phrase · `PP` prepositional
phrase · `DT` determiner · `NN` noun · `NNS` plural noun · `VBD` past-tense verb
· `VBZ` third-person verb · `IN` preposition. Sentence-final punctuation is
omitted.

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

*interest rates* is a single NP — a noun compound, not two separate arguments of
the verb.

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

*gives* is ditransitive, so the VP takes two NP objects — the recipient
(*everyone*) and the thing given (*a voice*).

#### 3. The man saw the dog with the telescope.

This one is structurally ambiguous. Both trees are grammatical, and they differ
only in where the PP attaches.

**Reading A — the man used the telescope.** The PP attaches to the VP, modifying
*saw*.

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

**Reading B — the dog had the telescope.** The PP attaches inside the object NP,
modifying *dog*.

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

#### What this demonstrates

- **Technique applied to a real problem.** Constituency structure is what meaning
  attaches to. Sentence 1 shows why: read *interest* and *rates* as separate
  objects and the sentence means something the writer did not say.
- **A live research issue.** Sentence 3 is PP-attachment ambiguity, and syntax
  alone cannot settle it — resolving it needs world knowledge or context, not a
  better grammar. This is the same failure mode as an agent that parses an
  instruction correctly and still grounds it to the wrong referent.

<div class="todo" markdown="1">
Add the remaining weekly formative activities as `### Week N — …` sections above,
each with its badge and the outcomes it evidences. If they grow past a handful,
move them to a page of their own.
</div>
