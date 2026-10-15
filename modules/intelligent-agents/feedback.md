---
title: Feedback
module: intelligent-agents
nav_order: 6
permalink: /modules/intelligent-agents/feedback/
summary: >-
  Feedback received from tutors and peers during the module, and what I changed
  as a result.
---

Feedback is recorded with the response to it. A log of comments received is not
evidence on its own; the evidence is the change that followed.

## Feedback log

<div class="wide" markdown="1">

| # | From | On | Feedback | My response to the design | Later, in the implementation |
| --- | --- | --- | --- | --- | --- |
| 1 | Tutor | [Team design proposal](../artefacts/#scholarplan--team-design-proposal) | No static structural view; add a UML class diagram of the main data structures, the agents and the blackboard | Agreed. The design shows behaviour but not structure, and does not draw the blackboard tables or which agent may write which | Done on 14 October 2026: a [class diagram, an ERD and an agent-to-table map](../artefacts/#structure-classes-and-blackboard-tables) |
| 2 | Tutor | Team design proposal | Evaluation criteria too broad; set measurable targets for test queries, deduplication thresholds, and Critic precision and recall | Agreed. §4 names an evaluation harness and its metrics but sets no numbers | Most targets were set; Critic precision and recall, and a target for paper recall, were not |
| 3 | Tutor | Team design proposal | No fallback for repeated conflicts or repeated Critic rejection; for example, cap each subtask at three re-planning attempts | Agreed. The design relies on the 20-step budget for the whole run | Repeated queries are refused, but there is still no per-subtask cap |

</div>

## Formal feedback

### Team design proposal — tutor feedback

<p class="post-meta">Development Team Project: Project Report · team submission, September 2026</p>

The feedback is reproduced verbatim.

<div class="post" markdown="1">

**Knowledge and Understanding of the Topic/Issues Under Consideration (25%)**

The work demonstrates outstanding domain knowledge, with architectural choices
well supported by relevant academic literature. It shows a clear understanding
of LLM limitations, resulting in a thoughtful and professionally considered
system design.

**Application of Knowledge and Understanding (25%)**

Your group makes very effective use of specialised techniques to address
practical challenges such as API rate limits and non-deterministic model
behaviour. The use of a Critic verifier to check claims adds a robust and
practical approach to reducing LLM hallucinations.

**Criticality (25%)**

The report provides a strong critical evaluation of agent architectures and
orchestration frameworks, with clear justification to reduce unnecessary
abstraction. It also considers key trade-offs around cost, single points of
failure, and task decomposition, supported by practical mitigation strategies.

**Structure and Presentation (25%)**

The report is well structured and professionally presented, with clear UML
activity and sequence diagrams that improve readability. The writing is concise,
follows the assignment guidelines closely, and maintains a consistently strong
academic standard of presentation.

**What the team did well**

1. Your group has used a strong range of relevant literature to support your
   design choices. The links you make between the different agent and
   architectural approaches show a good understanding of the area.
2. The modular architecture is well thought out, and using SQLite3 as a shared
   blackboard makes the different agents and their interactions clear. The
   architecture, activity and sequence diagrams also do a good job of showing
   the main data flows and re-planning process.
3. Your team has considered several practical challenges, including execution
   limits, model selection, rate limits and cost. These are realistic
   considerations and show good awareness of what would be involved in
   implementing the system.

**Guidance for Improvement**

1. Your group included good behavioural and sequence diagrams, but a static
   structural view, such as a UML Class Diagram, is missing. Adding one would
   give a clearer picture of the main data structures and how they connect to
   the agents and SQLite blackboard.
2. Your team identified non-determinism as an important challenge, but the
   evaluation criteria are still quite broad. You should give clear, measurable
   targets, including the test queries, deduplication thresholds and specific
   targets for Critic precision and recall.
3. Your team has considered atomic transactions, but there is less discussion
   of what happens when agents repeatedly conflict or a Critic keeps rejecting
   the same result. Consider adding clear fallback rules, such as limiting each
   subtask to three re-planning attempts before marking it as unresolvable.

</div>

#### My response

The feedback is on the design document only. Below, each point is answered for
the design first. A short note then says where the point stands in the
[implementation](../artefacts/#agent-based-system), which was built afterwards
from this design.

**1. A static structural view.** I agree. The design has activity and sequence
diagrams, which show behaviour, but nothing shows structure: which data the
blackboard holds and which agent may read or write each part. That is the
permission model the proposal claims from Gaia (§4) but never draws, so a class
diagram would have made that claim checkable.

*In the implementation:* done on 14 October 2026. A UML class diagram and an
entity-relationship diagram of the eight blackboard tables were added to the
repository and checked against the code. The agent-to-table permissions, which
neither diagram shows, are traced in a table beside them. All three are under
[Structure: classes and blackboard tables](../artefacts/#structure-classes-and-blackboard-tables).

**2. Measurable evaluation targets.** I agree. §4 describes "an evaluation
harness of fixed research questions with known relevant sources, measuring
source recall and Critic pass rate". But it does not say which questions, what
recall would count as success, or how accurate the Critic must be. Without
numbers, any result could be reported as acceptable.

*In the implementation:* most targets were set.

- **Test queries:** 4 fixed questions with 5 known papers each.
- **Deduplication thresholds:** a 0.95 cosine near-duplicate threshold and a
  0.25 relevance floor.
- **Critic target:** at least 11 of 13 labelled claims correct, with a balanced
  accuracy of at least 0.70.

The Critic target is not split into precision and recall, though, and recall
of known papers had no target. That is the metric that later varied from 20% to
55%.

**3. Fallback rules for repeated rejection.** I agree. The design's only bound
is the 20-step budget for the whole run. A subtask the Critic keeps rejecting
can use up that budget, and the design leaves the decision to give up to the
Planner. That contradicts the proposal's own LLM-Modulo argument (§3) that
control should not depend on the LLM. The tutor's rule (three attempts, then
mark the subtask unresolvable) is simple, testable and outside the model.

*In the implementation:* partly addressed. The Planner is refused if it repeats
a query, and it can abandon a subtask, but there is still no per-subtask cap.

<div class="todo" markdown="1">
Add the tutor feedback on the individual project presentation, and on the
informal e-Portfolio review offered in the last unit of the module, in the same
format.
</div>

## Patterns

Two of the three improvement points (2 and 3) ask for the same thing: replace a stated
intention with a concrete, checkable rule. "Evaluation criteria" should be
numeric targets. "Re-planning" should have a cap. The same gap appears
elsewhere in the portfolio:

- My Discussion 3 post ended on "clear guidelines and careful oversight" until
  [a peer turned it into specific safeguards](../discussions/#peer-responses-to-my-post-and-what-i-learned-1).
- The [team minutes](../team/#what-worked-and-what-did-not) record what was
  discussed but not what was decided.

This is a development objective in its own right, and belongs in the
[PDP](../skills/).
