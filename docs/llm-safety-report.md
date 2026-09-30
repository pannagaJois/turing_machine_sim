# Undecidability and LLM Safety

## The connection

The Halting Problem proves that no general algorithm can always correctly predict
whether an arbitrary program will halt, just by analyzing it. A large language model
is, in effect, a very complex program: it has an enormous number of possible inputs
and internal states, and its outputs depend on that input in ways that are not fully
predictable by a simpler checking program.

## What this means in practice

- No automated filter, classifier, or monitoring system can be proven to catch every
  unwanted output an LLM could ever produce, for every possible input.
- This does not mean safety work is pointless — most real-world prompts are far from
  the adversarial edge cases used in the Halting Problem proof, so practical
  detection can still work well most of the time.
- It does mean safety cannot rely on any single, perfect checker. Real systems use
  layered defenses: training-time alignment, input/output filtering, rate limits,
  human review, and monitoring — because no one layer can be a complete, provably
  correct guarantee.

## Takeaway

Undecidability gives a principled reason, grounded in computability theory rather
than just current technical limitations, for why AI safety is approached as
defense-in-depth rather than a single solved checking problem.

## Further grounding: Rice's Theorem

The Halting Problem is a special case of a more general result, **Rice's Theorem
(1953)**: no algorithm can decide any non-trivial semantic property of an arbitrary
program, not just whether it halts.

Properties like "is this model's output always truthful" or "will this system stay
aligned" are exactly this kind of property, so there can be no single, universal
algorithm that verifies them for every possible AI system in every situation. What
remains possible is narrower, bounded verification — testing a specific system under
specific assumptions — which is the practical approach most real safety engineering
already takes.

**Worth noting:** this extension of Rice's Theorem to AI traits is not universally
accepted as settled — some researchers argue the theorem's conditions don't cleanly
apply once resource bounds are taken into account. So undecidability gives a strong
theoretical reason to expect no perfect universal checker, but exactly how far that
limit extends to AI specifically is still debated.

### Sources
- Pentera, *Rice's Theorem and AI Safety* — https://pentera.io/?p=5122
- Futura Sciences, *Why Turing's discovery still blocks superintelligent AI* — https://www.futura-sciences.com/en/why-turings-forgotten-discovery-still-blocks-truly-superintelligent-ai-today_38245/
- arXiv, *From Trakhtenbrot's Wall to the Safety-Generality trade-off* — https://arxiv.org/pdf/2606.28639
- Review of *On Formally Undecidable Traits of Intelligent Machines* (counter-argument) — https://www.themoonlight.io/en/review/on-formally-undecidable-traits-of-intelligent-machines
