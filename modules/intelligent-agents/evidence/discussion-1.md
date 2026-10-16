---
title: "Appendix: Discussion 1 — Agent-Based Systems in contemporary organisations"
short_title: Discussion 1
module: intelligent-agents
nav_exclude: true
permalink: /modules/intelligent-agents/evidence/discussion-1/
summary: >-
  The full thread, reproduced verbatim from the module forum.
---

Appendix to the [Discussions](../../discussions/) page · 5–16 August 2026.

My posts are reproduced verbatim from the module forum, including their original
references; corrections are listed at the end. The summaries of other students'
posts are my own précis. Peers are identified by first name and initial.

The thread moved from a diagnosis — LLM-based
agents buy adaptability at the cost of reliability — to the question of which
controls make that trade-off manageable for an organisation.

## Part 1 — My thread

### My initial post

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

### Peer responses to my post

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

### My summary post

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

## Part 2 — My responses to peers

I responded to two other initial posts, both on Sunday, 9 August 2026 — a week
before I wrote my summary post. Each response is reproduced verbatim; the
summary of the peer's own post is my précis of it.

### Response to Luis T. — multi-agent systems in manufacturing

**His initial post.** Luis argued that centralised manufacturing control
achieves high productivity but depends on large monolithic software that is
expensive to customise and maintain (Leitão, 2009). Multi-agent systems
decompose the problem across autonomous agents and are already used in planning,
scheduling, logistics and energy reduction (Pulikottil et al., 2021). His
conclusion was that industrial adoption is still limited by two kinds of
barrier — **technical**, as there is no general reference architecture and
integrating heterogeneous systems and protocols is hard, and
**organisational**, as decentralised decision-making sits badly with managers
used to central control.

**My response**

<p class="post-meta">Posted Sunday, 9 August 2026 · 198 words excluding the salutation and references</p>

<div class="post" markdown="1">

Hi Luis,

I totally agree with your point that Multi-Agent Systems (MAS) are a great
alternative to monolithic manufacturing control systems. You have also correctly
identified the struggles and limitations that traditional centralized
architectures face with the extreme customization and agility demands of the
globalized economy.

However, in my opinion, the technical and organizational barriers that you have
mentioned are being resolved by recent advances. For instance, Bi et al. (2024)
illustrate that the challenge of integrating heterogeneous production systems can
be mitigated using a distributed decision-making framework, which can enable
resource allocation in real-time during disruptions, such as machine breakdowns.

Furthermore, organizational barriers can be addressed by integrating MAS with
Large Language Models (LLMs). As demonstrated by Lim et al. (2024), LLMs can be
used to interpret and act on natural language provided by users. This allows the
translation of human language into machine actions such as G-Code allocation.
Yet, LLMs raise new risks that did not exist before. Tikka et al. (2026) noted
that the probabilistic nature of LLMs can cause hallucinations that can lead to
inaccurate operational parameters. Consequently, we cannot rely on LLMs without
enforcing deterministic guardrails and Retrieval-Augmented Generation (RAG)
pipelines to mitigate these risks.

**References**

<div class="references" markdown="1">

Bi, M., Kovalenko, I., Tilbury, D.M. and Barton, K. (2024) 'Dynamic distributed
decision-making for resilient resource reallocation in disrupted manufacturing
systems', *International Journal of Production Research*, 62(5), pp. 1737–1757.
Available at: <https://arxiv.org/pdf/2507.19043>

Lim, J., Vogel-Heuser, B. and Kovalenko, I. (2024) 'Large Language
Model-Enabled Multi-Agent Manufacturing Systems', *2024 IEEE 20th International
Conference on Automation Science and Engineering (CASE)*, pp. 3940–3946.
Available at: <https://ieeexplore.ieee.org/document/10711432>

Tikka, P., Karjalainen, J., Alesani, A. and Goriachev, V. (2026) 'Large Language
Model Hallucination Mitigation in Three Industrial Use Cases', *IEEE Access*,
14, pp. 25564–25576. Available at: <https://arxiv.org/abs/2404.08189>

</div>

</div>

### Response to Khadijah H. — the rise of intelligent agents

**Her initial post.** Khadijah described AI agents as tools that remember tasks,
use one or more models and act with little supervision, reaching browsers, CRM
systems and cloud storage to do their work — behaving "more like an employee"
than a programmed robot (Boston Consulting Group, 2026). She set out use cases
across marketing, sales, IT, supply chain and software development (Hayes and
Downie, 2025), and framed the direction of travel as McKinsey's "agentic
organisation", in which early adopters gain an advantage in automation,
decision-making, cost and personalisation (Sukharevsky et al., 2025).

**My response**

<p class="post-meta">Posted Sunday, 9 August 2026 · 203 words excluding the salutation and references</p>

<div class="post" markdown="1">

Hi Khadijah,

I strongly agree with you that AI agents represent a significant technological
leap. You have correctly identified the concept of the "agentic organisation" and
the potential for competitive advantage that organisations can gain from it.

However, I would argue that AI agents cannot run autonomously without
supervision due to the risks that they introduce when executing complex,
high-stakes decisions. As Asaftei and Roberts (2026) noted, organisations must
shift their focus toward creating solid governance structures to mitigate risks
introduced by AI instead of deploying AI agents blindly.

Furthermore, as Slesarenko (2025) demonstrated, implementing a Human-in-the-Loop
(HitL) approach is necessary to ensure strict oversight of ethics and compliance
with safety and regulatory standards. This is explicitly validated by Jiang et
al. (2026), whose research on industrial control systems emphasises that the true
value of agentic AI currently lies in safety-aware and explainable decision
support rather than unrestricted autonomous control.

In conclusion, autonomous AI agents that execute actions without human
intervention can pose significant risks, as a single faulty decision by
autonomous agents can lead to data leaks, financial losses or system outages,
which can impact the organisation's reputation. Therefore, technical governance
must be applied to AI agents to enforce continued monitoring and
human-in-the-loop policies.

**References**

<div class="references" markdown="1">

Asaftei, G.M. and Roberts, R. (2026) 'State of AI trust in 2026: shifting to the
agentic era', *McKinsey & Company*. Available at:
<https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/tech-forward/state-of-ai-trust-in-2026-shifting-to-the-agentic-era>

Jiang, X., Xie, H., Wang, J., Yang, Z., Zhou, Y., Yao, L. and Zhu, Z. (2026)
'Agentic AI for Safety-Aware Process Monitoring and Fault Diagnosis: A Review'.
Available at: <https://www.proquest.com/docview/3363962734>

Slesarenko, A. (2025) 'Human-in-the-Loop (HitL) Agentic AI for High-Stakes
Oversight 2026', *OneReach.ai*. Available at:
<https://onereach.ai/blog/human-in-the-loop-agentic-ai-systems/>

</div>

</div>

## Referencing corrections

The posts above are reproduced verbatim, so their errors are left in place and
corrected here. Reviewing them for this portfolio, I found two:

1. Both of my own thread posts set the Mohajeri Parizi *et al.* (2019) entry in
   APA style (ampersand, no quotation marks, no editors) while every other entry
   is UoE Harvard.
2. In my response to Luis, two journal articles are linked to arXiv pages that
   are not the versions cited. One identifier dates from 2025 for a 2024 article,
   the other from 2024 for a 2026 one. The publisher DOI should have been used.

The corrected entries, checked against Crossref:

<div class="references" markdown="1">

Bi, M., Kovalenko, I., Tilbury, D.M. and Barton, K. (2024) ‘Dynamic distributed
decision-making for resilient resource reallocation in disrupted manufacturing
systems’, *International Journal of Production Research*, 62(5), pp. 1737–1757.
Available at: <https://doi.org/10.1080/00207543.2023.2200567> (Accessed: 15
October 2026).

Mohajeri Parizi, M., Sileno, G. and van Engers, T. (2019) ‘Integrating CP-nets
in reactive BDI agents’, in Baldoni, M., Dastani, M., Liao, B., Sakurai, Y. and
Zalila Wenkstern, R. (eds) *PRIMA 2019: Principles and Practice of Multi-Agent
Systems*. Lecture Notes in Computer Science. Cham: Springer, pp. 305–320.
Available at: <https://doi.org/10.1007/978-3-030-33792-6_19> (Accessed: 15
October 2026).

Tikka, P., Karjalainen, J., Alesani, A. and Goriachev, V. (2026) ‘Large language
model hallucination mitigation in three industrial use cases’, *IEEE Access*,
14, pp. 25564–25576. Available at: <https://doi.org/10.1109/ACCESS.2026.3659997>
(Accessed: 15 October 2026).

</div>
