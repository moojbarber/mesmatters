---
title: "UNS vs MES: can a unified namespace replace your MES?"
short: "UNS vs MES"
description: "A unified namespace is an architecture for sharing live data. MES/MOM is an application that runs and records the operation. What each does, where they overlap, and why most factories end up using them together."
published: 2026-10-23
category: education
art: network
---

"Do we still need an MES if we build a unified namespace?"

I hear this question a lot, usually after someone has watched a very convincing demo. It's a fair question. A unified namespace (UNS) has changed how many factories share shopfloor data, and some people argue it can replace a traditional MES.

I'll be honest about where I sit. I think a UNS is a genuinely useful pattern, but not a silver bullet. And the debate gets heated online, almost political at times, which I don't think helps anyone choose.

So let's compare what each one actually does.

## What a UNS is

A unified namespace is an architectural idea rather than a product. Every system publishes what it knows to one central, structured place, usually an MQTT broker, organised by the plant hierarchy: enterprise, site, area, line, machine. Any system that needs the data subscribes to it.

The big win is fewer point-to-point integrations. Instead of every system connecting to every other, each one connects once, to the namespace. Data becomes easier to find and reuse, and adding a new consumer is much simpler.

At heart, though, a UNS is an organisational structure on top of a broker. It shows what's happening right now.

## What MES/MOM is

MES/MOM is an application that runs the operation. It releases and dispatches orders, guides operators through the work, enforces checks, records what was made from what, and stores the history with its context: the order, the material lot, the operator, the reason.

It also makes decisions in the moment. It can stop someone consuming a quarantined lot, or trigger an inspection because the material changed.

## Side by side

| | UNS | MES/MOM |
| --- | --- | --- |
| **What it is** | An architecture for sharing data | An application for running operations |
| **Main job** | Make live data available to any system | Execute, enforce and record production, quality, inventory and maintenance |
| **Time horizon** | The current state | The full history, with context |
| **Business logic** | None on its own | Built in: orders, routings, checks, genealogy |
| **Operator interaction** | None on its own | Screens, instructions, sign-offs |
| **Traceability** | Not on its own | Lot and serial genealogy |
| **Typical owner** | IT/OT architecture team | Operations, with IT support |

## Where they overlap

The overlap is mostly in visibility. If what you need is live machine status, counts and a dashboard of what's running now, a UNS with some light applications around it can do a lot of that, quickly and cheaply.

It gets harder as soon as you need history or transactions. OEE is a good example. You can publish the current OEE to a UNS. But you can't aggregate OEE figures by order or by shift from the published values. You have to go back to the raw data, stored somewhere that keeps it, and calculated consistently, ideally to ISO 22400.

The same goes for genealogy and quality records, and anything an auditor will ask about. A UNS passes the data through. Something else has to keep it and give it meaning.

## Why they usually work together

In practice, the best architectures I see use both. Machines and sensors publish to the namespace. MES/MOM subscribes to the machine data it needs, adds the context of the order, the material lot, the operator and the shift, and publishes that contextualised data back to the UNS. Other systems, such as a data platform or an AI application, then subscribe to rich operational events rather than raw signals.

That makes MES/MOM one of the most valuable publishers into a UNS, not a competitor to it.

## Which do you need?

- **Mainly visibility, at a few sites, with a strong internal team?** A UNS with some light applications may be enough to start, especially if you build it with the end in mind.
- **Orders, quality, traceability and enforced processes?** You need MES/MOM, and a UNS can help connect it to everything else.
- **Lots of systems that need the same data?** A UNS is worth considering whichever MES/MOM approach you take.
- **Already running MES/MOM?** Publishing its contextualised data to a UNS is often the quickest way to make it useful to everyone else.

I go further into the wider choice of approaches in [Code, build, stitch or configure](/post/build-vs-buy-mes), and into the protocols underneath in [OPC UA, MQTT and UNS in plain English](/post/opc-ua-mqtt-uns-explained).

Where does a UNS sit in your architecture today: alongside your MES, or instead of one?
