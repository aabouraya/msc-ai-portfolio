---
title: Reflective Case Studies
short_title: Case studies
module: intelligent-agents
nav_order: 6
permalink: /modules/intelligent-agents/case-studies/
summary: >-
  Three incidents from building ScholarPlan, each in Rolfe et al.'s (2001) What,
  So what, Now what.
---

Evidence:
[development log](https://github.com/aabouraya/scholar_plan/blob/c66190e/docs/development_log.md)
and [test report](https://github.com/aabouraya/scholar_plan/blob/c66190e/docs/testing/test_report.md).

## 1. Explainable decisions: an explanation the system needed

**What.** I planned to use MiniCheck with Llama in the Critic, since MiniCheck
scores higher on the LLM-AggreFact benchmark (77.4 against 74.5). But MiniCheck
only answers yes or no, and the Planner needs a written reason to re-plan. So
Llama makes the Critic's decisions, and MiniCheck is used only for testing.

**So what.** The explanation's main reader is another agent: without a reason,
the re-planning loop has nothing to act on. I chose the lower-scoring model for
the decisions at no real cost, as both models agreed on every test claim. But a
stated reason may not be what caused a verdict (Turpin *et al.*, 2023), so the
trace linking each claim to its source matters more.

**Now what.** In future designs, I will decide early who reads each
explanation, and choose models that can provide it. I will also test that each
reason quotes text that really appears in the source, instead of trusting it.

## 2. AI safety constraints: bounds outside the model

**What.** Four rules bound the system: the Planner has three actions, repeated
searches are refused, a run stops after 20 steps, and unclear verdicts count as
rejections.

**So what.** The rules that worked were enforced in code, not requested in a
prompt, as LLM-Modulo argues (Kambhampati *et al.*, 2024). But the step budget
limits cost, not behaviour: every run finished in 3 steps, so only a test
exercised it. Rejecting unclear verdicts is safer but loses valid claims, the
safety–usefulness trade-off Amodei *et al.* (2016) describe.

**Now what.** Every safety rule will get a test that triggers it, and cost
limits will stay separate from behaviour limits.

## 3. Bias in autonomous decision-making: bias from retrieval

**What.** I tested ScholarPlan on four questions, each with five well-known
papers it should find. It found between 20% and 55% of them, a measure called
recall. The Planner searched differently each run, and the APIs ranked many
2026 papers above older landmark ones. My ranking already gave highly cited
papers a small boost, to favour influential work. When recall was low, I made
that boost apply to arXiv papers too.

**So what.** The recency skew came from the search, not the language model, yet
it decided whose work was included. The boost pushed the other way and brought
its own bias: favouring papers that are already popular is the Matthew effect
(Merton, 1968), a popularity bias (Mehrabi *et al.*, 2021). I had treated it as
a technical setting, not an ethical choice. The test was biased too: I chose
the five papers for each question myself, so recall measured how closely the
system matched my own view of which papers matter. And a review can pass 99% of
claim checks and still be one-sided, because the Critic checks that claims are
supported, not that sources are balanced.

**Now what.** I will make agents report their mix of sources, by year, venue
and citations, and treat ranking rules as ethical decisions.

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


Rolfe, G., Freshwater, D. and Jasper, M. (2001) *Critical reflection in nursing
and the helping professions: a user’s guide*. Basingstoke: Palgrave Macmillan.

Turpin, M., Michael, J., Perez, E. and Bowman, S.R. (2023) ‘Language models
don’t always say what they think: Unfaithful explanations in chain-of-thought
prompting’, in *Advances in Neural Information Processing Systems 36 (NeurIPS
2023)*. Available at: <https://arxiv.org/abs/2305.04388> (Accessed: 15 October
2026).

</div>
