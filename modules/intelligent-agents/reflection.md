---
title: Reflective Piece
short_title: Reflection
module: intelligent-agents
nav_order: 6
permalink: /modules/intelligent-agents/reflection/
summary: >-
  Reflection on the module as a whole, covering all four learning outcomes,
  structured with Rolfe et al.'s (2001) What, So what, Now what.
---

<p class="meta"><span class="muted">Evidences LO1, LO2, LO3, LO4</span></p>

This reflection follows Rolfe, Freshwater and Jasper's (2001) framework: what
happened, what it means, and what I will do differently.

## What?

I started the module assuming that a capable large language model (LLM) could
plan a multi-step task and check its own output. I tested that assumption twice:
first as one of three active members of a team designing ScholarPlan, a
multi-agent research assistant, and then alone, building and evaluating it.

In the team, my contribution was the system's dynamics rather than its
structure. I defined the agent roles and argued for a multi-agent design. I
worked out how the LLM would break goals into subtasks and what would happen
when one failed. I drew the blackboard interaction flows, and I wrote the
minutes for all four meetings ([team page](../team/#my-contribution)). Two
incidents shaped my learning most.

The first came in the team phase. One of our four members signed the team
contract last, attended no meetings and missed an internal deadline without
notice. The other three of us redistributed the work and submitted on time. The
member reappeared after the project was finished, saying they had done work that
another of us had already completed.

The second came in the build. Our design relied on low-temperature sampling to
control non-determinism. When I connected GPT-5-mini through Azure, it rejected
any temperature except its default. One of the design's main mitigations was
gone in an afternoon.

## So what?

**Feelings.** The team incident frustrated me and made me briefly anxious about
the deadline. I noticed that frustration pushed me towards taking the work on
myself rather than sharing it. My two active teammates stepped up, and sharing
the load produced better work than one person rushing would have. I do not know
the absent member's circumstances, and I tried to keep my response factual.

The temperature incident felt worse at first. It was my own design assumption
that failed, and I had presented it confidently. For a day I treated it as a
configuration problem to work around. That was the mistake: it was a design
problem.

**Analysis.** The temperature failure changed how I understood non-determinism.
I had treated it as a model setting to tune. Without that setting, I had to move
control into the architecture:

- strict JSON schemas that limit the Planner to three actions;
- an independent Critic;
- a bounded loop.

This is the LLM-Modulo argument: LLMs can generate plans but should not be
trusted to verify them (Kambhampati *et al.*, 2024). Before, I had cited it; now
I needed it. It also explained my later evaluation. Recall of well-known papers
swung between 20% and 55% because the Planner chose different queries each run
([project evaluation](../evaluation/)). Non-determinism did not disappear; it
moved to where I was not measuring it.

The same incident showed me the risk of relying on a single model. A model that
plans, writes and checks its own claims has one set of blind spots. Giving
verification to a different model family, and making the Planner answer its
written feedback (Shinn *et al.*, 2023), was the decision that most improved
ScholarPlan. It is a technical version of separation of duties.

The team incident taught the same lesson at another level. Our design split the
system into agents with clear responsibilities. Because of that, the missing
member's task had clear boundaries and could be reassigned without reworking the
rest. A loosely coupled team, like a blackboard system (Wooldridge, 2009), can
survive the failure of one part. My background in software engineering design is
why I pushed for clear task boundaries from the first meeting. I had seen
modularity as a software quality; I now see it as risk management for teams too.

Research on social loafing suggests that shared, unclear responsibility invites
withdrawal (Latané, Williams and Harkins, 1979). Our team contract, with named
owners for each section, limited the damage. My own part was weaker. My minutes
recorded discussion rather than decisions and owners, and they were written late
([team page](../team/#team-records)). So the gap was noticed at
the deadline rather than earlier.

**Feedback.** Feedback changed how I saw my own work. The tutor asked for
measurable evaluation targets and a three-attempt cap per subtask. In Discussion
3, a peer turned my "careful oversight" into specific safeguards. Together with
my minutes, the pattern was uncomfortable but clear: I tend to state an
intention where a checkable rule is needed. I set a numeric target for the
Critic, which passed, and none for recall, which was hard. Recognising this was
the most useful thing I learned about myself in this module.

## Now what?

Four changes follow.

1. **At work**, when I design LLM systems, I will split tasks across specialised
   agents instead of one large prompt. Each agent will have a single
   responsibility, the verifier will come from a different model family, and
   shared state will be visible to every agent. ScholarPlan's controller showed
   that this also makes a system easier to test and extend.
2. **Before a design is signed off**, I will run a short feasibility test of
   deployment constraints such as quotas, memory and supported parameters. Three
   of ScholarPlan's six design changes came from resources nobody had checked.
3. **I will turn intentions into checkable rules**: numeric targets set before
   tuning, and a test that triggers every safety rule.
4. **In teams**, I will raise a participation risk at the first missed check-in,
   not at the deadline. I will write minutes as decision, owner and due date
   within a day of each meeting. I also want to handle late disagreements more
   formally and calmly.

## References

<div class="references" markdown="1">

Kambhampati, S., Valmeekam, K., Guan, L., Verma, M., Stechly, K., Bhambri, S.,
Saldyt, L. and Murthy, A. (2024) ‘Position: LLMs can’t plan, but can help
planning in LLM-Modulo frameworks’, in *Proceedings of the 41st International
Conference on Machine Learning (ICML 2024)*. Vienna: PMLR 235. Available at:
<https://arxiv.org/abs/2402.01817> (Accessed: 2 September 2026).

Latané, B., Williams, K. and Harkins, S. (1979) ‘Many hands make light the work:
The causes and consequences of social loafing’, *Journal of Personality and
Social Psychology*, 37(6), pp. 822–832. Available at:
<https://doi.org/10.1037/0022-3514.37.6.822> (Accessed: 15 October 2026).

Rolfe, G., Freshwater, D. and Jasper, M. (2001) *Critical reflection in nursing
and the helping professions: a user’s guide*. Basingstoke: Palgrave Macmillan.

Shinn, N., Cassano, F., Gopinath, A., Narasimhan, K. and Yao, S. (2023)
‘Reflexion: Language agents with verbal reinforcement learning’, in *Advances in
Neural Information Processing Systems 36 (NeurIPS 2023)*. Available at:
<https://arxiv.org/abs/2303.11366> (Accessed: 2 September 2026).

Wooldridge, M. (2009) *An Introduction to MultiAgent Systems*. 2nd edn.
Chichester: John Wiley & Sons.

</div>
