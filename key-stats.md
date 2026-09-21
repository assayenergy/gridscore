# GridScore v0 — Key Stats

All figures as of 2026-09-21 (updated from the original 2026-08-05 baseline by a full evidence
refresh of Fermi America/Project Matador — see `evidence/01-fermi-america-project-matador.md`),
from the 21-project scored universe (`scored_table.csv`), reflecting the **renormalized** Physical
Commitment treatment (Physical excluded from both numerator and denominator for the 9 projects
whose generator setup plausibly qualifies for TCEQ permit-by-rule; total = other-four-signals / 75
× 100 — see `methodology.md` for the full rule and `scored_table.md` for the diff against the
earlier flat-+5-credit version). MW figures used are the largest publicly stated announced figure
per project (see `candidate_universe.md`; Fermi's ledger value is intentionally held at its
original 11,000 MW announcement, not the company's since-upsized 17,000 MW marketing claim — see
the evidence file); 2 of 21 projects (Google's Armstrong and Haskell County campuses) have no
disclosed per-site MW and are excluded from MW arithmetic below, noted separately.

**2026-09-21 update:** Fermi's score moved from 65 (Progressing) to 80 (Evidenced) — Financial
Commitment 5→12 (genuinely new evidence: a first binding customer lease, closed convertible notes,
confirmed capex) and Incentive Filings 7→15 (a correction: an executed Carson County tax abatement
existed since 2025-10-27 and was missed in the original research pass). Sponsor Track Record is
unchanged at 3/20 — the governance turmoil and litigation since Aug 5 are logged as an expanded
reversal flag, not a track-record score change, since the signal's own test (has anything been
energized) is untouched by them. Every number below reflects this update; the August counterfactual
section isolates what the correction alone (without the new Financial evidence) would have meant.

## Lead context: the Aug 3, 2026 Abbott directive

**On August 3, 2026, Governor Greg Abbott directed the Public Utility Commission of Texas and
ERCOT to conduct a comprehensive verification and audit of every data center project advancing
through ERCOT's interconnection process**, before any of them proceed further. The directive
requires PUCT and ERCOT to verify each project's power demand, water use, public financial
assistance received, community protections, and ownership — and to report the extent to which
data centers are paying their own way versus depending on the state, and providing their own
power versus depending on the ERCOT grid. ERCOT paused its "batch zero" interconnection review the
same week in response. Projects that fail to meet PUCT, ERCOT, or state requirements are to be
denied a grid connection. [Texas Tribune](https://www.texastribune.org/2026/08/03/texas-data-center-project-audit-greg-abbott/), [Houston Public Media](https://www.houstonpublicmedia.org/articles/news/energy-environment/2026/08/03/558529/gov-greg-abbott-pauses-new-data-centers-until-ercot-puct-audit-energy-water-usage/), [Governor's office](https://gov.texas.gov/news/post/governor-abbott-directs-comprehensive-data-center-audit) — captured 2026-08-05.

This is the regulatory backdrop the rest of this document sits inside: two days before this
dataset was compiled, the state itself formalized the exact question this project is trying to
answer at the project level — which of these announcements reflect verifiable, dispatchable,
paid-for infrastructure, and which don't. GridScore is not a substitute for that audit and has no
access to the non-public data PUCT/ERCOT can compel; it's a public-record-only companion exercise,
and should be read as such.

## The approval-to-energize funnel (exact figures, no rounding)

Sourced directly from ERCOT's own **Monthly Operational Overview (June 2026)**, published
2026-07-16 — read as raw PDF text, not an AI-summarized pass, per the same discipline applied to
the Comptroller registry:

> "Of the **8,926 MW** that have received Approval to Energize, ERCOT has observed a
> non-simultaneous monthly peak consumption of **3,966 MW** in June 2026, which is a slight
> decrease since May 2026." — ERCOT Monthly Operational Overview, June 2026, p.10.

That 3,966 MW is calculated as the sum of each individual approved load's own monthly peak — it
is ERCOT's own stated estimate of "how much approved load ERCOT believes is now operational,"
not a modeled or inferred figure. Both numbers come from ERCOT's **Large Load Interconnection
Queue** specifically (a separate ERCOT tracking system from the *generator* interconnection queue,
which is a different 462,785 MW figure covering power *plants*, not loads — the two are not
interchangeable and this document does not conflate them).

For the size of the full large-load request queue those 8,926 MW sit inside, the most-cited,
independently corroborated figure across multiple outlets (Utility Dive, Latitude Media, Market
Business News) is **~474.7 GW as of June 2026** (up from ~226 GW in November 2025) — a press-reported
figure, not one this session independently re-derived from ERCOT's own stacked-category chart on
the same page, which uses a by-year-of-expected-energization framing that isn't a simple
apples-to-apples match to a single "total queue" number. Flagging that distinction rather than
blending the two sourcing types into one implied-precise figure.

Put plainly: of a queue on the order of ~474.7 GW, ERCOT has approved **8,926 MW (1.9%)** to
energize, and observes only **3,966 MW (0.8%)** actually drawing power. Whatever the real size of
the "AI data center boom" in Texas turns out to be, the share of it that is currently operating,
by ERCOT's own operational count, rounds to less than one percent of the announced pipeline.

## Tier counts and aggregate MW (as of 2026-09-21, post-Fermi-refresh)

| Tier | # of projects | Aggregate announced MW (19 projects w/ disclosed MW) |
|---|---|---|
| Evidenced (70–100) | 8 | 15,791 MW |
| Progressing (40–69) | 7 | 6,330 MW |
| Announced-only (0–39) | 6 | 6,601 MW |
| **Total** | **21** | **28,722 MW** (across 19 MW-disclosed projects; 2 undisclosed — both in the Evidenced tier: Google's Armstrong and Haskell County campuses) |

Fermi moved Progressing→Evidenced this refresh (65→80), carrying its 11,000 MW ledger value with
it — that single move is why Evidenced is now the *largest* MW tier in the universe (15,791 MW)
rather than the smallest (4,791 MW as of the prior key-stats.md version). Before this move, tier
composition had shifted twice for other reasons (see `scored_table.md`'s transparency table): the
Physical Commitment renormalization crossed Core Scientific into Evidenced and Aligned/ECP+KKR into
Progressing.

## % of announced capacity that is Announced-only

**6,601 / 28,722 MW = 23.0%** — **unchanged by the Fermi refresh.** Fermi was never in the
Announced-only tier, so its move between Evidenced and Progressing has zero effect on this figure.
It's down from 26.2% at the start of the Physical Commitment correction pass and 25.5% under the
interim flat-credit version, for reasons unrelated to Fermi (Marathon, then Aligned and ECP+KKR,
moved out of Announced-only across those two corrections).

## The August counterfactual — what if the abatement had been caught on Aug 5?

Isolating just the incentive-filing correction (the Carson County abatement existed since
2025-10-27 and was missed originally) from the genuinely-new Financial Commitment evidence found
this refresh: Fermi's Aug-5-vintage score would have been **73** (Site 25 + Physical 25 + Financial
5 + Incentive 15 + Track 3), not 65 — **Progressing→Evidenced on the correction alone**, before any
of the September news. Because this counterfactual lands Fermi in the same tier (Evidenced) at the
same MW value (11,000, held) as today's actual 80, **the effect on tier counts and MW-by-tier is
identical to the table above** — Evidenced 8/15,791 MW, Progressing 7/6,330 MW, Announced-only
unchanged at 6/6,601 MW. The **23% Announced-only headline does not change** under this
counterfactual either, for the same reason it doesn't change today: Fermi was never in that tier.
The +7-point gap between the 73 counterfactual and the actual 80 is entirely the Financial
Commitment signal, and is genuinely new information from the last six weeks, not something a more
careful Aug 5 pass would have caught.

**Sensitivity note, updated:** Fermi's 11,000 MW is now inside the Evidenced tier, not Progressing.
Stripping it out of Evidenced instead: Evidenced drops to 4,791 MW, and Announced-only's share of
the *remaining* 17,722 MW-disclosed universe (excluding Fermi entirely) is 6,601/17,722 = **37.3%**
— unchanged from the prior version of this note, since that calculation was always about removing
Fermi from the *numerator's* base regardless of which tier it sat in. Whether to report the 23%
headline with or without this one outsized project remains a real editorial choice.

## Most / least evidenced megaprojects

- **Most evidenced: Meta's El Paso AI Data Center — 97/100.** Full or near-full marks on all five
  signals: a council-approved land sale to a named SPV, a PUC-filed dedicated power plant, an
  escalating $10B investment disclosure, an executed 25-year municipal + county tax abatement that
  survived a repeal vote, and the deepest hyperscale delivery record in the industry. (Google's
  Haskell "Journey" site, at 87/100 renormalized, is close behind but excludes one signal entirely
  from its denominator, so the two aren't directly comparable on the same basis.)
- **Least evidenced: Prometheus Hyperscale's Kaufman County campus — 25/100** (renormalized;
  was 19/100 before any Physical correction, 24/100 under the interim flat-credit version).
  Self-reported acreage with no CAD confirmation, no incentive filing found on any registry
  checked, and a founder with no direct prior data-center delivery background — none of that
  changed; only the Physical Commitment treatment did.
- **Notable: size and evidence still aren't tightly correlated, though this got weaker as a
  finding this refresh.** As of 2026-09-21, Fermi (the single largest project by MW, 11 GW) scores
  80/100 (Evidenced, tied for 3rd of 21) — no longer the clean "biggest ≠ best-evidenced" example it
  was at 65/100. The underlying reason it moved is instructive rather than reassuring: the Financial
  Commitment jump reflects a real signed lease, but Sponsor Track Record — the signal that most
  directly asks "should you trust this sponsor" — is still 3/20 and, if anything, has more
  documented reversal material behind it than before (see the expanded reversal flag). The most
  evidenced project on a like-for-like standard /100 basis remains **Meta (97/100)**, at 1,000 MW —
  one of the smaller projects in the universe — which is still the sharper illustration of the
  point.

## The zero-JETI finding — and why it's structural, not coincidental

**Zero of 21 projects hold an active Texas JETI Act (Ch. 403) agreement — and none of them ever
could.** The JETI Act's eligibility list is defined by NAICS code, and **data centers are
statutorily excluded from JETI eligibility**; eligible categories are things like advanced
manufacturing, dispatchable power generation, critical-infrastructure construction, and high-tech
R&D/equipment production. This was checked directly against the Comptroller's published
current-agreements list (9 active statewide agreements as of this session, none in the
data-center/AI-infrastructure sector) — but the more precise finding is that no data center in
Texas can appear on that list, by design, regardless of how "real" or evidenced it is.

**That is a distinct question from whether these projects' own power plants might qualify.** A
dispatchable, on-site generation facility — Fermi's gas turbines, Crusoe/Lancium's behind-the-meter
generation — sits under a different NAICS code (dispatchable power generation), which *is*
JETI-eligible. None of the generation plants in this universe were found to hold a JETI agreement
either, but that's a genuine "checked, not found" result for those specific facilities, not a
structural impossibility the way it is for the data centers themselves. **Precise claim: no data
center has, or can have, its own JETI agreement; whether their power plants separately qualify is
an open, plant-by-plant question this session did not exhaustively chase.**

The incentive activity that does exist for these projects instead runs through two *different*
channels: (1) the Comptroller's separate §151.359 "Qualifying Data Center" sales-tax-exemption
registry, which directly named 9 of the 21 projects (manually verified against the raw registry
table, not an AI summary — see `evidence_appendix.md`); and (2) county/municipal property-tax
abatements negotiated directly with a commissioners court or city council, confirmed for **3 of 21**
as of 2026-09-21 (Meta/El Paso; Google's Haskell/"Journey" site; and Fermi's Carson County Chapter
312 abatement, executed 2025-10-27 and confirmed this refresh by reading the county-clerk-filed
document directly — a fact that existed at the original Aug 5 capture and was missed then). [Ryan LLP](https://ryan.com/about-ryan/news-and-insights/2025/texas-jeti-incentive-strategy/), [KE Andrews](https://www.keatax.com/how-the-texas-jeti-act-shapes-manufacturing-energy-and-technology-investment/) — captured 2026-08-05, Fermi correction captured 2026-09-21.

## The permit-by-rule visibility finding

TCEQ physical-commitment evidence is sharply bimodal by project size. **7 of 21 projects have a
confirmed, docket-numbered TCEQ air permit or equivalent** (all among the largest sites — Fermi,
Abilene, Vantage/Frontier, Meta, Google/Armstrong via Crusoe's "Goodnight" plant, Riot's TDLR
permit, plus partial hits for Cipher). **9 of 21 have a power strategy that plausibly qualifies for
TCEQ's "permit by rule" under 30 TAC §106.511** — grid interconnection plus standard-size
backup/emergency generators, or reliance on an existing third-party plant — a category that
requires **no individual public notice and no opportunity for a hearing**, the same permitting
route commonly used for equipment like dry cleaners' boilers. For these 9, Physical Commitment is
not scored as a zero or a partial credit; it is **excluded from the calculation entirely** and
displayed as "n/o (§106.511)," with the total renormalized over the remaining 75 points (see
`methodology.md`). **Only 3 of 21 (Poolside, Tract, SB Energy) remain a true zero** — cases where
the project's own stated power strategy would need an individually-permitted facility at scale, and
none was found despite that expectation being reasonable.

The upshot, stated plainly: **the public visibility of physical build-out is a function of scale
and regulatory category, not of how real a project is.** A true zero is a more meaningful signal
than a blanket "no evidence found" would suggest; treating the other 9 as unobservable rather than
absent — and refusing to let that non-signal drag down an otherwise well-evidenced project's total
— is the more honest way to handle a genuine "can't tell," at the cost of making those 9 scores
non-comparable, signal-for-signal, to the 12 scored on the standard /100 basis. That tradeoff is
made explicit everywhere a renormalized score appears, not smoothed over.

## The no-public-queue-reconciliation finding

**There is no public mechanism to check any of these 21 projects against ERCOT's own
interconnection queue by name.** ERCOT publishes aggregate MW totals only — not a project
directory, not a county-level named list. The only per-project ERCOT status available publicly is
whatever a sponsor discloses about itself (e.g., Riot's own claim of "the first 1GW load ever
approved by ERCOT," PowerHouse's self-disclosed "500MW tranche ERCOT-approved"). There is no
independent registry to check either claim against — a limitation that now sits directly underneath
the Aug 3, 2026 Abbott directive's own stated goal of verifying exactly this kind of claim. See the
market-opacity finding in `candidate_universe.md` for the full framing. The PUC's SB6-mandated
transparency rulemaking, due by December 2026, was already aimed at this gap before the audit
directive gave it new urgency.
