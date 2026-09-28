# GridScore v0: Methodology

How I scored readiness for the 21 largest publicly announced ERCOT-bound data center
projects, what evidence it's built on, and where the score is deliberately conservative,
incomplete, or contested.

## The core rule

This scores **projects on public evidence**, not companies on character. Every scored signal has
a linked public source and a capture date (2026-08-05 throughout, unless noted). No evidence found
means the signal scores zero, logged as "no public evidence found (as of 2026-08-05)" — that is
explicitly not a claim the thing doesn't exist, only that I couldn't find it in public record.
When evidence was ambiguous, I scored conservatively and flagged it rather than picking the more
flattering read.

## The five signals

| Signal | Points | What earns full credit |
|---|---|---|
| Site control | 25 | Recorded ownership/lease with a traceable paper trail — a government counterparty (a city, county, or university) is the strongest version; an SEC-disclosed public-company transaction is the second-strongest. Partial credit for a self-disclosed but unconfirmed acquisition, or an affiliate LLC traceable via a filed deed. |
| Physical commitment | 25, or excluded (see below) | A docket-numbered TCEQ air permit tied to the specific site — the single strongest "this is real" signal, because it means someone is actually building generation. Building/TDLR permits count when TCEQ evidence isn't found. For projects where the absence of a permit is itself structurally uninformative, the signal is excluded from scoring entirely rather than defaulted to zero — see "Three meanings of a low Physical signal" below. |
| Financial commitment | 15 | An executed interconnection or power-supply agreement, a PUC filing, or an SEC-disclosed financing figure specific to the project. Corporate-level investment figures (not tied to this specific site) earn partial credit. |
| Incentive filings | 15 | An **executed** Texas JETI Act (Ch. 403) agreement or a county/municipal tax abatement agreement earns up to the full 15. A match on the Texas Comptroller's separate data center sales-tax-exemption registry (§151.3595 "Qualifying Large Data Center" table or §151.359 "Qualifying Data Center" table) — a real, verified state filing, but a different and lower bar than a negotiated abatement — caps at **7 of 15**. |
| Sponsor track record | 20 | A documented pattern of the sponsor (or, where relevant, its named founder) delivering announced projects before, at claimed scale, on roughly claimed timelines, with specific cited instances — not general reputation alone. |

**Tiers:** 70–100 Evidenced · 40–69 Progressing · 0–39 Announced-only. Neutral names on purpose —
not "real" and "fake."

## Documented reversals are flagged, not scored negative

Two projects (Fermi America's Project Matador, Poolside's Project Horizon) have publicly
documented, dated setbacks since their original announcement — a cancelled tenant-funding pact and
an open lawsuit in Fermi's case, a terminated anchor lease and a collapsed funding round in
Poolside's. I did not subtract points for these beyond what the underlying evidence already
implies (a company with no operating history and a cancelled deal naturally scores low on Sponsor
Track Record on the evidence alone). Instead, both carry a `documented_reversal_flag` with a
citation in every output table. The reasoning: this project scores evidence, not vibes, in both
directions — a reversal is a fact to report, not a hit to double-count.

## Site-control confidence labels

Every site-control score in `scored_table.csv` carries a confidence label:

- **government-record**: the paper trail runs through a government body's own action — a city
  council vote, a county commissioners court document, a university system lease, or an SEC
  filing (a legally binding federal disclosure, treated as government-record-equivalent for this
  purpose).
- **press-reported-only**: the only public evidence is the sponsor's own press release or trade
  coverage, with no independent government or filing-level confirmation found.

7 of 21 projects carry a government-record label; the rest are press-reported-only. That split is
itself worth reading as a finding: most of what the public "knows" about site control for these
projects is what the sponsor chose to say about it.

## The CAD-portal limitation (read this before trusting site-control scores)

**No individual county appraisal district (CAD) parcel record was pulled directly this session.**
I attempted one live lookup (Carson County CAD, for the Fermi America project) via an interactive
browser tool; the tool timed out and wasn't usable for the rest of the session. Generic web search
cannot reach the dynamic, form-based search portals that essentially every Texas CAD uses — this
is a real, structural gap in what's automatable, not a shortcut I took. Every "site control"
finding in this dataset is therefore sourced from a press release, an SEC filing, or a government
body's own minutes/records — never from an appraisal district's raw parcel data. Where that
distinction changes a score's reliability, it's marked in the near-tier-boundary watchlist in
`scored_table.md`. Treat every press-reported-only site-control score as provisional until someone
with working CAD access confirms it.

## The Comptroller data center registry (§151.359 / §151.3595) vs. JETI — two different programs, not interchangeable

I manually fetched and read the Texas Comptroller's "Qualifying Data Centers" registry
(comptroller.texas.gov/taxes/data-centers/data-center-lists.php) as raw HTML, not through an
AI-summarized tool — the earlier automated pass missed real matches (Hut 8's "Beacon Point 1,"
Google's "Project Goodnight," Fermi's own "Fermi Data Center 1") and wrongly called others
inconclusive. The registry has two tables: "Registered Qualifying Data Center Projects" (Tax Code
§151.359, "DC" registration numbers) and "Registered Qualifying Large Data Center Projects"
(§151.3595, "LD" numbers; certification requires at least 40 qualifying jobs, $500 million of capital
investment over five years and a contract for at least 20 MW of transmission capacity,
§151.3595(d)). Most matches in this dataset are in the §151.3595 table (labeling corrected
2026-09-28). Both are a state sales-tax exemption program with its own registration process; it
is **not** the JETI Act (Chapter 403) that the original rubric names, and it is not a negotiated,
project-specific incentive the way a county abatement is. I scored it as a real but lesser signal
(caps at 7/15) rather than either ignoring it or treating it as equivalent to an executed
abatement.

## Three meanings of a low Physical Commitment signal — and why one of them isn't "low" at all

A missing TCEQ docket can mean three different things, and treating them identically would have
been the single biggest distortion in this dataset. I sort every project into one of three states:

1. **Confirmed, permitted (score 5–25 on the standard 25-point scale).** A docket-numbered TCEQ air
   permit, a TDLR building permit, or equivalent was found and tied to the specific site. This is
   real, positive evidence — the strongest signal in the entire rubric, because building a
   dedicated generation plant at scale is expensive and hard to fake.
2. **True zero (score 0, on the standard scale).** The project's *own stated power strategy* would
   require an individually-permitted facility — dedicated primary generation at meaningful
   scale, the same class of build as the confirmed-permitted projects above — and no such permit
   was found despite that being the reasonable expectation. This applies to 1 of 21 projects:
   **Tract** (no operator/tenant named yet, so there is nothing to have even applied for a permit —
   a different flavor of zero, but still a real one: "not yet applicable" rather than "missing
   despite expectation"). A true zero here is a meaningful, informative absence. *(Updated
   2026-09-28: this read "3 of 21" at publication, with Poolside, SB Energy and Tract. SB Energy was
   re-sorted to "not observable by category" on 2026-09-26 after its S-1. Poolside was found on
   2026-09-28 to hold an issued TCEQ standard permit (183235, 2026-03-12) and is now
   confirmed-permitted. See `corrections.md`.)*
   A fourth state, **"applied, pending"** (8/25), was added 2026-09-28 for a dated application with
   no decision on record; see the section below.
3. **Not observable by category (excluded from scoring, not scored as zero).** The project's power
   strategy — a grid interconnection agreement plus standard-size backup/emergency generators, or
   reliance on an already-permitted third-party plant — is exactly the profile Texas's "permit by
   rule" regime (30 TAC §106.511, "Portable and Emergency Engines and Turbines") was built to wave
   through without individual public notice or a hearing. Multiple independent sources (Texas
   Tribune, University of Houston Law Center, floodlightnews.org) confirm data-center emergency
   diesel/gas arrays routinely qualify this way, sometimes totaling 150+ MW at a single site with
   zero public docket. **A missing permit here tells you nothing** — not that the generation exists,
   not that it doesn't. Scoring it as a zero would be treating a coin that hasn't been flipped as
   though it landed on tails.

## Physical Commitment renormalization for "not observable by category" projects

For the 12 projects in category 3 (9 at first publication; SB Energy added 2026-09-26; Riot and
Cipher added 2026-09-28), I do not
assign Physical Commitment a number on the 0–25 scale at all — not 25, not a partial credit, not a
symbolic small number. **The signal is excluded from both the numerator and the denominator**, and
the total is renormalized over the remaining four signals:

```
total = (Site Control + Financial Commitment + Incentive Filings + Sponsor Track Record)
        ÷ 75 × 100
```

75 is the combined maximum of the four remaining signals (25 + 15 + 15 + 20). The result still
lands on a 0–100 scale and uses the same 70/40 tier cutoffs, but it is **not directly comparable,
signal-for-signal, to a standard /100 score** — it answers "how strong is the evidence across the
four signals we can actually observe for this project," not "how strong is the evidence across all
five." I display Physical Commitment as **"n/o (§106.511)"** for these 12 rather than leaving a
blank or a zero, so the exclusion is visible everywhere the table appears, not just in a footnote.

**Why renormalize instead of the simpler options I tried first:** I initially scored the original 9 as a
true zero (Session 3, first pass), then as a flat +5 partial credit out of 100 (a correction pass),
before landing here. The zero was wrong because it punished projects for a regulatory category, not
for a lack of evidence. The flat +5 was an improvement but arbitrary — there's no principled reason
the "can't tell" credit should be worth exactly 5 points rather than 3 or 8, and a flat credit still
quietly dilutes a project's score on a signal that was never really being measured for it.
Renormalization removes the arbitrary constant and the dilution at the same time, at the cost of
making these scores (now 12) sit on a different footing than the other 9 — a tradeoff I judged better
than either alternative, but one you should weigh differently if you disagree.

### Transparency table — every score and tier that differs, flat-+5-credit vs. renormalized

| Project | Flat-+5 total (/100) | Renormalized total | Flat tier | Renormalized tier |
|---|---|---|---|---|
| Grand Prairie Campus (PowerHouse/Provident) | 29 | 32 | Announced-only | Announced-only |
| Beacon Point (Hut 8) | 51 | 61 | Progressing | Progressing |
| Childress Campus (Crusoe/Lancium) | 53 | 64 | Progressing | Progressing |
| Panhandle — Haskell Co. ("Journey") | 70 | 87 | Evidenced | Evidenced (no longer boundary-fragile) |
| **Project Caprock (Aligned)** | 38 | **44** | Announced-only | **Progressing** |
| **Denton Campus (Core Scientific)** | 62 | **76** | Progressing | **Evidenced** |
| Garden City Facility (Marathon) | 41 | 48 | Progressing | Progressing |
| Kaufman County Campus (Prometheus) | 24 | 25 | Announced-only | Announced-only |
| **Bosque County Campus (ECP+KKR/CyrusOne)** | 35 | **40** | Announced-only | **Progressing** |
| Stargate Milam County (SB Energy), moved to n/o 2026-09-26 | 52 | 63 | Progressing | Progressing |
| Corsicana Facility (Riot), moved to n/o 2026-09-28 | 73 | 91 | Evidenced | Evidenced |
| Barber Lake (Cipher), moved to n/o 2026-09-28 | 71 | 88 | Evidenced | Evidenced |

The SB Energy row was added when it moved into this category on 2026-09-26. Its flat-+5 figure is
computed for comparison only; it was never published. Arithmetic: 20 + 5 + 12 + 7 + 8 = 52 (flat);
(20 + 12 + 7 + 8) ÷ 75 × 100 = 47 ÷ 75 × 100 = 62.67 → 63 (renormalized). No tier difference.
Riot and Cipher were added 2026-09-28 (September audit), also comparison-only: Riot 22 + 5 + 15 + 15
+ 16 = 73 flat vs. (22 + 15 + 15 + 16) ÷ 75 × 100 = 90.67 → 91; Cipher 22 + 5 + 13 + 15 + 16 = 71 flat
vs. (22 + 13 + 15 + 16) ÷ 75 × 100 = 88. No tier difference for either.

Three tier changes emerged from renormalization beyond what the flat-credit version produced —
Aligned and ECP+KKR both cross Announced-only→Progressing, and Core Scientific crosses
Progressing→Evidenced. All three moves point the same direction (upward), because renormalization
is systematically more generous whenever a project's other four signals are strong relative to 75
— exactly the projects where a flat +5-out-of-100 credit was underselling them the most.

## The Financial Commitment scoring scale (written down explicitly, 2026-09-21)

This scale existed implicitly from the start but wasn't ever written out as a rubric until the
Fermi refresh forced the question of "why 12, not 10 or 15" to be answered precisely. Applying it
retroactively as a checklist, not just prose:

| Score | What it represents |
|---|---|
| **0–2** | No project-specific financing evidence; active negative events (a cancelled deal, a withdrawn commitment) with nothing to offset them. |
| **5** | Corporate-level financing exists (the sponsor has raised money, generally), but there is no project-specific agreement, and/or the company states outright that it has no binding tenant. |
| **8–10** | A project-specific agreement exists but is preliminary, non-binding, or a framework/MOU stage — not yet executed. |
| **12–13** | An executed, SEC-material, project-specific agreement exists (a lease, a PPA, an interconnection agreement), *with one or more specific, named reasons to discount full confidence in it* — a retracted claim, an unresolved concentration risk, a liquidity red flag sitting next to the deal. |
| **15** | The above, with no material discount factors identified. |

A future-dated performance/delivery date on an otherwise-executed agreement is **not**, on its own,
a reason to score below 12–13 — the rubric's bar is "executed," not "currently revenue-generating,"
and a forward performance date is a normal feature of this class of contract, not a sponsor-specific
weakness. What *does* justify sitting at 12–13 rather than 15 has to be a specific, named fact about
that particular deal (see Fermi's evidence file for a worked example: a retracted guarantor claim,
a repeat single-tenant concentration pattern, and a sharp cash drawdown immediately adjacent to the
signing).

**Projects currently scored 15/15 on Financial Commitment, flagged for re-check against this
explicit scale in the next refresh pass** (they were scored before the scale was written down, on
the same underlying judgment but without this checklist to audit against): Meta (El Paso, #9), Hut 8
(Beacon Point, #10), Riot Platforms (Corsicana, #12), Core Scientific (Denton, #16), Cipher Mining
(Barber Lake, #17 — re-scored 15 → 13 on 2026-09-28 after its lease amendment added named discount
factors), Energy Capital Partners + KKR/CyrusOne (Bosque County, #21). None of these are
known to be wrong — this is a consistency-audit flag, not a claim that any of them should move.

## Fourth Physical Commitment state — "applied, pending"

**Proposed 2026-09-23, revised 2026-09-25, adopted and applied 2026-09-28** (September audit; see
`corrections.md`). Applied to 3 projects: #6 Vantage/Frontier, #9 Meta/El Paso, #13 Google/Armstrong.

Since the Sept 21, 2026 directive, pending data center applications are paused pending the ERCOT
and TWDB audits; TCEQ reports compliance by Oct 19, 2026. Sources: [Office of the Governor,
2026-09-21](https://gov.texas.gov/news/post/governor-abbott-directs-tceq-to-halt-data-center-permits)
(primary); [Troutman Pepper Locke client alert](https://www.troutman.com/insights/governor-abbott-directs-tceq-to-halt-all-data-center-permits-pending-ercot-twdb-audits/), [Foley & Lardner client alert](https://www.foley.com/insights/publications/2026/09/texas-governor-abbott-directs-tceq-to-freeze-all-data-center-permits-in-a-whole-of-government-action/) — captured 2026-09-23.

**Criteria.** A dated *application on the merits* for the project's own generation or construction —
a TCEQ permit application, or a Public Utility Commission application for a dedicated generation
facility (for example, a certificate-of-convenience-and-necessity amendment) — naming the project's
site or a sponsor-controlled entity, with no grant, denial, or withdrawal on record. A PUC
application counts as a pending application on the same terms as a TCEQ one (decided 2026-09-28). A
Core Data Form or entity registration alone does not qualify: those are prerequisite
administrative steps, not an application on the merits.

Whether a given stalled application is delayed because of the September 21 directive specifically,
or for an ordinary review-queue reason unrelated to it, is generally **not observable from the
public record** — TCEQ's pending-application pages don't state a reason for a docket's silence.
The criteria above accordingly test only for the application's existence and undecided status, not
for why it's undecided. The directive is the reason this state is being added now, and the reason a
real "applied" case is more likely to sit undecided for a long stretch going forward — but it is
context for the proposal, not a term in the test itself.

**Score: 8 of 25** (standard scale, not renormalized — a real filing is observable evidence, not the
structurally-silent case §106.511 covers). Per `scored_table.csv` as of 2026-09-28, 8 sits below the
three 25/25 permits (Fermi, Crusoe Abilene, Poolside), equals CloudBurst's partial 8 (flood permit)
and exceeds PowerHouse Irving's partial 5 (building milestone). A pending application therefore
scores the same as, or more than, those two partial scores; both partial records are flagged as not
verified on the issuing portal. *(Corrected 2026-09-28: an earlier draft said 8 "sits below any
granted-permit score (5–25)," which was false.)* 8 mirrors the 8–10 "preliminary, not yet executed"
band already set for the analogous case in the Financial Commitment scale above.

This state is the mirror image of "not observable by category," not a variant of it: the §106.511
renormalization exists because a missing docket can be structurally uninformative — no notice
required, so silence proves nothing. Here a docket exists and is on record as undecided. Something
was found; it says "stuck," not "silent."

### Where it applies (2026-09-28)

| # | Project | Pending application | Status on the agency record, read 2026-09-28 | Physical | Total |
|---|---|---|---|---|---|
| 6 | Vantage — Frontier | TCEQ 182467 / PSDTX1692 / GHGPSDTX266 (VoltaGrid LLC) | "Status: PENDING"; technically complete and draft permit notice 2026-09-18 | 25 → 8 | 12 + 8 + 8 + 4 + 10 = 42 |
| 9 | Meta — El Paso | PUC Docket 59076 (El Paso Electric CCN amendment, McCloud Generation, 366 MW) | No final order; ALJ proposal for decision 2026-09-23 recommends approval "only if it is conditioned on EPE holding its customers harmless" | 22 → 8 | 25 + 8 + 15 + 15 + 20 = 83 |
| 13 | Google — Armstrong County | TCEQ 182880 / PSDTX1698 / GHGPSDTX268 (Crusoe Energy Systems LLC, "Goodnight") | "Status: PENDING"; working draft permit review 2026-08-28, modeling audit 2026-09-21 | 25 → 8 | 15 + 8 + 5 + 7 + 20 = 55 |

All three had been scored as confirmed permits before 2026-09-28. That was a method gap, not new
information: the applications were already pending at the 2026-08-05 capture. None of the three
TCEQ/PUC records shows a hold since the 2026-09-21 directive.

### The true-zero projects, checked against this state

Checked 2026-09-23 and again 2026-09-28. **Only 1 of 21 is a true zero as of 2026-09-28: Tract.**

- **#3 Poolside / Project Horizon — not a true zero (corrected 2026-09-28).** The 2026-09-23 check
  found only a TCEQ Core Data Form and concluded "true zero." It missed the permit behind it:
  Poolside LF Phase 2 DC OPS LLC holds TCEQ Electric Generating Units standard permit 183235, issued
  2026-03-12, for twelve gas turbines totaling 332.28 MW (6 × 30.34 + 6 × 25.04). Physical 0 → 25;
  total 15 + 25 + 2 + 7 + 2 = 51 (Progressing). A separate operating permit is still required. See
  `evidence/03-poolside-project-horizon.md`.
- **#4 Tract / Data Center Technology Park, Caldwell County.** No filing found naming Tract or its
  Caldwell County reinvestment-zone site, searched 2026-09-23. One document surfaced by search under
  Caldwell County's own permit records (Air Quality Permit No. 151716) is explicitly labeled
  "EXAMPLE A" by TCEQ itself — a template notice the county hosts for public education, for an
  unrelated concrete batch plant, dated 2020. Not evidence of anything. Consistent with Tract having
  no named operator or tenant yet, per the existing evidence file — there is no party positioned to
  have filed anything. Remains true zero.
  - Recomputed score: unchanged, Site 18 + Physical 0 + Financial 8 + Incentive 0 + Track Record 14
    = **40** (Progressing — exactly the published figure).
- **#8 SB Energy / Stargate Milam County — re-sorted 2026-09-26** to "not observable by category"
  after its S-1 (see `corrections.md`). Its only TCEQ authorization, PBR 183969 under §106.511, is a
  registration, not an application. (20 + 12 + 7 + 8) ÷ 75 × 100 = 62.67 → 63.

## Method change log

- **2026-09-28:** Added and applied Physical state "applied, pending" (8/25), drafted 2026-09-23
  after a reader's point about the Sept 21, 2026 TCEQ directive. A PUC application for dedicated
  generation counts as a pending application. Applied to #6 Vantage (59 → 42), #9 Meta (97 → 83) and
  #13 Google Armstrong (72 → 55).
- **2026-09-28:** Registry matches are labeled by table: §151.3595 ("Registered Qualifying Large
  Data Center Projects") or §151.359 ("Registered Qualifying Data Center Projects"). Scoring rule
  unchanged (registry-only caps at 7/15).
- **2026-09-28:** Incentive full credit (15) confirmed to require an executed local agreement, or
  minutes recording approval and authorization to execute; news reports are leads only. See the
  September audit entry in `corrections.md` for the four projects this moved.

## Known limitations (v0)

- **No CAD/deed record was independently pulled.** See above — this is the single biggest
  reliability caveat on the Site Control signal across the dataset.
- **The Google Haskell County site identity is unresolved.** "Journey," "Thelma," and a registry
  entry for "Fort Haskell Data Center" may or may not describe the same facility; a third,
  separate Crusoe Energy proposal in the same county had its abatement request rejected by the
  same commissioners court. Project #14 is scored using only the "Journey" evidence, the most
  documented candidate, and is marked ambiguous rather than resolved.
- **Two MW figures are genuinely undisclosed** (Google's Armstrong and Haskell County campuses,
  bundled into one statewide $40B/6,200MW+ PPA announcement) and excluded from MW arithmetic in
  `key-stats.md`.
- **There is no public registry to check any project's ERCOT interconnection status against.**
  Every ERCOT-approval claim in this dataset is the sponsor's own word, taken at face value where
  no counter-evidence exists. See `candidate_universe.md`'s market-opacity finding.
- **Sponsor Track Record is unevenly researched.** Several sponsors (Provident, CloudBurst/Evolve,
  Vantage, Aligned, CyrusOne) got a general-reputation assessment rather than cited-instance
  evidence, simply because this session's search budget ran out before a deeper pass on each. That
  shows up as a mid-range rather than a definitive score, and is marked as such in the evidence
  appendix.
- **Scoring judgment calls were made explicit, not hidden.** Two examples: Tract's founder-level
  track record (real, cited, but not the same as the company itself having delivered a site under
  this specific land-developer model) was scored as partial credit rather than zero or full marks;
  a project "topped out" reaching a construction milestone (PowerHouse/Irving) was treated as real,
  standard-scale physical-commitment evidence, distinct from an unverified inference that a
  facility "probably" holds permits because it's operating (Core Scientific and Marathon both fall
  into that latter case — no docket was found for either, and rather than guess, both were sorted
  into the "not observable by category" bucket and renormalized, on the judgment that their
  established, long-operating sites plausibly run on permit-by-rule-covered backup generation
  rather than nothing at all).
- **Renormalization makes 12 of 21 scores non-comparable, signal-for-signal, to the other 9.** This
  is a deliberate tradeoff, documented above, not an oversight. If you'd rather see all 21 on a
  strictly identical basis, the flat-+5-credit and true-zero versions of these same 12 scores are
  preserved in the transparency table above and in `scored_table.md`.
