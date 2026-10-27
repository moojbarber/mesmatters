---
title: "What is a unified namespace (UNS)? And where MES/MOM fits"
short: "Unified namespace (UNS)"
description: "A unified namespace shares live data through a central broker. What a UNS is, its risks, whether it can replace MES, and the alternatives."
published: 2026-10-23
category: education
art: network
---

"Do we still need an MES if we build a unified namespace?"

It's a common question, often after a convincing demo. A unified namespace (UNS) has become a popular topic, and some people argue it can replace a traditional MES. Others see it as a way of connecting MES/MOM to everything else.

This article sets out what a UNS is, what MES/MOM does, and the risks and alternatives worth knowing about.

## What a UNS is

A unified namespace is an architectural pattern rather than a product. It's a real-time view of whatever operational data connected applications have published to it, usually through an MQTT broker, organised by the plant hierarchy: enterprise, site, area, line, machine. Systems that need the data subscribe to it.

The idea is that each system connects once, to the namespace, rather than to each other. But point-to-point interfaces have strengths a UNS doesn't: the sender gets a response, so it knows each message arrived and was accepted, and a failure stays contained to one link.

At heart, though, a UNS is an organisational structure on top of a broker. It shows what's happening right now.

## What MES/MOM is

MES/MOM is an application that runs the operation. It releases orders, guides operators through the work, enforces checks, records what was made from what, and stores the history with its context: the order, the material lot, the operator, the reason.

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

The overlap is mostly in visibility. If what you need is live machine status and counts on a dashboard, a UNS with some light applications around it can show some of that.

It gets harder as soon as you need history or transactions. OEE is a good example. You can publish the current OEE to a UNS. But you can't aggregate OEE figures by order or by shift from the published values. You have to go back to the raw data, stored somewhere that keeps it, and calculated consistently, ideally to ISO 22400.

The same goes for genealogy and quality records, and anything an auditor will ask about. A UNS passes the data through. Something else has to keep it and give it meaning.

## Risks and alternatives

It's worth being clear about the risks before you commit to one.

- **No confirmation to the sender.** Publishing is fire-and-forget: the sending system doesn't know whether anyone received or processed the data. That's a poor fit for transactions such as order releases, consumption and quality holds.
- **Data can go missing quietly.** Without confirmation, data can fail to reach the systems it's meant for, and errors as data moves between platforms aren't visible. You find out when the numbers don't match.
- **No history or meaning on its own.** It shows the current state. Something else has to store the history and add the context.
- **It gets messy quickly.** Without strong ownership, topic structures and payloads drift, and the namespace soon becomes a large pile of tags.
- **The broker and security.** The broker becomes a critical piece of infrastructure, and a hub that everything can publish to and read from needs careful access control.

The alternatives are well proven. Direct interfaces through standard APIs give a confirmed response for transactions, and integration through ERP keeps business transactions in one place. For analytics and AI, a data platform brings the history together. Most architectures use a mix, chosen flow by flow.

## Where a UNS is used alongside MES/MOM

Where a UNS is in place, MES/MOM can subscribe to the machine data it needs, add the context of the order, the material lot, the operator and the shift, and publish that contextualised data back. Anything that must arrive, such as order releases, confirmations and quality status, should still go through interfaces that confirm it did.

## Where to start

- **Mainly live visibility?** A UNS can show current machine status, but plan for what comes next. As soon as you need history, transactions or traceability, you'll need more than a UNS.
- **Orders, quality, traceability and enforced processes?** You need MES/MOM, connected to the rest through interfaces that confirm data arrived.
- **Lots of systems that need the same data?** Direct interfaces, an integration platform or a data platform are usually the safer options. A UNS is another, with the risks above.
- **Already running MES/MOM?** Publishing its contextualised data to a data platform is often a quick way to make it useful to everyone else.

There's more on the wider choice of approaches in [Code, build, stitch or configure](/post/build-vs-buy-mes), and on the protocols underneath in [OPC UA, MQTT and UNS in plain English](/post/opc-ua-mqtt-uns-explained).

## My view

A UNS is a pattern to approach with caution. It can share live data, but it gives the sender no confirmation, keeps no history and needs strict governance to stay usable. For anything that must arrive, such as orders, consumption and quality status, I'd use interfaces that confirm it did. The debate gets heated online, almost political at times, which doesn't help anyone choose. Start from the flows you actually need, and pick the safest pattern for each one.

Where does a UNS sit in your architecture today: alongside your MES, or instead of one?
