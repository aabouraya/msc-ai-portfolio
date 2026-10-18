---
title: Formative Activities
short_title: Formative activities
module: intelligent-agents
nav_order: 3
permalink: /modules/intelligent-agents/formative-activities/
summary: >-
  My answers, and what each taught me. Evidences LO1 and LO2.
---

{% assign img = '/assets/img/intelligent-agents/formative/' %}

## 1. Agent dialogue in KQML and KIF

<figure>
  <a href="{{ img | append: 'kqml-brief.jpg' | relative_url }}"><img src="{{ img | append: 'kqml-brief.jpg' | relative_url }}" alt="Activity brief, Unit 6: create a KQML and KIF dialogue in which Alice, a procurement agent, asks Bob, a warehouse stock agent, about the stock of 50 inch televisions and their number of HDMI slots." loading="lazy"></a>
  <figcaption>The brief.</figcaption>
</figure>

<figure>
  <a href="{{ img | append: 'kqml-dialogue.png' | relative_url }}"><img src="{{ img | append: 'kqml-dialogue.png' | relative_url }}" alt="Sequence diagram of my answer. Alice sends ask-one with reply-with stock-q1 and content stock-level tv-50-inch ?units; Bob replies tell in-reply-to stock-q1 with stock-level tv-50-inch 25. Alice sends ask-one with reply-with spec-q1 and content hdmi-slots tv-50-inch ?count; Bob replies tell in-reply-to spec-q1 with hdmi-slots tv-50-inch 4. Every message uses language KIF and ontology warehouse-stock." loading="lazy"></a>
  <figcaption>My answer.</figcaption>
</figure>

<details markdown="1">
<summary>Full KQML messages</summary>

```
(ask-one :sender alice :receiver bob :language KIF :ontology warehouse-stock
         :reply-with stock-q1 :content (stock-level tv-50-inch ?units))
(tell    :sender bob :receiver alice :language KIF :ontology warehouse-stock
         :in-reply-to stock-q1 :content (stock-level tv-50-inch 25))
(ask-one :sender alice :receiver bob :language KIF :ontology warehouse-stock
         :reply-with spec-q1 :content (hdmi-slots tv-50-inch ?count))
(tell    :sender bob :receiver alice :language KIF :ontology warehouse-stock
         :in-reply-to spec-q1 :content (hdmi-slots tv-50-inch 4))
```

</details>

**Reflection.** The syntax was the easy part; the meaning was harder.
`stock-level` and `hdmi-slots` mean something only because both messages name
the same `warehouse-stock` ontology, and `:reply-with` is what lets Alice match
each answer to its question. Agent communication depends on agreed meaning, not
just well-formed messages.

## 2. Constituency-based parse trees

<figure>
  <a href="{{ img | append: 'parse-trees-brief.jpg' | relative_url }}"><img src="{{ img | append: 'parse-trees-brief.jpg' | relative_url }}" alt="Activity brief: create a constituency-based parse tree for three phrases: The government raised interest rates. The internet gives everyone a voice. The man saw the dog with the telescope." loading="lazy"></a>
  <figcaption>The brief.</figcaption>
</figure>

<div class="figure-pair">
<figure>
  <a href="{{ img | append: 'parse-tree-1.png' | relative_url }}"><img src="{{ img | append: 'parse-tree-1.png' | relative_url }}" alt="Parse tree 1: S splits into NP (DT The, NN government) and VP (VBD raised, NP with NN interest and NNS rates)." loading="lazy"></a>
  <figcaption>Sentence 1.</figcaption>
</figure>
<figure>
  <a href="{{ img | append: 'parse-tree-2.png' | relative_url }}"><img src="{{ img | append: 'parse-tree-2.png' | relative_url }}" alt="Parse tree 2: S splits into NP (DT The, NN internet) and VP (VBZ gives, NP with NN everyone, NP with DT a and NN voice)." loading="lazy"></a>
  <figcaption>Sentence 2.</figcaption>
</figure>
<figure>
  <a href="{{ img | append: 'parse-tree-3a.png' | relative_url }}"><img src="{{ img | append: 'parse-tree-3a.png' | relative_url }}" alt="Parse tree 3, reading A: the prepositional phrase with the telescope attaches to the VP, alongside VBD saw and the NP the dog, so the man used the telescope." loading="lazy"></a>
  <figcaption>3A: the man used it.</figcaption>
</figure>
<figure>
  <a href="{{ img | append: 'parse-tree-3b.png' | relative_url }}"><img src="{{ img | append: 'parse-tree-3b.png' | relative_url }}" alt="Parse tree 3, reading B: the prepositional phrase with the telescope attaches inside the object NP, to the dog, so the dog had the telescope." loading="lazy"></a>
  <figcaption>3B: the dog had it.</figcaption>
</figure>
</div>

**Reflection.** Sentence 3 has two valid trees, because *with the telescope*
can attach to *saw* or to *the dog*. Grammar alone cannot choose between them;
only context can. An agent can therefore parse an instruction correctly and
still act on the wrong meaning, so ambiguity should be flagged, not resolved
silently.
