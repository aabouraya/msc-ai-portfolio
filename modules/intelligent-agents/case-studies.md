---
title: Reflective Case Studies
short_title: Case studies
module: intelligent-agents
nav_order: 5
permalink: /modules/intelligent-agents/case-studies/
summary: >-
  Three short reflective case studies, each grounded in a decision or incident
  from building ScholarPlan, structured with Rolfe et al.'s (2001) What, So what,
  Now what.
---

<p class="meta"><span class="muted">Evidences LO2, LO3</span></p>

Each case study uses Rolfe, Freshwater and Jasper's (2001) framework: **What**
happened, **So what** it means, and **Now what** I will do differently. The
evidence for each is in the ScholarPlan
[development log](https://github.com/aabouraya/scholar_plan/blob/c66190e/docs/development_log.md),
[remediation log](https://github.com/aabouraya/scholar_plan/blob/c66190e/docs/remediation_log.md)
and [test report](https://github.com/aabouraya/scholar_plan/blob/c66190e/docs/testing/test_report.md).

## Case study 1 — Explainable decisions: an explanation the system needed

**What.** In iteration 4 I considered making MiniCheck the Critic, since it
scores higher than Llama on the LLM-AggreFact benchmark (77.4 against 74.5). I
kept Llama because MiniCheck only answers yes or no. The Planner re-plans from
the Critic's written reason, so without a reason the feedback loop has nothing
to act on. MiniCheck became a second opinion instead.

**So what.** In ScholarPlan, explanation is functional, not cosmetic: the main
reader of the Critic's explanation is another agent. Its reasons are contrastive
("the claim says *eliminates*; the source says *reduces*"), which Miller (2019)
identifies as the form of explanation people find most useful. I traded some
accuracy for explainability, a trade-off I had only read about before. The
reasons may not be faithful, though. A model's stated reason need not be what
caused its verdict (Turpin *et al.*, 2023). The stronger explainability is the
trace, which links every claim to the source it came from. A reader can check
it rather than trust it.

**Now what.** I will ask "who uses this explanation?" as a design requirement. I
will prefer provenance a reader can verify over plausible narrative reasons. I
will also test whether a rejection reason points to real text in the source.

## Case study 2 — AI safety constraints: bounds outside the model

**What.** ScholarPlan's autonomy is bounded in several ways:

- a strict schema allows only three Planner actions;
- repeated searches are refused;
- runs stop after 20 steps;
- costs are tracked;
- unclear Critic verdicts fail closed.

The tutor pointed out that a subtask the Critic keeps rejecting could still use
up the whole budget. I agreed, but did not build the per-subtask cap.

**So what.** The constraints that worked were enforced by code, not requested in
a prompt. The schema makes inventing an action impossible rather than
discouraged, which is the LLM-Modulo position (Kambhampati *et al.*, 2024). But
the 20-step budget bounds cost, not behaviour, and every evaluation run stopped
at step 3. The real kill switch was only exercised by a forced-rejection test.
Failing closed also has a price: each false rejection reduces coverage. This is
the tension between safety and usefulness that Amodei *et al.* (2016) describe.
Leaving the cap unbuilt was a prioritisation choice I made under deadline
pressure, and it is the gap a reviewer would find first.

**Now what.** I will write every safety rule as a testable invariant with a test
that triggers it, as I did for repeated searches. I will keep resource bounds
separate from behaviour bounds in future designs.

## Case study 3 — Bias in autonomous decision-making: bias from retrieval

**What.** Recall of well-known papers swung between 20% and 55%. For one question
it fell from 5 of 5 to 1 of 5. The APIs now rank many 2026 papers above older
landmark ones, and the Planner chooses different queries each run. To
compensate, I had added a citation bonus to the Processor's ranking.

**So what.** The bias came from retrieval and ranking, not from the language
model, and it decides whose work gets seen. My fix brought in the opposite bias.
Rewarding papers that are already cited is the Matthew effect (Merton, 1968), a
form of popularity bias in Mehrabi *et al.*'s (2021) terms. My evaluation was
biased too, because the "well-known papers" were my own choice of canon. Most
importantly, a review can pass 99% of claim checks and still be skewed. The
Critic checks support, not balance, so this bias passes the safety gate unseen.

**Now what.** I will measure what an agent retrieves (year, venue, citations),
not only its recall. I will report the source mix in the output itself, and
record ranking rules as design decisions with ethical weight.

## References

<div class="references" markdown="1">

Amodei, D., Olah, C., Steinhardt, J., Christiano, P., Schulman, J. and Mané, D.
(2016) ‘Concrete problems in AI safety’, *arXiv preprint* arXiv:1606.06565.
Available at: <https://arxiv.org/abs/1606.06565> (Accessed: 15 October 2026).

Kambhampati, S., Valmeekam, K., Guan, L., Verma, M., Stechly, K., Bhambri, S.,
Saldyt, L. and Murthy, A. (2024) ‘Position: LLMs can’t plan, but can help
planning in LLM-Modulo frameworks’, in *Proceedings of the 41st International
Conference on Machine Learning (ICML 2024)*. Vienna: PMLR 235. Available at:
<https://arxiv.org/abs/2402.01817> (Accessed: 2 September 2026).

Mehrabi, N., Morstatter, F., Saxena, N., Lerman, K. and Galstyan, A. (2021) ‘A
survey on bias and fairness in machine learning’, *ACM Computing Surveys*,
54(6), Article 115, pp. 1–35. Available at: <https://doi.org/10.1145/3457607>
(Accessed: 15 October 2026).

Merton, R.K. (1968) ‘The Matthew effect in science’, *Science*, 159(3810),
pp. 56–63. Available at: <https://doi.org/10.1126/science.159.3810.56>
(Accessed: 15 October 2026).

Miller, T. (2019) ‘Explanation in artificial intelligence: Insights from the
social sciences’, *Artificial Intelligence*, 267, pp. 1–38. Available at:
<https://doi.org/10.1016/j.artint.2018.07.007> (Accessed: 15 October 2026).

Rolfe, G., Freshwater, D. and Jasper, M. (2001) *Critical reflection in nursing
and the helping professions: a user’s guide*. Basingstoke: Palgrave Macmillan.

Turpin, M., Michael, J., Perez, E. and Bowman, S.R. (2023) ‘Language models
don’t always say what they think: Unfaithful explanations in chain-of-thought
prompting’, in *Advances in Neural Information Processing Systems 36 (NeurIPS
2023)*. Available at: <https://arxiv.org/abs/2305.04388> (Accessed: 15 October
2026).

</div>
