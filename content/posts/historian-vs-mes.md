---
title: "Historian vs MES: what each one stores, and when you need both"
short: "Historian vs MES"
description: "A historian stores high-frequency process values; MES/MOM records events with context and runs the work. What each stores, and how they work together."
published: 2026-09-30
category: education
art: pipeline
---

"We've already got a historian. Isn't that our MES?"

It's a common question, especially in process industries where historians have been around for decades. Both collect data from the shopfloor. Both show trends. But they store different things, for different people, and answer different questions.

## What a historian does

A process historian is a database built for time-series data at very high volume. It records machine signals and process variables, often every second or faster: temperatures, pressures, flows, speeds, levels, valve positions. It compresses that data efficiently so you can keep years of it.

Engineers love historians, rightly, for troubleshooting and long-term trending. "What was the oven temperature doing in the two hours before that batch failed?"

## What MES/MOM does

MES/MOM records operational events and gives them context. An order started on Line 3. 2,400 good parts, 60 scrapped for short shots. A 12-minute stop, reason: jam at station 2. Lot 7781 consumed into order 4521. A quality check failed and the lot was put on hold.

It also *manages* the work: dispatching orders, guiding operators, enforcing checks and recording genealogy. A historian watches the process; MES/MOM runs the operation.

## Side by side

| | Historian | MES/MOM |
| --- | --- | --- |
| **Stores** | Time-series values from tags | Events and transactions with context |
| **Typical frequency** | Sub-second to seconds | When something happens |
| **Context** | Tag, timestamp, value and a quality flag | Order, material, lot, machine, shift, operator, reason |
| **Main users** | Process and controls engineers | Operators, supervisors, quality, maintenance, planners |
| **Typical question** | What was this value doing over time? | What happened, to which order, and why? |
| **Manages work** | No | Yes |
| **Genealogy and traceability** | No | Yes |

## How they work together

Where you have both, many architectures use each for what it's good at:

- **The historian keeps the high-frequency signals.** MES/MOM doesn't need every reading.
- **MES/MOM keeps the events and the context.** Orders, lots, stops, reasons and results.
- **The two link by time and equipment.** When a lot fails inspection, MES/MOM tells you which machine and which hours; the historian shows you exactly what the process was doing then.
- **A data platform brings both together** when you want analytics or AI across many lines and sites.

Some MES/MOM platforms include historian capabilities, and some historians have added event features. The roles stay roughly the same. More on how these layers fit with data lakes and AI in [Historians, data lakes and data fabric](/post/manufacturing-data-platforms).

## Which do you need?

If it's running orders, tracing material and managing quality and maintenance, MES/MOM. Whether you also need a historian depends on how frequently you need data. MES/MOM can capture and record the process values most operations need. A historian earns its place when engineers need very high-frequency signals kept for long periods, which is more common in process industries.

## My view

The trap is assuming a historian, or an IIoT platform full of tags, is enough to run the operation. It isn't designed to manage a production order or trace a lot. Manufacturers who try end up building those functions on top, which is effectively building a homegrown MES. I make the same argument in [IIoT vs MES](/post/iiot-vs-mes). The opposite trap is forcing MES/MOM to store every high-frequency signal when nobody uses it. Where that level of detail is genuinely needed, that's what a historian is for.

Does your historian know which order was running when that value spiked?
