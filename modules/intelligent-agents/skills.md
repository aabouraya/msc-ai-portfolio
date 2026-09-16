---
title: Skills Matrix & PDP
short_title: Skills & PDP
module: intelligent-agents
nav_order: 5
permalink: /modules/intelligent-agents/skills/
summary: >-
  Professional skills matrix for this module and the associated personal
  development action plan.
---
{%- assign mod = site.data.modules | where: "slug", "intelligent-agents" | first -%}

Rated 1–5 on the scale defined on the programme
[Skills &amp; PDP]({{ '/skills/' | relative_url }}) page. The *Evidence* column is
what makes a rating defensible — a claimed level with nothing to point at is
just an assertion.

## Skills matrix

<div class="wide" markdown="1">

| Skill | Start | End | Evidence |
| --- | --- | --- | --- |
{% for skill in mod.skills %}| {{ skill }} | – | – | *artefact / section* |
{% endfor %}

</div>

<div class="todo" markdown="1">
Fill the **Start** column early in the module and the **End** column in the last
unit. Point the **Evidence** column at specific pages — for example
`[Team meeting notes](../team/)` — not at the module as a whole.
</div>

## Action plan

<div class="wide" markdown="1">

| # | Objective | Action | Success measure | Target | Status |
| --- | --- | --- | --- | --- | --- |
| 1 | *objective* | *action* | *measure* | *unit / date* | Open |

</div>

<div class="todo" markdown="1">
Three or four objectives, drawn from your start-of-module ratings and from
recurring themes in [Feedback](../feedback/). Close each one with a dated
outcome; anything still open at the end of the module carries forward to the
programme-level plan.
</div>
