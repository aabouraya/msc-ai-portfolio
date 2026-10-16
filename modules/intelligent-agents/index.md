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

## About this e-portfolio

The module's central project was ScholarPlan, an LLM-powered multi-agent system
for academic research. Given one research question, it plans its own searches,
gathers papers from OpenAlex, arXiv and Crossref, has an independent Critic
check every claim against its source, and writes a cited literature review. It
was designed as a team project, then built and evaluated by me. That two-phase
structure runs through the portfolio: what the design promised, what the
implementation showed, and what I learned from the gap.

**Where to start.** The assessed written work is on three pages:

- [Project evaluation](evaluation/): a critical evaluation of the design against
  the implementation;
- [Case studies](case-studies/): three reflective case studies;
- [Reflection](reflection/): the final reflective piece, also submitted to
  Turnitin.

The other pages hold the supporting evidence, mapped to the learning outcomes in
the [artefact index](#artefact-index) below. Much of it is reproduced verbatim
from work assessed earlier in the module: forum posts, meeting minutes and the
team design proposal.

**Word count** (prose only, excluding tables, captions and references):
this Overview 254, Project evaluation 478 and Case studies 632,
a total of 1,364 against the 1,500-word limit. The Reflection is 851 words
against its 1,000-word limit.

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

## Skills targeted in this module

{% for skill in mod.skills %}- {{ skill }}
{% endfor %}

Progress against these is tracked on the [Skills &amp; PDP](skills/) page for this
module, and rolled up on the programme-level
[Skills &amp; PDP]({{ '/skills/' | relative_url }}) page.
