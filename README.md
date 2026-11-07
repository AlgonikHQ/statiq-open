# StatiQ (open record)

StatiQ is the football model behind the tips on [90minwaffle.co.uk](https://90minwaffle.co.uk/edges/).

This repo exists for one reason: so you don't have to take our word for it.

## The promise
- Every tip goes up before kick-off, with the price it was taken at.
- Every result stays on the record. Wins, losses, voids, all of it.
- Nothing is deleted, edited after the fact, or quietly left out.

## What's in here
| File | What it is |
|---|---|
| `record.csv` | Every tip: date, match, league, market, price, result, profit |
| `verify.py` | Recalculate the record yourself from `record.csv` |
| `GRADING.md` | Exactly how each tip is settled, including abandoned matches |
| `CHECKS.md` | The checks every record update must pass before it goes live |

## How to check us

Download `record.csv` and `verify.py`, then run:

    python3 verify.py record.csv

It prints wins, losses, units and ROI. They should match the tips page on the site.
If they don't, tell us and it goes in our public [corrections log](https://90minwaffle.co.uk/corrections/).

## How the record is counted
- Stakes are 1-unit paper bets at the price recorded when each tip fired.
- Only tips with a real bookmaker price count towards units and ROI.
  Tips without a price count towards the win/loss record only.
- Every update runs consistency checks. If any fails, the record is not published until it's fixed.
- A separate audit re-grades every settled tip against the actual scores.

## What isn't here
How picks are made (the model, its inputs and its thresholds) stays private.
This repo is about checking results, not copying picks.

## Links
- Live record: https://90minwaffle.co.uk/edges/
- How it works: https://90minwaffle.co.uk/method/
- Corrections log: https://90minwaffle.co.uk/corrections/

18+ | Past results don't predict future ones | [BeGambleAware.org](https://www.begambleaware.org)

<!-- PRICECHECK_20261107 -->
## Independent price check

Every week each priced tip is checked against independent bookmaker prices from [Football-Data.co.uk](https://www.football-data.co.uk/): the market average and the best price available, before kick-off and at the close.

- **Impossible prices are removed.** If a recorded price is higher than the best price any bookmaker offered, the tip is excluded from units and ROI and listed with the reason, its original result and its price. On 7 November 2026 this removed 33 old tips, 32 of them from May 2026, before prices were timestamped. The record moved from 121-118, +27.44u, ROI +11.58% to 102-104, +14.08u, ROI +6.9%. The full note is on the site's Corrections page.
- **Closing line value (CLV) is published.** CLV compares our price with the market's closing price. Staying above zero over time is the clearest sign of a real edge. It's shown on the tips page and updated weekly, whether it's good or bad.
