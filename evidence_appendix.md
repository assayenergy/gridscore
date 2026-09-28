# GridScore v0 — Evidence Appendix (Session 3)

Scoring rationale per project, one paragraph each, with the citations that drove each signal score.
Full Session 2 evidence logs (all sources, all dead ends) are in `evidence/*.md` — this appendix is
the scoring-ready synthesis, and corrects two things the Session 2 AI-summarized registry fetch got
wrong or missed on manual re-check: it missed Hut 8's "Beacon Point 1," Google's "Project
Goodnight," and Fermi's own "Fermi Data Center 1" entirely, and it wrongly implied inconclusive
results for several matches that the raw table confirms or refutes cleanly.

**Correction pass (post-review):** Fermi's IPO date is corrected below to on/around Oct 1, 2025
(was mis-stated as Sept 2025). Nine projects' Physical Commitment signal is now **excluded from
scoring entirely and renormalized** — not scored as a zero, and not given a flat partial credit
either (an interim flat-+5 version was tried and superseded; see `methodology.md`) — displayed as
**"n/o (§106.511)"** because their generator setup plausibly qualifies for TCEQ permit-by-rule
coverage, making a missing public docket structurally uninformative. For these projects (12 after the 2026-09-28 audit: Riot and Cipher were added),
`total = (Site + Financial + Incentive + Track Record) ÷ 75 × 100`. Five of the original nine end up in a
different tier than they would have under the original true-zero scoring: Google/Haskell
("Journey") Progressing→Evidenced (65→87), Core Scientific/Denton Progressing→Evidenced (57→76),
Marathon/Garden City Announced-only→Progressing (36→48), Project Caprock/Aligned Announced-only→
Progressing (33→44), and Bosque County/ECP+KKR Announced-only→Progressing (30→40). All totals and
tiers below reflect the renormalized scores; see `scored_table.md` for the full diff against both
the true-zero and interim flat-+5-credit versions.

**September audit (2026-09-28):** every cited permit was re-checked against the issuing agency's
record and every county and city was searched for an executed incentive agreement. Eleven entries
below carry a dated revision note; the full list of score changes, with sources, is in
`corrections.md` (2026-09-28, "September audit"). Registry matches are now labeled by table:
§151.3595 for the "Registered Qualifying Large Data Center Projects" table, §151.359 for the
"Registered Qualifying Data Center Projects" table.

**1. Fermi America — Project Matador (80, Evidenced; 65, Progressing, at the 2026-08-05 capture).** Site Control 25: 99-year ground lease over a
5,236-acre site (4,523 acres commenced Sept. 2025 + a 713-acre tract pending; [424B4](https://www.sec.gov/Archives/edgar/data/2071778/000121390025094424/ea0252333-11.htm)
pp.iii, 3, 44; [10-K FY2025](https://www.sec.gov/Archives/edgar/data/2071778/000207177826000010/frmi-20251231.htm) p.110; corrected 2026-09-26, see corrections.md) from the Texas Tech University System, a named public counterparty — about the
strongest site-control paper trail in the universe, though the underlying *county* (Carson vs.
Potter/Randall) is separately unresolved. Physical 25: TCEQ Docket 2025-1898-AIR, approved as the
2nd-largest US Clean Air permit. Financial 5, Incentive 7 (registry match "Fermi Data Center 1,"
eff. 2025-09-05 — no JETI agreement, and none is possible: data centers are statutorily excluded
from JETI by NAICS code; Fermi's own gas plant, as a dispatchable generator, is a separate,
JETI-eligible question that was checked and not found), Track Record 3: development-stage company
(FRMI, IPO'd on/around Oct 1, 2025), cancelled tenant funding, no binding tenant, open class-action
suit — flagged as a documented reversal, not scored negative beyond what the thin track record
already reflects.
*Revised 2026-09-28 (catching up the 2026-09-21 Fermi refresh, which updated the other files but not
this entry):* Financial 5 → 12 (TensorWave lease signed 2026-08-09, closed convertible notes,
balance-sheet capex; discounted for a retracted guarantor claim, tenant concentration and the cash
drawdown) and Incentive 7 → 15 (executed Carson County Ch. 312 abatement, filed 2025-10-27, missed
on 2026-08-05). Registry: §151.3595. Physical 25 re-checked 2026-09-28: TCEQ 181009 "ISSUED",
complete 2026-02-25. Total 25 + 25 + 12 + 15 + 3 = 80. Full trail in
`evidence/01-fermi-america-project-matador.md` and `scored_table.md` (2026-09-21 correction note).

**2. Crusoe/Lancium — Abilene Campus (80, Evidenced; 72 before the 2026-09-28 audit).** Site 12 (press-only, no acreage/deed
found), Physical 25 (TCEQ Standard Permit approved 2025-01-22, ~360MW), Financial 10 (Microsoft
900MW + OpenAI 1.2GW leases confirmed by both companies), Incentive 7 (registry match — 8 separate
"Lancium Abilene Clean Campus" sub-buildings, I through VIII, most tenanted by Oracle America Cloud
Services LLC), Track Record 18 (Phase 1 delivered groundbreak-to-operational in ~15 months).
*Revised 2026-09-28:* Incentive 7 → 15. An executed City of Abilene Ch. 312 abatement with Lancium
LLC / Abilene DC 1, LLC (City Manager signed 2025-08-29; chain from 2021-12-21) and Taylor County
resolutions authorizing execution (2025-02-25, 2025-09-09) were missed on 2026-08-05. Physical 25
re-checked: standard permit 177263 ISSUED (amended 2025-01-22). Registry: §151.3595. Total 12 + 25 +
10 + 15 + 18 = 80.

**3. Poolside — Project Horizon (51, Progressing; 26, Announced-only, before the 2026-09-28 audit).** Site 15 (568-acre leasehold on a private ranch site,
Pecos County — landowner disclosed by sponsor Poolside; not an opaque LLC), Physical **0 — true zero, not NOC** (Poolside's own stated
power strategy is dedicated primary generation via aero-derivative turbines, a scale that would
need an individually-permitted facility like Fermi's or Vantage's, not a permit-by-rule-eligible
backup array; TCEQ search surfaced only an unrelated project in the same county), Financial 2,
Incentive 7 (registry match "Poolside Data Center, Pecos County I & II," eff. 2025-10-23 /
2026-03-06), Track Record 2. **Documented reversal**: CoreWeave's anchor lease terminated after
Poolside's funding round collapsed — logged as a flag, not a score penalty.
*Revised 2026-09-28:* Physical 0 → 25. The true zero was wrong: Poolside LF Phase 2 DC OPS LLC
holds TCEQ Electric Generating Units standard permit 183235, ISSUED 2026-03-12, for twelve gas
turbines totaling 332.28 MW (6 × 30.34 + 6 × 25.04) to power the on-site data center; a separate
operating permit is still required. Registry: §151.3595. Total 15 + 25 + 2 + 7 + 2 = 51.

**4. Tract — Caldwell County (40, Progressing — exactly on the tier floor).** Site 18
(self-disclosed but corporate-confirmed *closed* acquisition, 1,515→~3,000 acres), Physical **0 —
true zero, not NOC** (no tenant/operator named yet, so there is nothing to have applied for a
permit at all — this is a "not yet applicable" zero, distinct from both a confirmed generation
facility and a plausibly-PBR-covered one), Financial 8 (Blue Bonnet Electric Cooperative Facility
Design Agreement), Incentive 0 (no match on any registry or JETI), Track Record 14 (founder Grant
van Rooyen's cited prior instances — Cologix, Teraco — the company itself hasn't delivered a site
under this model yet, which is exactly why this project sits precisely on the tier boundary).

**5. PowerHouse/Provident — Grand Prairie (32, Announced-only, renormalized).** Site 10, Physical
**n/o (§106.511) — excluded, not scored**: the project's model is a grid-interconnected ERCOT
tranche (500MW→1.8GW), the kind of setup that would rely on standard emergency/backup gensets
rather than a dedicated primary plant — exactly the profile permit-by-rule is built for, so the
absence of a public TCEQ docket doesn't tell us much either way. Financial 6 (self-disclosed ERCOT
approval, unverifiable against any public registry), Incentive 0, Track Record 8 (sponsor's
concurrent Irving project reached a construction milestone). (10+6+0+8)/75×100 = 32.

**6. Vantage — Frontier (42, Progressing; 59 before the 2026-09-28 audit).** Site 12, Physical 25 (VoltaGrid TCEQ permit
182467/PSDTX1692/GHGPSDTX266, 700MW, Shackelford Co.; site street address removed 2026-09-28), Financial 8 ($25B
disclosed, no project-specific fee), Incentive 4 (circumstantial registry match only — 12 Vantage
TX entries all tenanted by Oracle, consistent with Frontier's known tenancy, but the registry has
no county field so this can't be positionally confirmed), Track Record 10 (general reputation,
no specific delivery citations pulled).
*Revised 2026-09-28:* Physical 25 → 8 ("applied, pending"). 182467 is an application, "Status:
PENDING" on TCEQ's record (draft permit notice 2026-09-18), not a granted permit. Registry:
§151.3595. Total 12 + 8 + 8 + 4 + 10 = 42.

**7. CloudBurst/Evolve — San Marcos (30, Announced-only).** Site 12, Physical 8 (confirmed Hays
County Flood Hazard Development Permit; Guadalupe Co.'s building/gas-plant permits not found),
Financial 10 (named Energy Transfer gas-supply agreement), Incentive 0, Track Record 0 (not
independently researched this session — this score reflects incomplete research, not a confirmed
absence of track record; flagged, not to be read as a finding).

**8. SB Energy — Stargate Milam County (63, Progressing; re-scored 2026-09-26 from 36,
Announced-only, after SB Energy's S-1 — see `corrections.md`).** Site 20, government-record (SEC
exhibit): the S-1 marks "Land Control" for both Milam buildings (S-1/A No. 2 p.11), and in EX-10.28
the landlord, listed subsidiary Milam County DC, LLC, leases "the Land" to the tenant. Whether the
land is owned or ground-leased is not stated (open). The deed previously cited here (Southridge Land
TX LLC, former Alcoa site) likely covers a different parcel (INFERENCE). Physical **n/o
(§106.511)**, renormalized: the S-1 describes power from "co-located power generation assets" (p.248)
delivered from the Ben Milam Solar (Orion 1–3) projects (p.200), with no gas-generation plan for Milam.
The only TCEQ air authorization found is PBR 183969 under §106.511, held by SB Energy subsidiary SE DC
Devco, LLC. Financial 12 (two executed, SEC-filed leases with an OpenAI affiliate, guaranteed by
OpenAI Global, LLC; discounted for construction financing "not yet closed", related-party
concentration, tenant buy-out rights after 365 days' delay, and ERCOT's energization pause).
Incentive 7 (§151.3595 registry match: the "Milam County Data Center" entry that this appendix
previously called unrelated belongs to SB Energy subsidiaries per the S-1's EX-21.1; a county Ch. 312
abatement is on 2025 agendas, but execution is not confirmed). Track Record 8 (strong utility-solar
delivery record, zero data-center-specific record; the S-1 confirms "No data center capacity is
currently in operation"). Total (20 + 12 + 7 + 8) / 75 × 100 = 62.67 → 63.

**9. Meta — El Paso (83, Evidenced; 97, the highest score in the universe, before the 2026-09-28 audit).** Site 25 (Wurldwide LLC,
Meta's own named SPV, bought city-owned land via a council-approved sale). Physical 22 (PUC filing
for a dedicated 366MW/813-generator plant, cost recovered from Meta under an approved rate).
Financial 15 ($10B disclosed investment). Incentive 15 (executed 25-year, 80% city abatement plus a
parallel county abatement — survived a repeal vote in June 2026 — the only *executed* municipal
abatement found in this universe as of 2026-08-05 (the 2026-09-28 audit found several more), plus a registry match on "Wurldwide LLC DBA Statue LLC," eff.
2025-09-17). Track Record 20 (Meta's global hyperscale delivery record).
*Revised 2026-09-28:* Physical 22 → 8 ("applied, pending"). The McCloud plant is PUC Docket 59076
with no final order; the ALJs' 2026-09-23 proposal for decision recommends approval "only if it is
conditioned on EPE holding its customers harmless from the capital and operating costs of the
Project. Without such a condition, the ALJs would recommend denial of the application." Incentive
15 confirmed (city agreements fully executed 2023-12-07; county authorized 2023-12-04). Total 25 +
8 + 15 + 15 + 20 = 83.

**10. Hut 8 — Beacon Point (61, Progressing, renormalized).** Site 10 (self-reported, no CAD
confirmation). Physical **n/o (§106.511) — excluded, not scored**: Beacon Point's power strategy
is a grid interconnection agreement with AEP Texas, not dedicated on-site generation, so standard
backup gensets (plausibly permit-by-rule-eligible) are the expected physical footprint here — the
company's own claim of being outside city/county permitting jurisdiction is unverified, and no
TCEQ docket was found, but that absence is consistent with the PBR pattern, not informative on its
own. Financial 15 (SEC 8-K: 1,000MW AEP Texas interconnection, $19.6B combined lease value —
tenant itself remains unnamed). Incentive 7 (registry match "Beacon Point 1 Data Center," eff.
2026-04-16 — missed by the Session 2 AI-summarized fetch, found on manual re-check). Track Record
14 (delivered on its own announced timeline; short corporate history). (10+15+7+14)/75×100 ≈ 61.

**11. Crusoe/Lancium — Childress (75, Evidenced, renormalized; 64, Progressing, before the 2026-09-28 audit).** Site 15 (270 acres owned
outright by Lancium, per company disclosure). Physical **n/o (§106.511) — excluded, not scored**:
Lancium's own materials describe this site as running on a 1GW *grid* interconnect (ERCOT-approved)
rather than dedicated primary generation — the TCEQ search found Crusoe's other-county permits
(Abilene, Armstrong), not one for Childress specifically, which is consistent with a
grid-plus-backup-gensets profile rather than evidence the generation doesn't exist. Financial 8
(self-disclosed ERCOT approval). Incentive 7 (registry match — Childress explicitly named, eff.
2025-03-25). Track Record 18 (explicitly the second site using "the same partnership structure
established in Abilene," a direct, named precedent). (15+8+7+18)/75×100 ≈ 64.
*Revised 2026-09-28:* Incentive 7 → 15. Childress County executed Ch. 312 abatements (Phases 1–10)
and a Ch. 381 agreement with Lancium entities, signed by the County Judge 2025-03-10 — missed on
2026-08-05. Registry: §151.3595. (15 + 8 + 15 + 18) / 75 × 100 = 74.67 → 75.

**12. Riot Platforms — Corsicana (91, Evidenced, renormalized — highest score in the universe after the 2026-09-28 audit; 80 before).** Site 22 (SEC-disclosed sequential land
purchases, 265+355+238 acres). Physical 20 (TDLR building permit, "Project Ditto," $400M).
Financial 15 (the only ERCOT-approval claim in the universe independently repeated across multiple
trade-press outlets, not just the sponsor's own materials). Incentive 7 (registry match — 3
separate Corsicana entries). Track Record 16 (delivered initial 400MW on schedule, SEC-auditable).
*Revised 2026-09-28:* Physical 20 → n/o (§106.511), renormalized: "Project Ditto" is a TDLR
accessibility registration ("Project Registered"), not a building permit, and the site is
grid-supplied. Incentive 7 → 15: Navarro County resolution of 2024-10-15, "The County Judge is
hereby authorized to execute the AGREEMENT" with Riot Corsicana LLC, county-signed — missed on
2026-08-05. Registry: §151.3595. (22 + 15 + 15 + 16) / 75 × 100 = 90.67 → 91.

**13. Google — Panhandle, Armstrong County (55, Progressing; 72, Evidenced, before the 2026-09-28 audit).** Site 15 (1,300 acres, local news
confirmed, no deed pulled). Physical 25 (Crusoe's TCEQ permit for the "Goodnight Data Center Power
Plant," 933MW, explicitly filed to power this co-located Google site). Financial 5 (statewide $40B
figure only, no site-specific number). Incentive 7 (registry match "Project Goodnight," eff.
2025-06-20 — exact name correspondence to the TCEQ filing). Track Record 20 (Google's global
delivery record).
*Revised 2026-09-28:* Physical 25 → 8 ("applied, pending"): Crusoe's 182880 is "Status: PENDING" on
TCEQ's record, in technical review. Incentive stays 7 (registry, §151.3595); an executed Armstrong
County abatement with GN DC1, LLC (2025-10-14 / 2025-11-03) is recorded as a lead because GN DC1's
tie to Google is UNVERIFIED. Total 15 + 8 + 5 + 7 + 20 = 55.

**14. Google — Panhandle, Haskell County, scored as "Journey" (87, Evidenced, renormalized).**
Site 20 (Haskell County Commissioners Court tax-abatement document — a real government record, but
**the site identity is ambiguous**: "Journey," "Thelma," and a registry entry "Fort Haskell Data
Center" may or may not be the same facility; a third, unrelated Crusoe Energy proposal in the same
county had its own abatement request rejected 4-0 by the same court, underscoring how crowded and
confusing Haskell County's data-center landscape is in the public record). Physical **n/o
(§106.511) — excluded, not scored** (no TCEQ docket found for this specific site; Google's
Armstrong sibling site uses dedicated co-located generation, but nothing found here confirms Journey
follows the same model rather than a grid-plus-backup approach, so this is a genuine unknown, not
inferred either way). Financial 10 (the court record itself discloses ~$1B Phase 1 capex).
Incentive 15 (the abatement is executed, not just filed — full credit tier; approved 2025-06-24,
effective 2025-07-31 on the last signature, corrected 2026-09-28). Track Record 20
(Google). (20+10+15+20)/75×100 ≈ 87 — notably more solid than the 70-exactly-on-the-floor result
the interim flat-+5 treatment produced, though the underlying site-identity ambiguity is unchanged.

**15. Aligned — Project Caprock (44, Progressing, renormalized).** Site 10, Physical **n/o
(§106.511) — excluded, not scored**: Aligned's own materials describe funding dedicated electrical
*infrastructure* in partnership with utility Xcel Energy, which reads as grid-side investment
rather than a standalone primary generation plant — consistent with the standard-backup-genset
profile, so no TCEQ docket found doesn't move this one way or the other. Financial 6 ($5B regional
figure, self-funded infrastructure with named utility Xcel Energy), Incentive 7 (registry match
"LBB01 Data Center," eff. 2026-07-10 — exact match to Aligned's own building name), Track Record 10
(established multi-market operator, no specific citations pulled). (10+6+7+10)/75×100 ≈ 44 — this
is one of three projects that cross from Announced-only into Progressing under renormalization
(vs. the original true-zero scoring), a swing worth double-checking since it rests on a plausibility
call about Aligned's power strategy, not confirmed evidence either way.

**16. Core Scientific — Denton Campus (76, Evidenced, renormalized).** Site 25 (City of Denton
council action confirming a land lease — about as strong as site control gets short of a raw
deed). Physical **n/o (§106.511) — excluded, not scored**: the site has run on a municipal-utility
(Denton Municipal Electric) grid connection since 2022 — a long-operating, grid-interconnected
profile where standard backup generation is the expected footprint, not a dedicated primary plant;
no docket was found, which fits that profile rather than suggesting an absence of any generation
at all. Financial 15 ($1.2B CoreWeave expansion, $6.1B total investment, $194M projected city tax
revenue). Incentive 7 (§151.3595 registry match "Denton Data Center," eff. 2024-09-19; confirmed 2026-09-28 in the
Comptroller's Large Data Center table with Core Scientific as operator). Track Record 10 (site
operating since 2022, but the corporate parent filed Chapter 11 on 2022-12-21 and emerged 2024-01-23
per its 10-K FY2024 — both facts logged, not averaged away; "clean" site history is UNVERIFIED,
corrected 2026-09-28, see `corrections.md`). (25+15+7+10)/75×100 ≈ 76 — the largest single
jump of any project under renormalization, crossing Progressing→Evidenced (was 57 under true-zero
scoring), because its non-Physical signals are unusually strong relative to the 75-point base.

**17. Cipher Mining — Barber Lake (88, Evidenced, renormalized; 72 before the 2026-09-28 audit).** Site 22 (SEC-adjacent disclosure of a closed
$67.5M acquisition). Physical 12 (TCEQ activity confirmed for a "portable plant" — construction
support, not a full generation permit). Financial 15 (Fluidstack HPC deal: ~$830M contracted
revenue, up to $9.0B potential value, $333M Google-backstopped debt). Incentive 7 (registry match
"Cipher Barber Lake LLC Data Center," eff. 2025-11-07 — also reveals the actual end-tenant is
Anthropic, PBC, with Fluidstack as operator). Track Record 16 (delivered acquisition-to-fully-leased
in ~14 months, SEC-auditable).
*Revised 2026-09-28:* Physical 12 → n/o (§106.511), renormalized: the "portable plant" was not
found; the site's TCEQ record is PBR 182754 under §106.511 (152 emergency generators). Financial 15
→ 13: the 2026-09-24 lease amendment adds named discounts (change-order-driven phased delivery Q4
2026–Q1 2027; Cipher bears the first $359.3M of cost overruns); the 8-K puts pre-amendment contracted
revenue at $3.8 billion (not ~$830M) and post-amendment at over $9 billion. Incentive 7 → 15:
Mitchell County Phase I Ch. 312 abatement executed (Comptroller execution date 2025-12-15) — missed
on 2026-08-05. Registry: §151.3595. (22 + 13 + 15 + 16) / 75 × 100 = 88.

**18. PowerHouse — Irving Campus (28, Announced-only).** Site 10 (50-acre purchase with Harrison
Street, specific address disclosed). Physical 5 ("topped out" milestone — real public reporting of
construction progress, not an inference, though no permit number was found). Financial 5
(infrastructure-readiness only — adjacent Oncor substation). Incentive 0 (registry has only an
unrelated "QTS Irving DC3" entry). Track Record 8 (same sponsor as project #5, concurrent
execution).

**19. Marathon Digital — Garden City (48, Progressing, renormalized).** Site 22 (SEC-adjacent
disclosure, both MARA and seller Applied Digital are public companies). Physical **n/o (§106.511)
— excluded, not scored**: the facility converts flare gas to power via distributed, modular
generator units at wellhead scale — an architecture industry-wide that typically runs on
small-per-unit, PBR-plausible permitting rather than one large individually-permitted plant; it has
operated since 2023 with no docket located, consistent with that pattern. Financial 5 (documented
stranded-gas power arrangement, no $ interconnection figure). Incentive 0 (confirmed non-match —
Marathon was explicitly absent from the registry on manual check). Track Record 9 (SEC accounting
restatements and a cancelled earnings call are real negatives; clean site-level operations since
2023 is a real positive — both logged). (22+5+0+9)/75×100 ≈ 48 — crosses Announced-only→Progressing
under renormalization (was 36 under true-zero scoring).

**20. Prometheus Hyperscale — Kaufman County (25, Announced-only — lowest score in the universe,
renormalized).** Site 8 (self-reported acreage only). Physical **n/o (§106.511) — excluded, not
scored**: the site's stated design uses modular Jenbacher reciprocating gas engines plus battery
storage, an architecture that fits the PBR-plausible modular-genset pattern rather than one large
individually-permitted plant. Financial 5 (named ENGIE/Conduit Power partnerships, no dollar figure
for this site). Incentive 0. Track Record 6 (founder has no direct prior data-center background;
senior hired leadership — ex-BP CEO, ex-Meta/Equinix infrastructure exec — carries individual
credibility but the company has no delivered facility yet in Texas or its other flagship state,
Wyoming). (8+5+0+6)/75×100 ≈ 25 — remains the lowest score in the universe under every scoring
treatment tried this session.

**21. ECP+KKR/CyrusOne — Bosque County (40, Progressing, renormalized — exactly on the tier
floor).** Site 5 (location described only as "adjacent to" an existing plant — the weakest
site-control evidence in the universe). Physical **n/o (§106.511) — excluded, not scored**: this
project's power comes from Calpine's existing, already-permitted Thad Hill Energy Center via a
power-supply agreement — CyrusOne has no reason to file its own generation permit at all, since it
isn't building new generation, which is a structurally different (and arguably stronger) reason for
an absent docket than the backup-genset cases elsewhere in this list. Financial 15 (CyrusOne/Calpine
400MW power-supply agreement, ~$4B investment — very well documented). Incentive 0 (no CyrusOne
match on the registry; **manual check surfaced two other, unrelated Bosque County data-center
registrations — Google's "C1 Bosque I" and Amazon's "C1 Bosque II"** — neither is this project, but
both are new information for a future universe revision). Track Record 10 (strong general
reputation for both CyrusOne and the PE sponsors, no specific citations pulled). (5+15+0+10)/75×100
≈ 40 — the weakest Site Control score in the universe (5/25) is nearly enough on its own to keep
this out of Progressing; it clears the floor by a single point's worth of rounding, so treat this
one as fragile in the other direction from most of the watchlist.
*Updated 2026-09-28 (score unchanged):* Bosque County minutes of 2024-11-12 approved entering a 30%
Ch. 312 abatement with CyrusOne, LP; no authorization to execute and no executed copy found —
recorded as a lead, Incentive stays 0.
