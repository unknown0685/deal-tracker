# 📈 Interview-Ready Tracker
**Last updated:** Sat Oct 3, 2026 (seed) · [Today's brief](daily/2026/2026-10-03.md) · [Macro](macro/dashboard.md) · [Markets](markets/dashboard.md) · [Themes](themes.md) · [Excel](Tracker.xlsx)

## Top of mind (as of Oct 3, 2026)
- **The Fed is hiking, not cutting.** It raised 25bp on Sep 16 to 3.75–4.00%, the first hike since 2023, under Chair Warsh. The median dot implies one more this year ([fedratecalc](https://fedratecalc.com/fomc-meeting-schedule/september-2026/)).
- **The jobs miss changed the October math.** Payrolls were +29k vs 84k est. and unemployment rose to 4.2%. Hike odds fell from 64% to ~22%, yet the 10y still closed at 5.28% ([Yahoo](https://finance.yahoo.com/markets/stocks/articles/p-500-nasdaq-dow-end-222859024.html)).
- **The 10y hit a 2002 high (5.34%) in Q3, and global M&A fell 41% q/q to $993bn.** YTD is still a record since 2001 at $3.9tn ([Reuters/LSEG](https://www.globalbankingandfinance.com/global-m-deal-rush-fades-third-quarter-rising-borrowing/)).
- **All-stock is the deal structure of the moment:** Cegid–Silae (€10bn), IRT–Centerspace ($8.1bn), Tamarack–Headwater (C$10bn) ([Intellizence](https://intellizence.com/insights/merger-and-acquisition/top-5-ma-deals-of-the-week-reshaping-aerospace-software-real-estate-energy-and-banking/)).
- **REIT take-privates:** Blackstone/H&R REIT (C$6.7bn), Ares/Whitestone ($1.7bn), Brookfield/Peakstone ($1.2bn). See [Themes §3](themes.md).
- **Private-credit redemption stress:** Blackstone held its 5% gate; Blue Owl investors sought to pull 39% of a $5bn fund ([Benzinga](https://www.benzinga.com/markets/private-markets/26/10/62146487/blue-owl-investors-seek-to-pull-39-from-5b-tech-credit-fund)).
- **Oil and Iran:** WTI is ~$91. GS sees Brent at $85 by Dec as Gulf disruption persists ([Arab News](https://www.arabnews.com/business/oil-rises-as-risks-of-prolonged-mideast-conflict-fan-supply-worries-3000890)).
- **Sponsor auction to watch:** KKR, Blackstone and Warburg are circling Cary at ~€3bn (reported) ([Bloomberg](https://www.bloomberg.com/news/articles/2026-10-02/kkr-blackstone-are-among-suitors-for-windshield-repairer-cary)).

## The tape (Fri Oct 2 close)
| S&P 500 | Nasdaq | Dow | 2y | 10y | 30y | Fed funds | WTI |
|---|---|---|---|---|---|---|---|
| 7,722.72 (+0.73%) | 27,190.86 (+1.2%) | 51,176.96 (+0.49%) | 4.78%* | 5.28% | 5.62% | 3.75–4.00% | $91.11 |
\*Oct 1, Fed H.15. Sources: [Yahoo](https://finance.yahoo.com/markets/stocks/articles/p-500-nasdaq-dow-end-222859024.html), [H.15](https://www.federalreserve.gov/releases/h15/)

## Firm quick-answers
| Firm | Recent deal to cite | Why it matters | Page |
|---|---|---|---|
| Evercore | HighPeak Energy sale process (reported) | Energy M&A on the oil spike | [→](firms/evercore.md) |
| Centerview | Semrush → Adobe, $1.9bn (Nov '25) | Sole-advisor sell-side; to be refreshed | [→](firms/centerview.md) |
| PJT | ⏳ backfill pending | | [→](firms/pjt.md) |
| Lazard | AUM $290.3bn (Aug) | Asset-mgmt outflows vs advisory growth | [→](firms/lazard.md) |
| Moelis | Taylor Morrison → Berkshire, $8.5bn | Housing-shortage bet; record pipeline | [→](firms/moelis.md) |
| Perella Weinberg | Buying Gleacher Shacklock (UK) | Boutique consolidation | [→](firms/perella-weinberg.md) |
| Guggenheim | Destination XL merger; Millstein acquisition | Restructuring build-out | [→](firms/guggenheim.md) |
| Qatalyst | ⏳ backfill pending (CyberArk → PANW as context) | | [→](firms/qatalyst.md) |
| Goldman Sachs | #1–2 in 2026 M&A tables | Fees lag announcements | [→](firms/goldman-sachs.md) |
| Morgan Stanley | ~$1tn of deals YTD | ECM leader in an AI-IPO year | [→](firms/morgan-stanley.md) |
| J.P. Morgan | #1–2 in 2026 M&A tables | Bank vs private credit in LBO financing | [→](firms/jpmorgan.md) |
| Blackstone | H&R REIT take-private, C$6.7bn | Public-to-private RE arbitrage | [→](firms/blackstone.md) |
| KKR | Cary auction (reported) | Sponsor appetite despite 5% rates | [→](firms/kkr.md) |
| Apollo | NSG closed; $1.25bn BMG–Concord solution | Capital solutions > classic LBO | [→](firms/apollo.md) |
| Carlyle | Continuation vehicle (Moelis-advised) | Exits slow → CVs | [→](firms/carlyle.md) |
| TPG · Bain · Thoma Bravo · H&F · Advent · EQT · Starwood | ⏳ backfill pending | | [firms/](firms/) |
| Silver Lake | EA take-private (2025, context) | Largest LBO ever | [→](firms/silver-lake.md) |
| Warburg Pincus | Ingenia ~$1.5bn raised bid; Cary | RE platforms + growth | [→](firms/warburg-pincus.md) |
| Brookfield | Peakstone Realty, $1.2bn | REIT take-private; AI-power infra | [→](firms/brookfield.md) |
| Ares | Whitestone REIT, $1.7bn | Private credit bellwether + RE | [→](firms/ares.md) |

---

## How to use this
- **5 minutes before an interview:** this page, then the firm's page (its "Ready answer" is written to be said out loud).
- **Going deeper:** [themes.md](themes.md) connects deals to macro; every daily brief lives in [daily/](daily/) and is never deleted.
- **Excel:** [Tracker.xlsx](Tracker.xlsx) holds the full deal ledger, market time series and macro events, with live formulas and native charts. It is rebuilt daily from [data/](data/).
- **Change coverage:** edit [firms.csv](firms.csv) (add a row). The next run creates the page and backfills ~120 days.
- **How it updates:** a Claude cloud routine runs daily at 6:30am ET, reads [CLAUDE.md](CLAUDE.md), researches, and commits here. Everything is versioned in git history, so nothing is ever lost.
