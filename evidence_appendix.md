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
coverage, making a missing public docket structurally uninformative. For these 9,
`total = (Site + Financial + Incentive + Track Record) ÷ 75 × 100`. Five of the nine end up in a
different tier than they would have under the original true-zero scoring: Google/Haskell
("Journey") Progressing→Evidenced (65→87), Core Scientific/Denton Progressing→Evidenced (57→76),
Marathon/Garden City Announced-only→Progressing (36→48), Project Caprock/Aligned Announced-only→
Progressing (33→44), and Bosque County/ECP+KKR Announced-only→Progressing (30→40). All totals and
tiers below reflect the renormalized scores; see `scored_table.md` for the full diff against both
the true-zero and interim flat-+5-credit versions.

**1. Fermi America — Project Matador (65, Progressing).** Site Control 25: 99-year leasehold over
5,855 acres from the Texas Tech University System, a named public counterparty — about the
strongest site-control paper trail in the universe, though the underlying *county* (Carson vs.
Potter/Randall) is separately unresolved. Physical 25: TCEQ Docket 2025-1898-AIR, approved as the
2nd-largest US Clean Air permit. Financial 5, Incentive 7 (registry match "Fermi Data Center 1,"
eff. 2025-09-05 — no JETI agreement, and none is possible: data centers are statutorily excluded
from JETI by NAICS code; Fermi's own gas plant, as a dispatchable generator, is a separate,
JETI-eligible question that was checked and not found), Track Record 3: development-stage company
(FRMI, IPO'd on/around Oct 1, 2025), cancelled tenant funding, no binding tenant, open class-action
suit — flagged as a documented reversal, not scored negative beyond what the thin track record
already reflects.

**2. Crusoe/Lancium — Abilene Campus (72, Evidenced).** Site 12 (press-only, no acreage/deed
found), Physical 25 (TCEQ Standard Permit approved 2025-01-22, ~360MW), Financial 10 (Microsoft
900MW + OpenAI 1.2GW leases confirmed by both companies), Incentive 7 (registry match — 8 separate
"Lancium Abilene Clean Campus" sub-buildings, I through VIII, most tenanted by Oracle America Cloud
Services LLC), Track Record 18 (Phase 1 delivered groundbreak-to-operational in ~15 months).

**3. Poolside — Project Horizon (26, Announced-only).** Site 15 (568-acre leasehold on the named
Mitchell family's Longfellow Ranch), Physical **0 — true zero, not NOC** (Poolside's own stated
power strategy is dedicated primary generation via aero-derivative turbines, a scale that would
need an individually-permitted facility like Fermi's or Vantage's, not a permit-by-rule-eligible
backup array; TCEQ search surfaced only an unrelated project in the same county), Financial 2,
Incentive 7 (registry match "Poolside Data Center, Pecos County I & II," eff. 2025-10-23 /
2026-03-06), Track Record 2. **Documented reversal**: CoreWeave's anchor lease terminated after
Poolside's funding round collapsed — logged as a flag, not a score penalty.

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

**6. Vantage — Frontier (59, Progressing).** Site 12, Physical 25 (VoltaGrid TCEQ permit
182467/PSDTX1692/GHGPSDTX266, 700MW, filed for 299 FM 604 Shackelford Co.), Financial 8 ($25B
disclosed, no project-specific fee), Incentive 4 (circumstantial registry match only — 12 Vantage
TX entries all tenanted by Oracle, consistent with Frontier's known tenancy, but the registry has
no county field so this can't be positionally confirmed), Track Record 10 (general reputation,
no specific delivery citations pulled).

**7. CloudBurst/Evolve — San Marcos (30, Announced-only).** Site 12, Physical 8 (confirmed Hays
County Flood Hazard Development Permit; Guadalupe Co.'s building/gas-plant permits not found),
Financial 10 (named Energy Transfer gas-supply agreement), Incentive 0, Track Record 0 (not
independently researched this session — this score reflects incomplete research, not a confirmed
absence of track record; flagged, not to be read as a finding).

**8. SB Energy — Stargate Milam County (36, Announced-only).** Site 20 (a real deed was filed with
Milam County for ~4,709 acres, but the connection to SB Energy runs through a registered Menlo
Park address for "Southridge Land TX LLC," not a named party — inferred, not confirmed). Physical
**0 — true zero, not NOC**: SB Energy's own materials describe building new, dedicated generation
to supply "the majority of the campus's power" — a scale of primary generation that, like Fermi's
or Vantage's, would need an individual TCEQ permit and should be publicly visible; none was found,
which is a more meaningful absence here than at the smaller, grid-reliant projects. Financial 8
(corporate-level $1B SoftBank/OpenAI investment), Incentive 0 (the registry's own
"Milam County Data Center" entry uses entirely different LLC names — MDC Building 1 LLC / Orion DC
I LLC — confirmed as a *different*, unrelated Milam County project on manual check), Track Record 8
(strong utility-solar delivery record, zero data-center-specific record).

**9. Meta — El Paso (97, Evidenced — highest score in the universe).** Site 25 (Wurldwide LLC,
Meta's own named SPV, bought city-owned land via a council-approved sale). Physical 22 (PUC filing
for a dedicated 366MW/813-generator plant, cost recovered from Meta under an approved rate).
Financial 15 ($10B disclosed investment). Incentive 15 (executed 25-year, 80% city abatement plus a
parallel county abatement — survived a repeal vote in June 2026 — the only *executed* municipal
abatement found in this universe, plus a registry match on "Wurldwide LLC DBA Statue LLC," eff.
2025-09-17). Track Record 20 (Meta's global hyperscale delivery record).

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

**11. Crusoe/Lancium — Childress (64, Progressing, renormalized).** Site 15 (270 acres owned
outright by Lancium, per company disclosure). Physical **n/o (§106.511) — excluded, not scored**:
Lancium's own materials describe this site as running on a 1GW *grid* interconnect (ERCOT-approved)
rather than dedicated primary generation — the TCEQ search found Crusoe's other-county permits
(Abilene, Armstrong), not one for Childress specifically, which is consistent with a
grid-plus-backup-gensets profile rather than evidence the generation doesn't exist. Financial 8
(self-disclosed ERCOT approval). Incentive 7 (registry match — Childress explicitly named, eff.
2025-03-25). Track Record 18 (explicitly the second site using "the same partnership structure
established in Abilene," a direct, named precedent). (15+8+7+18)/75×100 ≈ 64.

**12. Riot Platforms — Corsicana (80, Evidenced).** Site 22 (SEC-disclosed sequential land
purchases, 265+355+238 acres). Physical 20 (TDLR building permit, "Project Ditto," $400M).
Financial 15 (the only ERCOT-approval claim in the universe independently repeated across multiple
trade-press outlets, not just the sponsor's own materials). Incentive 7 (registry match — 3
separate Corsicana entries). Track Record 16 (delivered initial 400MW on schedule, SEC-auditable).

**13. Google — Panhandle, Armstrong County (72, Evidenced).** Site 15 (1,300 acres, local news
confirmed, no deed pulled). Physical 25 (Crusoe's TCEQ permit for the "Goodnight Data Center Power
Plant," 933MW, explicitly filed to power this co-located Google site). Financial 5 (statewide $40B
figure only, no site-specific number). Incentive 7 (registry match "Project Goodnight," eff.
2025-06-20 — exact name correspondence to the TCEQ filing). Track Record 20 (Google's global
delivery record).

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
Incentive 15 (the abatement is executed, not just filed — full credit tier). Track Record 20
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
revenue). Incentive 7 (registry match "Denton Data Center," eff. 2024-09-19). Track Record 10
(clean site-level operating history since 2022, but the corporate parent went through Chapter 11 in
2022–2023 — both facts logged, not averaged away). (25+15+7+10)/75×100 ≈ 76 — the largest single
jump of any project under renormalization, crossing Progressing→Evidenced (was 57 under true-zero
scoring), because its non-Physical signals are unusually strong relative to the 75-point base.

**17. Cipher Mining — Barber Lake (72, Evidenced).** Site 22 (SEC-adjacent disclosure of a closed
$67.5M acquisition). Physical 12 (TCEQ activity confirmed for a "portable plant" — construction
support, not a full generation permit). Financial 15 (Fluidstack HPC deal: ~$830M contracted
revenue, up to $9.0B potential value, $333M Google-backstopped debt). Incentive 7 (registry match
"Cipher Barber Lake LLC Data Center," eff. 2025-11-07 — also reveals the actual end-tenant is
Anthropic, PBC, with Fluidstack as operator). Track Record 16 (delivered acquisition-to-fully-leased
in ~14 months, SEC-auditable).

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
