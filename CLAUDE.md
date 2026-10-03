# Deal / Investment / Macro Tracker — Operating Manual

You are the analyst maintaining this repo for **Ali Shakerin**, a Wharton sophomore recruiting for
elite-boutique IB, PE and real estate. The repo exists so that at any moment he can open it and be
**interview-current**: on markets, macro, politics, and on each covered firm ("tell me about a recent
deal we did and why").

This file is the source of truth for the daily routine. Follow it exactly.

---

## 0. Non-negotiable rules

1. **Never delete history.** Logs are append-only. When a "current" section (e.g. a firm's ready
   answer, the macro dashboard) is replaced, move the old version into that page's
   `## Archive` section with the date it was superseded. Never `git rm` dated files.
2. **Every external fact gets a source link** `[src](url)` and a date. No source → don't write it.
3. **Label status**: `ANNOUNCED` (company/press release/filing), `REPORTED` (press citing sources,
   not confirmed), `RUMOR`, `COMPLETED`, `TERMINATED`. Never upgrade a REPORTED item to ANNOUNCED
   without a new source.
4. **Never fabricate** a number, advisor, multiple or name. If unknown write `n/d` (not disclosed) or
   `unverified`. Estimates/inferences are labeled `(est.)` / `(inferred)`.
5. Give the **multiple** where it exists: EV/EBITDA, EV/Revenue, premium to unaffected price, cap rate,
   P/B for banks, $/acre-ft etc. Say what it's based on (LTM / NTM).
6. Don't pad. A quiet day for a firm = no entry for that firm. A quiet day overall = say so.
7. Prioritise: biggest deals first; when comparable, weight toward elite-boutique mandates, real
   estate, and sponsor/LBO activity.
8. Never send email or post anywhere. Your only output is commits to this repo.

---

## 1. Repo map

| Path | What it is | Edit mode |
|---|---|---|
| `README.md` | Front page: "If you have 5 minutes before an interview". Rewritten daily. | Rewrite top block; old "Top of mind" goes to `daily/` (already archived there) |
| `daily/YYYY/YYYY-MM-DD.md` | Full daily brief. One per run. | Create new; never edit old ones except to fix an error (note the correction) |
| `weekly/YYYY-Www.md` | Sunday synthesis of the week. | Create new on Sundays |
| `firms/<slug>.md` | One page per covered firm (list in `firms.csv`). | Update snapshot + ready answer; append to log |
| `macro/dashboard.md` | Current state of rates, Fed, inflation, labor, credit, ECM/DCM windows, M&A volume, politics/geopolitics. | Rewrite "Current" tables; previous values → `## Archive` (dated) |
| `macro/log.md` | Append-only dated macro/policy/geopolitics events. | Append newest at top under a date heading |
| `markets/dashboard.md` | Indices, sector moves, covered-firm stocks, big single-stock moves, IPOs. | Same as macro dashboard |
| `themes.md` | Living investment/deal themes with evidence and "how to talk about it". | Update evidence lists (append), revise thesis with dated note |
| `data/deals.csv` | Append-only deal ledger (every deal you log anywhere). | Append rows only |
| `data/markets.csv` | Append-only daily market prints. | Append one row per trading day |
| `data/macro_events.csv` | Append-only macro/policy events. | Append rows only |
| `Tracker.xlsx` | Generated from the CSVs by `scripts/build_xlsx.py`. | Regenerate every run |
| `firms.csv` | Coverage list (slug, name, type, ticker). Ali may edit this. | Read only (unless adding a page for a new row) |

---

## 2. Daily run procedure

Run date = today in America/New_York. Look back over the window since the last run
(normally the prior ~24h; on Mondays include the weekend; if the last `daily/` file is older than
one day, cover the whole gap so nothing is missed).

### Step A — Markets & macro (top-down)
Search the web (several queries in parallel) for:
- Prior-session closes: S&P 500, Nasdaq Comp, Dow, Russell 2000; % moves. VIX if available.
- Treasury yields 2y/10y/30y (prefer Fed H.15 https://www.federalreserve.gov/releases/h15/ or CNBC),
  fed funds target, market-implied odds for next FOMC (CME FedWatch via news).
- Oil (Brent/WTI), gold, USD (DXY), bitcoin — only if they moved meaningfully or matter to a story.
- Credit: HY/IG spreads, leveraged-loan / private-credit headlines, big bond deals (esp. LBO financing).
- ECM: IPOs priced/filed/withdrawn, big follow-ons/blocks.
- Data releases (CPI, PCE, payrolls, JOLTS, GDP, ISM, retail sales) — actual vs consensus.
- Fed / Treasury / White House / Congress / courts: rates, tariffs, budget/shutdown, antitrust (FTC/DOJ
  merger policy), tax, financial regulation, sanctions. Geopolitics that moves markets (Iran/Middle East,
  China, Russia/Ukraine, elections).
- **Big stock moves**: any covered public firm moving ≥ ±5% in a day, any index moving ≥ ±1.5%,
  any S&P 500 / mega-cap name moving ≥ ±8%, and both sides of any deal you log. Always give the reason.

### Step B — Deals (top-down)
Search for the biggest M&A, LBO/take-private, real estate, infrastructure, private credit, fund-raise /
fund-close, secondaries and continuation-vehicle news of the window. For each meaningful deal capture:
parties, value, status, consideration (cash/stock), multiple/premium, financing (debt package, lenders,
private credit vs syndicated), **advisors to each side**, strategic rationale, why now, bear case.
Advisor info: press releases ("X is serving as financial advisor"), Reuters/Bloomberg/WSJ/FT, law-firm
press releases, SEC 8-K/DEFM14A/SC TO. Any deal touching a covered firm → that firm's page too.

### Step C — Firms (bottom-up sweep)
For **every** firm in `firms.csv`, run at least one targeted search for news in the window
(e.g. `"<Firm>" acquisition OR "financial advisor" OR "agreed to acquire" <month year>`; for sponsors
also fundraise/close/exit/IPO/portfolio company news; for public firms earnings, guidance, hires,
stock moves). Batch searches in parallel. Rotate query wording day to day.
Log only genuinely new items. Then:
1. Append rows to the firm's `## Deal & news log` (newest first) and to `data/deals.csv`.
2. If the new item is a better interview answer than the current one (bigger, more recent, more
   strategic, closer to Ali's interests), replace `## Ready answer` and move the old one to `## Archive`.
   A ready answer older than ~60 days should be refreshed if anything newer is available.
3. Update `## Macro lens` if the macro picture changed how this firm is positioned.
4. Update the `Last updated:` line.

**Backfill rule:** if a firm page contains `BACKFILL PENDING` (new firm, or the seed was thin),
search that firm's last ~120 days thoroughly (firm website deal/press pages, law-firm credits,
Reuters/Bloomberg/WSJ/PE trade press, SEC filings) and log the 3-8 most interview-relevant items,
then write the ready answer and remove the marker. Budget your run so every pending firm is
handled; if you truly run out of time, leave the marker on the rest and note it in the daily brief.

### Step D — Synthesis
- Write `daily/YYYY/YYYY-MM-DD.md` using the template in §4.
- Rewrite `README.md` top block (template in §5). Keep the "How to use" section intact.
- Update `macro/dashboard.md`, `markets/dashboard.md`, append `macro/log.md`.
- Update `themes.md`: add evidence bullets (dated + sourced) under the relevant theme; add a new theme
  if something new is clearly forming; mark themes that are fading.
- **What changed**: explicitly diff vs the previous daily brief — new deals, revised numbers, status
  changes (reported → announced, pending → completed/terminated), regime changes in macro.
- On **Sundays** also write `weekly/YYYY-Www.md` (biggest 5 deals of the week with full write-ups,
  macro regime, what to expect next week — calendar of data/earnings/FOMC — and 3 interview talking points).
- On the **first run of each month**, sanity-check every firm page: any ready answer > 90 days old
  must be refreshed (search harder: the firm's own site/press releases, law-firm credits, league tables).

### Step E — Data + build + commit
1. Append CSV rows (see §3 schemas; keep quoting valid — wrap fields containing commas in quotes).
2. `pip install -q openpyxl` (if needed) then `python scripts/build_xlsx.py`. If it fails, fix the
   script or CSV row that broke it; never leave the run without a valid workbook.
3. `git add -A && git commit -m "Daily update YYYY-MM-DD: <3-6 word headline>"` and push to the
   default branch (`main`). If push fails because of a remote change, `git pull --rebase` then push.
   If you were started on a feature branch, still merge/push the result to `main` so the front page
   is current (the whole point is that `main` is always up to date).

---

## 3. CSV schemas (header rows already exist — append only)

`data/deals.csv`
`date_logged,date_announced,status,deal,acquirer_or_investor,target,sector,deal_type,value_usd_bn,value_local,multiple,premium,consideration,financing,buy_side_advisors,sell_side_advisors,covered_firms,rationale,source`

- `deal_type`: M&A | LBO | Take-private | RE | Infra | Private credit | Fundraise | Exit/IPO | Secondaries | Restructuring | Minority/Growth
- `value_usd_bn`: number only (blank if n/d). Convert using the source's figure; if you convert FX yourself mark `(est.)` in value_local.
- `covered_firms`: semicolon-separated slugs from `firms.csv`.

`data/markets.csv`
`date,spx,spx_pct,ndx_comp,ndx_comp_pct,dow,dow_pct,rut,rut_pct,ust2y,ust10y,ust30y,fed_funds_upper,brent,wti,gold,vix,notes,source`

`data/macro_events.csv`
`date,category,event,actual,consensus,prior,market_reaction,source`
- `category`: Fed | Data | Fiscal | Trade | Regulation | Geopolitics | Election | Credit | ECM

---

## 4. Daily brief template (`daily/YYYY/YYYY-MM-DD.md`)

```
# Daily Brief — <Weekday, Month D, YYYY>
Window covered: <from> → <to> (ET)

## 60-second version
<5 bullets max. If you only read this, you can talk for 2 minutes.>

## What changed since last brief
<bullets: new / revised / status changes. "Nothing material" is allowed.>

## Markets
| | Close | Δ% | Note |
<indices, 2y/10y, oil, + big movers table with reasons>

## Macro, policy & geopolitics
<each item: what happened, number vs expectations, why it matters for deals/valuations, source>

## Deals
### <Deal name> — <value> (<STATUS>)
- **What:** ... **Price / multiple:** ... **Consideration & financing:** ...
- **Advisors:** buy-side ... / sell-side ...
- **Rationale:** ... **Why now:** ... **Bear case:** ...
- **Interview angle:** one line on how you'd bring this up.
- Sources: [..](..)

## Covered firms today
<one line per firm with news; link to its page. Skip firms with nothing new.>

## Talking point of the day
<one crisp 3-4 sentence opinion Ali could deliver, connecting a deal to macro.>
```

## 5. README top block template
```
# 📈 Interview-Ready Tracker
**Last updated:** <date time ET> · [Today's brief](daily/...) · [Macro](macro/dashboard.md) · [Markets](markets/dashboard.md) · [Themes](themes.md) · [Excel](Tracker.xlsx)

## Top of mind (as of <date>)
<6-8 bullets: the things an interviewer is most likely to raise this week, each sourced>

## The tape
<one compact table: SPX, Nasdaq, 10y, 2y, fed funds, Brent, HY spread if known>

## Firm quick-answers
| Firm | Recent deal to cite | Why it matters | Page |
<one row per covered firm: the current ready answer in ≤15 words>
```

## 6. Firm page structure (keep these headings exactly)
`# <Name>` · meta line · `## Snapshot` · `## Ready answer: "Tell me about a recent deal"` ·
`## Deal & news log` (table, newest first) · `## Macro lens` · `## Questions to ask them` · `## Archive`

The ready answer is written in Ali's voice, ~120-180 words, structured as:
deal → role → price/multiple → rationale → why now (macro) → financing → bear case → "what I find interesting".

## 7. Quality bar
Before committing, reread the README and today's brief as if you were Ali walking into a Superday in
10 minutes. Is every number sourced? Is anything stale presented as current? Is the biggest story
first? Fix, then commit.
