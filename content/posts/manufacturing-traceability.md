---
title: "Your traceability probably isn't as good as you think"
short: "Manufacturing traceability"
description: "Batch-level tracking and backflushing in ERP is better than nothing, but nowhere near what's possible. What full traceability looks like, and why it matters in a recall."
published: 2026-10-16
category: education
art: flow
---

Most manufacturers think they've got traceability sorted.

They don't.

I see it all the time. Traceability at order or batch level in ERP, often with backflushing. It's better than nothing. But it's nowhere near what's possible, and you usually find that out on the worst possible day: when a recall or a serious complaint lands.

## What ERP traceability usually gives you

ERP typically knows that a production order consumed certain materials and produced a certain quantity. With backflushing, consumption is often calculated from the bill of materials after the fact, not recorded as it happened.

So you know roughly what went into an order. You don't know exactly which lot went into which part of it, when, or under what conditions.

For a straightforward product with low risk, that may be enough. For most manufacturers, it isn't.

## What full traceability looks like

With [MES/MOM](/post/what-is-mes-and-why-is-it-important-in-manufacturing), traceability can go much deeper:

- **Serialised items**, tracked individually
- **Specific lot quantities**, so you know exactly how much of each lot went into each output
- **Time-based traceability** for continuous processes, using actual lead times through the line
- **Bi-directional** tracing: forwards from a raw material lot to every finished product it touched, and backwards from a finished product to everything that went into it

That's the genealogy. But it's only the start.

## The supplementary data is where the real value is

The difference between adequate and excellent traceability is everything you capture alongside the genealogy:

- **Tooling** used at each operation
- **Quality results** at every level: goods-in inspection, in-process checks, final inspection
- **Context**: operator, timestamp, machine and machine position
- **Process parameters** at the time the item or batch was made: temperatures, pressures, speeds

When a quality issue is detected, this is what makes root cause analysis straightforward instead of guesswork. You can see that every failed part came from the same cavity of the same mould, during the same two hours, when the temperature drifted.

## Why it matters in a recall

Picture a complaint arriving on a Friday afternoon.

With order-level ERP traceability, you know which orders might be affected. You quarantine everything from that period to be safe. You spend the weekend in spreadsheets and paper records trying to narrow it down.

With full traceability, you trace the affected lot forwards in minutes, identify exactly which finished products contain it, check their inspection results and process conditions, and quarantine only what's genuinely at risk.

Speed is only part of it. The bigger differences are how much good product you destroy, how much customer trust you keep, and how confident you are in front of a regulator.

## Inventory and quality on the same data

This is a good example of why I care about MOM rather than separate systems.

Traceability needs inventory movements, production events and quality results linked together. If inventory lives in one system and quality in another, you can trace the material, but not easily its inspection status at each step. Every integration boundary is a place where context gets lost.

When they share one platform, an inspection result is attached to the lot it was performed on, and the lot is attached to everything made from it.

## It still syncs with ERP

None of this replaces ERP. MES/MOM holds the detail and sends ERP what it needs, at the right level: actual consumption rather than backflushed estimates. ERP's data gets better, not worse. More on that in [MES vs ERP](/post/implementing-mes-can-simplify-your-erp).

## A simple test

Pick a finished product shipped last month. Ask your team how long it would take to tell you every raw material lot in it, the inspection results at each stage, and the machine conditions when it was made.

If the answer is measured in days, your traceability isn't as good as you think. If it's measured in minutes, congratulations. You're in the minority.

When did you last run a mock recall, and how long did it take?
