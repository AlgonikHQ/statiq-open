# How every tip is graded

## Result types
| Status | Meaning | Counts in win/loss? |
|---|---|---|
| WIN | The tip won | Yes |
| LOSS | The tip lost | Yes |
| VOID | The bet was returned, for example the match was postponed or cancelled | No |
| EXCLUDED | Removed from the record for a stated reason, such as a data error when the tip fired. The reason is in the `note` column | No |
| PENDING | Not settled yet | No |

Nothing is ever deleted. Void and excluded tips stay in `record.csv` with their reason.

## Abandoned matches
We settle these the way bookmakers do. A market already decided when the match was abandoned
stands (for example, Over 2.5 goals when it was already 4-0). Anything not yet decided is void.
The tip carries a note saying so.

## Stakes and profit
- Every tip is a 1-unit paper bet at the price recorded when it fired.
- A win returns price minus 1 (a win at 1.80 = +0.80 units). A loss is -1 unit.

## Which tips count towards units and ROI
| `price_type` | What it means | Units and ROI? |
|---|---|---|
| verified | A real bookmaker price was captured before kick-off | Yes |
| stats | A stats-based call with no price attached | Win/loss only |
| pre_audit | Early beta tips, before real prices were captured | Win/loss only |

"Last 200" means the most recent 200 decided tips (wins and losses).
