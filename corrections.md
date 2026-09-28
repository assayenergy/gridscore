# Corrections

Dated log of every change to a published figure or claim in this repository. Entries are added
forward only. Earlier corrections made before this file existed are recorded inline where they were
made (`scored_table.md`, `key-stats.md`, `evidence_appendix.md`, `evidence/01-fermi-america-project-matador.md`).

---

## 2026-09-26: Fermi America / Project Matador (`evidence/01-fermi-america-project-matador.md`)

### 1. TTU leasehold acreage: "~5,855 acres" corrected to 5,236 acres (4,523 commenced + 713 pending)

- **What changed:** Site Control, first paragraph. "Holds a 99-year sovereign leasehold over ~5,855
  acres" now reads as a 5,236-acre Project Matador site under the TTU ground lease: 4,523 acres
  commenced in September 2025, plus a 713-acre tract to be added on transfer from a federal agency,
  still not commenced as of 2026-06-30. Arithmetic: 4,523 + 713 = 5,236.
- **Why:** 5,855 is not the lease acreage in any SEC filing. It comes from Fermi's own NRC Combined
  License Application, Part 1, Rev. 0 (ADAMS ML25169A396, submitted June 2025, pp.1-2, 1-3). That
  application predates the 2025-08-11 first lease amendment, which reduced the site from the original
  5,769 acres. The Amarillo Tribune article the evidence file cited for this fact says 5,769, not
  5,855, so the figure was also attributed to the wrong source.
- **Sources:** [424B4, 2025-10-01](https://www.sec.gov/Archives/edgar/data/2071778/000121390025094424/ea0252333-11.htm),
  pp.iii, 3, 44; [10-K FY2025, 2026-03-30](https://www.sec.gov/Archives/edgar/data/2071778/000207177826000010/frmi-20251231.htm),
  p.110; [10-Q Q2 2026](https://www.sec.gov/Archives/edgar/data/0002071778/000207177826000051/frmi-20260630.htm),
  p.17; NRC COL Part 1 Rev. 0, read from the
  [amarillotribune.org mirror](https://amarillotribune.org/wp-content/uploads/2025/07/ML25169A396-1.pdf)
  because nrc.gov returned HTTP 403. All captured 2026-09-26.
- **Score effect:** none. Site Control stays 25/25; it scores the existence of the government-counterparty
  lease, not its acreage.
- **Not yet corrected elsewhere:** the same 5,855 figure appears in `evidence_appendix.md` and
  `scoring_rubric_template.csv`. Flagged, not edited in this pass.

### 2. One-day share-price drop on 2025-12-12: "33.4%" / "about 33%" corrected to 33.8%

- **What changed:** Financial Commitment and Documented Reversal sections. The drop is now 33.8%
  ($15.25 close on 2025-12-11 to $10.09 close on 2025-12-12). Arithmetic: 15.25 − 10.09 = 5.16;
  5.16 ÷ 15.25 = 0.3384.
- **Why:** 33.4% came from the headline and URL of a 2025-12-14 Yahoo Finance article that gives no prices and
  no time basis. The evidence file wrongly called it "the more precise" figure. The daily closes give 33.8%.
- **Sources:** Yahoo Finance chart API, FRMI daily closes 2025-12-08 to 2025-12-16 (captured
  2026-09-26). This matches *Lupia v. Fermi Inc.*, No. 1:26-cv-00050 (S.D.N.Y.), Complaint ¶5
  ($5.16, 33.8%, $10.09 close). **Limit:** only one market-data source could be read; Nasdaq's API
  returned no rows, and Stooq requires browser verification.
- **Score effect:** none. The drop is part of a reversal flag, not a scored input.
- **Not yet corrected elsewhere:** "about 33%" / "~33%" appears in `essay-final.md` (published),
  `scored_table.md` and `scored_table.csv`. 33.8% rounds to "about 34%." Flagged, not edited in this pass.

### 3. "Parallel class action" removed: it was a press release, not a separate filing

- **What changed:** Documented Reversal section. "Plus a parallel … filing for the same Oct 1–Dec 11,
  2025 class period" is removed. The text now says one securities class action (*Lupia*) was filed and
  explains what the source actually shows.
- **Why:** The source is a plaintiff law firm's press releases (e.g. PR Newswire, 2026-01-29). They
  state that "a class action lawsuit has been filed against Fermi Inc." for that class period, with
  a March 6, 2026 lead-plaintiff deadline. They do not say the firm filed a case and give no docket
  number. A CourtListener search of dockets with "Fermi" in the case name, filed 2025-12-01 to
  2026-09-30, returned Lupia as the only securities case. Fermi's Q2 2026 10-Q describes a single
  putative securities class action.
- **Sources:** [PR Newswire release, 2026-01-29](http://www.prnewswire.com/news-releases/class-action-reminder-berger-montague-advises-fermi-inc-nasdaq-frmi-investors-to-inquire-about-a-securities-fraud-lawsuit-by-march-6-2026-302673606.html);
  [Lupia docket](https://www.courtlistener.com/docket/72106801/lupia-v-fermi-inc/);
  [10-Q Q2 2026](https://www.sec.gov/Archives/edgar/data/0002071778/000207177826000051/frmi-20260630.htm),
  Legal Proceedings. Captured 2026-09-26.
- **Score effect:** none. The reversal flag stands on the Lupia case and the AICA termination.
- **Not yet corrected elsewhere:** `scored_table.md` and `scored_table.csv` both still say "plus a
  parallel … filing." Flagged, not edited in this pass.

**Propagated 2026-09-26 (supersedes the three "Not yet corrected elsewhere" notes above):** items 1–3 were also corrected in `evidence_appendix.md` (Fermi entry), `scoring_rubric_template.csv` (row 2: site-control evidence, source URL, capture date, last_updated), `scored_table.md` (Fermi reversal flag) and `scored_table.csv` (row 2 reversal_citation). The published `essay-final.md` ("about 33%") is intentionally left unchanged.

---

## 2026-09-26: `scoring_rubric_template.csv` house-rule cleanup

- Removed a private landowner name and a site street address from scoring_rubric_template.csv (house rule). Earlier versions remain in git history; no history rewrite.
- Removed the same private landowner name (Poolside / Project Horizon site) from `candidate_universe.md` (project 3 row) and `evidence_appendix.md` (Poolside entry). Both now use the scoring_rubric_template.csv row 3 wording: "a private ranch site, Pecos County (landowner disclosed by sponsor Poolside; not an opaque LLC)." `evidence/03-poolside-project-horizon.md` still contains the name; it will be handled in the September refresh.
- Project 16 (Core Scientific, Denton): the `sponsor_track_record_source_url` in scoring_rubric_template.csv pointed to a TipRanks article about Marathon Digital's restatements, the source for project 19, apparently copied into the wrong row. It is replaced with Core Scientific's [10-K FY2024](https://www.sec.gov/Archives/edgar/data/1839341/000162828025008302/core-20241231.htm), which documents the Chapter 11 filing (2022-12-21) and emergence (2024-01-23). The Track Record score (10/20) is unchanged. The published rationale (`evidence_appendix.md`) rests on a clean site history since 2022 plus the Chapter 11, and uses nothing from the Marathon article. The rationale was uncited in `evidence/16`; see the open items below.
- Projects 16 and 19 in scoring_rubric_template.csv: an unquoted comma in `physical_commitment_status` ("no evidence found (dead end, not absence)") had split one field into two, shifting every later column one place right (30 fields vs. a 29-column header). The field is now quoted and both rows have 29 fields. **No values changed.**
- **Open, not changed (needs a decision):** `evidence/16` and scoring_rubric_template.csv row 16 (`sponsor_track_record_evidence`, `inferred_flags`) still describe Core Scientific as "being acquired by CoreWeave (~$9B deal)." Core Scientific terminated that merger agreement on 2025-10-30 after its stockholders did not approve it ([8-K, Item 1.02, accession 0001140361-25-039808](https://www.sec.gov/Archives/edgar/data/1839341/000114036125039808/ef20057995_8k.htm)). That predates the 2026-08-05 capture, so the statement was already stale when captured.

---

## 2026-09-26: SB Energy / Stargate Milam County re-scored 36 → 63 (`evidence/08-sb-energy-stargate-milam.md`)

SB Energy / Stargate Milam re-scored 36 -> 63 (Progressing) after its S-1 (public 2026-09-01). Three errors: the Aug 5 incentive entry ('NOT a match') was wrong; the Comptroller registry entry is SB Energy's. The 'true zero' Physical label was wrong once the S-1 showed a co-located solar plan with backup engines registered under §106.511. The site-control basis cited a deed that likely covers a different parcel; the score now rests on the S-1 and a filed lease. The launch post (2026-09-25) and 'Three Places' piece repeated the old score; both carry correction notes on Substack. True zeros are now 2 of 21. methodology.md's '3 of 21' text will be updated with the September refresh (pending).

- **Signals:**

  | Signal | Before | After |
  |---|---|---|
  | Site | 20 | 20 (new basis) |
  | Physical | 0, true zero | n/o (§106.511), excluded |
  | Financial | 8 | 12 |
  | Incentive | 0 | 7 |
  | Track Record | 8 | 8 |
  | Scoring basis | standard /100 | renormalized /75 |

- **Arithmetic:**
  - Before: 20 + 0 + 8 + 0 + 8 = 36.
  - After: (20 + 12 + 7 + 8) / 75 × 100 = 47 / 75 × 100 = 62.67 → 63.
- **Why, by error:**
  1. **Incentive.** The Comptroller's "Milam County Data Center" entries name MDC Building 1, LLC, MDC Building 2, LLC, Orion DC I, LLC and Milam County DC, LLC. The S-1's EX-21.1 lists the MDC and Milam County DC entities as SB Energy subsidiaries, and S-1/A No. 2 p.248 names Orion DC I, LLC as the OpenAI-affiliated tenant. I called the entry "confirmed NOT a match" on 2026-08-05; that was wrong. The score is capped at 7 because execution of the county Ch. 312 abatement is not confirmed.
  2. **Physical.** S-1/A No. 2 describes power from "co-located power generation assets" (p.248) delivered from Orion 1–3, the Ben Milam Solar projects (p.200, p.256). It has no gas plan for Milam. TCEQ shows PBR 183969 under §106.511 for SB Energy subsidiary SE DC Devco, LLC.
  3. **Site.** The Southridge Land TX LLC / former-Alcoa deed is not named in the S-1 or EX-21.1. It likely covers a different parcel (INFERENCE). Site control now rests on S-1/A No. 2 p.11 ("Land Control") and EX-10.28, in which listed subsidiary Milam County DC, LLC leases "the Land" to the tenant. Owned vs. ground lease is open.
  - **Financial** (new information, not a correction): executed, SEC-filed leases, discounted for four named factors (see evidence/08).
- **Sources:**
  - [S-1](https://www.sec.gov/Archives/edgar/data/2133037/000162828026059639/sbenergy-sx1.htm)
  - [S-1/A No. 1 (EX-10.28, EX-10.29)](https://www.sec.gov/Archives/edgar/data/2133037/000162828026060761/sbenergy-sx1a1exhibitsonly.htm)
  - [S-1/A No. 2](https://www.sec.gov/Archives/edgar/data/2133037/000162828026062846/sbenergy-sx1a2.htm)
  - [EX-21.1](https://www.sec.gov/Archives/edgar/data/2133037/000162828026062846/exhibit211-sx1a2.htm)
  - [Comptroller data center registry](https://comptroller.texas.gov/taxes/data-centers/data-center-lists.php)
  - [TCEQ Air Permits search](https://www2.tceq.texas.gov/airperm/index.cfm) (RN112444104)
  - All captured 2026-09-26. Full comparison in `evidence/08-s1-vs-record-DRAFT.md`.
- **Tier effect:**
  - Before → after: Evidenced 8 / Progressing 7 / Announced-only 6 → 8 / 8 / 5.
  - Progressing MW: 6,330 + 1,200 = 7,530.
  - Announced-only MW: 6,601 − 1,200 = 5,401.
  - Total unchanged: 15,791 + 7,530 + 5,401 = 28,722.
- **Changed in this pass:** `evidence/08-sb-energy-stargate-milam.md`, `scored_table.csv` (row 8), `scored_table.md` (table row moved from rank 16 to rank 10; ranks 11–15 renumbered; tier tallies; watchlist note), `evidence_appendix.md` (entry 8; renormalized count 9 → 10), `key-stats.md` (tier table, true-zero count; renormalized count 9 → 10), `scored_table.md` intro counts (standard 12 → 11, renormalized 9 → 10), `scoring_rubric_template.csv` (row 8, new basis), `key-stats.md` registry count (9 → 11, plus Frontier's circumstantial match noted as such) and permit count (7 → 9, split 4 full / 5 partial), `make_charts.py` (chart 2 footer: the hardcoded "9 scores renormalized" now counts renormalized rows from `scored_table.csv`, giving 10), `charts/chart2_all_projects.png` and `charts/chart3_mw_by_tier.png` (regenerated).
- key-stats.md registry (9 -> 11) and permit (7 -> 9) counts were already stale before this pass; corrected to match scored_table.csv.
- **Not changed, intentionally:** `essay-final.md` (published essay; gets a Substack note) and `methodology.md` (uncommitted refresh edits pending).

---

## 2026-09-28: September audit

Every project's Physical and Incentive evidence was re-checked for all 21 projects. For Physical,
each cited permit's status was read on the issuing agency's own record (TCEQ, PUC, TDLR). For
Incentive, each county and city was searched for an executed Ch. 312, 380 or 381 agreement: the
agreement itself, or minutes recording approval and authorization to execute. News reports were
used as leads only. All sources captured 2026-09-28.

### Score changes (old → new)

| # | Project | Signal | Old → new | Total (tier) | Source |
|---|---|---|---|---|---|
| 3 | Poolside — Project Horizon | Physical | 0 (true zero) → 25 | 26 → 51 (Announced-only → Progressing) | TCEQ Electric Generating Units standard permit 183235, "ISSUED" 2026-03-12, 332.28 MW ([TCEQ](https://www2.tceq.texas.gov/airperm/index.cfm?fuseaction=airpermits.project_report&proj_id=406111)) |
| 6 | Vantage — Frontier | Physical | 25 → 8 (applied, pending) | 59 → 42 (Progressing) | TCEQ 182467 "Status: PENDING" ([TCEQ](https://www2.tceq.texas.gov/airperm/index.cfm?fuseaction=airpermits.project_report&proj_id=402091)) |
| 9 | Meta — El Paso | Physical | 22 → 8 (applied, pending) | 97 → 83 (Evidenced) | PUC Docket 59076, no final order; ALJ proposal for decision 2026-09-23 ([PFD](https://interchange.puc.texas.gov/Documents/59076_176_1686197.PDF)) |
| 13 | Google — Armstrong County | Physical | 25 → 8 (applied, pending) | 72 → 55 (Evidenced → Progressing) | TCEQ 182880 "Status: PENDING" ([TCEQ](https://www2.tceq.texas.gov/airperm/index.cfm?fuseaction=airpermits.project_report&proj_id=404507)) |
| 12 | Riot — Corsicana | Physical | 20 → n/o (§106.511) | 80 → 91 (Evidenced) | TDLR TABS2026020144 is an accessibility registration, not a permit ([TDLR](https://www.tdlr.texas.gov/TABS/Search/Project/TABS2026020144)); grid-supplied site |
| 12 | Riot — Corsicana | Incentive | 7 → 15 | (same) | Navarro County resolution 2024-10-15, "The County Judge is hereby authorized to execute the AGREEMENT" ([minutes](https://navarro.easydocs.us/minutes/LinkedDir/2024/2024-10-15-Regular.PDF)) |
| 17 | Cipher — Barber Lake | Physical | 12 → n/o (§106.511) | 72 → 88 (Evidenced) | TCEQ PBR 182754 under §106.511, emergency generators; "portable plant" not found ([TCEQ](https://www2.tceq.texas.gov/airperm/index.cfm?fuseaction=airpermits.project_report&proj_id=403704)) |
| 17 | Cipher — Barber Lake | Financial | 15 → 13 | (same) | 8-K 2026-09-25: lease amendment with change-order-driven phased delivery and Cipher bearing the first $359.3M of overruns ([8-K](https://www.sec.gov/Archives/edgar/data/1819989/000181998926000043/cifr-20260924.htm)) |
| 17 | Cipher — Barber Lake | Incentive | 7 → 15 | (same) | Mitchell County Phase I Ch. 312 abatement, Comptroller "Abatement Execution Date: 2025-12-15" ([record](https://comptroller.texas.gov/economy/development/search-tools/ch312/abatements-details.php?id=000019866)) |
| 2 | Crusoe/Lancium — Abilene | Incentive | 7 → 15 | 72 → 80 (Evidenced) | City of Abilene Ch. 312 agreement, executed (City Manager signed 2025-08-29), Taylor County authorization ([city](https://abilenetx.gov/2476/Tax-Abatements)) |
| 11 | Crusoe/Lancium — Childress | Incentive | 7 → 15 | 64 → 75 (Progressing → Evidenced) | Childress County Ch. 312 Phases 1–10 and Ch. 381, signed 2025-03-10 ([county](https://www.childresstx.us/pages/tax-abatements)) |

**Arithmetic (recomputed from `scored_table.csv` in code):**
- #3: 15 + 25 + 2 + 7 + 2 = 51. #6: 12 + 8 + 8 + 4 + 10 = 42. #9: 25 + 8 + 15 + 15 + 20 = 83.
  #13: 15 + 8 + 5 + 7 + 20 = 55. #2: 12 + 25 + 10 + 15 + 18 = 80.
- #11: (15 + 8 + 15 + 18) ÷ 75 × 100 = 56 ÷ 75 × 100 = 74.67 → 75.
- #12: (22 + 15 + 15 + 16) ÷ 75 × 100 = 68 ÷ 75 × 100 = 90.67 → 91.
- #17: (22 + 13 + 15 + 16) ÷ 75 × 100 = 66 ÷ 75 × 100 = 88.
- **Tiers:** Evidenced 8 · Progressing 8 · Announced-only 5 → Evidenced 8 · Progressing 9 ·
  Announced-only 4.
- **MW by tier:** Evidenced 15,791 + 1,000 (Childress) = 16,791; Progressing 7,530 + 2,000
  (Poolside) − 1,000 (Childress) = 8,530; Announced-only 5,401 − 2,000 = 3,401; total 28,722
  unchanged. Announced-only share 3,401 ÷ 28,722 = 11.8%.
- **Physical categories:** confirmed-permitted 5 (3 full, 2 partial), applied-pending 3, true zero
  1 (Tract), not observable 12; 5 + 3 + 1 + 12 = 21. Scoring basis: 9 standard /100, 12
  renormalized /75.

### What went wrong, in plain words

1. **County abatements were not searched systematically in August.** The 2026-08-05 capture relied
   mostly on the state registry and news. It did not go county by county, and city by city, for
   signed agreements. Five executed or authorized local abatements were missed that way: Fermi's
   (caught 2026-09-21), and now Crusoe Abilene's, Childress's, Riot's and Cipher's. All five existed
   before the capture.
2. **Pending applications were scored as permits.** Vantage's and Google Armstrong's TCEQ
   applications and Meta's PUC application were scored 22–25 as if granted. None has been decided.
   They are now scored 8, "applied, pending." Riot's TDLR record was also treated as a building
   permit; it is an accessibility registration.

**Ledger Watch #1 (2026-09-28) said Poolside had no permit application; it holds standard permit
183235, issued 2026-03-12.** I missed it on 2026-08-05 and again on 2026-09-23: the 2026-09-23
re-check found Poolside's TCEQ site registration and stopped there instead of looking up the
permit recorded on the same site.

### Text-only corrections (no score change)

- **#14 Google Haskell:** the "Journey" abatement was approved 2025-06-24 but is effective
  2025-07-31, the date of the last signature ([agreement](https://newtools.cira.state.tx.us/upload/page/9220/docs/Homebound%20Group%20LLC.pdf)).
- **`evidence_appendix.md` entry 1 (Fermi)** still showed "65, Progressing" and Financial 5 /
  Incentive 7 from the 2026-08-05 capture; the 2026-09-21 refresh updated every other file but not
  this entry. It now shows 80, Evidenced, with a dated note. No score change.
- **Registry statute:** registry matches are now labeled by the table they appear in. Eleven
  projects' entries are in "Registered Qualifying Large Data Center Projects" (Tax Code §151.3595):
  Fermi, Crusoe Abilene, Poolside, SB Energy, Meta, Hut 8, Crusoe Childress, Riot, Google Armstrong,
  Core Scientific, Cipher. Aligned's "LBB01 Data Center" and Haskell's "Fort Haskell" entry are in
  "Registered Qualifying Data Center Projects" (§151.359), so they keep that label. The repository
  previously said §151.359 for all of them.
- **#17 Cipher:** "~$830M contracted revenue" (TheMinerMag, 2025-11-20) replaced with the 8-K
  figures: $3.8 billion before the 2026-09-24 amendment, over $9 billion after.
- **Leads recorded, not scored:** #13, an executed Armstrong County abatement with GN DC1, LLC,
  whose tie to Google is UNVERIFIED (Incentive stays 7); #21, Bosque County minutes of 2024-11-12
  approving a 30% abatement with CyrusOne, LP, with no authorization to execute or executed copy
  found (Incentive stays 0); #3, a Pecos County agenda item to execute an abatement with Poolside
  Inc. (2025-11-10), minutes not posted (Incentive stays 7).
- **Leads that did not hold:** Tract (Caldwell County's April 2026 abatement is with a different
  company, EDC Austin, LLC); CloudBurst (Guadalupe County approved an abatement 2026-04-21 without
  authorizing execution, and the attached agreement is an unsigned draft).
- **Street addresses removed** from `evidence/06-vantage-frontier-shackelford.md`,
  `evidence/12-riot-platforms-corsicana.md`, `evidence_appendix.md` (entry 6) and
  `scoring_rubric_template.csv` (rows 6, 12) under the house rule. Earlier versions remain in git
  history; no history rewrite.
- **`key-stats.md` figures that were already stale:** the Announced-only share still read 23.0%
  (6,601 MW) after the 2026-09-26 SB Energy re-score; on that date it should have been 5,401 ÷
  28,722 = 18.8%. The registry count read "11 of 21"; a recount from `scored_table.csv`, before and
  after this audit, gives 12.
- **Flagged, not scored:** TCEQ application 182267 (Abilene) was withdrawn 2026-04-20; Crusoe's NSR
  application 182126 (Abilene) has a public hearing request (2026-08-24); the Longhorn permit's TCEQ
  letter prints RN112029079 while the permit search lists RN112029061; Mitchell County's filed
  stamp on the Cipher agreement reads "JAN 02 2025" against a handwritten execution date of
  2 January 2026. CloudBurst's flood permit and PowerHouse Irving's building record could not be
  verified (the county and city portals need a login); both partial scores stand, flagged.

### Other corrections made in this pass (no score change)

1. **`methodology.md`, true-zero and renormalized counts.** "Exactly 3 of 21" true-zero projects now
   reads 1 of 21 (Tract): SB Energy moved to "not observable by category" on 2026-09-26 and
   Poolside to confirmed-permitted in this audit. The renormalized count now reads 12 (9 at first
   publication, plus SB Energy 2026-09-26, Riot and Cipher 2026-09-28), and "the other 12" standard
   scores now reads 9. SB Energy, Riot and Cipher were added to the flat-+5 vs. renormalized
   transparency table, comparison-only and never published: SB Energy 20 + 5 + 12 + 7 + 8 = 52 vs.
   63; Riot 73 vs. 91; Cipher 71 vs. 88. Counts from `scored_table.csv`: `physical_commitment_category`
   "true-zero" = project 4; "n/o (§106.511)" = projects 5, 8, 10, 11, 12, 14, 15, 16, 17, 19, 20, 21;
   21 − 12 = 9.
2. **`evidence/03-poolside-project-horizon.md`, private landowner name removed.** The landowner
   family's name and the ranch name were removed from Site control and from the Physical re-check
   note, with a contact email domain and the names of a landowner-affiliated LLC and oil-and-gas
   entity. Site control now uses the `scoring_rubric_template.csv` row 3 wording: "a private ranch
   site, Pecos County (landowner disclosed by sponsor Poolside; not an opaque LLC)." The Rock House
   Draw lead is identified by facility name only. House rule; flagged in the 2026-09-26 cleanup
   entry. Earlier versions remain in git history; no history rewrite.
3. **`evidence/16-core-scientific-denton.md`, stale CoreWeave merger text.** "Core Scientific itself
   is being acquired by CoreWeave in a ~$9B deal" is replaced; same fix in
   `scoring_rubric_template.csv` row 16 (`sponsor_track_record_evidence`, `inferred_flags`).
   Core Scientific's stockholders did not approve the merger, and "on October 30, 2025 … Core
   Scientific terminated the Merger Agreement, effective immediately"
   ([8-K filed 2025-10-30, Item 1.02, accession 0001140361-25-039808](https://www.sec.gov/Archives/edgar/data/1839341/000114036125039808/ef20057995_8k.htm)).
   The statement was already stale at the 2026-08-05 capture.
4. **`evidence/16`, "operated without major incident since 2022" labeled UNVERIFIED** (also in
   `evidence_appendix.md` entry 16 and `scoring_rubric_template.csv` row 16). No public source
   supports it, and the record is not clean: the City of Denton and Denton Municipal Electric had
   claims against Core Scientific in the bankruptcy, settled by court order 2023-08-16 for $1.5
   million in lease cure costs (10-K FY2024, Note 3, p. 95). Track Record 10 now rests on cited
   facts: Chapter 11 filed 2022-12-21 (Note 1, p. 84), emerged 2024-01-23 (Item 1, p. 10), Denton
   site operating (p. 8).
   [10-K FY2024](https://www.sec.gov/Archives/edgar/data/1839341/000162828025008302/core-20241231.htm).
5. **`evidence/16`, Comptroller registry entry misidentified.** The 2026-08-05 note read "Cottonwood,
   Cedarvale" as this project's entries. The actual row is "Denton Data Center | 09/19/2024",
   occupant Coreweave Compute Acquisition Co V LLC, operators Core Scientific, Inc. / Coreweave, Inc.
   (Large Data Center table, LD394824; §151.3595). "Cottonwood Data Center" is Core Scientific's
   Pecos, Texas site (10-K FY2024, p. 8); "Cedarvale" is the Ward County site sold in the bankruptcy
   (Note 3, p. 96). Same fix in `scoring_rubric_template.csv` row 16; `evidence_appendix.md` was
   already right. Incentive stays 7: (25 + 15 + 7 + 10) ÷ 75 × 100 = 76.
   [Comptroller data center lists](https://comptroller.texas.gov/taxes/data-centers/data-center-lists.php).

### Changed in this pass

`scored_table.csv` (rows 2, 3, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 21), `scored_table.md`
(re-ranked table, counts, transparency table, tier tallies, watchlist), `scoring_rubric_template.csv`
(rows 2, 3, 6, 8, 9, 11, 12, 13, 14, 15, 16, 17, 21), `evidence_appendix.md`, `key-stats.md`,
`methodology.md` ("applied, pending" adopted and applied; true-zero count; renormalized counts;
registry labels), evidence files 01, 02, 03, 06, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 21,
`README.md` and `evidence-summary.md` (statute label only), `charts/chart2_all_projects.png` and
`charts/chart3_mw_by_tier.png` (regenerated from the CSV by `make_charts.py`), and `make_charts.py`
itself (chart 3 now labels a tier segment under 20% of the bar below it, because the smaller
Announced-only segment clipped its label; no data logic changed).

Replaced "see corrections.md" with the full corrections URL in four CSV rows (1, 2, 8, 11) and the
matching `scored_table.md` note; fixed a typo in the Bosque note. No score changed.

**Not changed, intentionally:** `essay-final.md` (published; Meta's 97 and the tier and MW figures in
it are now superseded and need a correction note where it is published).
