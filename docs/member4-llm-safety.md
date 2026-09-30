# Member 4 — LLM Safety Connection, Report & Slides

## 1. Research

Starting point: Member 3's Halting Problem proof. Research question: does this
connect to AI safety as more than a loose analogy? It does, via Rice's Theorem
(1953), which extends the Halting Problem to say no algorithm can decide any
non-trivial semantic property of an arbitrary program.

Several sources apply this directly to AI safety properties, and a counter-view
exists too — some researchers argue the theorem's conditions don't cleanly apply
once resource bounds are considered. Both sides are cited in
`docs/llm-safety-report.md`.

## 2. The conceptual bridge (final report)

Full writeup in `docs/llm-safety-report.md`: state the connection, explain what it
does and doesn't mean in practice, conclude with why this motivates defense in
depth rather than a single solved check.

## 3. Compiling the final report

The complete deliverable is the whole `docs/` folder read as one unit — formal
definition and designs from Member 1, the engine writeup from Member 2, the proof
and simulator test from Member 3, and the safety argument here.

Demo flow for presenting live: run `src/main.py` to show the addition machine, both
palindrome checks, and the halting contradiction printout in one pass.
