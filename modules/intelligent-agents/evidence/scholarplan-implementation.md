---
title: "Appendix: ScholarPlan implementation write-up"
short_title: ScholarPlan implementation write-up
module: intelligent-agents
nav_exclude: true
permalink: /modules/intelligent-agents/evidence/scholarplan-implementation/
summary: >-
  The full write-up of my individual ScholarPlan implementation and presentation.
---

Appendix to the [Artefacts](../../artefacts/#agent-based-system) page, which shows the code, diagrams and results.

**The brief.** Build the agent designed in the team project and present it. The
team proposal is in the [evidence appendix](../team-proposal/). This part is my
individual work.

**The evidence.**

- **Code:** [github.com/aabouraya/scholar_plan](https://github.com/aabouraya/scholar_plan/tree/c66190e),
  pinned to commit `c66190e`, the version presented. The repository includes the
  tests, evaluation runs, a development log and a remediation log.
- **Presentation:** [slide deck](https://docs.google.com/presentation/d/1cRRCG0g3pqrjCc7xxqDpI_tBM-J0sCwP/edit?usp=sharing)
  (11 slides, on Google Drive). The submitted version was narrated; this copy has
  the narration removed to keep it small. Slide 6 holds the demo, a screen
  recording of a real run.

## What it does

Given one research question, ScholarPlan plans its own searches, gathers papers
from OpenAlex, arXiv and Crossref, and summarises them into short claims. A
separate model checks every claim against its source, and the system writes a
cited literature review. A typical run takes 3 to 4 steps, about 2 minutes and
about $0.03.

```bash
uv run scholarplan "How does the attention mechanism in Transformers work?"
uv run scholarplan search runs/<timestamp> "why scale the dot product"   # offline, no LLM
```

Setup (Python 3.11, uv, and an Azure deployment of both models) is in the
[repository README](https://github.com/aabouraya/scholar_plan/blob/c66190e/README.md).

## How it works

<figure>
  <a href="{{ '/assets/img/intelligent-agents/scholarplan-implementation.png' | relative_url }}"><img src="{{ '/assets/img/intelligent-agents/scholarplan-implementation.png' | relative_url }}" alt="Implementation architecture: a Controller above a shared SQLite blackboard. The deliberative Planner sits on one side; the reactive Retriever, Processor, Critic and Archivist on the other. Agents connect only to the blackboard."></a>
  <figcaption>The implemented architecture, from the presentation. Agents never call each other; every agent reads and writes only the blackboard.</figcaption>
</figure>

| Agent | Kind | What it does |
| --- | --- | --- |
| Planner | deliberative, GPT-5-mini | Runs a ReAct loop. Each step writes a Thought and one Action (`search`, `abandon` or `finish`), and must address any Critic feedback first. Writes the final synthesis. |
| Retriever | reactive, no LLM | Searches the three APIs for a pending subtask, removes duplicates by DOI, arXiv ID or title, and records where each paper came from. |
| Processor | reactive, GPT-5-mini | Ranks sources with local MiniLM embeddings and summarises the top 3 into at most 4 claims each. |
| Critic | reactive, Llama-3.3-70B | Checks every claim against the source abstract. A summary passes only if all its claims are supported; otherwise it writes feedback for the Planner. |
| Archivist | reactive, no LLM | Exports the report, BibTeX, a vector index and the full trace. |

A controller runs one Planner step, then lets the reactive agents act until none
can, and repeats. It stops when the Planner finishes, when coverage is met (3
subtasks with at least 2 verified summaries each), or after 20 steps. The Critic
is a different model family from the Processor, so the two are less likely to
share blind spots.

## Structure: classes and blackboard tables

The proposal showed behaviour (activity and sequence diagrams) but not
structure, which was the tutor's first improvement point. These two diagrams
were added to the repository afterwards, in commit
[`460fb65`](https://github.com/aabouraya/scholar_plan/tree/460fb65/diagrams)
(14 October 2026), and checked against the code.

<figure>
  <a href="{{ '/assets/img/intelligent-agents/scholarplan-class-diagram.png' | relative_url }}"><img src="{{ '/assets/img/intelligent-agents/scholarplan-class-diagram.png' | relative_url }}" alt="UML class diagram: the Planner, Retriever, Processor, Critic and Archivist classes implement an Agent protocol with can_act and act. The controller creates the Blackboard and asks who can act. Each agent reads and writes the Blackboard class, and uses supporting modules: llm, sources, citations, index, embeddings and http_cache."></a>
  <figcaption>Class diagram. Every agent implements the same two-method <code>Agent</code> protocol, so the controller never needs to know which agent it is running.</figcaption>
</figure>

<figure>
  <a href="{{ '/assets/img/intelligent-agents/scholarplan-erd.png' | relative_url }}"><img src="{{ '/assets/img/intelligent-agents/scholarplan-erd.png' | relative_url }}" alt="Entity-relationship diagram of the eight blackboard tables. A subtask finds many sources and groups many summaries; a source is summarised in many summaries; a summary contains many claims; feedback is about a subtask or a summary. The run, thoughts and synthesis tables stand alone."></a>
  <figcaption>Entity-relationship diagram of the blackboard. The status columns are the triggers: a new row status is what tells the next agent it can act.</figcaption>
</figure>

Neither diagram shows which agent writes which table. That is the permission
model the proposal took from the Gaia methodology (section [4](../team-proposal/#development-approach)), so it is traced here
from the code:

| Agent | Writes to |
| --- | --- |
| Planner | `thoughts`, `subtasks` (new or abandoned), `synthesis`, `feedback` (when a query is refused) |
| Retriever | `subtasks` (claims a pending one, marks it done), `sources`, `feedback` |
| Processor | `sources` (relevance, status), `summaries` and their `claims`, `subtasks`, `feedback` |
| Critic | `claims` (verdicts), `summaries` (verified or rejected), `synthesis` (verdict), `feedback` |
| Archivist | nothing; it reads the blackboard and writes the output files to disk |
| Controller | `run`, `thoughts` (observations) |

Every agent can write `feedback`. That is the only way a reactive agent can
change what the Planner does next.

## What changed from the design

Building it showed where the team design did not hold. Each change is recorded
in the [development log](https://github.com/aabouraya/scholar_plan/blob/c66190e/docs/development_log.md).

| The design said | What was built | Why |
| --- | --- | --- |
| The Llama Critic can run locally via Ollama (section [3](../team-proposal/#design-decisions)) | Azure only | It needs about 40 GB of memory; the laptop has 32 GB |
| The Critic is unit-tested against MiniCheck (sections [4](../team-proposal/#development-approach) and [6](../team-proposal/#tools-libraries-models-and-environments)) | Unit tests use a fake model; MiniCheck is a second opinion | MiniCheck answers only yes or no, and the Planner needs the Critic's written reason to re-plan |
| About 50 hand-labelled claims for the Critic | 13 claims | A smaller set was built; it is listed as a limitation |
| GPT-5-nano as a fallback model | No fallback | Azure for Students has no GPT-5-nano quota |
| Full text where open access, abstracts as fallback (section [2.2](../team-proposal/#assumptions)) | Abstracts only | Abstracts are always available from the APIs; full text often is not |
| Low-temperature sampling (section [5](../team-proposal/#anticipated-challenges)) | Strict JSON schemas for GPT-5-mini; temperature 0 for Llama | GPT-5-mini accepts only its default temperature |

## Results

It was built in four iterations, each ending with a test that had to pass before
the next began. Eleven problems found on the way are in the
[remediation log](https://github.com/aabouraya/scholar_plan/blob/c66190e/docs/remediation_log.md).
The final [test report](https://github.com/aabouraya/scholar_plan/blob/c66190e/docs/testing/test_report.md)
(3 October 2026) shows:

| Level | Result |
| --- | --- |
| Unit and component (fake LLMs, saved API responses) | 67 passed |
| Integration (live APIs and models) | 3 passed |
| Critic on 13 hand-labelled claims | 13 of 13 correct; no unsupported claim accepted |
| Critic against MiniCheck, a second independent checker | Agreed on all 192 claims checked |
| End to end, 4 fixed research questions | 4 of 4 finished, no API errors, 99% of claims passed, about $0.03 per run |

<figure>
  <a href="{{ '/assets/img/intelligent-agents/scholarplan-eval-run.png' | relative_url }}"><img src="{{ '/assets/img/intelligent-agents/scholarplan-eval-run.png' | relative_url }}" alt="Terminal output of the end-to-end evaluation on 4 questions, 3 October 2026: recall retrieved 20%, recall cited 15%, claim pass rate 99%, 3.0 steps, $0.030 per run."></a>
  <figcaption>The end-to-end evaluation run on 3 October 2026.</figcaption>
</figure>

In one run the Critic rejected a summary and the first synthesis draft. The
Planner redrafted, and the second draft passed. That is the re-planning loop
working on real data rather than only under fault injection.

## Limitations

- **Recall of well-known papers is low and unstable.** Across four saved runs it
  was 25%, 55%, 50% and 20%. The Planner picks different queries each run, and
  recent papers now outrank older landmark ones. With one run per setting, the
  evaluation cannot show whether the tuning between runs helped.
- **The Critic checks support, not coverage.** A review can be fully verified
  and still miss the key papers.
- **Abstracts only.** A claim can be true of the paper but not checkable from
  its abstract.
- **Small labelled set.** 13 claims, and only one real claim was rejected, so the
  test of rejections is thin.

## Legal, social, ethical and professional considerations

- **Citing every claim.** Only claims the Critic supports reach the report, each
  with its source. The trace records which database each paper came from and
  when, so a reader can check any claim.
- **Using the APIs fairly.** Requests follow each API's rate limits, with
  throttling and retries that respect `Retry-After`, and are cached so the same
  call is not repeated. arXiv's open access interoperability is acknowledged in
  the README.
- **Secrets.** API keys live in a git-ignored `.env` with restricted
  permissions, and are never written to the cache.
- **Cost.** The 20-step budget and per-call cost tracking keep runs within the
  one-off student credit.
- **Use of AI tools.** Claude Code was used to help write, test and document the
  code, and the repository says so. The design decisions were mine.

## What this demonstrates

- **LO2.** It applies agent techniques (ReAct planning, Reflexion-style
  re-planning, blackboard coordination) to a real problem with real uncertainty.
  It is evaluated honestly, including the results that did not improve.
- **LO3.** It uses software tools chosen by evidence, tested at four levels, and
  built with attention to provenance, fair API use, secrets and cost.
