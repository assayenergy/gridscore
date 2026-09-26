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
