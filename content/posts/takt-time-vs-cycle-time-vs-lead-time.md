---
title: "Takt time vs cycle time vs lead time: what each one measures"
short: "Takt vs cycle vs lead time"
description: "Takt time is the pace demand sets, cycle time is how fast you work and lead time is how long customers wait. How to calculate each, and how they relate."
published: 2026-10-24
category: education
art: timeline
---

Takt time, cycle time and lead time all sound like ways of saying "how long it takes". They're often used interchangeably, and that leads to bad decisions about capacity and promises to customers.

Each one answers a different question.

## Takt time: the pace demand sets

**Takt time** is the rate you need to produce at to meet customer demand. It comes from the German word for a beat or pulse.

**Takt time = available production time ÷ customer demand**

If a line runs for 450 minutes a shift and customers need 900 units a shift, takt time is 30 seconds. To keep up, you need to finish one unit every 30 seconds.

Takt time is a target set by the market. It doesn't measure your process at all.

On a paced line, such as a moving automotive assembly line, you'll often hear takt used for the fixed time each unit spends at every station. That's takt in practice: the line is set to advance at takt time, sometimes slightly faster to allow for losses. Line balancing then spreads the work across stations so each one's tasks fit within that time, with as little idle time as possible. When demand changes, takt changes, and the line is re-balanced or the shift pattern adjusted.

## Cycle time: how fast you actually work

**Cycle time** is how long it actually takes to complete one unit, or one step, from start to finish. You measure it on the line.

People use it in slightly different ways. It can mean the time for one operation, or for a unit to pass through the whole line. Agree which one you mean before you compare numbers.

If cycle time is longer than takt time, you can't keep up with demand without overtime or more capacity. If it's well under takt time, you have spare capacity, or more resources than you need.

## Lead time: how long the customer waits

**Lead time** is the total time from a customer placing an order to receiving it. It includes everything: order processing, waiting for materials, queuing between operations, processing itself, inspection and shipping.

Manufacturing lead time is the shopfloor part of that, from releasing an order to finishing it.

In most factories, processing is a small fraction of lead time. Most of it is waiting.

## Side by side

| | Takt time | Cycle time | Lead time |
| --- | --- | --- | --- |
| **Question it answers** | How fast do we need to produce? | How fast do we actually produce? | How long does the customer wait? |
| **Set by** | Customer demand | The process | The whole system, including waiting |
| **Calculated from** | Available time ÷ demand | Measured on the line | Order to delivery |
| **Typical unit** | Seconds or minutes per unit | Seconds or minutes per unit | Hours, days or weeks |
| **Used to** | Balance lines and staff them | Find bottlenecks and improve | Set customer promises and cut waiting |

## How they relate

The three tell a story together.

**Cycle time against takt time** tells you whether you can meet demand. Compare them station by station and the bottleneck usually jumps out.

**Lead time against total cycle time** tells you how much waiting is in the system. If a product needs 40 minutes of actual work but takes five days to get through the factory, the opportunity is in the queues, not the machines.

## Where the real numbers come from

Most planning systems use standard cycle times that someone entered years ago. Actual cycle times drift with product mix, operators, tooling and machine condition.

MES/MOM measures them as work happens: actual cycle times by product and machine, along with the waiting between operations. That replaces estimates with measured values, and keeps schedules realistic. More in [APS vs ERP scheduling](/post/aps-vs-mes-scheduling) and [Manufacturing KPIs beyond OEE](/post/manufacturing-kpis-beyond-oee).

When did you last compare your standard cycle times with what the line actually does?
