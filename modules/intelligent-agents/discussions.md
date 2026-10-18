---
title: Collaborative Discussions
short_title: Discussions
module: intelligent-agents
nav_order: 4
permalink: /modules/intelligent-agents/discussions/
summary: >-
  What I learned from each forum discussion, with my posts as screenshots.
---

## Discussion 1 — Agent-based systems in organisations

<p class="meta"><span class="muted">August 2026</span></p>

<div class="learned" markdown="1">
<p class="learned-title">What I learned</p>

**From my research**

- Reactive and BDI agents follow predefined plans, so they struggle when the
  environment changes. LLMs add reasoning, task decomposition and memory.
- That flexibility costs reliability: hallucination, cascading failures and
  miscoordination between agents, which become governance risks for
  organisations.

**From the discussion**

- **Reliability is an architecture problem.** Isaac showed that errors spread
  at handoffs between agents, so outputs should be verified there, processes
  evaluated as well as outcomes, and agents tested in a sandbox before going
  live.
- **Autonomy must be bounded.** Kapinga argued that autonomy does not make an
  agent trustworthy. Panagiotis added that an agent's independence should
  match the cost of its failure, and Imoh that humans keep judgement and
  accountability.
- **Control works best as a hybrid.** In Luis's thread, an LLM that removes a
  usability barrier brings hallucination with it, so it needs guardrails. The
  thread settled on central governance with decentralised execution.

</div>

<div class="shots">
  <a class="shot" href="{{ '/assets/img/intelligent-agents/discussions/d1-initial-post.png' | relative_url }}">
    <img src="{{ '/assets/img/intelligent-agents/discussions/d1-initial-post.png' | relative_url }}" alt="Forum screenshot: my initial post on agent-based systems, with responses from Isaac S. and Kapinga D." loading="lazy">
    <span class="shot-text"><span class="shot-title">Initial post</span><span class="shot-meta">5 Aug</span></span>
  </a>
  <a class="shot" href="{{ '/assets/img/intelligent-agents/discussions/d1-summary-post.png' | relative_url }}">
    <img src="{{ '/assets/img/intelligent-agents/discussions/d1-summary-post.png' | relative_url }}" alt="Forum screenshot: my summary post for Discussion 1." loading="lazy">
    <span class="shot-text"><span class="shot-title">Summary post</span><span class="shot-meta">16 Aug</span></span>
  </a>
  <a class="shot" href="{{ '/assets/img/intelligent-agents/discussions/d1-peer-response.png' | relative_url }}">
    <img src="{{ '/assets/img/intelligent-agents/discussions/d1-peer-response.png' | relative_url }}" alt="Forum screenshot: Luis T.'s post on multi-agent systems in manufacturing, my response, and the replies that followed." loading="lazy">
    <span class="shot-text"><span class="shot-title">Reply to Luis T.</span><span class="shot-meta">9 Aug</span></span>
  </a>
  <a class="shot" href="{{ '/assets/img/intelligent-agents/discussions/d1-peer-response-2.png' | relative_url }}">
    <img src="{{ '/assets/img/intelligent-agents/discussions/d1-peer-response-2.png' | relative_url }}" alt="Forum screenshot: Khadijah H.'s post on the rise of intelligent agents, my response, and replies from Panagiotis M. and Imoh E." loading="lazy">
    <span class="shot-text"><span class="shot-title">Reply to Khadijah H.</span><span class="shot-meta">9 Aug</span></span>
  </a>
</div>

## Discussion 3 — Ethics of generative AI

<p class="meta"><span class="muted">October 2026</span></p>

<div class="learned" markdown="1">
<p class="learned-title">What I learned</p>

**From my research**

- Generative AI's main risks are copyright, because models train on scraped
  work without consent, and misinformation, because synthetic media is
  realistic enough to deceive.
- Both come from the same strength: models learn from vast, uncurated data and
  reproduce its patterns convincingly.

**From the discussion**

- **I overstated my evidence.** Lara showed that deepfakes have been *used* in
  elections, not shown to *change* results. The defensible harm is lost trust
  in authentic information.
- **Oversight needs specific safeguards.** Isaac turned my "careful oversight"
  into checks at each stage: record data provenance before training, test
  outputs before deployment, and do not rely on labels alone at distribution.
- **Every safeguard has a trade-off.** Researching watermarking for my reply,
  I found it must balance invisibility, speed and resistance to removal. Isaac
  added that a watermark can confirm machine generation, never human
  authorship.

</div>

<div class="shots">
  <a class="shot" href="{{ '/assets/img/intelligent-agents/discussions/d3-initial-post.png' | relative_url }}">
    <img src="{{ '/assets/img/intelligent-agents/discussions/d3-initial-post.png' | relative_url }}" alt="Forum screenshot: my initial post on the ethics of generative AI, with responses from Lara K. and Isaac S." loading="lazy">
    <span class="shot-text"><span class="shot-title">Initial post</span><span class="shot-meta">30 Sep</span></span>
  </a>
  <a class="shot" href="{{ '/assets/img/intelligent-agents/discussions/d3-summary-post.png' | relative_url }}">
    <img src="{{ '/assets/img/intelligent-agents/discussions/d3-summary-post.png' | relative_url }}" alt="Forum screenshot: my summary post for Discussion 3." loading="lazy">
    <span class="shot-text"><span class="shot-title">Summary post</span><span class="shot-meta">13 Oct</span></span>
  </a>
  <a class="shot" href="{{ '/assets/img/intelligent-agents/discussions/d3-peer-response.png' | relative_url }}">
    <img src="{{ '/assets/img/intelligent-agents/discussions/d3-peer-response.png' | relative_url }}" alt="Forum screenshot: Isaac S.'s post, my response, Yasmin A.'s response and Isaac's summary." loading="lazy">
    <span class="shot-text"><span class="shot-title">Reply to Isaac S.</span><span class="shot-meta">4 Oct</span></span>
  </a>
</div>
