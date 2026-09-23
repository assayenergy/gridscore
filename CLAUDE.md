# CLAUDE.md
This is a public Assay Energy repository. Its commit history is part of what
Assay publishes as a tamper-evident record.

## Hard rules
- Never force-push, rebase published commits, or rewrite history.
- Never commit or push without first showing the diff and waiting for approval.
- Before any commit, scan and show results: no .env, no /data, no .parquet,
  no owner names, no parcel street addresses, GPINs, or lat/long coordinates.
- Parcel-level data never belongs here. If a task would add it, stop and say so.
- Never invent rows, figures, or sources to satisfy an instruction. If input
  data is missing, stop and ask.

## Evidence rules
- Every factual claim cites a public source, with a capture date where possible.
- Anything not directly sourced is labeled INFERENCE or UNVERIFIED. No unlabeled
  estimates.
- Recompute every figure in code; show the arithmetic.
- Reversals (cancelled deals, lawsuits, lost tenants) are flagged with a
  citation, never subtracted from a score.
- Corrections go in corrections.md with the date. Never silently edit a
  published number.
- Any file about Virginia counties opens with:
  "Disclosure: the author has a financial interest in land acquisition in the
  counties covered by this research."

## Voice
- Never "we". The public record is the subject; "Assay" is the voice of the
  method; "I" only when owning a mistake.
