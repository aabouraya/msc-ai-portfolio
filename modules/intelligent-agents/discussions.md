---
title: Collaborative Discussions
short_title: Discussions
module: intelligent-agents
nav_order: 1
permalink: /modules/intelligent-agents/discussions/
summary: >-
  Initial posts, peer responses and summary posts from the collaborative
  discussion forum. Evidences LO1 and LO4.
---

Each discussion is recorded in three sections: my initial post, a summary of the
peer responses it drew and what I took from them, and my summary post. My own
posts are reproduced verbatim as submitted.

Peers are identified by first name and initial only.

## Discussion 1 — Agent-Based Systems in contemporary organisations

<p class="meta"><span class="badge badge--completed">completed</span> <span class="muted">Units 1–3</span></p>

The thread ran from 5 to 16 August 2026. It moved from a diagnosis — LLM-based
agents buy adaptability at the cost of reliability — to the question of which
controls make that trade-off manageable for an organisation.

### 1. My initial post

<p class="post-meta">Posted Wednesday, 5 August 2026 · 241 words excluding references</p>

<div class="post" markdown="1">

The concept of Agent-Based Systems is by no means new. As Mohajeri Parizi et al.
(2019) describe, traditional frameworks such as reactive agent architectures and
Belief-Desire-Intention (BDI) models that are grounded in predefined rule sets
form the core fundamentals of Agent-Based Systems. However, Schulz and Jander
(2025) also argue that traditional frameworks struggle in rapidly changing
environments due to their dependency on static, developer-defined plans.

The turning point came with the rise of Large Language Models (LLMs), as
Agent-Based Systems became more powerful due to the capabilities LLMs can
provide. As Li et al. (2024) noted, LLMs can be used in Agent-Based Systems as
cognitive engines that provide the agent with natural language reasoning,
dynamic task decomposition, and memory. However, using LLMs can compromise the
agent's reliability due to hallucination errors, as discussed by Li et al.
(2024), and cascading failures and inconsistencies, as highlighted by Hammond et
al. (2025).

Despite these flaws, companies are eager to move toward modern agent-based
systems. For contemporary organisations, the use of agent-based systems can
provide significant strategic and operational benefits. As Li et al. (2024)
illustrated, agent-based systems can automate complex workflows such as software
development and financial trading more efficiently due to their ability to adapt
dynamically to unexpected changes. However, Hammond et al. (2025) warn that
advanced agent-based systems have introduced significant governance challenges
for organisations due to the operational risks that they pose, such as
inter-agent miscoordination and unpredictable destabilising dynamics.

**References**

<div class="references" markdown="1">

Mohajeri Parizi, M., Sileno, G., & van Engers, T. (2019). Integrating CP-Nets in
Reactive BDI Agents. *Lecture Notes in Computer Science*, 305–320.
<https://doi.org/10.1007/978-3-030-33792-6_19>

Schulz, T. and Jander, K. (2025) 'Dynamic plan generation with LLMs: automatic
execution of abstract BDI-agent goals', *International Journal of Parallel,
Emergent and Distributed Systems*, pp. 1–21. doi: 10.1080/17445760.2025.2541956

Li, X., Wang, Y., Zhang, R., Liu, C. and Chen, H. (2024) 'A survey on LLM-based
multi-agent systems: workflow, infrastructure, and challenges', *Vicinagearth*,
1(9), pp. 1–43. Available at:
<https://www.researchgate.net/publication/384732283_A_survey_on_LLM-based_multi-agent_systems_workflow_infrastructure_and_challenges>

Hammond, L., Chan, A., Clifton, J., Hoelscher-Obermaier, J., Khan, A., McLean,
E., Smith, C., Barfuss, W., Foerster, J., Gavenčiak, T., Han, T.A., Hughes, E.,
Kovařík, V., Kulveit, J., Leibo, J.Z., Oesterheld, C., de Witt, C.S., Shah, N.,
Wellman, M., Bova, P. and Cimpeanu, T. (2025) 'Multi-agent risks from advanced
AI', *arXiv preprint* arXiv:2502.14143. Available at:
<https://arxiv.org/abs/2502.14143>

</div>

</div>

### 2. Peer responses and what I learned

Two peers responded.

**Isaac S.** (6 August 2026) accepted the trade-off I described and moved the
thread from diagnosis to mitigation, proposing three controls:

- **Verify outputs before handoff** — dedicated hallucination detection improves
  factual accuracy (Anaokar et al., 2025).
- **Evaluate the process, not only the outcome** — final-success metrics hide
  where execution actually broke down (Ma et al., 2024).
- **Test in a sandbox before granting live access** — simulated tool
  environments surface risky behaviour first (Ruan et al., 2024).

**Kapinga D.** (16 August 2026) agreed that LLM agents handle dynamic settings
better than static BDI plans, but argued that greater autonomy does not by itself
produce greater trustworthiness. Governance therefore has to be explicit: human
oversight, monitoring frameworks, and clearly defined operational boundaries
(Hammond et al., 2025).

**What I learned**

- I had framed reliability as a *model* limitation. It is mostly an
  **architectural and evaluation** problem.
- Errors propagate at **handoffs between agents**, so that is where verification
  belongs.
- Measuring only the outcome hides where a failure began.
- Sandboxed testing turns governance from a policy statement into a design
  practice.

These controls make failures detectable and containable. They do not remove them.

### 3. My summary post

<p class="post-meta">Posted Sunday, 16 August 2026 · 347 words excluding references</p>

<div class="post" markdown="1">

This discussion examined how transitioning from traditional agent architectures
to large language model (LLM) powered agents increased both the capabilities and
the risk of agent-based systems.

In my initial post, I argued that reactive and Belief-Desire-Intention (BDI)
architectures rely on predefined rule sets as described by Mohajeri Parizi et al.
(2019), and consequently face challenges in rapidly changing environments due to
their dependence on static, predefined plans as demonstrated by Schulz and Jander
(2025). LLMs address these limitations by functioning as cognitive engines that
provide natural language reasoning, dynamic task decomposition, and memory, as
shown by Li et al. (2024). This enables organisations to automate complex
workflows, including software development and financial trading. However, I also
emphasised the associated costs of this flexibility, such as hallucinations and
errors, as noted by Li et al.(2024), cascading failures, inter-agent
miscoordination, and unpredictable, destabilising dynamics that present
significant governance challenges, as described by Hammond et al. (2025).

The peer response concurred with this assessment and shifted the discussion
toward mitigation strategies. Three controls were proposed. First, verify agent
outputs before they are used by subsequent agents or workflow stages, supported
by evidence that dedicated hallucination detection enhances factual accuracy, as
shown by Anaokar et al.(2025). Next, evaluate processes rather than solely final
outcomes, as end-state success metrics can obscure points of execution failure,
as noted by Ma et al.(2024), and finally, test new agents in simulated tool
environments to reveal risky behaviours prior to granting live access, as
described by Ruan et al. (2024).

Through this exchange, I learned that adaptability and control must advance in
tandem. My initial perspective considered reliability primarily as a model
limitation, but the discussion revealed it is predominantly an architectural and
evaluation issue. Specifically, errors propagate during handoffs between agents,
indicating that verification should occur at these junctures. Measuring only
outcomes obscures the sources of failures, while sandboxed testing transforms
governance from a policy statement into a design practice. Although these
measures mitigate rather than eliminate risk, they enhance the detectability and
containment of failures, which is essential for organisational trust in such
systems.

**References**

<div class="references" markdown="1">

Mohajeri Parizi, M., Sileno, G., & van Engers, T. (2019). Integrating CP-Nets in
Reactive BDI Agents. *Lecture Notes in Computer Science*, 305–320.
<https://doi.org/10.1007/978-3-030-33792-6_19>

Schulz, T. and Jander, K. (2025) 'Dynamic plan generation with LLMs: automatic
execution of abstract BDI-agent goals', *International Journal of Parallel,
Emergent and Distributed Systems*, pp. 1–21. doi: 10.1080/17445760.2025.2541956

Li, X., Wang, Y., Zhang, R., Liu, C. and Chen, H. (2024) 'A survey on LLM-based
multi-agent systems: workflow, infrastructure, and challenges', *Vicinagearth*,
1(9), pp. 1–43. Available at:
<https://www.researchgate.net/publication/384732283_A_survey_on_LLM-based_multi-agent_systems_workflow_infrastructure_and_challenges>

Hammond, L., Chan, A., Clifton, J., Hoelscher-Obermaier, J., Khan, A., McLean,
E., Smith, C., Barfuss, W., Foerster, J., Gavenčiak, T., Han, T.A., Hughes, E.,
Kovařík, V., Kulveit, J., Leibo, J.Z., Oesterheld, C., de Witt, C.S., Shah, N.,
Wellman, M., Bova, P. and Cimpeanu, T. (2025) 'Multi-agent risks from advanced
AI', *arXiv preprint* arXiv:2502.14143. Available at:
<https://arxiv.org/abs/2502.14143>

Anaokar, S., Ganatra, S., Kashid, H., Bhattacharyya, S., Nair, S., Sekhar, R.,
Manohar, S., Hemrajani, R. and Bhattacharyya, P. (2025) 'HalluDetect: detecting,
mitigating, and benchmarking hallucinations in conversational systems in the
legal domain', *Proceedings of the 2025 Conference on Empirical Methods in
Natural Language Processing: Industry Track*. Suzhou, China, 5–9 November.
Association for Computational Linguistics, pp. 1822–1847. Available at:
<https://doi.org/10.18653/v1/2025.emnlp-industry.128> (Accessed: 6 August 2026).

Ma, C., Zhang, J., Zhu, Z., Yang, C., Yang, Y., Jin, Y., Lan, Z., Kong, L. and
He, J. (2024) 'AgentBoard: an analytical evaluation board of multi-turn LLM
agents', *Advances in Neural Information Processing Systems*, 37, pp.
74325–74362. Available at: <https://doi.org/10.52202/079017-2365> (Accessed: 6
August 2026).

Ruan, Y., Dong, H., Wang, A., Pitis, S., Zhou, Y., Ba, J., Dubois, Y., Maddison,
C. and Hashimoto, T. (2024) 'Identifying the risks of LM agents with an
LM-emulated sandbox', *The Twelfth International Conference on Learning
Representations (ICLR 2024)*. Vienna, Austria, 7–11 May. Available at:
<https://proceedings.iclr.cc/paper_files/paper/2024/hash/7274ed909a312d4d869cc328ad1c5f04-Abstract-Conference.html>
(Accessed: 6 August 2026).

</div>

</div>

<div class="todo" markdown="1">
**One fix to carry forward.** Both posts set the Mohajeri Parizi et al. (2019)
entry in APA (ampersand, year after the names, no quotation marks) while every
other entry is UoE Harvard. The posts are reproduced verbatim here because they
are a transcript, so correct the style in future submissions rather than editing
the record.
</div>
