---
title: "First pass yield vs rolled throughput yield: which one tells the truth?"
short: "FPY vs RTY"
description: "First pass yield measures right first time at one step. Rolled throughput yield multiplies every step. How to calculate both, and what final yield hides."
published: 2026-10-24
category: education
art: spc
---

"Our yield is 97%." It sounds good. But which yield? The yield you report and the yield the line actually achieves can be very different numbers.

## Final yield: what comes out the end

**Final yield** is simply good units out divided by units started. If you start 1,000 and ship 970, final yield is 97%.

The problem is that it counts reworked units as good. A part that was fixed twice before it passed looks exactly the same as one that was right first time. That hidden rework costs time and capacity.

## First pass yield: right first time, at one step

**First pass yield** (FPY), sometimes called first time yield, is the share of units that pass a step without rework or scrap. Some manufacturers, particularly in automotive, use first time through quality (FTTQ) for a similar measure, often across a whole process and counting any repair or retest as a failure.

**FPY = units passing first time ÷ units entering the step**

If 1,000 units enter a welding step and 950 pass without rework, FPY for that step is 95%.

FPY shows how well each step really performs. It's often measured for a single step, or for the line as a whole.

## Rolled throughput yield: right first time, all the way through

**Rolled throughput yield** (RTY) is the probability that a unit gets through every step of the process right first time. You multiply the FPY of each step together.

**RTY = FPY step 1 × FPY step 2 × FPY step 3 … and so on**

Take a line with four steps, each with an FPY of 95%. RTY is 0.95 × 0.95 × 0.95 × 0.95, which is about 81%. So only 81 units in every 100 make it through without being touched again, even though every step looks good on its own and final yield might be 97%.

## Side by side

| | Final yield | First pass yield | Rolled throughput yield |
| --- | --- | --- | --- |
| **Measures** | Good units out of units started | Units right first time at a step | Units right first time across all steps |
| **Counts rework as good?** | Yes | No | No |
| **Scope** | Whole process | One step, or the line | Whole process, step by step |
| **Shows hidden rework?** | No | At that step | Across the process |
| **Best for** | Reporting output | Finding weak steps | Seeing the true cost of quality |

## Why it matters

RTY is the metric that reveals the "hidden factory": the rework loops and re-inspections that never show up in final yield. It's popular in Six Sigma for exactly that reason.

The weakest steps drag RTY down fastest, so it also tells you where to focus. Improving one poor step from 80% to 95% lifts RTY far more than polishing a step that's already at 99%.

## Where the data comes from

To calculate FPY and RTY you need to know, at every step, which units passed first time and which were reworked. On paper, rework is often not recorded at all.

MES/MOM records each pass, fail and rework against the unit or lot and the operation, so FPY and RTY can be calculated automatically, by product and line. More in [Manufacturing KPIs beyond OEE](/post/manufacturing-kpis-beyond-oee).

If you multiplied your step yields together today, how close would the answer be to the yield you report?
