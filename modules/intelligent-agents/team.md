---
title: Team Exercises
short_title: Team
module: intelligent-agents
nav_order: 3
permalink: /modules/intelligent-agents/team/
summary: >-
  The team design project: my contribution, the team's records, how the team
  worked against its contract, and the outcome. Evidences LO1–LO4.
---

## My contribution

<div class="wide" markdown="1">

| What I did | When | Where it ended up |
| --- | --- | --- |
| Drafted the team contract and asked the team to review and sign it | 30 Jul 2026 | [Team contract](#team-records) |
| Argued for cooperating specialised agents over one monolithic program, on modularity, scalability and task separation | Meeting 1 | Proposal section [3](../evidence/team-proposal/#design-decisions) |
| Worked out how goals break into subtasks, and what happens when one fails | Meeting 1 | Proposal section [3](../evidence/team-proposal/#design-decisions); the re-planning loop in my [implementation](../evidence/scholarplan-implementation/#how-it-works) |
| Co-presented the first high-level design draft | Meeting 2 | Proposal Figure 1 |
| Co-authored the requirements, execution tools and development methods draft | Meeting 3 | Proposal sections [2](../evidence/team-proposal/#system-requirements-and-assumptions), [4](../evidence/team-proposal/#development-approach) and [6](../evidence/team-proposal/#tools-libraries-models-and-environments) |
| Drew the blackboard interaction flows: how agents share state | Meeting 4 | Proposal Figures 2 and 3 |

</div>

## Who owned what

<div class="wide" markdown="1">

| Part of the [team proposal](../evidence/team-proposal/) | Where it was produced | Owner, as minuted |
| --- | --- | --- |
| Agent roles and the multi-agent justification (section [3](../evidence/team-proposal/#design-decisions)) | Meeting 1 | Me |
| High-level design and architecture view (section [3](../evidence/team-proposal/#design-decisions), Figure 1) | Meetings 2–4 | Yasmin, co-presented with me in Meeting 2 |
| Requirements, assumptions, tools and development approach (sections [2](../evidence/team-proposal/#system-requirements-and-assumptions), [4](../evidence/team-proposal/#development-approach) and [6](../evidence/team-proposal/#tools-libraries-models-and-environments)) | Meetings 3–4 | Adel A., co-authored with me in Meeting 3 |
| Blackboard interaction flows (Figures 2 and 3) | Meeting 4 | Me |

</div>

## Team records

Select a record to open it full size. Surnames and the document link are hidden.

{% assign shots = '/assets/img/intelligent-agents/team/' %}
<div class="shots shots--three">
  <a class="shot" href="{{ shots | append: 'team-contract-signed.png' | relative_url }}">
    <img src="{{ shots | append: 'team-contract-signed.png' | relative_url }}" alt="The signed team contract: goals, expectations, policies, roles, consequences and the members' signatures." loading="lazy">
    <span class="shot-text"><span class="shot-title">Signed team contract</span><span class="shot-meta">Signed 30 Jul – 15 Aug 2026 · goals, roles, consequences</span><span class="shot-open">Open full size →</span></span>
  </a>
  <a class="shot" href="{{ shots | append: 'team-contract.png' | relative_url }}">
    <img src="{{ shots | append: 'team-contract.png' | relative_url }}" alt="Forum screenshot: my post asking the team to review and sign the team contract I drafted." loading="lazy">
    <span class="shot-text"><span class="shot-title">Contract sent for signature</span><span class="shot-meta">30 Jul 2026 · drafted by me</span><span class="shot-open">Open full size →</span></span>
  </a>
  <a class="shot" href="{{ shots | append: 'meeting-1.png' | relative_url }}">
    <img src="{{ shots | append: 'meeting-1.png' | relative_url }}" alt="Forum screenshot: minutes of Meeting 1, initial architecture brainstorming and governance." loading="lazy">
    <span class="shot-text"><span class="shot-title">Meeting 1</span><span class="shot-meta">6 Aug 2026 · team contract, agent roles, LLM planning</span><span class="shot-open">Open full size →</span></span>
  </a>
  <a class="shot" href="{{ shots | append: 'meeting-2.png' | relative_url }}">
    <img src="{{ shots | append: 'meeting-2.png' | relative_url }}" alt="Forum screenshot: minutes of Meeting 2, high-level design draft and scope definition." loading="lazy">
    <span class="shot-text"><span class="shot-title">Meeting 2</span><span class="shot-meta">14 Aug 2026 · first design draft, co-presented by me</span><span class="shot-open">Open full size →</span></span>
  </a>
  <a class="shot" href="{{ shots | append: 'meeting-3.png' | relative_url }}">
    <img src="{{ shots | append: 'meeting-3.png' | relative_url }}" alt="Forum screenshot: minutes of Meeting 3, draft consolidation and alignment." loading="lazy">
    <span class="shot-text"><span class="shot-title">Meeting 3</span><span class="shot-meta">24 Aug 2026 · requirements draft, co-authored by me</span><span class="shot-open">Open full size →</span></span>
  </a>
  <a class="shot" href="{{ shots | append: 'meeting-4.png' | relative_url }}">
    <img src="{{ shots | append: 'meeting-4.png' | relative_url }}" alt="Forum screenshot: minutes of Meeting 4, finalising the system design and requirements." loading="lazy">
    <span class="shot-text"><span class="shot-title">Meeting 4</span><span class="shot-meta">29 Aug 2026 · blackboard flows, presented by me</span><span class="shot-open">Open full size →</span></span>
  </a>
</div>

## The contract against practice

<div class="wide" markdown="1">

| The contract said | What happened |
| --- | --- |
| Weekly virtual meetings | Four Zoom meetings, 6–29 August |
| Daily updates on the Group A forum | Day-to-day chat and file sharing moved to a WhatsApp group; the forum kept the formal record: the contract and the minutes |
| A single shared document with version tracking | The contract was drafted and signed in Google Docs |
| A member unresponsive for 48 hours: reallocate their tasks | Applied. One member signed last, joined no meeting and missed an internal deadline. The other three reallocated the task and submitted on time |
| Roles: lead, architect, research specialist, quality editor | Work split by area instead: structure (Yasmin), requirements (Adel A.) and dynamics (me) |
| At least two diagrams, for example sequence and class | Architecture, activity and sequence diagrams, but no class diagram. It was the tutor's first improvement point; I added one in my [implementation](../artefacts/#structure-classes-and-blackboard-tables) |

</div>

## Outcome

The tutor's feedback on the team proposal, by marking criterion. The full
feedback, and my response to its three improvement points, are in the
[evidence appendix](../evidence/tutor-feedback/).

<div class="wide" markdown="1">

| Criterion | The tutor's verdict |
| --- | --- |
| Knowledge and understanding | "Outstanding domain knowledge, with architectural choices well supported by relevant academic literature" |
| Application of knowledge | "Very effective use of specialised techniques to address practical challenges such as API rate limits and non-deterministic model behaviour" |
| Criticality | "A strong critical evaluation of agent architectures and orchestration frameworks" |
| Structure and presentation | "Well structured and professionally presented" |

</div>

## What worked and what did not

<div class="wide" markdown="1">

| | What happened | Why |
| --- | --- | --- |
| **Worked** | Each meeting built on the last: concept, then draft, then consolidation, then final. Nothing was reopened | The team contract was agreed before any design work |
| **Worked** | Work split by interest and stayed split. Consolidation meant merging, not reconciling | Structure, requirements and dynamics each had one owner |
| **Did not** | My minutes record what was discussed, not what was decided, who owns the follow-up, or by when | I wrote them as agendas |

</div>
