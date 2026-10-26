---
title: "What is a unified namespace (UNS)? And where MES/MOM fits"
short: "Unified namespace (UNS)"
description: "A unified namespace shares live data through a central broker. What a UNS is, whether it can replace MES, and how UNS and MES/MOM work together."
published: 2026-10-23
category: education
art: network
---

"Do we still need an MES if we build a unified namespace?"

It's a common question, often after a convincing demo. A unified namespace (UNS) has changed how many factories share shopfloor data, and some people argue it can replace a traditional MES. Others see it as a way of connecting MES/MOM to everything else.

This article sets out what a UNS is, what MES/MOM does, and where they fit together.

## What a UNS is

A unified namespace is an architectural idea rather than a product. Every system publishes what it knows to one central, structured place, usually an MQTT broker, organised by the plant hierarchy: enterprise, site, area, line, machine. Any system that needs the data subscribes to it.

Its appeal is that each system connects once, to the namespace, so data becomes easier to find and reuse, and adding a new consumer is simpler. Point-to-point interfaces still have real strengths, though: the sender gets a response, so it knows each message arrived, and a failure stays contained to one link.

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

## Can a UNS replace your MES?

For visibility, partly. For running the operation, no.

The overlap is mostly in visibility. If what you need is live machine status and counts on a dashboard, a UNS with some light applications around it can do a lot of that, quickly and cheaply.

It gets harder as soon as you need history or transactions. OEE is a good example. You can publish the current OEE to a UNS. But you can't aggregate OEE figures by order or by shift from the published values. You have to go back to the raw data, stored somewhere that keeps it, and calculated consistently, ideally to ISO 22400.

The same goes for genealogy and quality records, and anything an auditor will ask about. A UNS passes the data through. Something else has to keep it and give it meaning.

## Challenges and alternatives

A UNS is a sensible pattern, and it's worth being clear about what comes with it.

- **No confirmation to the sender.** Publishing is fire-and-forget: the sending system doesn't know whether anyone received or processed the data. That's fine for status and measurements, and a poor fit for transactions such as order releases and quality holds.
- **No history or meaning on its own.** It shows the current state. Something else has to store the history and add the context.
- **Governance and naming.** Without strong ownership, topic structures and payloads drift, and the namespace slowly becomes a large pile of tags.
- **The broker and security.** The broker becomes a critical piece of infrastructure, and a hub that everything can publish to and read from needs careful access control.

The alternatives are well proven. Direct interfaces through standard APIs give a confirmed response for transactions, and integration through ERP keeps business transactions in one place. For analytics and AI, a data platform brings the history together. Most architectures use a mix, chosen flow by flow.

## How they work together

Many architectures use both. Machines and sensors publish to the namespace. MES/MOM subscribes to the machine data it needs, adds the context of the order, the material lot, the operator and the shift, and publishes that contextualised data back to the UNS. Other systems, such as a data platform or an AI application, then subscribe to rich operational events rather than raw signals.

## Where to start

- **Mainly visibility, at a few sites, with a strong internal team?** A UNS with some light applications may be enough to start, especially if you build it with the end in mind.
- **Orders, quality, traceability and enforced processes?** You need MES/MOM, and a UNS can help connect it to everything else.
- **Lots of systems that need the same data?** A UNS is one option worth considering, alongside direct interfaces and a data platform, whichever MES/MOM approach you take.
- **Already running MES/MOM?** Publishing its contextualised data to a UNS, or to a data platform, is often a quick way to make it useful to everyone else.

There's more on the wider choice of approaches in [Code, build, stitch or configure](/post/build-vs-buy-mes), and on the protocols underneath in [OPC UA, MQTT and UNS in plain English](/post/opc-ua-mqtt-uns-explained).

## My view

I think a UNS is a genuinely useful pattern, but not a silver bullet, and its limits matter as much as its strengths. The debate gets heated online, almost political at times, which doesn't help anyone choose. In the architectures I see working best, MES/MOM is one of the most valuable publishers into the UNS, rather than a competitor to it.

Where does a UNS sit in your architecture today: alongside your MES, or instead of one?
