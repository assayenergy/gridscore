# GridScore v0 — Session 2 Evidence Summary (pre-scoring)

All 21 projects dug across the five signals, batched by source type (CAD/site-control search →
TCEQ/physical → financial/ERCOT-SEC-PUC → JETI/incentive → sponsor track record). Full detail in
`evidence/*.md` per project and `scoring_rubric_template.csv`. **No scores applied yet** — this
is a coverage/quality summary for review before Session 3.

Legend: ● strong evidence · ◐ partial/self-reported · ○ no public evidence found (dead end) · ◌ inconclusive (needs manual verification) · ▲ evidence found but negative/adverse

| # | Project | Site Control | Physical | Financial | Incentive | Sponsor Track Record |
|---|---|---|---|---|---|---|
| 1 | Fermi America — Matador | ● (TTU leasehold) | ● (TCEQ approved) | ▲ (funding cancelled) | ○ | ▲ (no ops history, lawsuit) |
| 2 | Crusoe/Lancium — Abilene | ◐ | ● (TCEQ approved) | ◐ | ◌ (registry match, unverified) | ● (fast delivery) |
| 3 | Poolside — Horizon | ◐ | ○ (wrong project surfaced) | ▲ (anchor lease terminated) | ◌ | ▲ (lost tenant + funding) |
| 4 | Tract — Caldwell | ● | ○ (no tenant yet — expected) | ◐ | ○ | mixed (strong founder / zero co. delivery) |
| 5 | PowerHouse/Provident — Ellis | ◐ | ○ | ◐ (self-disclosed only) | ○ | ◐ |
| 6 | Vantage — Frontier | ◐ | ● (TCEQ docket) | ◐ | ◌ | ◐ (general reputation) |
| 7 | CloudBurst — San Marcos | ◐ | ◐ (1 of 2 permits) | ◐ | ○ | not researched |
| 8 | SB Energy — Milam | ● (inferred via deed/LLC) | ○ | ◐ | ○ | mixed (solar strong / DC record zero) |
| 9 | Meta — El Paso | ● | ● (PUC filing) | ● | ● | ● (strongest tier) |
| 10 | Hut 8 — Beacon Point | ◐ | ◐ (unusual jurisdiction claim) | ● (SEC 8-K) | ○ | ◐ (short history) |
| 11 | Crusoe/Lancium — Childress | ● | ○ | ◐ (self-disclosed) | ● (named match) | ● (direct precedent) |
| 12 | Riot — Corsicana | ● (SEC trail) | ● (TDLR permit) | ● (strongest — 3rd-party corroborated) | ● (named match) | ● (auditable) |
| 13 | Google — Armstrong Co. | ● | ● (direct TCEQ tie) | ◐ (statewide only) | ◌ | ● (strongest tier) |
| 14 | Google — Haskell Co. | ◐ (naming ambiguity) | ○ | ◐ (statewide only) | ◌ | ● (strongest tier) |
| 15 | Aligned — Caprock | ◐ | ○ | ◐ | ● (named match) | ◐ (general reputation) |
| 16 | Core Scientific — Denton | ● (city council confirmed) | ○ | ● | ◌ | mixed (bankruptcy history) |
| 17 | Cipher — Barber Lake | ● | ◐ (portable-plant only) | ● | ● (named match) | ● (auditable) |
| 18 | PowerHouse — Irving | ◐ | ◐ | ◐ | ○ | ◐ |
| 19 | Marathon — Garden City | ● | ○ | ◐ | ○ (confirmed non-match) | mixed (restatements vs. clean ops) |
| 20 | Prometheus — Kaufman | ◐ | ○ | ◐ | ○ | mixed (no founder DC background) |
| 21 | ECP+KKR/CyrusOne — Bosque | ○ (location only) | ○ | ● | ◌ | ◐ (general reputation) |

## Headline findings

1. **Zero of 21 projects have an active JETI Act agreement.** Checked directly against the
   Comptroller's current-agreements list (9 active statewide, none in this sector). This is a
   real, confirmed finding — not a search failure — and probably belongs in the publication:
   the headline incentive program isn't where these projects' incentives are actually showing up.
2. **A different, adjacent state program is where the incentive trail actually lives.** The
   Comptroller's "Qualifying Data Center" registry (Tax Code §151.359 sales-tax exemption —
   distinct from JETI) directly named 8 of the 21 projects, several by exact facility name
   (Cipher's "Barber Lake," Aligned's "Abernathy (LBB01)," Lancium's "Childress"). This is a
   different signal than the spec's #4 definition (JETI/Ch.403/county abatement) — logged
   separately in each evidence file, not conflated with it. **Caveat: these registry matches came
   from an AI-summarized page fetch, not a manual read of the raw table — worth a manual
   confirmation pass before the numbers go in scoring**, since several (Vantage, Google, Core
   Scientific, CyrusOne) couldn't be pinned to the specific county in this list.
3. **County/municipal abatements are the real incentive-filing signal for at least 2 projects** —
   Meta (El Paso city + county, 25-year 80% abatement, survived a repeal vote) and CoreWeave's
   Bastrop County abatement (not in the 21, but useful precedent showing this pattern exists and
   is findable when it's there).
4. **Two projects show a documented negative reversal since announcement**, not just "thin
   evidence": Poolside's Project Horizon lost its anchor tenant and funding round, and Fermi
   America has a cancelled tenant funding pact, an 65-80% stock decline, and an open class-action
   lawsuit. Both are exactly the kind of "announced ≠ real" cases the publication is built to
   surface — and both were kept on the list per your instruction to score evidence, not vibes.
5. **The clearest site-control evidence in the universe comes from deals with a named, public
   counterparty** — Meta/Wurldwide LLC (City of El Paso), Fermi/TTU (Texas Tech University
   System), Core Scientific (City of Denton council minutes) — because a government counterparty
   leaves a paper trail private-to-private land deals don't. SB Energy's Milam County deed is the
   best example of the spec's "affiliate LLC traceable via filing" pattern working as intended.
6. **CAD portal access was a hard blocker this entire session**, not just a Tract/Caldwell issue.
   The browser tool timed out on the one live attempt (Carson CAD) and wasn't usable for the rest;
   generic web search cannot reach dynamic county parcel-search forms. Every "site control"
   finding above is sourced from press/SEC/company disclosure or a government body's own minutes
   — not from a single county appraisal district record pulled directly. This is worth fixing
   (working browser access, or manual CAD lookups) before treating site-control evidence as final.
7. **Physical commitment (TCEQ) is the strongest-populated signal** for the biggest projects (7 of
   21 have a real docket number), because the biggest sites' gas-turbine buildouts are exactly
   what triggers TCEQ's public-notice process. It's the weakest-populated signal for mid-size and
   smaller projects (9 of 21: no evidence found) — plausibly because smaller/behind-the-meter
   generator arrays can qualify for permit-by-rule with no individual public notice (flagged by
   multiple sources this session, e.g. Texas Tribune, University of Houston Law Center) — that
   itself is a documented finding about the permitting system, not a data gap to apologize for.
8. **Google's Haskell County entry (#14) has an unresolved naming ambiguity** ("Journey" vs.
   "Thelma" vs. a 2024 "Musselman Tech" acquisition) that should be resolved before scoring —
   it may bear on whether the dropped-third-site decision in `candidate_universe.md` still holds.

## What's genuinely unresolved and needs a decision before Session 3

- Manual verification of the Comptroller Data Center registry raw table (item 2 above) —
  I can do this now if you want it before scoring, or flag it as a scoring-time caveat.
- Google Haskell naming ambiguity (item 8).
- Whether "Qualifying Data Center" registry entries should count toward the rubric's Incentive
  Filings signal at all, given they're a different statute than JETI/Ch.403 — my inclination is
  no (score them 0 for signal #4, but cite the registry match as context in the evidence
  appendix), but this is your call on how strictly to read the rubric.
