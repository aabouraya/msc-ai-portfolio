---
title: Research Methods and Professional Practice
module: research-methods-and-professional-practice
nav_order: 0
short_title: Overview
permalink: /modules/research-methods-and-professional-practice/
summary: >-
  Principles of academic investigation, critical evaluation of literature and
  methodology, and the production of a research proposal — alongside the
  professional, legal, social, cultural and ethical context of computing.
---
{%- assign mod = site.data.modules | where: "slug", "research-methods-and-professional-practice" | first -%}

<div class="todo" markdown="1">
This module has not started yet. The learning outcomes and required artefacts
are recorded below so that work can be filed against them from the first unit.
</div>

## Learning outcomes

{% for outcome in mod.outcomes %}
**LO{{ forloop.index }}.** {{ outcome }}
{% endfor %}

## Required e-Portfolio artefacts

This module requires **two** collaborative discussion summaries, and the
statistical analysis activities carried out during the module must be included.

| Artefact | Evidences |
| --- | --- |
| Collaborative discussion forum summary 1 | LO1, LO2 |
| Collaborative discussion forum summary 2 | LO1, LO2 |
| Reflective piece *(strict word limit)* | a key module aim |
| Statistical analysis activities | LO3 |
| Feedback from peers and tutors | – |
| Professional skills matrix and action plan (PDP) | – |
| Other artefacts, mapped to the learning outcomes | varies |

## Skills targeted in this module

{% for skill in mod.skills %}- {{ skill }}
{% endfor %}
