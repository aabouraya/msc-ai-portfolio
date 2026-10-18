---
title: Reflective Case Studies
short_title: Case studies
module: intelligent-agents
nav_order: 6
permalink: /modules/intelligent-agents/case-studies/
summary: >-
  Three incidents from building ScholarPlan, each in Rolfe et al.'s (2001) What,
  So what, Now what. Evidences LO2 and LO3.
---

Evidence:
[development log](https://github.com/aabouraya/scholar_plan/blob/c66190e/docs/development_log.md)
and [test report](https://github.com/aabouraya/scholar_plan/blob/c66190e/docs/testing/test_report.md).

## 1. Explainable decisions: an explanation the system needed

**What.** MiniCheck outscores Llama on LLM-AggreFact (77.4 against 74.5), but
I kept Llama as the Critic: MiniCheck answers only yes or no, and the Planner
re-plans from the Critic's written reason.

**So what.** The explanation's main reader is another agent, so it is
functional. Its reasons are contrastive ("the claim says *eliminates*; the
source says *reduces*"), the form Miller (2019) finds most useful. I traded
accuracy for explainability. Yet a stated reason may not be what caused the
verdict (Turpin *et al.*, 2023); the trace linking each claim to its source can
be checked rather than trusted.

**Now what.** I will treat "who uses this explanation?" as a requirement, and
test that reasons point to real source text.

## 2. AI safety constraints: bounds outside the model

**What.** Autonomy is bounded by a three-action schema, refused repeat
searches, a 20-step budget and verdicts that fail closed. The tutor noted that
repeated rejection could still exhaust the budget. I agreed, but did not build
a per-subtask cap.

**So what.** The bounds that worked were enforced in code, not requested in a
prompt, as LLM-Modulo argues (Kambhampati *et al.*, 2024). But the budget bounds
cost, not behaviour: every run stopped at step 3, so only a forced test
exercised it. Failing closed also costs coverage, the safety–usefulness tension
Amodei *et al.* (2016) describe. Skipping the cap under deadline pressure was a
mistake.

**Now what.** Every safety rule will be an invariant with a test that triggers
it, and resource bounds will be separate from behaviour bounds.

## 3. Bias in autonomous decision-making: bias from retrieval

**What.** Recall of well-known papers swung between 20% and 55%, because the
APIs rank recent papers above landmark ones. I added a citation bonus to
compensate.

**So what.** The bias came from retrieval, not the model, and decides whose
work is seen. My fix added the opposite bias: rewarding cited papers is the
Matthew effect (Merton, 1968), a popularity bias (Mehrabi *et al.*, 2021). Even
my "well-known papers" were my own canon. A review can pass 99% of claim checks
and still be skewed, because the Critic checks support, not balance.

**Now what.** I will measure and report the mix an agent retrieves (year,
venue, citations), and treat ranking rules as ethical decisions.

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
