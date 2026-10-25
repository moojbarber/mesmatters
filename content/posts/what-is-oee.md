---
title: "What is OEE? How to calculate overall equipment effectiveness"
short: "What is OEE?"
description: "How to calculate OEE step by step with worked examples, and why the bottleneck is the machine that really counts when you measure a line."
published: 2023-06-08
updated: 2026-10-25
category: education
art: rings
start: 4
---

Overall equipment effectiveness (OEE) is the most widely used measure of how well a production line performs. It compares the good product a line actually made with the good product it could have made in the time it was planned to run.

> OEE asks: are we making good product, at full speed, for all of the time we planned to?

Every loss reduces OEE, and breaking it into its parts shows where those losses are. That's what makes it useful for improvement.

## The OEE formula

> **OEE = Availability × Performance × Quality**

The international standard for OEE and related measures is ISO 22400. It defines each component precisely, along with many other manufacturing KPIs. Part of it is [free to view online](https://www.iso.org/obp/ui/#iso:std:iso:22400:-2:ed-1:v1:en), and the full standard is worth buying if you're setting up KPIs across several sites. This article uses plain descriptive terms rather than the ISO names.

## Availability

Availability is the share of planned time that the line was actually running. Time the line wasn't planned to run, such as weekends when the factory is closed, is excluded.

> **Availability = Run time ÷ Planned production time**

If a line is planned for an 8-hour shift and stops for 2 hours, availability is 6 ÷ 8 = 75%.

### Why the bottleneck is what counts

Most lines have several machines, each doing a different operation. For OEE, the machine that matters is the bottleneck: the one with the lowest throughput.

If other machines are faster than the bottleneck, they can stop for short periods without affecting output. If the bottleneck keeps running, the line can't produce any faster, so those stops don't change OEE.

Longer stops elsewhere do reach the bottleneck. A stop upstream eventually starves it of material. A stop downstream eventually blocks it, because it has nowhere to send its output.

## Performance

Performance compares how fast the line actually ran with its target speed. Each operation has a target cycle time: how long it should take to make one unit.

> **Performance = Quantity produced ÷ Target quantity**

The target quantity is what the line would have made in its run time at the target cycle time. Quantity produced includes scrap.

If a line should make 6 pieces a minute, its target cycle time is 10 seconds. If it actually makes 4 pieces a minute, its actual cycle time is 15 seconds, and performance is 10 ÷ 15 = 67%.

Formally, both quantities are multiplied by the target cycle time, so everything is expressed in time. That lets you compare products with different cycle times. The time terms cancel out, which is why the simple version above works.

**Performance above 100%** means the target cycle time in your master data is too slow. It's tempting to leave it and enjoy the higher score, but that hides the improvement opportunity. Recognise what the team has achieved, then update the target.

## Quality

Quality is the share of everything produced that was good.

> **Quality = Good quantity ÷ Quantity produced**

If a line makes 100 pieces and 95 are good, quality is 95%.

Scrap reduces the quality figure. Rework doesn't, but it still costs OEE: reworked parts go through the process more than once, so it takes longer to make the same good quantity, and that shows up in performance.

Some processes produce an expected amount of waste as part of the process. Planned waste of that kind isn't counted as a quality loss.

## Putting it together

> **OEE = Availability × Performance × Quality**

Expanded, that's:

> **OEE = (Run time ÷ Planned time) × (Quantity produced ÷ Target quantity) × (Good quantity ÷ Quantity produced)**

Which simplifies to:

> **OEE = Good quantity ÷ (Planned production time ÷ Target cycle time)**

That's the good product made, compared with what the line could have made in the planned time at the target speed.

So why split it into three parts at all? Because the parts tell you where the losses are, and that's where improvement starts.

## A worked example outside the factory

OEE can measure the effectiveness of almost anything. Imagine someone typing for an hour.

- **Availability.** They plan to type for 60 minutes, but take a 10-minute coffee break and stop 5 minutes early for lunch. They type for 45 minutes, so availability is 75%.
- **Performance.** Their top speed is 50 words a minute, but they average 40. Performance is 80%.
- **Quality.** Typing errors that need correcting cost 5%, so quality is 95%.

The most they could have typed in the hour is 60 × 50 = 3,000 words.

> OEE = 75% × 80% × 95% = 57%, or 1,710 words.

## Where you count changes where losses show

Move the sensor that counts production and your performance and quality figures can swing, while OEE stays exactly the same.

That's because OEE comes down to good units multiplied by target cycle time, divided by planned time. If good units and planned time don't change, neither does OEE. Where you count only shifts the losses between the components.

**Counting before the bottleneck** makes the bottleneck look as if it's hitting its speed, because it's being fed well. Scrap inside the bottleneck becomes invisible, and back-ups downstream show as idle time, so availability looks worse than it is.

**Counting after the bottleneck** reflects what was actually sold. If the machine struggled, that shows as a speed loss, and availability measures the time it spent producing good parts.

Some practical guidance on data points:

- **Downtime.** If you can only monitor one machine, make it the bottleneck. Track the others to see whether it's being starved or blocked.
- **Scrap.** Ideally after every operation that can produce it. Where you can't, prioritise.
- **Counts.** The more places the better, ideally an "in" and an "out" for the line, so you can see losses by operation.
- **Short stops.** Stops of a few seconds are rarely recorded by hand, but they add up.

## Capturing the data

The most accurate OEE comes from capturing data automatically from the equipment in real time, usually through OPC UA or a similar connection. More in [OPC UA vs MQTT](/post/opc-ua-vs-mqtt).

Operators can record the data manually, but manual OEE is almost always higher than reality. Short stops go unrecorded, and durations get rounded.

When a plant moves from manual to automatic capture, OEE usually drops sharply. Explain the change to operators and managers before it happens, so the lower figure is seen as a more accurate starting point rather than a sudden failure. That new baseline is where improvement starts.

## Benchmarking

Because OEE is expressed in time, it can be compared across products, processes, plants and even industries.

Typical figures vary widely by industry. An OEE of 85% is often quoted as world class, a figure that comes from the total productive maintenance (TPM) tradition. Many manufacturers operate well below that, and a realistic target depends on your industry and starting point.

OEE isn't the only time base. OOE and TEEP measure against operating time and calendar time instead, which answers different questions. More in [OEE vs OOE vs TEEP](/post/oee-vs-teep).

## How to improve OEE

Start by measuring it accurately. Then work on the biggest losses.

**Downtime** is usually the largest loss. Frequent short stops can cost as much as rare long ones. Common causes include short stops for settings and minor faults, breakdowns, changeovers and waiting for materials or people. Maintenance built into MES/MOM, including autonomous maintenance by operators, helps reduce breakdowns. More in [maintenance strategies](/post/preventive-vs-predictive-maintenance).

**Speed and quality losses** often come from running below the target rate to avoid problems, or from problems caught too late. Accurate target cycle times make speed losses visible, and in-process checks with SPC at the line catch quality problems early. More in [SPC on the shopfloor](/post/spc-on-the-shopfloor).

To put a value on improvement, try the [What is 1% of OEE worth?](/tools/oee-one-percent) calculator.

## Summary

OEE multiplies availability, performance and quality to show how much good product a line made compared with what it could have made in the planned time. Accurate, automatic data from the bottleneck gives a trustworthy figure, and breaking it into its components shows where to focus. MES/MOM captures that data in real time, by line and shift. Other measures that sit alongside OEE are covered in [Manufacturing KPIs beyond OEE](/post/manufacturing-kpis-beyond-oee).

## My view

OEE is only as good as the data behind it. I'd rather see an honest 55% from automatic capture than a manual 80% that nobody believes, because the honest figure is the one you can improve.

What would your OEE be if every short stop were counted?
