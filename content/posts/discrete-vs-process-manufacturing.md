---
title: "Discrete vs process manufacturing: the types of manufacturing, and why they change your MES choice"
short: "Discrete vs process"
description: "Discrete, repetitive, job shop, batch, continuous and mixed-mode manufacturing explained. How each type works, how it differs, and why it drives your data, KPIs and MES/MOM choice."
published: 2026-04-29
category: education
art: tanks
---

"What's the difference between process and discrete manufacturing?"

It's one of the most common questions in manufacturing, and the answer has a big effect on which systems fit.

## The simple version

**Discrete:** the final product could, in theory, be taken apart back into its components. A bike.

**Process:** no matter what you do, you can't get back to the raw materials. A cake. You're never getting that egg back.

That's the core idea. In practice each side splits into a few types, and plenty of factories run more than one.

## Discrete manufacturing

Individual, countable items. You count pieces, and often track serial numbers. Within discrete, there are distinct patterns.

**Repetitive.** The same or similar products run continuously on dedicated lines at high volume. Think automotive components, consumer electronics, white goods or packaged goods. Performance is about line rate and OEE.

**Job shop or high-mix, low-volume.** Many different products in small quantities, each following its own route through shared machines. Think machining or fabrication. Changeovers and scheduling are the big challenges.

**Assembly.** Components brought together into a finished product, from simple kits to complex machines. Getting parts to the line when they're needed, in sequence, matters most, along with recording which components went into which unit.

## Process manufacturing

Materials are transformed: mixed, blended, heated or reacted. You measure in kilograms and litres, not pieces. Recipes and formulations matter, and natural variation in raw materials means yield varies too.

**Batch.** A defined quantity is made in one run, following a recipe, and the whole batch is treated as one unit for quality and traceability. Common in food, pharmaceuticals, cosmetics and speciality chemicals.

**Continuous.** Material flows through the process without stopping, often 24 hours a day, for weeks or months. Think refining, paper, steel, extrusion or bulk chemicals. Stopping is expensive, so stability and process control are everything, and traceability is often time-based rather than by lot.

## Mixed-mode

Many manufacturers don't fit one category. A food company mixes a batch (process), then fills and packs it into cases (discrete). A plastics company runs a continuous extrusion line that feeds discrete cutting and packing.

Mixed-mode is common, and the handover points between modes are where systems are most tested.

## Side by side

| Type | Unit of measure | Traceability | What drives performance | Examples |
| --- | --- | --- | --- | --- |
| **Repetitive** | Pieces | Lot or serial | Line rate and OEE | Automotive parts, electronics |
| **Job shop** | Pieces | Lot or serial, by order | Changeovers and scheduling | Machining, fabrication |
| **Assembly** | Pieces | Serial, with component genealogy | Material availability and sequence | Machinery, vehicles |
| **Batch** | Weight or volume | Batch or lot | Recipe adherence and yield | Food, pharma, cosmetics, chemicals |
| **Continuous** | Weight or length | Time-based | Stability and uptime | Refining, paper, steel, extrusion |
| **Mixed-mode** | Converts between them | A mix | All of the above, at the handover points | Food, pharma, plastics, packaging |

## A separate question: how you respond to demand

People often mix manufacturing type up with production strategy, which is a different axis:

- **Make to stock:** build ahead of demand to forecast.
- **Make to order:** build once the customer orders.
- **Configure to order:** build a standard product with customer-chosen options. More in [From CPQ to the shopfloor](/post/cpq-to-shopfloor).
- **Engineer to order:** design and build something unique for each customer.

A job shop can be engineer to order, and a repetitive line can be make to stock. Both axes shape what you need from MES/MOM.

## Why the type matters for MES/MOM

The type of manufacturing shapes almost every decision in a project.

**Process design.** Repetitive lines think in rates. Job shops think in routings. Batch thinks in recipe steps and parameters. Continuous thinks in stability over time.

**Data and KPIs.** Units of measure, how you calculate yield, how traceability works (serial, lot or time-based), and which quality checks matter.

**Operator screens.** A discrete operator wants to see the next part and its count. A process operator wants the current recipe step and its parameters. Same system, very different screens.

**Technology choice.** Not every MES handles every type well. Some were built for discrete and stretched into process, or the other way round. You'll feel that in unit-of-measure handling, recipe management, traceability and mixed-mode handovers.

## What to ask a vendor

Pin this down early in any evaluation:

- Can you show me my type of manufacturing running in your system, not a similar one?
- How do you handle mixed-mode, where one line is process and the next is discrete?
- How do units of measure convert between operations, from kilograms in to cases out?
- How do you handle time-based traceability on continuous lines?
- Is all of that done through configuration, or customisation?

## My view

I've been explaining MES for well over a decade, and this question matters more than people realise. Mixed-mode is far more common than most software brochures suggest. I'd look for a platform that handles every mode across the enterprise through configuration. If a vendor needs custom work to handle your basic manufacturing type, that's a warning sign. More on that in [Configure, don't customise](/post/configure-dont-customise).

How would you describe your own manufacturing: one type, or a mix?
