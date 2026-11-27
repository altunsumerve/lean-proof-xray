# Narrator protocol / Anlatıcı kuralları

This is the instruction given to the language model that writes the story. It is the only place in this
repository where a language model is used. Everything the model is allowed to look at is produced by the
deterministic tools; everything it writes is checked by `denetle.py`.

Replace `<MAP>` by the result folder (for example `sinama/grh76`) and `<SRC>` by a checkout of the proof's source.

---

Narrate the approach of a large machine-checked Lean proof by reading ONLY the few places the map points to.

You may use only these four things:

1. The map: `<MAP>/CIKTI_en.md`, and
   `python3 arac/hikaye/harita.py <MAP> --top 40` (heaviest steps),
   `python3 arac/hikaye/harita.py <MAP> NAME ...` (share, what the step exists for, heaviest parts under it).
   "Share" is the part of the proof that exists only for that step. It is not importance.
2. The code of single declarations, comments stripped: `python3 arac/hikaye/kaynak.py <SRC> NAME ...`
   (works for theorems and for definitions).
3. The required questions: `python3 arac/hikaye/sorular.py <MAP> <SRC>`.
4. The checker: `python3 arac/hikaye/denetle.py <MAP> story.md questions.md`.

Rules. No web. Do not open any other file: not the source tree directly, no guides, no READMEs, no papers.
Do not use what you remember about this theorem or its authors. Every claim about how this proof goes must
come from a statement or code you were shown; mark anything else "(guess)". A short true story is a success;
a fluent story you cannot support is a failure.

Method.
- Round 1, the skeleton: use the map to find the junctions (the heavy steps and the step that combines them).
  Read the code of those junctions to see what is combined, in what order, and why the combination gives the
  result. Open the definitions of the quantities that appear in the junction statements.
- Round 2, the why: run `python3 arac/hikaye/sorular.py <MAP> <SRC> > questions.md` and answer EVERY question in it
  from code, going as deep as each one needs. These questions are produced by fixed rules from the map; a story
  that skips them stops at the skeleton. Then revise the story so that it uses what you found.
  Do not try to read everything else.

Write `story.md` with these sections:

    # Story of the proof
    ## The idea in five sentences   (the mechanism of the whole proof; each sentence rests on code you read)
    ## For a mathematician          (at most 400 words; the steps in the order they are combined, and why)
    ## For everyone                 (at most 6 plain sentences, no formulas)
    ## What I could not tell        (specific bullets; this section is not optional)
    ## Answers to the required questions   (one line per question: "- Q3: ..."; write NOT FOUND and where you looked if so)
    ## Claims                       (at least 15 lines, each exactly one of:)
    - STEP `Name`
    - UNDER `A` `B`        (B exists only for A)
    - SHARE `Name` 55.7

Use backticks in the prose only for names of steps that are in the map. Run the checker. If it reports names
that are not steps, wrong claims, or heavy steps the story never mentions, fix the story honestly (do not
delete claims to make it pass) and run it again. Report the number of lookups you made.
