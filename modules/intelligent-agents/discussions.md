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

Each discussion is recorded in two parts. **Part 1** is my own thread — my
initial post, the peer responses it drew, and my summary post. **Part 2** is the
responses I wrote to other students' initial posts. Everything I submitted is
reproduced verbatim; the summaries of other people's posts are my own précis.

Peers are identified by first name and initial only.

## Discussion 1 — Agent-Based Systems in contemporary organisations

<p class="meta"><span class="badge badge--completed">completed</span> <span class="muted">Units 1–3</span></p>

The thread ran from 5 to 16 August 2026. It moved from a diagnosis — LLM-based
agents buy adaptability at the cost of reliability — to the question of which
controls make that trade-off manageable for an organisation.

### Part 1 — My thread

#### My initial post

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

#### Peer responses to my post, and what I learned

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

#### My summary post

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

### Part 2 — My responses to peers

I responded to two other initial posts, both on Sunday, 9 August 2026 — a week
before I wrote my summary post. Each response is reproduced verbatim; the
summary of the peer's own post is my précis of it.

#### Response to Luis T. — multi-agent systems in manufacturing

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

**What I learned**

- A "limited adoption" claim needs a date check. The integration barrier Luis
  cited from 2009–2021 sources has partial answers now (Bi et al., 2024), so the
  argument is about *how far* the barrier has moved, not whether it exists.
- Organisational barriers can have technical remedies. A natural-language
  interface (Lim et al., 2024) lowers the cost of accepting decentralisation,
  rather than arguing managers out of it.
- **Every fix carries its own failure mode.** Adding an LLM to remove a
  usability barrier introduces hallucination. I reached the same trade-off I had
  argued in my own initial post, but from the manufacturing side — which is what
  made me treat it as general rather than domain-specific.

#### Response to Khadijah H. — the rise of intelligent agents

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

**What I learned**

- The "agent as employee" analogy is good for adoption and bad for
  accountability. An employee can be held answerable; an agent cannot, so the
  responsibility stays with whoever deployed it.
- Early-adopter advantage arguments price the upside and rarely price the cost
  of one bad autonomous action — data leak, financial loss, outage.
- The useful question is not *how autonomous* but *autonomous over what*.
  Safety-aware, explainable decision support (Jiang et al., 2026) with a human
  in the loop (Slesarenko, 2025) is where the value sits today.
- Arguing this twice in one day, in two different domains, is what turned it from
  an opinion into the position I took in my summary post.

### Referencing corrections

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

Consistent referencing is objective 3 in my [PDP](../skills/#action-plan).

## Discussion 3 — Deep learning and the ethics of generative AI

<p class="meta"><span class="badge badge--completed">completed</span> <span class="muted">30 September – 13 October 2026</span></p>

The thread ran from 30 September to 13 October 2026. It started from two ethical
concerns about generative AI, copyright and misinformation. It ended on the
argument that both risks come from the property that makes deep learning
powerful, so no single safeguard can cover them.

### Part 1 — My thread

#### My initial post

<p class="post-meta">Posted Wednesday, 30 September 2026 · 173 words excluding references</p>

<div class="post" markdown="1">

In recent years, deep learning technologies have transformed interactions with
digital content, including text and images. Generative AI models such as ChatGPT
and DALL-E provide advanced content-creation capabilities that were not possible
before. However, these advancements in content generation present significant
ethical implications that need to be examined.

A primary ethical concern is copyright infringement. As Buick (2025) noted,
generative AI models are trained on datasets collected from the internet, which
often include copyrighted texts. These texts may be used to generate new outputs
without obtaining consent from the original creators.

Misinformation and deception represent additional critical ethical concerns, as
generative AI models can produce realistic synthetic content that poses
significant risks. As illustrated by Romero (2024), AI-generated images and
videos have been used to manipulate election outcomes and facilitate investment
scams. Such threats undermine society's capacity to trust digital information.

In conclusion, generative AI enables powerful new forms of digital content, but
also brings important ethical risks. Clear guidelines and careful oversight are
essential to maximise its benefits and limit potential harms.

**References**

<div class="references" markdown="1">

Buick, A. (2025) Copyright and AI training data—transparency to the rescue?
Journal of intellectual property law & practice. [Online] 20 (3), 182–192.

Romero Moreno, F. (2024) Generative AI and deepfakes: a human rights approach to
tackling harmful content. International review of law, computers & technology.
[Online] 38 (3), 297–326.

</div>

</div>

#### Peer responses to my post, and what I learned

Two peers responded.

**Lara K.** (1 October 2026) said my claim that AI-generated content had been
used to "manipulate election outcomes" conflated the *use* of deceptive content
with *evidence* that it changed a result. She cited three studies:

- **No decisive effect on outcomes.** In a non-representative sample of
  election deepfakes from 11 countries, none had decisively influenced an
  election (Łabuz and Nehring, 2024). The broader concern is declining trust in
  information, politics and the media.
- **Low credibility does not prevent harm.** Political deepfakes can
  delegitimise a targeted politician even when viewers do not find them highly
  credible (Hameleers, van der Meer and Dobber, 2024).
- **Voting intentions can shift, and fact checks help.** Deepfakes shifted
  attitudes and voting intentions towards a fictitious politician, and
  journalistic fact checks substantially reduced the effect (Dan, 2026).

She asked which interventions I would prioritise: detection before content
spreads, fact-checking after it spreads, or longer-term media literacy.

**Isaac S.** (2 October 2026) agreed that oversight is needed. He argued that it
should be stated as safeguards at specific points in the lifecycle:

- **Before training, document provenance.** An audit of more than 1,800 text
  datasets found widespread missing or inaccurate licence information (Longpre
  et al., 2024), so a platform's licence label is not enough. Keep records of
  creators and permitted uses, and give creators a way to challenge inclusion.
- **Before deployment, test outputs.** Diffusion models can reproduce memorised
  training images (Carlini et al., 2023). Deduplication and close-match screening
  help, but they should be evaluated rather than assumed to work.
- **At distribution, don't rely on labels alone.** Deepfake videos stayed
  influential despite explicit advance warnings (Clark and Lewandowsky, 2026).
  Combine labels with advertiser verification, endorsement checks, rapid review
  of impersonation reports, and an appeals process for moderation errors.

**What I learned**

- I overstated the evidence. The source supported *use* of deepfakes around
  elections, not proof that they *changed* results. My summary post says
  "target elections" instead.
- The more defensible harm is **erosion of trust in authentic information**,
  which does not depend on proving an effect on any single election.
- "Clear guidelines and careful oversight" was a conclusion with no mechanism.
  Isaac's response turned it into checks at data collection, model evaluation
  and content distribution.
- Copyright and deepfake risks share one cause. Models learn from vast,
  uncurated data and reproduce its patterns convincingly, and that is also what
  makes them useful.

#### My summary post

<p class="post-meta">Posted Tuesday, 13 October 2026 · 307 words excluding references</p>

<div class="post" markdown="1">

This discussion examined the ethical implications of generative AI, a deep
learning application. My initial post raised two concerns. The first was
copyright infringement: models are trained on scraped datasets that contain
copyrighted works used without creators' consent (Buick, 2025). The second was
misinformation: realistic synthetic content has been used to target elections
and facilitate investment scams (Romero Moreno, 2024).

My peers sharpened both arguments. Lara pointed out that I had conflated the use
of deceptive content with evidence that it changed election results. Łabuz and
Nehring (2024) found that none of the deepfakes in their sample had decisively
influenced an election outcome, but they noted declining trust in information.
Even when people don't see them as credible, deepfakes can delegitimise
politicians (Hameleers, van der Meer and Dobber, 2024). They can also shift
voting intentions, although journalistic fact-checks reduce this effect (Dan,
2026).

Isaac turned my call for oversight into concrete safeguards. An audit of more
than 1,800 datasets found widespread missing or inaccurate licence information
(Longpre et al., 2024), so developers should document data provenance rather
than rely on platform labels. Carlini et al. (2023) showed that diffusion models
can reproduce memorised training images, supporting the case for testing outputs
before deployment. Clark and Lewandowsky (2026) found that deepfakes remained
influential despite warnings, indicating that disclosure labels alone are
insufficient.

I learned that these risks stem from the same property that makes deep learning
powerful: models learn from vast, uncurated datasets and convincingly reproduce
their patterns. I also learned that deepfakes' main harm may be eroding trust in
authentic information, rather than any proven effect on election results.
Oversight therefore needs to cover the full lifecycle: data collection, model
evaluation and content distribution. Because no single safeguard is sufficient,
layered measures combining provenance records, memorisation testing, labelling,
fact-checking and media literacy offer the most realistic protection.

**References**

<div class="references" markdown="1">

Buick, A. (2025) 'Copyright and AI training data—transparency to the rescue?',
*Journal of Intellectual Property Law & Practice*, 20(3), pp. 182–192.

Carlini, N., Hayes, J., Nasr, M., Jagielski, M., Sehwag, V., Tramèr, F., Balle,
B., Ippolito, D. and Wallace, E. (2023) 'Extracting training data from diffusion
models', in *32nd USENIX Security Symposium (USENIX Security 23)*. USENIX
Association, pp. 5253–5270. Available at:
<https://www.usenix.org/conference/usenixsecurity23/presentation/carlini>

Clark, S. and Lewandowsky, S. (2026) 'The continued influence of AI-generated
deepfake videos despite transparency warnings', *Communications Psychology*, 4,
article 13. Available at: <https://doi.org/10.1038/s44271-025-00381-9>

Dan, V. (2026) 'Deepfakes as a democratic threat: Experimental evidence shows
noxious effects that are reducible through journalistic fact checks', *The
International Journal of Press/Politics*, 31(3), pp. 525–550. Available at:
<https://doi.org/10.1177/19401612251317766>

Hameleers, M., van der Meer, T.G.L.A. and Dobber, T. (2024) 'Distorting the
truth versus blatant lies: The effects of different degrees of deception in
domestic and foreign political deepfakes', *Computers in Human Behavior*, 152,
article 108096. Available at: <https://doi.org/10.1016/j.chb.2023.108096>

Łabuz, M. and Nehring, C. (2024) 'On the way to deep fake democracy? Deep fakes
in election campaigns in 2023', *European Political Science*, 23(4), pp.
454–473. Available at: <https://doi.org/10.1057/s41304-024-00482-9>

Longpre, S., Mahari, R., Chen, A., Obeng-Marnu, N., Sileo, D., Brannon, W.,
Muennighoff, N., Khazam, N., Kabbara, J., Perisetla, K., Wu, X., Shippole, E.,
Bollacker, K., Wu, T., Villa, L., Pentland, S. and Hooker, S. (2024) 'A
large-scale audit of dataset licensing and attribution in AI', *Nature Machine
Intelligence*, 6, pp. 975–987. Available at:
<https://doi.org/10.1038/s42256-024-00878-8>

Romero Moreno, F. (2024) 'Generative AI and deepfakes: a human rights approach
to tackling harmful content', *International Review of Law, Computers &
Technology*, 38(3), pp. 297–326.

</div>

</div>

### Part 2 — My responses to peers

I responded to one other initial post, on Sunday, 4 October 2026 — nine days
before I wrote my summary post. The response is reproduced verbatim; the
summary of the peer's own post is my précis of it.

#### Response to Isaac S. — content, source and accountability

**His initial post.** Isaac argued that the core problem with generative AI is
not that it produces convincing content, but that it weakens the link between
content, its source and responsibility for its consequences. He traced three
concerns across the system lifecycle:

- **Training data.** Use of copyright-protected material is legally uncertain,
  and opaque training datasets make accountability hard (Pasetti et al., 2025).
  Creators can contribute to a model's capability without knowing, being
  credited or being paid.
- **Bias.** Models can reproduce and amplify inequality in their training data
  (Hagendorff, 2024; Afreen, Mohaghegh and Doborjeh, 2025), so technical
  performance alone is not an adequate evaluation.
- **Epistemic trust.** Political deepfakes using advanced text-to-speech were
  harder to tell from authentic material than voice-actor versions (Groh et al.,
  2024). Widespread synthetic content may make authenticity itself harder to
  establish.

He concluded that generative AI is not inherently unethical, and that data
governance, bias evaluation, human oversight, provenance and accountability
should be designed in rather than added after harm occurs.

**My response**

<p class="post-meta">Posted Sunday, 4 October 2026 · 217 words excluding the salutation and references</p>

<div class="post" markdown="1">

Hi Isaac,

Your post has provided a thoughtful analysis of the ethical concerns intrinsic
to generative AI content. Identifying the weakening connection between content,
its original source and accountability is the core idea that anchors your
argument. Addressing these ethical concerns across the full lifecycle of deep
learning, starting from data training governance to post-deployment output,
provides a clear framework to mitigate these risks. Additionally, your use of
the note from Groh et al. (2024) effectively underscores the threats posed by
synthetic media to trust and authenticity.

Although I strongly agree that safeguards must be embedded in the system
architecture rather than added as a post-hoc precaution, your argument could be
strengthened by exploring the technical challenges and trade-offs that
complicate proactive provenance mechanisms.

In order to address these challenges, Kirchenbauer et al. (2023) proposed a
token-level watermarking algorithm that embeds detectable signatures by softly
biasing token selection. Conversely, Cao (2025) highlights that practical
watermarking schemes face critical trade-offs. Specifically, balancing token
imperceptibility, computational latency, and resilience against adversarial
paraphrasing or removal remains a major engineering hurdle. Consequently,
embedding provenance into high-throughput or open-weight models introduces
technical constraints that policy frameworks alone cannot solve.

Overall, your analysis makes a powerful case for aligning technical architecture
with ethical responsibility, framing accountability as an essential engineering
requirement rather than an afterthought.

**References**

<div class="references" markdown="1">

Cao, L. (2025) 'Watermarking for AI content detection: A review on text, visual,
and audio modalities', *arXiv*, article arXiv:2504.03765. Available at:
<https://doi.org/10.48550/arxiv.2504.03765> (Accessed: 4 October 2026).

Kirchenbauer, J., Geiping, J., Wen, Y., Katz, J., Miers, I. and Goldstein, T.
(2023) 'A watermark for large language models', *Proceedings of the 40th
International Conference on Machine Learning*, PMLR 202, pp. 17061-17084.
Available at: <https://doi.org/10.48550/arxiv.2301.10226> (Accessed: 4 October
2026).

</div>

</div>

**What happened next.** Yasmin A. also responded to Isaac's post, on 6 October 2026. She
proposed dataset records with consent and opt-out, bias testing across the
lifecycle by diverse teams, and provenance metadata combined with media
literacy. She also asked who is responsible when safeguards fail. Isaac's
summary post (11 October 2026) took up my point directly. He agreed that
watermarking must balance imperceptibility, latency and resistance to
paraphrasing, and added a point I had not made. Generation-time watermarking
depends on the provider implementing it, so the *presence* of a watermark can
show text was generated, but its *absence* cannot prove human authorship.

**What I learned**

- Agreeing with a post and then naming the engineering cost of its proposal
  moved the thread more than agreement alone. Isaac's summary built a paragraph
  on it.
- Watermarking is evidence in one direction only. It can confirm machine
  generation but cannot confirm human authorship, and open-weight models can
  leave it out entirely. That is why my own summary post argues for layered
  measures rather than any single provenance control.
- Isaac and Yasmin both ended on accountability. Assigning responsibility to
  developers and deploying organisations is a design decision, made before
  deployment, not something to settle after an incident.

### Referencing corrections

As in Discussion 1, the posts are left verbatim and corrected here. In my
initial post, the two entries are in a library-catalogue style rather than UoE
Harvard: no quotation marks, an "[Online]" tag and no DOI. In my response to
Isaac, the Kirchenbauer *et al.* (2023) entry cites the ICML proceedings but
links the arXiv preprint. The corrected entries:

<div class="references" markdown="1">

Buick, A. (2025) ‘Copyright and AI training data—transparency to the rescue?’,
*Journal of Intellectual Property Law & Practice*, 20(3), pp. 182–192. Available
at: <https://doi.org/10.1093/jiplp/jpae102> (Accessed: 15 October 2026).

Kirchenbauer, J., Geiping, J., Wen, Y., Katz, J., Miers, I. and Goldstein, T.
(2023) ‘A watermark for large language models’, in *Proceedings of the 40th
International Conference on Machine Learning (ICML 2023)*. Honolulu: PMLR 202,
pp. 17061–17084. Available at:
<https://proceedings.mlr.press/v202/kirchenbauer23a.html> (Accessed: 15 October
2026).

Romero Moreno, F. (2024) ‘Generative AI and deepfakes: a human rights approach
to tackling harmful content’, *International Review of Law, Computers &
Technology*, 38(3), pp. 297–326. Available at:
<https://doi.org/10.1080/13600869.2024.2324540> (Accessed: 15 October 2026).

</div>
