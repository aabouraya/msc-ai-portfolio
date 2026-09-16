---
title: Machine Learning
module: machine-learning
nav_order: 0
short_title: Overview
permalink: /modules/machine-learning/
summary: >-
  Applying and critically appraising machine learning techniques to real-world
  problems, including dataset suitability and the professional and ethical
  issues facing ML practitioners.
---
{%- assign mod = site.data.modules | where: "slug", "machine-learning" | first -%}

<div class="todo" markdown="1">
This module has not started yet. The learning outcomes and required artefacts
are recorded below so that work can be filed against them from the first unit.
</div>

## Learning outcomes

{% for outcome in mod.outcomes %}
**LO{{ forloop.index }}.** {{ outcome }}
{% endfor %}

## Required e-Portfolio artefacts

| Artefact | Evidences |
| --- | --- |
| Collaborative discussion forum summaries | LO1, LO2 |
| Outcomes from the team exercises | LO1–LO4 |
| Reflective piece *(strict word limit)* | LO1–LO4 |
| Summary of learning outcomes | – |
| Team meeting notes | LO4 |
| Feedback from peers and tutors | – |
| Professional skills matrix and action plan (PDP) | – |
| Other artefacts, mapped to the learning outcomes | varies |

## Skills targeted in this module

{% for skill in mod.skills %}- {{ skill }}
{% endfor %}
