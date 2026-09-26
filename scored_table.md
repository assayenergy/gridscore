# GridScore v0 — Scored Table (Session 3, corrected + renormalized)

Scored per the five-signal rubric. Tiers: 70–100 Evidenced · 40–69 Progressing · 0–39
Announced-only. Two scoring regimes now coexist, both landing on the same 0–100 scale:

- **Standard /100** — used for the 11 projects with either a confirmed Physical Commitment
  finding (partial or full) or a genuine true zero. All 5 signals count, denominator is 100.
- **Renormalized /75** — used for the 10 projects whose generator setup plausibly qualifies for
  TCEQ permit-by-rule (§106.511) coverage, meaning a public docket's absence is structurally
  uninformative, not evidence of anything. Physical Commitment is **excluded from both the
  numerator and the denominator** rather than scored: `total = (Site + Financial + Incentive +
  Track Record) / 75 × 100`. Physical displays as **"n/o (§106.511)"** — not observed, not zero.

Per Vish's ruling: Incentive Filings scores cap at **7/15** when the only evidence is a §151.359
Qualifying Data Center registry match; an **executed JETI agreement or county/municipal
abatement** can score up to the full 15 — though no data center can hold a JETI agreement in the
first place (see the JETI-NAICS footnote in `key-stats.md`). No negative scoring is applied for
documented reversals — those are logged as a flag with citation, never subtracted.

**Correction (2026-08-05, pre-publication check):** this table was previously left sorted in an
order computed before the renormalization pass — Riot (80) was listed above Haskell/Journey (87),
and Core Scientific (76) was listed near the bottom of the Evidenced band instead of near the top.
Re-sorted below by total score, descending, ties sharing a rank. No scores changed, only the order.

**Correction (2026-09-21 Fermi refresh):** Fermi's row is updated below — Financial 5→12,
Incentive 7→15, Track Record unchanged at 3, total 65→80, tier Progressing→Evidenced. The Incentive
change is a correction to a research miss (an executed Carson County tax abatement existed since
2025-10-27 and was missed originally), not new information; the Financial change reflects genuinely
new evidence since Aug 5 (a first binding customer lease, closed convertible notes, confirmed
capex). See `evidence/01-fermi-america-project-matador.md` for the full citation trail, including
two corrected/removed claims from the prior draft (a misattributed 8-K accession, and litigation
that had the moving party backwards).

| Rank | Project | Sponsor | County | MW | Site (25) | Physical (25) | Financial (15) | Incentive (15) | Track Record (20) | **Total** | Scoring basis | Tier | Reversal |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | El Paso AI Data Center | Meta | El Paso Co. | 1,000 | 25 | 22 | 15 | 15 | 20 | **97** | standard /100 | Evidenced | — |
| 2 | Panhandle — Haskell Co. ("Journey") | Google | Haskell Co. | n/d | 20 | n/o (§106.511) | 10 | 15 | 20 | **87** | renormalized /75 | Evidenced | — |
| 3 | Project Matador (HyperGrid) | Fermi America | Carson Co.* | 11,000 | 25 | 25 | 12 | 15 | 3 | **80** | standard /100 | Evidenced | **YES** |
| 3 | Corsicana Facility | Riot Platforms | Navarro Co. | 1,000 | 22 | 20 | 15 | 7 | 16 | **80** | standard /100 | Evidenced | — |
| 5 | Denton Campus | Core Scientific | Denton Co. | 391 | 25 | n/o (§106.511) | 15 | 7 | 10 | **76** | renormalized /75 | Evidenced | — |
| 6 | Abilene Campus | Crusoe/Lancium | Taylor Co. | 2,100 | 12 | 25 | 10 | 7 | 18 | **72** | standard /100 | Evidenced | — |
| 6 | Panhandle — Armstrong Co. | Google | Armstrong Co. | n/d | 15 | 25 | 5 | 7 | 20 | **72** | standard /100 | Evidenced | — |
| 6 | Barber Lake | Cipher Mining | Mitchell Co. | 300 | 22 | 12 | 15 | 7 | 16 | **72** | standard /100 | Evidenced | — |
| 9 | Childress Campus | Crusoe/Lancium | Childress Co. | 1,000 | 15 | n/o (§106.511) | 8 | 7 | 18 | **64** | renormalized /75 | Progressing | — |
| 10 | Stargate Milam County | SB Energy (SoftBank) | Milam Co. | 1,200 | 20 | n/o (§106.511) | 12 | 7 | 8 | **63** | renormalized /75 | Progressing | — |
| 11 | Beacon Point | Hut 8 | Nueces Co. | 1,000 | 10 | n/o (§106.511) | 15 | 7 | 14 | **61** | renormalized /75 | Progressing | — |
| 12 | Frontier | Vantage Data Centers | Shackelford Co. | 1,400 | 12 | 25 | 8 | 4 | 10 | **59** | standard /100 | Progressing | — |
| 13 | Garden City Facility | Marathon Digital | Glasscock Co. | 200 | 22 | n/o (§106.511) | 5 | 0 | 9 | **48** | renormalized /75 | Progressing | — |
| 14 | Project Caprock | Aligned Data Centers | Hale Co. | 540 | 10 | n/o (§106.511) | 6 | 7 | 10 | **44** | renormalized /75 | Progressing | — |
| 15 | Data Center Technology Park | Tract | Caldwell Co. | 2,000 | 18 | 0 (true zero) | 8 | 0 | 14 | **40** | standard /100 | Progressing | — |
| 15 | Bosque County Campus | ECP+KKR/CyrusOne | Bosque Co. | 190 | 5 | n/o (§106.511) | 15 | 0 | 10 | **40** | renormalized /75 | Progressing | — |
| 17 | Grand Prairie Campus | PowerHouse/Provident | Ellis Co. | 1,800 | 10 | n/o (§106.511) | 6 | 0 | 8 | **32** | renormalized /75 | Announced-only | — |
| 18 | San Marcos Data Center I | CloudBurst/Evolve | Hays/Guadalupe Co. | 1,200 | 12 | 8 | 10 | 0 | 0 | **30** | standard /100 | Announced-only | — |
| 19 | Irving Campus | PowerHouse Data Centers | Dallas Co. | 201 | 10 | 5 | 5 | 0 | 8 | **28** | standard /100 | Announced-only | — |
| 20 | Project Horizon | Poolside AI | Pecos Co. | 2,000 | 15 | 0 (true zero) | 2 | 7 | 2 | **26** | standard /100 | Announced-only | **YES** |
| 21 | Kaufman County Campus | Prometheus Hyperscale | Kaufman Co. | 200 | 8 | n/o (§106.511) | 5 | 0 | 6 | **25** | renormalized /75 | Announced-only | — |

*Fermi's county assignment (Carson primary vs. Potter/Randall touching) is unresolved. n/d = MW not
disclosed per-site. ⬆ = moved up a tier under renormalization vs. the prior flat-+5-credit
treatment. Table re-sorted by total score; rank ties broken alphabetically, not meaningfully
ordered.

## Transparency table — every score/tier that differs, flat-+5-credit vs. renormalized

This is the diff between the *previous* correction (a flat +5 points added to Physical
Commitment, scored out of 100 as before) and the *current* renormalization (Physical excluded
entirely, total computed out of the remaining 75 points). Only the 9 NOC projects are affected;
the other 12 are identical under both treatments.

| Project | Flat-+5 total (/100) | Renormalized total (/75→100) | Flat tier | Renormalized tier |
|---|---|---|---|---|
| Grand Prairie Campus (PowerHouse/Provident) | 29 | 32 | Announced-only | Announced-only |
| Beacon Point (Hut 8) | 51 | 61 | Progressing | Progressing |
| Childress Campus (Crusoe/Lancium) | 53 | 64 | Progressing | Progressing |
| Panhandle — Haskell Co. ("Journey") | 70 | **87** | Evidenced | Evidenced (now solid, not boundary-fragile) |
| **Project Caprock (Aligned)** | 38 | **44** | Announced-only | **Progressing** |
| **Denton Campus (Core Scientific)** | 62 | **76** | Progressing | **Evidenced** |
| Garden City Facility (Marathon) | 41 | 48 | Progressing | Progressing |
| Kaufman County Campus (Prometheus) | 24 | 25 | Announced-only | Announced-only |
| **Bosque County Campus (ECP+KKR/CyrusOne)** | 35 | **40** | Announced-only | **Progressing** |

**Three additional tier changes emerged from renormalization that the flat-credit version missed**:
Aligned and ECP+KKR both cross from Announced-only into Progressing, and Core Scientific crosses
from Progressing into Evidenced. In every case the direction is the same — renormalization is more
generous than a flat +5 whenever a project's *other four* signals are strong relative to 75 points,
because those points now carry more relative weight once Physical stops diluting the denominator.
Google/Haskell ("Journey") goes from sitting exactly on the Evidenced floor (70, fragile) to
comfortably inside it (87) — a materially different confidence read on the same underlying facts.

**Tier tallies, prior version (before the 2026-09-21 Fermi refresh):** Evidenced 7 · Progressing 8
· Announced-only 6. **After the Fermi refresh (2026-09-21): Evidenced 8 · Progressing 7 · Announced-only
6.** Fermi moved Progressing→Evidenced (65→80); no other project changed that pass. **Current, after
the SB Energy re-score (2026-09-26): Evidenced 8 · Progressing 8 · Announced-only 5.** SB Energy moved
Announced-only→Progressing (36→63); see `corrections.md`.

## Reversal flags (informational only — not scored as penalties)

- **Fermi America (Project Matador) — expanded 2026-09-21:** original reversal unchanged ($150M
  tenant funding pact cancelled 2025-12-12, stock down 33.8% same day, one securities class action, *Lupia v. Fermi Inc. et al.*,
  No. 1:26-cv-00050 S.D.N.Y., filed 2026-01-05; corrected 2026-09-26, see corrections.md). Since Aug 5: CEO Neugebauer
  terminated **for Cause** (2026-04-30, 8-K/A accession 000121390026050183); CFO Everson resigned
  (2026-04-19); Everson separately resigned **from the board** (2026-07-10, 8-K accession
  000121390026077385) over a records-access/Finance-Committee dispute; *Neugebauer v. Fermi Inc. et
  al.* (Cause No. 26-BC01B-0034, Business Court of Texas, amended 2026-09-21 to add 3 directors) and
  *Fermi Inc. v. Neugebauer* (No. 5:2026cv00100, N.D. Tex., TRO denied); a reported, unconfirmed
  (Bisnow) subpoena for Project Matador/former-management records. Counterweight, same window: first
  binding customer lease (TensorWave) and first hardware on-site. Full citations in
  `evidence/01-fermi-america-project-matador.md`.
- **Poolside (Project Horizon):** CoreWeave's 250MW anchor lease terminated ~late March 2026 after
  Poolside's $2B Series C failed to close; project reported scaled to a 400MW revival with no
  replacement tenant as of July 30, 2026. See `evidence/03-poolside-project-horizon.md`.

## Re-refreshed near-boundary watchlist — press-reported-only site control, within ~5 of a cutoff

Recomputed on the renormalized totals. This list changed again from the prior version: Aligned
newly qualifies (its renormalized total moved closer to 40), and **ECP+KKR/CyrusOne now sits
exactly on the Progressing floor at 40** — both artifacts of renormalization lifting NOC projects
more than the flat credit did.

| Project | County | Total | Boundary | Distance |
|---|---|---|---|---|
| **Data Center Technology Park (Tract)** | Caldwell Co. | 40 | Progressing floor | exactly on it |
| **Bosque County Campus (ECP+KKR/CyrusOne)** | Bosque Co. | 40 | Progressing floor | exactly on it |
| **Abilene Campus (Crusoe/Lancium)** | Taylor Co. | 72 | Evidenced floor | +2 |
| **Panhandle — Armstrong Co. (Google)** | Armstrong Co. | 72 | Evidenced floor | +2 |
| **Project Caprock (Aligned)** | Hale Co. | 44 | Progressing floor | +4 |
| *Childress Campus (Crusoe/Lancium) — just outside the ~5 window* | Childress Co. | 64 | Evidenced floor | −6 (noting it since it's close, not a strict qualifier) |

Excluded from this specific cut because their site-control confidence is government-record, not
press-reported-only, even though their totals are also near a cutoff: SB Energy (63, re-scored from
36 on 2026-09-26, see `corrections.md`; government-record via SEC exhibit; 70 − 63 = 7 below the
Evidenced floor, just outside the ~5 window), Google/Haskell (87, government-record, no
longer boundary-fragile after renormalization), Marathon (48, government-record, not close to a
cutoff under the new total).

## Google Haskell County identity resolution (30-minute time-box, per Vish's instruction)

Unchanged from the prior write-up — still genuinely unresolved:

- **"Journey"** (north Haskell) and **"Thelma"** (south Haskell) are two distinct, real,
  Google-linked sites developed by "Housebound Group" / "Homebound Group LLC." Journey has a
  confirmed Haskell County Commissioners Court tax abatement, approved 2025-06-24, with ~$1B
  Phase 1 capex disclosed in the court record itself. [Court filing PDF](https://newtools.cira.state.tx.us/upload/page/9220/docs/Homebound%20Group%20LLC.pdf), [DCD](https://www.datacenterdynamics.com/en/news/google-linked-housebound-group-files-for-two-data-center-projects-in-haskell-texas/) — captured 2026-08-05.
- The §151.359 registry's "Fort Haskell Data Center" entry (eff. 2024-01-16) does not obviously
  correspond to either name and predates the Nov 2025 Google announcement.
- **A third, separate Haskell County data-center project — sponsored by Crusoe Energy — had its
  tax abatement request formally REJECTED** by the same commissioners court (4-0 vote, June 9).
  Not one of the 21 scored projects; out of scope for this session.

**Resolution applied:** Project #14 (renumbered #3 by rank in the table above) is scored using
only the verifiable "Journey" evidence. Site identity is marked ambiguous in the public record —
though renormalization has made the *total score* materially less sensitive to that ambiguity than
it was under the flat-credit treatment (87 vs. a prior 70-exactly-on-the-floor).
