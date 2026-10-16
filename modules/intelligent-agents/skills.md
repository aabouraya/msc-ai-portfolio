---
title: Skills Matrix & PDP
short_title: Skills & PDP
module: intelligent-agents
nav_order: 7
permalink: /modules/intelligent-agents/skills/
summary: >-
  Professional skills matrix for this module and the associated personal
  development action plan.
---

Rated 1–5 on the scale defined on the programme
[Skills &amp; PDP]({{ '/skills/' | relative_url }}) page. The *Evidence* column is
what makes a rating defensible — a claimed level with nothing to point at is
just an assertion.

## Skills matrix

Evidence includes what went less well. A rating is easier to defend when the
evidence shows the weak side too.

<div class="wide" markdown="1">

| Skill | Start | End | Evidence |
| --- | --- | --- | --- |
| Time management | – | – | The implementation was built in [four iterations with dated gates](../artefacts/#what-changed-from-the-design), 14 September to 9 October. Against that, [all four sets of minutes were written up late](../team/#what-worked-and-what-did-not), on 1 September |
| Commercial awareness | – | – | Models were chosen on benchmark and cost within a one-off $100 credit ([proposal §3](../artefacts/#design-decisions)), and a run costs about $0.03 ([results](../artefacts/#results)). [Discussion 1](../discussions/#discussion-1--agent-based-systems-in-contemporary-organisations) covers what agent systems offer organisations, and what they risk |
| Critical thinking and analysis | – | – | [Response to Isaac](../discussions/#discussion-3--deep-learning-and-the-ethics-of-generative-ai) names the engineering trade-offs of watermarking. The [changes from the design](../artefacts/#what-changed-from-the-design) record where the design did not hold. The [limitations](../artefacts/#limitations) report results that did not improve |
| Communication and literacy skills | – | – | Forum posts in [Discussions](../discussions/), the [team proposal](../artefacts/#scholarplan--team-design-proposal), and the [presentation](../artefacts/#scholarplan--implementation-and-presentation). Against that: inconsistent reference styles in Discussion 1, and a wrong in-text surname in my Discussion 3 initial post |
| IT and digital | – | – | [ScholarPlan](../artefacts/#agent-based-system): five agents, 67 offline and 3 live tests, and an evaluation harness. Also the [KQML and KIF dialogue](../artefacts/#week-6--creating-agent-dialogues-in-kqml-and-kif) |
| Resilience | – | – | Eleven problems were found and fixed during the build ([remediation log](https://github.com/aabouraya/scholar_plan/blob/c66190e/docs/remediation_log.md)). The design was changed when the local Llama Critic would not fit in memory ([changes from the design](../artefacts/#what-changed-from-the-design)) |
| Interpersonal | – | – | Responses to [Luis](../discussions/#discussion-1--agent-based-systems-in-contemporary-organisations), [Khadijah](../discussions/#discussion-1--agent-based-systems-in-contemporary-organisations) and [Isaac](../discussions/#discussion-3--deep-learning-and-the-ethics-of-generative-ai), each agreeing first and then adding a counterpoint. Isaac's summary built on mine |
| Problem-solving | – | – | Test-first fixes for the arXiv ID and Azure timeout bugs, each shown failing and then passing. A new Critic rule for claims stronger or weaker than their source brought it to 13 of 13 correct ([remediation log](https://github.com/aabouraya/scholar_plan/blob/c66190e/docs/remediation_log.md), issues 4, 10 and 11) |
| Ethical awareness | – | – | [Discussion 3](../discussions/#discussion-3--deep-learning-and-the-ethics-of-generative-ai) on copyright and deepfakes. The [legal, social, ethical and professional considerations](../artefacts/#legal-social-ethical-and-professional-considerations) of ScholarPlan, including disclosure of AI tool use |
| Teamwork / global citizen and leadership | – | – | [Meeting log](../team/#meeting-log): minutes for all four meetings, co-presenting the design and requirements drafts, and the Blackboard interaction flows ([my contribution](../team/#my-contribution)) |
| Critical reflection | – | – | "What I learned" sections in each [discussion](../discussions/). [My response to the tutor's feedback](../feedback/#my-response), and the [pattern](../feedback/#patterns) across that feedback, the discussions and the minutes |

</div>

<div class="todo" markdown="1">
Add your own **Start** and **End** ratings. Rate Start as you were in July
2026, before the module, not with hindsight.
</div>

## Action plan

Each objective comes from a weakness recorded elsewhere in this module. The
source is linked so the objective can be checked against it.

<div class="wide" markdown="1">

| # | Objective | Source | Action | Success measure | Target | Status |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Turn intentions into checkable rules | Tutor feedback points 2 and 3; [the pattern](../feedback/#patterns) | For every evaluation criterion or control in a design, write the number or rule: a target, a threshold or a cap. Start by adding Critic precision and recall targets and a three-attempt cap per subtask to ScholarPlan | The next design document has a numeric target for every evaluation criterion, and its feedback does not repeat the point | Next team project (Machine Learning) | Open |
| 2 | Minutes that record decisions | [Team: what did not work](../team/#what-worked-and-what-did-not) | Use a *decision, owner, due date* format, and post minutes within one day of each meeting | Every meeting in the next team project has minutes with at least one recorded decision and owner, posted the next day | Next team project (Machine Learning) | Open |
| 3 | Consistent UoE Harvard referencing | Discussion 1 fixes; my Discussion 3 initial post; the Kirchenbauer et al. (2023) entry in my response to Isaac | Check every reference against the UoE Harvard guide before posting. Cite the version actually read, with its DOI | No style mismatches in the next module's discussion posts on a self-check before submission | First discussion of the next module | Open |
| 4 | Show structure as well as behaviour | Tutor feedback point 1 | Draw a UML class diagram and an ERD of ScholarPlan's blackboard tables and agents, showing which agent writes which table. Include a structural view in every future design | The diagrams are added to [Artefacts](../artefacts/#structure-classes-and-blackboard-tables) | End of this module | **Closed** 14 Oct 2026: class diagram, ERD and agent-to-table map added |
| 5 | Check deployment constraints before design sign-off | [Project evaluation](../evaluation/#where-the-design-did-not-hold): three of six design changes came from unchecked resources | Before a design is agreed, run a short feasibility test of every model and service it depends on: quota, memory and supported parameters | The next design needs no change caused by a constraint that a feasibility test would have found | Next team project (Machine Learning) | Open |
| 6 | Raise participation risks early | [Reflection](../reflection/#so-what): the missing contribution was noticed at the deadline | Raise a missed check-in with the team at the time, and agree a reassignment date in writing | No task in the next team project is reassigned in the final week before submission | Next team project (Machine Learning) | Open |

</div>

Close each objective with a dated outcome rather than deleting the row.
Anything still open at the end of the module carries forward to the programme
[action plan]({{ '/skills/' | relative_url }}#action-plan).
