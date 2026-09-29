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
