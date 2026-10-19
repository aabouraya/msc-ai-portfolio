---
title: "Final Project: ScholarPlan"
short_title: Final project
module: intelligent-agents
nav_order: 2
permalink: /modules/intelligent-agents/evaluation/
summary: >-
  My build of the team design (week 11), evaluated against that design
  (week 7).
---

## What was built

**Code:** [github.com/aabouraya/scholar_plan](https://github.com/aabouraya/scholar_plan/tree/c66190e),
as presented. **Presentation:**
[slides](https://docs.google.com/presentation/d/1cRRCG0g3pqrjCc7xxqDpI_tBM-J0sCwP/edit?usp=sharing),
demo on slide 6.

<figure>
  <a href="{{ '/assets/img/intelligent-agents/scholarplan-implementation.png' | relative_url }}"><img src="{{ '/assets/img/intelligent-agents/scholarplan-implementation.png' | relative_url }}" alt="Implementation architecture: a Controller above a shared SQLite blackboard. The deliberative Planner sits on one side; the reactive Retriever, Processor, Critic and Archivist on the other. Agents connect only to the blackboard."></a>
  <figcaption>Agents coordinate only through the blackboard.</figcaption>
</figure>

| Agent | Kind | Role |
| --- | --- | --- |
| Planner | Deliberative, GPT-5-mini | ReAct loop: `search`, `abandon` or `finish` |
| Retriever | Reactive | Searches arXiv, OpenAlex, Crossref |
| Processor | Reactive, GPT-5-mini | Ranks sources; summarises into claims |
| Critic | Reactive, Llama-3.3-70B | Checks claims against abstracts |
| Archivist | Reactive | Exports report, BibTeX, trace |

### Structure

<figure>
  <a href="{{ '/assets/img/intelligent-agents/scholarplan-class-diagram.png' | relative_url }}"><img src="{{ '/assets/img/intelligent-agents/scholarplan-class-diagram.png' | relative_url }}" alt="UML class diagram: the Planner, Retriever, Processor, Critic and Archivist classes implement an Agent protocol with can_act and act. The controller creates the Blackboard and asks who can act. Each agent reads and writes the Blackboard class, and uses supporting modules: llm, sources, citations, index, embeddings and http_cache."></a>
  <figcaption>Every agent implements one two-method protocol.</figcaption>
</figure>

<figure>
  <a href="{{ '/assets/img/intelligent-agents/scholarplan-erd.png' | relative_url }}"><img src="{{ '/assets/img/intelligent-agents/scholarplan-erd.png' | relative_url }}" alt="Entity-relationship diagram of the eight blackboard tables. A subtask finds many sources and groups many summaries; a source is summarised in many summaries; a summary contains many claims; feedback is about a subtask or a summary. The run, thoughts and synthesis tables stand alone."></a>
  <figcaption>Blackboard tables. A row's status triggers the next agent.</figcaption>
</figure>

### Results

[Test report](https://github.com/aabouraya/scholar_plan/blob/c66190e/docs/testing/test_report.md):

| Test | Result |
| --- | --- |
| Unit and component | 67 passed |
| Integration, live APIs | 3 passed |
| Critic, 13 hand-labelled claims | 13 correct |
| Critic against MiniCheck | Agreed on 192 claims |
| End to end, 4 questions | 4 finished; 99% of claims passed; $0.03 per run |

<figure>
  <a href="{{ '/assets/img/intelligent-agents/scholarplan-eval-run.png' | relative_url }}"><img src="{{ '/assets/img/intelligent-agents/scholarplan-eval-run.png' | relative_url }}" alt="Terminal output of the end-to-end evaluation on 4 questions, 3 October 2026: recall retrieved 20%, recall cited 15%, claim pass rate 99%, 3.0 steps, $0.030 per run."></a>
  <figcaption>Evaluation run, 3 October 2026.</figcaption>
</figure>

### Legal, ethical and professional practice

- **Provenance:** only verified claims reach the report, with sources.
- **Fair API use:** rate limits, retries and caching.
- **Secrets:** keys in a git-ignored `.env`.
- **Cost:** a step budget and cost tracking.

## What the design got right

**The architecture held.** The hybrid design was never restructured. Adding MiniCheck touched no
other agent: the decoupling Hayes-Roth (1985) claims for blackboards.

**The independent Critic was the best decision.** A different model family
from the writer produced the results above, and live it forced a redraft of a
weak synthesis.

## Where it did not hold

| Design | Built | Why |
| --- | --- | --- |
| Local Llama Critic | Azure only | Needs 40 GB; laptop has 32 |
| Low temperature | Strict JSON schemas | GPT-5-mini allows only its default |
| GPT-5-nano fallback | None | No quota |
| Full text | Abstracts | Full text often unavailable |
| 50 labelled claims | 13 | Time |
| MiniCheck with the Llama Critic | Testing only | Gives no reason to re-plan from |

Three changes came from resources nobody checked; a one-day feasibility test
would have found them. Of the tutor's improvement points, I added the class
diagram, set a Critic target but none for recall, and did not build the
three-attempt cap.

## Weaknesses

1. **The evaluation cannot support my main claim.** Recall was 25%, 55%, 50%
   and 20%, one run per setting, so I tuned against noise
   ([case study 3](../case-studies/)).
2. **"Every claim is verified"** means against an abstract, and checks support,
   not coverage.
3. **Rejections were barely tested:** only one real claim was rejected.

## Judgement

The engineering succeeded; the evaluation method is the weakest part. Next
time I would set a recall target before tuning, repeat each question, build the
cap and label 50 claims.

## References

<div class="references" markdown="1">

Hayes-Roth, B. (1985) ‘A blackboard architecture for control’, *Artificial
Intelligence*, 26(3), pp. 251–321. Available at:
<https://doi.org/10.1016/0004-3702(85)90063-3> (Accessed: 2 September 2026).


</div>
