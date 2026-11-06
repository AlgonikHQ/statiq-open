# The checks behind every record update

The record on the site is rebuilt every few minutes. Before it's published, every one of these must pass.
If any fails, the old record stays up and we're alerted.

1. **The groups add up.** Wins and losses across verified, stats and pre-audit tips add up to the all-time total.
2. **Wins + losses = decided.** No tip is counted twice or missed.
3. **Every tip is accounted for.** Decided + pending + void + excluded = every tip ever published.
4. **The weeks add up.** Every week's results add up to the all-time total.
5. **Units recalculate from the tips.** The headline units are re-added from each individual tip.
6. **It matches the bot's own ledger.** The published record must match the tip bot's running total exactly.

## Independent re-grading
Separately, an audit re-checks every settled tip against the actual final scores, to catch any tip graded wrongly.

## Corrections
Anything we get wrong goes in the public [corrections log](https://90minwaffle.co.uk/corrections/):
what was shown, what's correct, and what it affected.
