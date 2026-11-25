#!/usr/bin/env python3
"""Measure how often the MCP server's match_archetype ranks the right archetype,
using the recognition evals as the test set. Run from this directory."""
import sys, json
sys.argv = ["x"]
sys.path.insert(0, ".")
import bundle_mcp_server as s
arch = {c for c, v in s.CARDS.items() if v["type"] == "archetype"}
top1 = top3 = n = 0
for e in s.EVALS:
    if e["kind"] != "recognize": continue
    want = [u for u in e["uses"] if u in arch]
    if not want: continue
    n += 1
    got = [c["id"] for c in json.loads(s.match_archetype(e["prompt"], limit=3))["candidates"]]
    h1 = got[0] in want; h3 = any(g in want for g in got)
    top1 += h1; top3 += h3
    print(f"{e['id']:9} want={want[0]:38} got={got}")
print(f"top1 {top1}/{n}  top3 {top3}/{n}")
