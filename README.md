# GridScore

GridScore scores the 21 largest publicly announced ERCOT-bound data center projects in Texas on
one question: how much of each announcement is backed by verifiable public-record evidence, not
how likely it is to actually get built. Each project is scored 0–100 across five signals — site
control, physical commitment (on-site generation permits), financial commitment, incentive
filings, and sponsor track record — with every point traced to a cited public source and a
capture date. Where no public evidence was found, the score says so explicitly, and says what
that does and doesn't mean.

**Read the analysis:** [The Texas Governor Ordered a Data Center Audit. I Already Started One by Hand](https://vishtella.substack.com/p/the-texas-governor-ordered-a-data)

## What's in this repo

- **[spec.md](spec.md)**: the original project brief — the five-signal rubric, weights, and
  session plan this whole exercise followed.
- **[methodology.md](methodology.md)**: how each signal is scored, the site-control confidence
  labels, the §151.359-vs-JETI distinction, the Physical Commitment renormalization rule (and why
  a flat credit was tried and rejected first), and every known limitation. Start here if you want
  to check the scoring logic before trusting a number.
- **[candidate_universe.md](candidate_universe.md)**: how the 21-project universe was compiled,
  the market-opacity finding (no public way to reconcile a named project against ERCOT's queue),
  and the decisions made about which projects to include.
- **[scored_table.csv](scored_table.csv)** / **[scored_table.md](scored_table.md)**: the full
  scored table — every signal score, tier, provenance confidence label, and reversal flag for all
  21 projects, plus the near-tier-boundary watchlist and the transparency table showing every
  score computed under both the standard and renormalized treatment.
- **[evidence_appendix.md](evidence_appendix.md)**: one paragraph per project explaining the score
  with its supporting citations. The full, unabridged research trail (every source, every dead
  end) is in `evidence/`, one file per project.
- **[key-stats.md](key-stats.md)**: the headline numbers — tier counts, aggregate MW by tier, the
  ERCOT approval-to-energize funnel, the zero-JETI finding, the permit-by-rule visibility finding,
  and the Aug 3, 2026 Abbott audit directive that this analysis landed two days ahead of.
- **`charts/`**: the three publication charts (funnel, all-21-projects, MW-by-tier), same visual
  system as the [FlexValue](#) piece this one follows.
- **[essay-final.md](essay-final.md)**: the published write-up.

## Data sources

County appraisal district and county clerk records (where accessible); TCEQ air permit dockets
and public-notice filings; the Texas Comptroller's JETI current-agreements list and separate
§151.359 Qualifying Data Center registry (read as raw HTML, not summarized); PUCT and ERCOT
filings and monthly operational reports; SEC filings (8-K, 10-K, and related exhibits) for
publicly traded sponsors; county commissioners court and city council records for incentive
agreements; and federal court filings for the one documented securities litigation referenced.
Full citations are inline in `evidence/` and `evidence_appendix.md`.

## Known limitations

No individual county CAD parcel record was pulled directly — Texas county appraisal districts run
on dynamic, form-based search portals that generic web search and static fetch tools can't reach.
Every site-control finding here is sourced from a press release, an SEC filing, or a government
body's own minutes/records, never from raw parcel data. See `methodology.md` for this and every
other limitation, stated plainly rather than smoothed over.

## Related

Piece one in this series: [FlexValue](https://github.com/tptella/flexvalue) — what grid
flexibility is worth, node by node, in the same ERCOT market this piece scores the demand side of.
