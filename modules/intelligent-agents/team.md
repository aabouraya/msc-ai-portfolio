---
title: Team Exercises
short_title: Team
module: intelligent-agents
nav_order: 2
permalink: /modules/intelligent-agents/team/
summary: >-
  Outputs from the team exercises, role allocation and meeting notes.
  Evidences LO1–LO4.
---

The team project is the design of a multi-agent system: cooperating specialised
agents rather than one monolithic program, with an LLM handling goal
decomposition and re-planning. Four design meetings ran from 6 to 29 August 2026,
producing a high-level design, a system requirements specification, and the
interaction flows for agent communication.

I took the minutes for all four meetings and posted them to the module forum on
1 September 2026. They are reproduced verbatim below, with one disclosed change:
team members' surnames are reduced to an initial, for consistency with how peers
are identified elsewhere in this portfolio.

## Meeting log

<div class="wide" markdown="1">

| # | Date | Present | Focus | My contribution, as minuted |
| --- | --- | --- | --- | --- |
| 1 | 6 Aug 2026 | Me, Yasmin | Team contract; agent roles; LLM planning and re-planning | Defined agent roles and the justification for a multi-agent design |
| 2 | 14 Aug 2026 | Me, Yasmin, Adel A. | First HLD draft; scoping requirements, tooling and methodology | Co-presented the HLD draft with Yasmin |
| 3 | 24 Aug 2026 | Me, Yasmin, Adel A. | Requirements and methodology draft; consolidated HLD | Co-authored and presented the requirements, execution tools and development methods draft |
| 4 | 29 Aug 2026 | Me, Yasmin, Adel A. | Finalised requirements; visual HLD; Blackboard interaction flow | Presented the interaction flow diagrams for the Blackboard pattern |

</div>

The design moved in one direction across the four meetings: concept and
governance first, then a draft design, then consolidation, then a finalised
design plus the interaction detail. Nothing was reopened once agreed, which is
the main reason four meetings were enough.

### Meeting 1 — Initial Architecture Brainstorming &amp; Governance

<p class="post-meta">6 August 2026 · minuted by me</p>

<div class="post" markdown="1">

- **Date:** August 6, 2026
- **Attendees:** Ahmed Abou Raya, Yasmin

**Agenda &amp; Discussion Points**

1. **Team Governance:** Reviewed and established the core team contract.
2. **Multi-Agent Concept &amp; Responsibilities:**
   - Defined initial agent roles and individual responsibilities within the
     architecture.
   - Justified the multi-agent approach (cooperating specialized agents vs. a
     single monolithic program) to ensure modularity, scalability, and robust
     task separation.

**LLM Planning Mechanisms:**

- Evaluated how the LLM will manage dynamic goal decomposition into discrete
  subtasks.
- Defined handling mechanisms for dynamic re-planning when a subtask encounters
  failure or exceptions.

</div>

### Meeting 2 — High-Level Design Draft &amp; Scope Definition

<p class="post-meta">14 August 2026 · minuted by me</p>

<div class="post" markdown="1">

- **Date:** August 14, 2026
- **Attendees:** Ahmed Abou Raya, Yasmin, Adel A.

**Agenda &amp; Discussion Points**

1. **HLD Review:** Ahmed and Yasmin presented an initial high-level design (HLD)
   draft reflecting concepts discussed during Meeting 1.
2. **Requirements &amp; Tooling Scoping:**
   - Welcomed Adel A. to the architectural discussions.
   - Brainstormed next steps for defining comprehensive System Requirements,
     selecting target tools/frameworks, and setting up the project methodology.

</div>

### Meeting 3 — Draft Consolidation &amp; Alignment

<p class="post-meta">24 August 2026 · minuted by me</p>

<div class="post" markdown="1">

- **Date:** August 24, 2026
- **Attendees:** Ahmed Abou Raya, Yasmin, Adel A.

**Agenda &amp; Discussion Points**

1. **System Requirements &amp; Methodology Draft:** Ahmed and Adel prepared and
   presented a draft outlining system requirements, execution tools, and
   development methods.
2. **Consolidated High-Level Design:** Yasmin presented a consolidated version of
   the High-Level Design document, integrating updates and feedback from prior
   sessions.

</div>

### Meeting 4 — Finalize high system design and system requirements

<p class="post-meta">29 August 2026 · minuted by me</p>

<div class="post" markdown="1">

- **Date:** August 29, 2026
- **Attendees:** Ahmed Abou Raya, Yasmin, Adel A.

**Agenda &amp; Discussion Points**

1. **Consolidated System Requirements:** Adel presented the standardized and
   finalized system requirements derived from previous drafts.
2. **Visual High-Level Design (HLD):** Yasmin shared a newly formatted, visual
   version of the High-Level Design featuring structured architectural diagrams.
3. **Blackboard Interaction Flow:** Ahmed presented detailed interaction flow
   diagrams illustrating the Blackboard architecture pattern for agent
   communication and state sharing.

</div>

## Team output

The four meetings produced three artefacts: the high-level design, the system
requirements specification, and the Blackboard interaction flow diagrams.

<div class="todo" markdown="1">
None of the three documents are in this repository yet. Add them under
[Artefacts](../artefacts/) — the HLD and requirements specification as files, the
Blackboard interaction flows as images — and link them from here. The minutes
establish that they exist and who produced them; the documents themselves are
what evidence LO1–LO3.
</div>

### My contribution

Taken from the minutes rather than from memory:

- **Agent roles and the multi-agent justification** (Meeting 1) — arguing
  cooperating specialised agents over a single monolithic program, on modularity,
  scalability and task separation.
- **LLM planning and failure handling** (Meeting 1) — how goals decompose into
  discrete subtasks, and what happens when a subtask fails or raises an
  exception.
- **The first HLD draft** (Meeting 2), co-presented with Yasmin.
- **System requirements, execution tools and development methods draft**
  (Meeting 3), co-authored with Adel A.
- **Blackboard interaction flow diagrams** (Meeting 4) — how agents communicate
  and share state through a common blackboard.
- **Minutes for all four meetings**, written and posted to the forum.

The through-line is the *dynamics* of the system rather than its static
structure: how a goal becomes subtasks, what happens when one fails, and how
agents exchange state. Yasmin owned the structural view (the HLD and its visual
form) and Adel A. owned the requirements specification.

## What worked and what did not

**What worked.** Two things, both visible in the record:

- **Meetings built on each other rather than revisiting.** Meeting 1 settled the
  concept, 2 drafted, 3 consolidated, 4 finalised. Agreeing the team contract
  before any design work is the most likely reason this held.
- **Work split along interests and stayed there.** Structure, requirements and
  dynamics each had a clear owner, so consolidation was merging rather than
  reconciling.

**What did not.** One weakness in my own record-keeping, which is worth stating
plainly because it is the part I controlled:

- **The minutes record discussion, not decisions.** They say what was covered and
  who presented, but never *what was agreed*, who owned the follow-up, or by
  when. Meeting 1 "evaluated" LLM planning mechanisms and "defined" handling
  mechanisms without saying what was settled. For a four-meeting project with
  three people that was recoverable; on anything larger it would not be.
- **They were written up late.** All four were posted on 1 September, after the
  last meeting, rather than after each one. That is why they read as agendas.

<div class="todo" markdown="1">
**Carry into the [PDP](../skills/):** adopt a decision-and-owner format for
minutes — *decision, owner, due date* — and write them up within a day of the
meeting. Then reflect on the team process in the
[Reflection](../reflection/) piece, where the word limit applies.
</div>
