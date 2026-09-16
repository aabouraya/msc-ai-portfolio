---
title: Knowledge Representation and Reasoning
module: knowledge-representation-and-reasoning
nav_order: 0
short_title: Overview
permalink: /modules/knowledge-representation-and-reasoning/
summary: >-
  Formal approaches to representing knowledge, the properties of
  knowledge-based systems, and modelling techniques applied to KRR problems.
---
{%- assign mod = site.data.modules | where: "slug", "knowledge-representation-and-reasoning" | first -%}

<div class="todo" markdown="1">
This module has not started yet. The learning outcomes and required artefacts
are recorded below so that work can be filed against them from the first unit.
</div>

## Learning outcomes

{% for outcome in mod.outcomes %}
**LO{{ forloop.index }}.** {{ outcome }}
{% endfor %}

## Required e-Portfolio artefacts

Note that this module has no team component — there are no team meeting notes.

| Artefact | Evidences |
| --- | --- |
| Collaborative discussion forum summaries | LO1–LO3 |
| Reflective piece *(strict word limit)* | LO1–LO4, and the module aims |
| Summary of learning outcomes | – |
| Feedback from peers and tutors | – |
| Professional skills matrix and action plan (PDP) | – |
| Other artefacts, mapped to the learning outcomes | varies |

## Skills targeted in this module

{% for skill in mod.skills %}- {{ skill }}
{% endfor %}
