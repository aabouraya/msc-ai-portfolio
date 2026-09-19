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
| Team project — agent design | [Team](team/) | LO1, LO2, LO3 | Not started |
| Team project — meeting notes (4 design meetings, Aug 2026) | [Meeting log](team/#meeting-log) | LO4 | Complete |
| Agent-based system implementation | [Artefacts](artefacts/) | LO2, LO3 | Not started |
| Tutor and peer feedback log | [Feedback](feedback/) | LO4 | Not started |
| Professional skills matrix and PDP | [Skills &amp; PDP](skills/) | LO4 | Not started |
| Reflective piece | [Reflection](reflection/) | LO1–LO4 | Not started |

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
