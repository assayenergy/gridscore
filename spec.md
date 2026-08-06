# GridScore v0 — Spec & Session Brief
*Drop into the new `gridscore` project folder as `spec.md`. Source of truth for all sessions.*

## What we are building
A published, evidence-linked **readiness score** for the 20 largest publicly announced data center projects seeking ERCOT interconnection. One-shot manual/assisted compilation — no pipelines, no app. Output feeds publication piece two ("Scoring what's real in the 438 GW queue") on the FlexValue Substack.

## The core rule (non-negotiable)
This scores **projects on public evidence**, not companies on character. Every scored signal MUST have a linked public source and a capture date. No evidence = signal scores zero with status "no public evidence found (as of DATE)" — which is explicitly NOT a claim that the thing doesn't exist. All published language must reflect this framing. When evidence is ambiguous, score conservatively and flag it.

## The five signals (v0 weights — Vish may tune)
1. **Site control — 25 pts.** County appraisal district (CAD) / deed records showing the sponsor or a traceable affiliate owns or controls the announced site. Full points: recorded ownership/lease. Partial: option/affiliate LLC traceable via filings. Sources: county CAD online searches, county clerk records.
2. **Physical commitment — 25 pts.** TCEQ air permits for backup generators at the site (the strongest single "this is real" signal), plus building permits where findable. Sources: TCEQ permit database (public, searchable), municipal permit portals.
3. **Financial commitment — 15 pts.** Posted interconnection/study fees, executed interconnection agreements, or financing disclosures. Sources: ERCOT/PUC filings where visible, SEC filings, municipal utility board minutes.
4. **Incentive filings — 15 pts.** JETI Act / Chapter 403 (former 313) applications or county abatement agreements disclosing MW, capex, timeline. Sources: Texas Comptroller JETI database, county commissioners court records.
5. **Sponsor track record — 20 pts.** Has this sponsor energized announced projects before, at claimed scale, roughly on claimed timelines? Sources: SEC filings, prior project press vs. delivery record. Score the pattern, cite the instances.

**Tiers:** 70–100 = **Evidenced** · 40–69 = **Progressing** · 0–39 = **Announced-only**. (Deliberately neutral tier names — not "real/fake.")

## Session plan
**Session 1 — Universe + rubric.** Compile the candidate list: the 20 largest publicly announced ERCOT-bound data center projects (news, press releases, trade press, ERCOT county-level aggregates as cross-check). For each: sponsor, county, announced MW, announcement date, source links. Encode the rubric as a scoring template (CSV/sheet). STOP for Vish's confirmation of the 20 before any digging.

**Session 2 — Evidence digging (the long one).** For each confirmed project, work the five signals in order. Log per signal: evidence found (URL + date + one-line description) or "no public evidence found (as of DATE)". Maintain an evidence.md per project. Batch by source type (all TCEQ searches together, all CAD searches together) — faster than project-by-project. Flag every inference (e.g., affiliate-LLC land ownership) as inferred, not confirmed.

**Session 3 — Scoring + outputs.** Apply the rubric. Produce: scored table (CSV + markdown), tier assignments, per-project evidence appendix, a key-stats.md (aggregate MW by tier, % of announced capacity that is Announced-only, most/least evidenced megaprojects), and a methodology.md in the same open style as FlexValue's. No essay prose.

## Practical notes for the agent
- CAD and TCEQ interfaces vary by county and are clunky; when a search dead-ends, log HOW it dead-ended (searched X for Y, zero results) — that's part of the evidence trail.
- Affiliate LLC tracing: data center sponsors routinely buy land through SPVs; check Texas SOS entity records to connect LLC names to sponsors, and mark such connections "inferred via entity records."
- Capture dates on everything. The published claim is "as of [date]," and the PUC's transparency rules landing by Dec 2026 will let future versions re-score with better data.
- If a project's announced location is too vague to search records against (no county/site identifiable), score what's searchable and flag "location unverifiable from public announcements" — that itself is signal.

## Vish's decisions
1. Confirm the 20-project list after Session 1 (before digging starts).
2. Signal weights (defaults above).
3. Tier names/cutoffs (defaults above).
