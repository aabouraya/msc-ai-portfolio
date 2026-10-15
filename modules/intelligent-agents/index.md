---
title: Intelligent Agents
module: intelligent-agents
nav_order: 0
short_title: Overview
permalink: /modules/intelligent-agents/
summary: >-
  Agent architectures, multi-agent coordination and the design and
  implementation of an agent-based system, with attention to the legal, social,
  ethical and professional context.
---
{%- assign mod = site.data.modules | where: "slug", "intelligent-agents" | first -%}

## Learning outcomes

On completion of this module I should be able to:

{% for outcome in mod.outcomes %}
**LO{{ forloop.index }}.** {{ outcome }}
{% endfor %}

## Artefact index

Every artefact in this module maps to at least one learning outcome. This table
is the map — it is what a reader should be able to check the portfolio against.

| Artefact | Section | Evidences | Status |
| --- | --- | --- | --- |
| Collaborative Discussion 1 — my thread and my responses to peers | [Discussion 1](discussions/#discussion-1--agent-based-systems-in-contemporary-organisations) | LO1, LO4 | Complete |
| Collaborative Discussion 3 — deep learning and the ethics of generative AI | [Discussion 3](discussions/#discussion-3--deep-learning-and-the-ethics-of-generative-ai) | LO1, LO4 | Complete |
| Team project — ScholarPlan design proposal (team submission, Sep 2026) | [Artefacts](artefacts/#scholarplan--team-design-proposal) · [Team](team/#team-output) | LO1, LO2, LO3 | Complete |
| Team project — meeting notes (4 design meetings, Aug 2026) | [Meeting log](team/#meeting-log) | LO4 | Complete |
| Individual project — ScholarPlan implementation and presentation | [Artefacts](artefacts/#agent-based-system) · [Code](https://github.com/aabouraya/scholar_plan/tree/c66190e) | LO2, LO3 | Complete |
| Critical evaluation of the final project — design (week 7) against implementation (week 11) | [Project evaluation](evaluation/) | LO1, LO2, LO3 | Draft |
| Three reflective case studies — XAI, AI safety constraints, bias | [Case studies](case-studies/) | LO2, LO3 | Draft |
| Week 6 formative activity — agent dialogues in KQML and KIF | [Artefacts](artefacts/#week-6--creating-agent-dialogues-in-kqml-and-kif) | LO1, LO2 | Complete |
| Formative activity — constituency-based parse trees | [Artefacts](artefacts/#constituency-based-parse-trees) | LO2 | Complete |
| Tutor and peer feedback log — tutor feedback on the team design document, with my response | [Feedback](feedback/) | LO4 | Draft |
| Professional skills matrix and PDP | [Skills &amp; PDP](skills/) | LO4 | Draft |
| Reflective piece | [Reflection](reflection/) | LO1–LO4 | Draft |

<div class="todo" markdown="1">
Update the **Status** column as you go (`Not started` → `Draft` → `Complete`),
and add rows for anything you produce that is not listed — seminar preparation,
reading notes, code experiments. The requirement is not just to include
artefacts but to *show how they relate to the learning outcomes*, which is what
the **Evidences** column does.
</div>

## Skills targeted in this module

{% for skill in mod.skills %}- {{ skill }}
{% endfor %}

Progress against these is tracked on the [Skills &amp; PDP](skills/) page for this
module, and rolled up on the programme-level
[Skills &amp; PDP]({{ '/skills/' | relative_url }}) page.
