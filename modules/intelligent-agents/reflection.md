---
title: Reflective Piece
short_title: Reflection
module: intelligent-agents
nav_order: 7
permalink: /modules/intelligent-agents/reflection/
summary: >-
  The module as a whole. Evidences LO1–LO4.
---

This reflection follows Rolfe, Freshwater and Jasper's (2001) framework: what
happened, what it means, and what I will do differently.

## What?

During this module I went through a journey of new experiences, starting with
the team project, continuing through the formative activities and ending with
my individual implementation. It exposed me to areas I had not worked in before
and changed much of what I thought I knew. I came to it as a software engineer
who assumed that a large language model's (LLM's) behaviour could be controlled
through its settings. The units and discussions first made me question that
assumption, and the individual project finally overturned it.

**The team project.** Our team designed ScholarPlan, a multi-agent research
assistant. I drafted the team contract and arranged our four meetings. I
contributed to the high-level design and system requirements with my team
members. I also led the system's dynamics: I argued for specialised agents rather than
one program, designed how the LLM would break goals into subtasks and recover
when one failed, and drew the blackboard interaction flows
([team project](../team-project/#my-contribution)).

**The units and formative activities** gave me the vocabulary: logic-based
agents, deliberative and reactive architectures, an agent dialogue in KQML and
constituency parse trees. In the first discussion, I argued that LLM
agents trade reliability for adaptability, and peers pushed me further: their
autonomy must be bounded.

**The individual project.** Finally, I implemented the design on my own: five
agents coordinating through a shared blackboard, with a different model checking every
claim. The assumption broke early. The design relied on low-temperature sampling
to limit non-determinism, but GPT-5-mini on Azure rejected any temperature
except its default. The Critic changed too. The design used MiniCheck as the
yardstick for testing it, and MiniCheck scored higher than Llama on a
fact-checking benchmark, so I considered making it the Critic. But it answers
only yes or no, and the Planner re-plans from the Critic's written reason. Llama
stayed the Critic, and MiniCheck became a second opinion. Later, every evaluation
run finished, yet recall of well-known papers swung between 20% and 55%.

## So what?

**Feelings.** The temperature failure hit hardest. It was my own design
assumption, and I had presented it confidently. For a day I treated it as a
configuration problem to work around. That was the mistake: it was a design
problem. Looking back, my confidence came from reading about LLMs rather than
from running them.

**Knowledge.** Without that setting, I had to move control into the
architecture: strict JSON schemas limiting the Planner to three actions, an
independent Critic and a bounded loop. This is the LLM-Modulo argument: LLMs can
generate plans but should not be trusted to verify them (Kambhampati *et al.*,
2024). Before, I had cited it. Now I needed it. Non-determinism did not
disappear. It moved into the Planner's choice of queries, where I was not
measuring it ([project evaluation](../evaluation/)).

The units and activities turned out to be foundations. The KQML exercise showed
that a message means something only against a shared ontology, and the blackboard
schema plays that role. The deliberative–reactive distinction became the design itself: only
the Planner deliberates. Giving verification to a different model family, and
making the Planner answer its written feedback (Shinn *et al.*, 2023), was the
decision that most improved ScholarPlan. It is a technical version of separation
of duties. The MiniCheck decision sharpened this: I gave up a higher benchmark
score because the Planner needed a reason to act on, not just a verdict. An
explanation can be a functional requirement, not a courtesy to the user.

**Ethics.** I had expected ethical risk to sit in the language model. Writing the
case studies showed me it sat in my own design choices. To lift recall, I added a
citation bonus to the ranking, which rewards papers that are already popular, a
form of popularity bias (Mehrabi *et al.*, 2021). A review could pass 99% of
claim checks and still be skewed, because the Critic checks support, not
balance. Every ranking rule was an ethical decision I had made as a technical
one.

**Teamwork.** My software engineering background is why I pushed for clear task
boundaries from the first meeting. It paid off: each area had one owner, so we worked in parallel, and when one of
our four members stopped responding, their task could be reassigned without
reworking the rest. A loosely coupled team, like a blackboard system (Wooldridge, 2009), survives the failure of one part. I
had seen modularity as a software quality, but I now see it as risk management for
teams too.

**Others' views.** The tutor asked for
measurable evaluation targets and a three-attempt cap per subtask. In the third
discussion, a peer turned my "careful oversight" into specific safeguards, and
another showed that I had overstated my evidence on deepfakes. The pattern was
uncomfortable but clear: I tend to state an intention where a checkable rule is
needed. I set a numeric target for the Critic, which passed, and none for recall,
which was hard. It was the most useful thing I learned about myself.

## Now what?

Five changes follow.

1. **At work**, when I design LLM systems, I will split tasks across specialised
   agents instead of one large prompt, with a verifier from a different model
   family and shared state visible to all.
2. **Before a design is signed off**, I will run a short feasibility test of
   deployment constraints such as quotas, memory and supported parameters. Three
   of ScholarPlan's six design changes came from resources nobody had checked.
3. **I will turn intentions into checkable rules**: numeric targets set before
   tuning, and a test that triggers every safety rule.
4. **I will report what an agent retrieves**, such as the years and venues of
   its sources, and record ranking rules as design decisions with ethical
   weight.
5. **In teams**, I will keep agreeing owners and check-ins at the first meeting,
   and raise a participation risk at the first missed check-in, not at the
   deadline.

## References

<div class="references" markdown="1">

Kambhampati, S., Valmeekam, K., Guan, L., Verma, M., Stechly, K., Bhambri, S.,
Saldyt, L. and Murthy, A. (2024) ‘Position: LLMs can’t plan, but can help
planning in LLM-Modulo frameworks’, in *Proceedings of the 41st International
Conference on Machine Learning (ICML 2024)*. Vienna: PMLR 235. Available at:
<https://arxiv.org/abs/2402.01817> (Accessed: 2 September 2026).


Mehrabi, N., Morstatter, F., Saxena, N., Lerman, K. and Galstyan, A. (2021) ‘A
survey on bias and fairness in machine learning’, *ACM Computing Surveys*,
54(6), Article 115, pp. 1–35. Available at: <https://doi.org/10.1145/3457607>
(Accessed: 15 October 2026).

Rolfe, G., Freshwater, D. and Jasper, M. (2001) *Critical reflection in nursing
and the helping professions: a user’s guide*. Basingstoke: Palgrave Macmillan.

Shinn, N., Cassano, F., Gopinath, A., Narasimhan, K. and Yao, S. (2023)
‘Reflexion: Language agents with verbal reinforcement learning’, in *Advances in
Neural Information Processing Systems 36 (NeurIPS 2023)*. Available at:
<https://arxiv.org/abs/2303.11366> (Accessed: 2 September 2026).

Wooldridge, M. (2009) *An Introduction to MultiAgent Systems*. 2nd edn.
Chichester: John Wiley & Sons.

</div>
