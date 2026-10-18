---
title: "Team Project: ScholarPlan Design"
short_title: Team project
module: intelligent-agents
nav_order: 1
permalink: /modules/intelligent-agents/team-project/
summary: >-
  The Group A design proposal, weeks 1–7, and my part in it.
---

[Proposal](../evidence/team-proposal/) · [Tutor feedback](../evidence/tutor-feedback/)

<figure>
  <a href="{{ '/assets/img/intelligent-agents/scholarplan-architecture.png' | relative_url }}"><img src="{{ '/assets/img/intelligent-agents/scholarplan-architecture.png' | relative_url }}" alt="Architecture diagram: the Planner, Retriever, Processor, Critic and Archivist each connect only to a central shared blackboard."></a>
  <figcaption><strong>Figure 1.</strong> Architecture.</figcaption>
</figure>

<figure>
  <a href="{{ '/assets/img/intelligent-agents/scholarplan-activity.png' | relative_url }}"><img src="{{ '/assets/img/intelligent-agents/scholarplan-activity.png' | relative_url }}" alt="UML activity diagram in swimlanes for User, Planner, Retriever, Processor, Critic and Archivist, with a dashed re-planning loop from Critic rejection back to the Planner."></a>
  <figcaption><strong>Figure 2.</strong> Activity (mine).</figcaption>
</figure>

<figure>
  <a href="{{ '/assets/img/intelligent-agents/scholarplan-sequence.png' | relative_url }}"><img src="{{ '/assets/img/intelligent-agents/scholarplan-sequence.png' | relative_url }}" alt="UML sequence diagram of the agents reading and writing the blackboard, with a loop over subtasks and the Archivist writing to disk at the end."></a>
  <figcaption><strong>Figure 3.</strong> Sequence (mine).</figcaption>
</figure>

## My contribution

<div class="wide" markdown="1">

| What I did | When | Effect on the team |
| --- | --- | --- |
| Drafted the [contract](#team-records) and asked everyone to sign | 30 Jul | Rules agreed before design began |
| Argued for specialised agents | Meeting 1 | Adopted as the core design (section [3](../evidence/team-proposal/#design-decisions)) |
| Designed subtask decomposition and failure handling | Meeting 1 | Became the re-planning loop |
| Presented the design draft with Yasmin | Meeting 2 | Basis of Figure 1 |
| Wrote requirements and tools with Adel A. | Meeting 3 | Sections [2](../evidence/team-proposal/#system-requirements-and-assumptions), [4](../evidence/team-proposal/#development-approach), [6](../evidence/team-proposal/#tools-libraries-models-and-environments) |
| Drew the blackboard flows | Meeting 4 | Figures 2 and 3, which the tutor singled out |

</div>

**How well I did.** I took the initiative: I contacted every member, arranged
and attended all four meetings, and delivered all my tasks.

**The outcome.** The tutor found "outstanding domain knowledge" and "clear UML
activity and sequence diagrams that improve readability"
([feedback](../evidence/tutor-feedback/)).

## Team records

{% assign shots = '/assets/img/intelligent-agents/team/' %}
<div class="shots shots--three">
  <a class="shot" href="{{ shots | append: 'team-contract-signed.png' | relative_url }}">
    <img src="{{ shots | append: 'team-contract-signed.png' | relative_url }}" alt="The signed team contract: goals, expectations, policies, roles, consequences and the members' signatures." loading="lazy">
    <span class="shot-text"><span class="shot-title">Signed contract</span><span class="shot-meta">30 Jul – 15 Aug</span></span>
  </a>
  <a class="shot" href="{{ shots | append: 'team-contract.png' | relative_url }}">
    <img src="{{ shots | append: 'team-contract.png' | relative_url }}" alt="Forum screenshot: my post asking the team to review and sign the team contract I drafted." loading="lazy">
    <span class="shot-text"><span class="shot-title">Contract sent</span><span class="shot-meta">30 Jul</span></span>
  </a>
  <a class="shot" href="{{ shots | append: 'meeting-1.png' | relative_url }}">
    <img src="{{ shots | append: 'meeting-1.png' | relative_url }}" alt="Forum screenshot: minutes of Meeting 1, initial architecture brainstorming and governance." loading="lazy">
    <span class="shot-text"><span class="shot-title">Meeting 1</span><span class="shot-meta">6 Aug</span></span>
  </a>
  <a class="shot" href="{{ shots | append: 'meeting-2.png' | relative_url }}">
    <img src="{{ shots | append: 'meeting-2.png' | relative_url }}" alt="Forum screenshot: minutes of Meeting 2, high-level design draft and scope definition." loading="lazy">
    <span class="shot-text"><span class="shot-title">Meeting 2</span><span class="shot-meta">14 Aug</span></span>
  </a>
  <a class="shot" href="{{ shots | append: 'meeting-3.png' | relative_url }}">
    <img src="{{ shots | append: 'meeting-3.png' | relative_url }}" alt="Forum screenshot: minutes of Meeting 3, draft consolidation and alignment." loading="lazy">
    <span class="shot-text"><span class="shot-title">Meeting 3</span><span class="shot-meta">24 Aug</span></span>
  </a>
  <a class="shot" href="{{ shots | append: 'meeting-4.png' | relative_url }}">
    <img src="{{ shots | append: 'meeting-4.png' | relative_url }}" alt="Forum screenshot: minutes of Meeting 4, finalising the system design and requirements." loading="lazy">
    <span class="shot-text"><span class="shot-title">Meeting 4</span><span class="shot-meta">29 Aug</span></span>
  </a>
</div>
