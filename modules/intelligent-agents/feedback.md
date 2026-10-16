---
title: Feedback
module: intelligent-agents
nav_order: 6
permalink: /modules/intelligent-agents/feedback/
summary: >-
  Feedback received from tutors and peers during the module, and what I changed
  as a result.
---

Each point is recorded with what changed as a result.

## Feedback log

<div class="wide" markdown="1">

| # | From | On | Feedback | My response to the design | Later, in the implementation |
| --- | --- | --- | --- | --- | --- |
| 1 | Tutor | [Team design proposal](../artefacts/#scholarplan--team-design-proposal) | No static structural view; add a UML class diagram of the main data structures, the agents and the blackboard | Agreed. The design shows behaviour but not structure, and does not draw the blackboard tables or which agent may write which | Done on 14 October 2026: a [class diagram, an ERD and an agent-to-table map](../artefacts/#structure-classes-and-blackboard-tables) |
| 2 | Tutor | Team design proposal | Evaluation criteria too broad; set measurable targets for test queries, deduplication thresholds, and Critic precision and recall | Agreed. §4 names an evaluation harness and its metrics but sets no numbers | Most targets were set; Critic precision and recall, and a target for paper recall, were not |
| 3 | Tutor | Team design proposal | No fallback for repeated conflicts or repeated Critic rejection; for example, cap each subtask at three re-planning attempts | Agreed. The design relies on the 20-step budget for the whole run | Repeated queries are refused, but there is still no per-subtask cap |

</div>

Verbatim feedback and my full response: [evidence appendix](../evidence/tutor-feedback/).

<div class="todo" markdown="1">
Add the tutor feedback on the individual project presentation, and on the
informal e-Portfolio review offered in the last unit of the module, in the same
format.
</div>

## Patterns

Points 2 and 3 ask for a checkable rule in place of an intention. The same gap
appears elsewhere:

| Where | The intention | The checkable rule it needed |
| --- | --- | --- |
| Tutor point 2 | "Evaluation criteria" | Numeric targets, including Critic precision and recall |
| Tutor point 3 | "Re-planning" | A cap of three attempts per subtask |
| [Discussion 3](../discussions/#discussion-3--deep-learning-and-the-ethics-of-generative-ai) | "Clear guidelines and careful oversight" | Safeguards at data collection, evaluation and distribution, supplied by a peer |
| [Team minutes](../team/#what-worked-and-what-did-not) | A record of what was discussed | Decision, owner and due date |

This is objective 1 in my [PDP](../skills/#action-plan).
