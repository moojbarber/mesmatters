---
title: "Process before technology: map your as-is before you buy anything"
short: "Process mapping"
description: "Digitise a broken process and you get a faster broken process. How to map what really happens on your shopfloor with swimlanes, then design something better."
published: 2026-05-05
category: advice
art: flow
---

Before you buy software, evaluate a vendor or connect a single machine, you need to understand your processes.

Otherwise you'll just digitise a mess. And if you digitise a broken process, you get a faster broken process.

This is the work most manufacturers skip. It's also the work that makes the biggest difference.

## Same product, different process

Here's something I've seen in almost every manufacturer.

Two factories making the same product, using different processes. Not slightly different: different routings, different quality checks, different changeover steps, even different words for the same thing.

It's not just between sites. Inside one factory, day shift and night shift often do things differently. Both acceptable, so nobody questions it. But the data isn't comparable, and nobody can say which way is better.

Processes evolve organically. Someone finds a quicker way. A supervisor's workaround sticks. Over the years, the "official" process bears little resemblance to what actually happens.

You can't standardise what you haven't documented. And you need to decide which process to digitise before you build it into software.

## Start with the physical structure

Map the skeleton first, top down: enterprise, site, area, line, machine.

It sounds basic, but agreeing this hierarchy early saves a lot of pain later. It's what your process maps, your data and your reports will all hang on.

## Then map what actually happens

Map what really happens, warts and all, rather than what the manual or the ISO documentation says.

The tool I like for this is a swimlane diagram, with a twist:

- **Across the top**, a lane for each department or system: ERP, production, quality, inventory, maintenance, automation.
- **Down the side**, a lane for each manufacturing process: cutting, welding, mixing, painting, assembly, packing.

That gives you a grid. Each activity sits in the cell where that department meets that process.

Take welding as an example. Material is delivered to the line (inventory). Orders are released (ERP). The order is started and the machine changed over (production). Input material is consumed (inventory). An in-line check is performed, with rework if it fails (quality). Counts are recorded (production). Finished material is labelled (inventory). ERP is updated.

Lay it out like that and the invisible becomes visible. You see every handoff, every place information has to move between people or systems, and every gap.

## Involve the people who do the work

Map with operators, quality technicians, maintenance engineers and logistics, not just managers.

They know the workarounds. They know the tribal knowledge. They know the step that's in the procedure but never happens, and the one that always happens but isn't written down anywhere.

And be honest. If the map is messy, that's what you're going to fix. A perfect-looking diagram of a process that doesn't exist is worse than useless.

## Then question everything

Once you've mapped the as-is, ask of every step:

- Why do we do it this way?
- What would happen if we stopped?
- Does it add value, or just time?
- Is it a genuine requirement, or someone's preference?

You'll hit resistance. "We've always done it this way." "Our process is different." Sometimes that's true. Most of the time it's habit. More on that in [Configure, don't customise](/post/configure-dont-customise).

## Design the to-be, for the operator

The to-be process isn't the as-is with a screen bolted on. It should be simpler, more standard, with technology reinforcing it.

Design it for the person doing the work. If your new process takes twelve clicks to replace two seconds on paper, you've gone backwards.

## Why it pays back

Doing this upfront:

- Makes your requirements specific, so your RFP is focused and vendors can respond properly
- Reduces customisation, because you've simplified before you build
- Speeds up implementation, because the configuration team knows exactly what to build
- Gives you the basis for testing and training

Skip it, and you'll do the same work later, during the project, with the clock running and the services bill growing.

When did you last map what really happens on your shopfloor, rather than what the procedure says?
