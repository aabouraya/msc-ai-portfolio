# Discussion 3 — Deep learning and the ethics of generative AI

Collaborative discussion, Intelligent Agents module, 30 September – 13 October 2026. Evidence for the
[Discussions](https://aabouraya.github.io/msc-ai-portfolio/modules/intelligent-agents/discussions/) page of my e-portfolio.

My posts are reproduced verbatim from the module forum, including their original
references; corrections are listed at the end. The summaries of other students'
posts are my own précis. Peers are identified by first name and initial.

The thread started from two ethical
concerns about generative AI, copyright and misinformation. It ended on the
argument that both risks come from the property that makes deep learning
powerful, so no single safeguard can cover them.

## Part 1 — My thread

### My initial post

<p class="post-meta">Posted Wednesday, 30 September 2026 · 173 words excluding references</p>

<div class="post" markdown="1">

In recent years, deep learning technologies have transformed interactions with
digital content, including text and images. Generative AI models such as ChatGPT
and DALL-E provide advanced content-creation capabilities that were not possible
before. However, these advancements in content generation present significant
ethical implications that need to be examined.

A primary ethical concern is copyright infringement. As Buick (2025) noted,
generative AI models are trained on datasets collected from the internet, which
often include copyrighted texts. These texts may be used to generate new outputs
without obtaining consent from the original creators.

Misinformation and deception represent additional critical ethical concerns, as
generative AI models can produce realistic synthetic content that poses
significant risks. As illustrated by Romero (2024), AI-generated images and
videos have been used to manipulate election outcomes and facilitate investment
scams. Such threats undermine society's capacity to trust digital information.

In conclusion, generative AI enables powerful new forms of digital content, but
also brings important ethical risks. Clear guidelines and careful oversight are
essential to maximise its benefits and limit potential harms.

**References**

<div class="references" markdown="1">

Buick, A. (2025) Copyright and AI training data—transparency to the rescue?
Journal of intellectual property law & practice. [Online] 20 (3), 182–192.

Romero Moreno, F. (2024) Generative AI and deepfakes: a human rights approach to
tackling harmful content. International review of law, computers & technology.
[Online] 38 (3), 297–326.

</div>

</div>

### Peer responses to my post

Two peers responded.

**Lara K.** (1 October 2026) said my claim that AI-generated content had been
used to "manipulate election outcomes" conflated the *use* of deceptive content
with *evidence* that it changed a result. She cited three studies:

- **No decisive effect on outcomes.** In a non-representative sample of
  election deepfakes from 11 countries, none had decisively influenced an
  election (Łabuz and Nehring, 2024). The broader concern is declining trust in
  information, politics and the media.
- **Low credibility does not prevent harm.** Political deepfakes can
  delegitimise a targeted politician even when viewers do not find them highly
  credible (Hameleers, van der Meer and Dobber, 2024).
- **Voting intentions can shift, and fact checks help.** Deepfakes shifted
  attitudes and voting intentions towards a fictitious politician, and
  journalistic fact checks substantially reduced the effect (Dan, 2026).

She asked which interventions I would prioritise: detection before content
spreads, fact-checking after it spreads, or longer-term media literacy.

**Isaac S.** (2 October 2026) agreed that oversight is needed. He argued that it
should be stated as safeguards at specific points in the lifecycle:

- **Before training, document provenance.** An audit of more than 1,800 text
  datasets found widespread missing or inaccurate licence information (Longpre
  et al., 2024), so a platform's licence label is not enough. Keep records of
  creators and permitted uses, and give creators a way to challenge inclusion.
- **Before deployment, test outputs.** Diffusion models can reproduce memorised
  training images (Carlini et al., 2023). Deduplication and close-match screening
  help, but they should be evaluated rather than assumed to work.
- **At distribution, don't rely on labels alone.** Deepfake videos stayed
  influential despite explicit advance warnings (Clark and Lewandowsky, 2026).
  Combine labels with advertiser verification, endorsement checks, rapid review
  of impersonation reports, and an appeals process for moderation errors.

### My summary post

<p class="post-meta">Posted Tuesday, 13 October 2026 · 307 words excluding references</p>

<div class="post" markdown="1">

This discussion examined the ethical implications of generative AI, a deep
learning application. My initial post raised two concerns. The first was
copyright infringement: models are trained on scraped datasets that contain
copyrighted works used without creators' consent (Buick, 2025). The second was
misinformation: realistic synthetic content has been used to target elections
and facilitate investment scams (Romero Moreno, 2024).

My peers sharpened both arguments. Lara pointed out that I had conflated the use
of deceptive content with evidence that it changed election results. Łabuz and
Nehring (2024) found that none of the deepfakes in their sample had decisively
influenced an election outcome, but they noted declining trust in information.
Even when people don't see them as credible, deepfakes can delegitimise
politicians (Hameleers, van der Meer and Dobber, 2024). They can also shift
voting intentions, although journalistic fact-checks reduce this effect (Dan,
2026).

Isaac turned my call for oversight into concrete safeguards. An audit of more
than 1,800 datasets found widespread missing or inaccurate licence information
(Longpre et al., 2024), so developers should document data provenance rather
than rely on platform labels. Carlini et al. (2023) showed that diffusion models
can reproduce memorised training images, supporting the case for testing outputs
before deployment. Clark and Lewandowsky (2026) found that deepfakes remained
influential despite warnings, indicating that disclosure labels alone are
insufficient.

I learned that these risks stem from the same property that makes deep learning
powerful: models learn from vast, uncurated datasets and convincingly reproduce
their patterns. I also learned that deepfakes' main harm may be eroding trust in
authentic information, rather than any proven effect on election results.
Oversight therefore needs to cover the full lifecycle: data collection, model
evaluation and content distribution. Because no single safeguard is sufficient,
layered measures combining provenance records, memorisation testing, labelling,
fact-checking and media literacy offer the most realistic protection.

**References**

<div class="references" markdown="1">

Buick, A. (2025) 'Copyright and AI training data—transparency to the rescue?',
*Journal of Intellectual Property Law & Practice*, 20(3), pp. 182–192.

Carlini, N., Hayes, J., Nasr, M., Jagielski, M., Sehwag, V., Tramèr, F., Balle,
B., Ippolito, D. and Wallace, E. (2023) 'Extracting training data from diffusion
models', in *32nd USENIX Security Symposium (USENIX Security 23)*. USENIX
Association, pp. 5253–5270. Available at:
<https://www.usenix.org/conference/usenixsecurity23/presentation/carlini>

Clark, S. and Lewandowsky, S. (2026) 'The continued influence of AI-generated
deepfake videos despite transparency warnings', *Communications Psychology*, 4,
article 13. Available at: <https://doi.org/10.1038/s44271-025-00381-9>

Dan, V. (2026) 'Deepfakes as a democratic threat: Experimental evidence shows
noxious effects that are reducible through journalistic fact checks', *The
International Journal of Press/Politics*, 31(3), pp. 525–550. Available at:
<https://doi.org/10.1177/19401612251317766>

Hameleers, M., van der Meer, T.G.L.A. and Dobber, T. (2024) 'Distorting the
truth versus blatant lies: The effects of different degrees of deception in
domestic and foreign political deepfakes', *Computers in Human Behavior*, 152,
article 108096. Available at: <https://doi.org/10.1016/j.chb.2023.108096>

Łabuz, M. and Nehring, C. (2024) 'On the way to deep fake democracy? Deep fakes
in election campaigns in 2023', *European Political Science*, 23(4), pp.
454–473. Available at: <https://doi.org/10.1057/s41304-024-00482-9>

Longpre, S., Mahari, R., Chen, A., Obeng-Marnu, N., Sileo, D., Brannon, W.,
Muennighoff, N., Khazam, N., Kabbara, J., Perisetla, K., Wu, X., Shippole, E.,
Bollacker, K., Wu, T., Villa, L., Pentland, S. and Hooker, S. (2024) 'A
large-scale audit of dataset licensing and attribution in AI', *Nature Machine
Intelligence*, 6, pp. 975–987. Available at:
<https://doi.org/10.1038/s42256-024-00878-8>

Romero Moreno, F. (2024) 'Generative AI and deepfakes: a human rights approach
to tackling harmful content', *International Review of Law, Computers &
Technology*, 38(3), pp. 297–326.

</div>

</div>

## Part 2 — My responses to peers

I responded to one other initial post, on Sunday, 4 October 2026 — nine days
before I wrote my summary post. The response is reproduced verbatim; the
summary of the peer's own post is my précis of it.

### Response to Isaac S. — content, source and accountability

**His initial post.** Isaac argued that the core problem with generative AI is
not that it produces convincing content, but that it weakens the link between
content, its source and responsibility for its consequences. He traced three
concerns across the system lifecycle:

- **Training data.** Use of copyright-protected material is legally uncertain,
  and opaque training datasets make accountability hard (Pasetti et al., 2025).
  Creators can contribute to a model's capability without knowing, being
  credited or being paid.
- **Bias.** Models can reproduce and amplify inequality in their training data
  (Hagendorff, 2024; Afreen, Mohaghegh and Doborjeh, 2025), so technical
  performance alone is not an adequate evaluation.
- **Epistemic trust.** Political deepfakes using advanced text-to-speech were
  harder to tell from authentic material than voice-actor versions (Groh et al.,
  2024). Widespread synthetic content may make authenticity itself harder to
  establish.

He concluded that generative AI is not inherently unethical, and that data
governance, bias evaluation, human oversight, provenance and accountability
should be designed in rather than added after harm occurs.

**My response**

<p class="post-meta">Posted Sunday, 4 October 2026 · 217 words excluding the salutation and references</p>

<div class="post" markdown="1">

Hi Isaac,

Your post has provided a thoughtful analysis of the ethical concerns intrinsic
to generative AI content. Identifying the weakening connection between content,
its original source and accountability is the core idea that anchors your
argument. Addressing these ethical concerns across the full lifecycle of deep
learning, starting from data training governance to post-deployment output,
provides a clear framework to mitigate these risks. Additionally, your use of
the note from Groh et al. (2024) effectively underscores the threats posed by
synthetic media to trust and authenticity.

Although I strongly agree that safeguards must be embedded in the system
architecture rather than added as a post-hoc precaution, your argument could be
strengthened by exploring the technical challenges and trade-offs that
complicate proactive provenance mechanisms.

In order to address these challenges, Kirchenbauer et al. (2023) proposed a
token-level watermarking algorithm that embeds detectable signatures by softly
biasing token selection. Conversely, Cao (2025) highlights that practical
watermarking schemes face critical trade-offs. Specifically, balancing token
imperceptibility, computational latency, and resilience against adversarial
paraphrasing or removal remains a major engineering hurdle. Consequently,
embedding provenance into high-throughput or open-weight models introduces
technical constraints that policy frameworks alone cannot solve.

Overall, your analysis makes a powerful case for aligning technical architecture
with ethical responsibility, framing accountability as an essential engineering
requirement rather than an afterthought.

**References**

<div class="references" markdown="1">

Cao, L. (2025) 'Watermarking for AI content detection: A review on text, visual,
and audio modalities', *arXiv*, article arXiv:2504.03765. Available at:
<https://doi.org/10.48550/arxiv.2504.03765> (Accessed: 4 October 2026).

Kirchenbauer, J., Geiping, J., Wen, Y., Katz, J., Miers, I. and Goldstein, T.
(2023) 'A watermark for large language models', *Proceedings of the 40th
International Conference on Machine Learning*, PMLR 202, pp. 17061-17084.
Available at: <https://doi.org/10.48550/arxiv.2301.10226> (Accessed: 4 October
2026).

</div>

</div>

**What happened next.** Yasmin A. also responded to Isaac's post, on 6 October 2026. She
proposed dataset records with consent and opt-out, bias testing across the
lifecycle by diverse teams, and provenance metadata combined with media
literacy. She also asked who is responsible when safeguards fail. Isaac's
summary post (11 October 2026) took up my point directly. He agreed that
watermarking must balance imperceptibility, latency and resistance to
paraphrasing, and added a point I had not made. Generation-time watermarking
depends on the provider implementing it, so the *presence* of a watermark can
show text was generated, but its *absence* cannot prove human authorship.

## Referencing corrections

As in Discussion 1, the posts are left verbatim and corrected here. In my
initial post, the two entries are in a library-catalogue style rather than UoE
Harvard: no quotation marks, an "[Online]" tag and no DOI. In my response to
Isaac, the Kirchenbauer *et al.* (2023) entry cites the ICML proceedings but
links the arXiv preprint. The corrected entries:

<div class="references" markdown="1">

Buick, A. (2025) ‘Copyright and AI training data—transparency to the rescue?’,
*Journal of Intellectual Property Law & Practice*, 20(3), pp. 182–192. Available
at: <https://doi.org/10.1093/jiplp/jpae102> (Accessed: 15 October 2026).

Kirchenbauer, J., Geiping, J., Wen, Y., Katz, J., Miers, I. and Goldstein, T.
(2023) ‘A watermark for large language models’, in *Proceedings of the 40th
International Conference on Machine Learning (ICML 2023)*. Honolulu: PMLR 202,
pp. 17061–17084. Available at:
<https://proceedings.mlr.press/v202/kirchenbauer23a.html> (Accessed: 15 October
2026).

Romero Moreno, F. (2024) ‘Generative AI and deepfakes: a human rights approach
to tackling harmful content’, *International Review of Law, Computers &
Technology*, 38(3), pp. 297–326. Available at:
<https://doi.org/10.1080/13600869.2024.2324540> (Accessed: 15 October 2026).

</div>
