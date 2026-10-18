---
title: "Appendix: Tutor feedback on the team design proposal"
short_title: Tutor feedback
module: intelligent-agents
nav_exclude: true
permalink: /modules/intelligent-agents/evidence/tutor-feedback/
summary: >-
  The tutor's feedback on the team design proposal, reproduced unchanged.
---

<p class="post-meta">Development Team Project: Project Report · team submission, September 2026</p>

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

