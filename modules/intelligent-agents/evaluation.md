---
title: Final Project Evaluation
short_title: Project evaluation
module: intelligent-agents
nav_order: 4
permalink: /modules/intelligent-agents/evaluation/
summary: >-
  A critical evaluation of ScholarPlan across both phases: the team design
  (week 7) and my implementation (week 11).
---

<p class="meta"><span class="muted">Evidences LO1, LO2, LO3</span></p>

This page judges the [team design proposal](../artefacts/#scholarplan--team-design-proposal)
against what my [implementation](../artefacts/#agent-based-system) showed when it
was built and tested.

## What the design got right

**The architecture held.** The hybrid structure (a deliberative ReAct Planner,
reactive specialists and a shared blackboard) was built as designed and never
needed restructuring. Because the controller only asks "who can act?", agents
never call each other. Adding MiniCheck as a second checker and adding offline
search touched no other agent. This is the decoupling Hayes-Roth (1985) claims
for blackboard systems, and it was what made four short iterations practical.

**The independent Critic was the most valuable decision.** Checking claims with
a different model family from the one that wrote them gave 13 of 13 correct
verdicts on labelled claims and full agreement with MiniCheck on 192 claims. In
one live run it also rejected a weak synthesis, which the Planner then redrafted.

## Where the design did not hold

Six design decisions changed during the build
([changes from the design](../artefacts/#what-changed-from-the-design)). Three of
them were forced by the environment rather than chosen. The local Llama Critic
needed about 40 GB of memory on a 32 GB laptop, GPT-5-nano had no quota, and
GPT-5-mini would not accept a low temperature. The design assumed resources that
nobody had checked. A one-day feasibility test before design sign-off would have
found all three. Deployment constraints shape the architecture, so they belong
in the design, not after it.

## Weaknesses in my implementation

1. **The evaluation cannot support the claim I most wanted to make.** Recall of
   well-known papers was 25%, 55%, 50% and 20% across four runs, with one run per
   setting, so I was tuning against noise. The tutor's second improvement point
   asked for measurable targets. I set one for the Critic, which passed, and none
   for recall, which was hard. That is a bias in how I evaluated my own work.
2. **The guarantee is narrower than the presentation implied.** "Every claim is
   verified" means verified against an abstract. The Critic checks support, not
   coverage, so a fully verified review can still miss the key papers.
3. **Control still partly depends on the LLM.** The proposal argued, after
   Kambhampati *et al.* (2024), that control should sit outside the model. Yet
   deciding to give up on a subtask is still left to the Planner. The tutor's
   per-subtask cap, which I agreed with, was not built.
4. **Rejections were barely tested.** Only one real claim was rejected, so the
   Critic's ability to catch errors rests on 13 labelled cases.

## Overall judgement

The architecture and the engineering process succeeded. Four gated iterations
and test-first fixes for eleven recorded issues produced a system that finished
every evaluation run for about $0.03. The evaluation method is the weakest part.
If I built it again, I would:

- set a recall target before tuning, not after;
- run each question several times and report the spread;
- add the three-attempt cap per subtask;
- build the 50-claim labelled set the design promised, with more false claims.

## References

<div class="references" markdown="1">

Hayes-Roth, B. (1985) ‘A blackboard architecture for control’, *Artificial
Intelligence*, 26(3), pp. 251–321. Available at:
<https://doi.org/10.1016/0004-3702(85)90063-3> (Accessed: 2 September 2026).

Kambhampati, S., Valmeekam, K., Guan, L., Verma, M., Stechly, K., Bhambri, S.,
Saldyt, L. and Murthy, A. (2024) ‘Position: LLMs can’t plan, but can help
planning in LLM-Modulo frameworks’, in *Proceedings of the 41st International
Conference on Machine Learning (ICML 2024)*. Vienna: PMLR 235. Available at:
<https://arxiv.org/abs/2402.01817> (Accessed: 2 September 2026).

</div>
