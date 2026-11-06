#!/usr/bin/env python3
"""Recalculate the StatiQ record from record.csv - the same rules the site uses.
Usage: python3 verify.py record.csv"""
import csv, sys
rows = list(csv.DictReader(open(sys.argv[1] if len(sys.argv) > 1 else "record.csv", encoding="utf-8")))
def tally(rs):
    w = sum(r["status"] == "WIN" for r in rs); l = sum(r["status"] == "LOSS" for r in rs)
    return w, l, (round(100.0 * w / (w + l), 1) if w + l else 0)
w, l, sr = tally(rows)
p = sum(r["status"] == "PENDING" for r in rows); v = sum(r["status"] == "VOID" for r in rows); x = sum(r["status"] == "EXCLUDED" for r in rows)
ver = [r for r in rows if r["price_type"] == "verified" and r["status"] in ("WIN", "LOSS")]
units = round(sum(float(r["profit"] or 0) for r in ver), 2); staked = round(sum(float(r["stake"] or 1) for r in ver), 2)
vw, vl, _ = tally(ver)
dec = [r for r in rows if r["status"] in ("WIN", "LOSS")]; lw, ll, _ = tally(dec[-200:])
print("All calls:      %d-%d (%.1f%% won)" % (w, l, sr))
print("Real prices:    %d-%d | %+.2f units | ROI %+.2f%% (%d tips)" % (vw, vl, units, 100.0 * units / staked if staked else 0, len(ver)))
print("Last 200 calls: %d-%d" % (lw, ll))
print("Also listed:    %d pending, %d void, %d excluded (reasons in the note column)" % (p, v, x))
print("Every tip accounted for:", w + l + p + v + x == len(rows), "(%d tips)" % len(rows))
