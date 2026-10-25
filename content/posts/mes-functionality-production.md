---
title: "MES functionality: production monitoring"
short: "Production monitoring"
description: "How MES/MOM runs and monitors production orders in real time: counts, scrap, rework, downtime and labour, and how machine data feeds OEE."
published: 2023-06-08
updated: 2026-10-25
category: education
art: signal
series: functionality
order: 1
---

Managing and monitoring production is the most fundamental job of an MES. Once the schedule is released, operators start and run production orders on the line, and MES records what happens, often by talking directly to the equipment. A large amount of useful data is collected as a by-product.

The production order is the main context in any MES. In a good system, everything is tied back to it: production counts and downtime, but also quality checks and the material consumed and created.

For many manufacturers, production monitoring is their first step into MES. There are good standalone production monitoring and OEE tools on the market, often cheaper than a full MES/MOM. The trade-off is what happens when requirements grow beyond production, which is covered in [MES vs MOM](/post/mes-vs-mom).

## What production monitoring records

### Production counts

Counts show how much has been made against the plan, in real time. Comparing actual against planned output shows where a line is falling behind, and feeds the performance and quality parts of OEE.

How you count depends on the process:

- **Discrete items:** count each piece.
- **Batches:** weigh the batch.
- **Multi-cavity tools or presses:** count machine cycles, and let MES multiply by the number of pieces made per cycle.
- **Continuous material:** measure length or weight, and convert where needed.

Some MES platforms record the same output in more than one unit. A reel of material might be recorded in metres, and also in square metres by multiplying by the width.

### Scrap

Scrap is output that's defective or unusable, or material that's wasted. Recording it in real time, with a reason, shows quality problems while there's still time to act, and builds the history needed to spot repeat causes.

Some equipment records scrap automatically, such as vision systems or in-line gauges. Where the machine knows the cause, the reason should be logged automatically too. Where it doesn't, the operator adds the reason.

### Rework

A defective item can sometimes be saved by sending it back through earlier operations, or to a dedicated rework step. Rework is most common in discrete and assembly processes, and for higher-value items.

Rework still costs time and capacity. First pass yield measures how much is right first time: if 100 pieces are made and 3 need rework, first pass yield is 97%. Rework also lowers OEE, because more time is spent on the same piece. More in [First pass yield vs rolled throughput yield](/post/first-pass-yield-vs-rolled-throughput-yield).

### Downtime

Downtime is time when equipment isn't producing, through breakdowns, changeovers, missing materials or people, or other causes. It's one of the biggest sources of lost output.

Frequent short stops often cost more than the occasional long one. A breakdown is visible and gets attention. A stop of a few seconds, repeated hundreds of times a shift for the same reason, rarely gets recorded at all, but it interrupts the operator constantly and drains availability.

Without automatic capture from the machine, those short stops usually go unnoticed. That's why OEE often drops when MES is first introduced: the figures become accurate for the first time. Downtime data matters to maintenance as much as production, which is covered in [MES functionality: maintenance](/post/mes-functionality-maintenance).

### Labour

Labour is a large part of production cost. MES can record who worked on which order and for how long, which supports costing and staffing decisions.

Individual logins work better than shared ones. They allow time to be allocated properly, and let MES restrict actions to people with the right qualifications. Some businesses and unions push back, so it's worth agreeing the approach early. More in [skills you can enforce, not just record](/post/skills-enforcement-shopfloor).

### OEE

OEE (overall equipment effectiveness) measures how well equipment is used, compared with its full potential. It depends directly on the data above. More in [What is OEE?](/post/what-is-oee) and [OEE vs OOE vs TEEP](/post/oee-vs-teep).

### Executing production orders

MES shows each order's progress against the plan, so supervisors can see early when a job will finish late or a line becomes a bottleneck. How orders get onto the line in the first place is covered in [MES functionality: production scheduling](/post/mes-functionality-scheduling).

## Preventing problems, not just recording them

Production monitoring is sometimes seen as a way of recording what happened. A good MES also prevents problems, by validating actions as they happen:

- The wrong material can't be consumed.
- An order can't start without its first-off check.
- A stop can't be closed without a reason.
- An operator without the right qualification can't run the machine.

A system that only records creates a digital paper trail. A system that validates stops mistakes before they become scrap.

## Automatic vs manual data collection

| | Automatic | Manual |
| --- | --- | --- |
| **Timing** | Real time | When the operator gets to it |
| **Accuracy** | High, including short stops | Prone to rounding and gaps |
| **Operator effort** | None | Takes time from the job |
| **Cost to set up** | Machine connectivity needed | Low |

Automatic collection is usually preferable where the equipment allows it. Manual entry still has a place for older machines, or for information only a person can give, such as the reason behind a stop.

## Connecting to machines

The most common standard for machine data is OPC UA, which replaced the older OPC DA. OPC UA is more secure, using certificates for authentication. MQTT is widely used too, particularly for moving data from many devices to many systems, and MTConnect is common on machine tools. More in [OPC UA vs MQTT](/post/opc-ua-vs-mqtt).

Connection can work in both directions. In more advanced processes, starting an order in MES can send the right program and parameters to the machine, so it runs the correct job. That should always go through the control layer, which keeps responsibility for safe operation. More in [PLC vs SCADA vs DCS vs MES](/post/plc-vs-scada-vs-dcs-vs-mes).

## What happens to the data

MES captures data at a much finer level than ERP, and sends summaries back to ERP for costing and planning. ERP doesn't need every transaction, only the totals. More in [How MES takes complexity out of your ERP](/post/mes-simplifies-erp).

The detailed data is valuable for continuous improvement, and increasingly for analytics and AI, because each event comes with the context of the order and the operator. More in [contextualised data](/post/contextualised-manufacturing-data).

## What it delivers

- **Paperless production:** the schedule reaches the line in real time, and workflows make sure exceptions are handled the same way every time.
- **Real-time visibility:** OEE by line and shift, while there's still time to act.
- **More output from the same equipment:** downtime causes become visible, including the short stops nobody wrote down.
- **Less waste:** scrap and rework are recorded with reasons, so the biggest causes can be tackled.
- **Fair comparisons:** the same measures across machines and sites make benchmarking meaningful.
- **Better use of people:** labour data supports staffing and shift decisions.

## My view

Think about where your requirements are heading before you choose. A standalone monitoring tool can be a quick win, but if you'll need the other pillars on the same data within a few years, I'd start on a platform that can grow into them rather than replace a stop-gap later.

This article is part of the [MES functionality series](/post/mes-functionality-guide). Related: [Manufacturing KPIs beyond OEE](/post/manufacturing-kpis-beyond-oee).

How many of your short stops are being recorded today?
