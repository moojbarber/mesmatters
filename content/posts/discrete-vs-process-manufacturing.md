---
title: "Discrete vs process manufacturing: why it changes your MES choice"
short: "Discrete vs process"
description: "Not all manufacturing is the same. How discrete, process, batch, assembly and mixed-mode manufacturing differ, and why the type drives your data, KPIs and MES/MOM choice."
published: 2026-04-29
category: education
art: tanks
---

"What's the difference between process and discrete manufacturing?"

I've been explaining MES to people for well over a decade, and this question comes up constantly from people new to manufacturing. It matters more than people realise, especially when you're choosing technology.

## The simple version

At a high level, I explain it like this.

**Discrete:** the final product could, in theory, be taken apart back into its components. A bike.

**Process:** no matter what you do, you can't get back to the raw materials. A cake. You're never getting that egg back.

That's the core idea. In practice there are a few more shades.

## Discrete manufacturing

Individual, countable items. Automotive parts, electronics, machined components, consumer goods.

You count pieces. You often track serial numbers. Cycle times and piece counts drive performance. In high-mix, low-volume environments, frequent changeovers are the biggest constraint.

## Process manufacturing

Materials are transformed: mixed, blended, heated, reacted. Food and beverage, chemicals, pharmaceuticals, plastics.

You measure in litres, kilograms and tonnes, not pieces. Recipes and formulations matter, including substitutions when an ingredient isn't available. Natural variation in raw materials means yield varies too.

## Batch manufacturing

Sits between the two. A defined quantity is produced in one run, and the whole batch is treated as a single unit for quality and traceability. Common in food, pharma and speciality chemicals.

## Assembly

Bringing components together into a finished product. Automotive, electronics, machinery. The challenge is having the right components at the right time in the right sequence, and recording which components went into which product.

## Mixed-mode

Many manufacturers don't fit one category. A food company mixes a batch (process), then fills and packs it into cases (discrete). A plastics company runs a continuous extrusion line that feeds discrete cutting and packing.

This is far more common than most software brochures suggest.

## Why the type matters for MES/MOM

The type of manufacturing shapes almost every decision in a project.

**Process design.** Discrete thinks in cycle times and piece counts. Process thinks in batch sizes and recipe parameters. Assembly thinks in sequencing.

**Data and KPIs.** Units of measure, how you calculate yield, how traceability works (serial, lot or time-based), which quality checks matter.

**Operator screens.** A discrete operator wants to see the next part and its count. A process operator wants the recipe step, the parameters and the time remaining. Same system, very different screens.

**Technology choice.** Not every MES handles every type well. Some were built for discrete and stretched into process, or the other way round. You'll feel that in unit-of-measure handling, recipe management and traceability.

## What to ask a vendor

Pin this down early in any evaluation:

- Can you show me my type of manufacturing running in your system, not a similar one?
- How do you handle mixed-mode, where one line is process and the next is discrete?
- How do units of measure convert between operations, from kilograms in to cases out?
- Is that done through configuration, or customisation?

The best platforms handle all modes across the enterprise through configuration. If a vendor needs custom work to handle your basic manufacturing type, that's a warning sign. More on that in [Configure, don't customise](/post/configure-dont-customise).

How would you describe your own manufacturing: one type, or a mix?
