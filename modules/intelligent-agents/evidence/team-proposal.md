---
title: "Appendix: ScholarPlan team design proposal"
short_title: ScholarPlan team design proposal
module: intelligent-agents
nav_exclude: true
permalink: /modules/intelligent-agents/evidence/team-proposal/
summary: >-
  The team's design proposal, reproduced verbatim as submitted in September 2026.
---

Appendix to the [Artefacts](../../artefacts/#design-and-modelling) and [Team](../../team/) pages. This was a team submission (Group A); how the work was divided is on the Team page.

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
| Plan the work | Planner (deliberative, ReAct loop) | Sections [3](#design-decisions) and [5](#anticipated-challenges) |
| Find documents or online content | Retriever (arXiv, OpenAlex, Crossref) | Sections [2.1](#requirements) and [6](#tools-libraries-models-and-environments) |
| Process or reason over the data | Processor and Critic (claim-level verification) | Sections [3](#design-decisions) and [5](#anticipated-challenges) |
| Do something meaningful with the result | Archivist (report, BibTeX, vector index, trace) | Sections [2.1](#requirements) and [7](#conclusion) |

The proposal is reproduced verbatim below, including the figures as submitted.
Only the heading levels and line wrapping are changed so that it fits this page.
How the work was divided is recorded on the [Team](../../team/) page.
The tutor's feedback on the proposal, with my response, is in the
[evidence appendix](../tutor-feedback/).

<div class="post" markdown="1">

## 1. Introduction

Academic literature searching is repetitive yet error-prone when delegated to a
single large language model (LLM), because unaided LLMs plan unreliably and
fabricate citations (Ji *et al.*, 2023; Kambhampati *et al.*, 2024). This
proposal presents ScholarPlan, a multi-agent system in which an LLM Planner
decomposes a research goal, cooperating agents retrieve, summarise, and verify
evidence from open scholarly sources, and an Archivist stores the results
offline.

## 2. System Requirements and Assumptions

### 2.1 Requirements

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

### 2.2 Assumptions

- Sources are mainly English; full text exists only for open-access works, with
  abstracts as fallback.
- Single user, single run, single machine; no authentication, multi-tenancy, or
  distributed deployment.
- Free-tier quotas and the one-off Azure student credit suffice for
  demonstration scale.

## 3. Design Decisions

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

## 4. Development Approach

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

## 5. Anticipated Challenges

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

## 6. Tools, Libraries, Models and Environments

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

## 7. Conclusion

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

## What this demonstrates

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
