---
title: "OPC UA, MQTT and UNS in plain English"
short: "OPC UA, MQTT and UNS"
description: "The shopfloor connectivity layer without the rabbit hole. What OPC UA, MQTT and a unified namespace are, how they relate to MES/MOM, and what to ask vendors."
published: 2026-07-07
category: education
art: network
---

Even without a connection to the equipment, MES/MOM is useful. When people enter data, it's still captured against the order, the material and the machine, so the context is there. But it's far more valuable when the data is collected automatically from the machines, in real time, and that's what manufacturers should be aiming for.

That's the connectivity layer. And it's surrounded by acronyms and strong opinions. I won't go down every rabbit hole, but you need enough to have a sensible conversation.

## OPC UA

OPC stands for Open Platform Communications. OPC UA (Unified Architecture) is the modern version and the industry standard for machine-to-system communication.

What makes it useful:

- It's platform-independent and vendor-neutral, so equipment from different manufacturers can be read in a consistent way.
- It doesn't just carry values. It carries structure and meaning: this tag is a temperature, on this machine, in these units. And it has security built in.

If there's one connectivity standard to know, it's this one. Many machines and PLCs support it directly, and gateways can translate older protocols into it.

## MQTT

MQTT is a lightweight messaging protocol. Instead of a system asking each machine for data, devices *publish* messages to a central broker, and any system that's interested *subscribes* to them.

It's simple, efficient and works well over unreliable networks, which is why it's popular for IIoT and edge devices. On its own, MQTT doesn't define what the data means. Extensions such as Sparkplug add that structure.

OPC UA and MQTT aren't really competitors. Both can be used in the same factory, so pick the right one for each job.

## Unified namespace (UNS)

A unified namespace is an architectural pattern rather than a product. It's a real-time view of whatever operational data connected applications have published to it, usually through an MQTT broker, organised by the plant hierarchy: enterprise, site, area, line, machine.

Systems publish what they know, and others can subscribe. It's one integration option, alongside point-to-point interfaces, which give the sender a response, and integration through ERP.

It's worth being clear about its limitations:

- **No confirmation for the sender.** Data is published, and the publisher doesn't know whether the system that needed it received or processed it. Errors as data moves between platforms aren't visible.
- **Data can fail to arrive where it's meant to be.** Without that confirmation, a missed production confirmation or stock movement can go unnoticed until someone finds the numbers don't match.
- **No history by default.** It shows what's happening right now. On its own it doesn't keep the history, and it doesn't add the meaning. You still need applications around it to do that.
- **It can get messy quickly.** It needs a strict structure, strong governance of who publishes what, and a broker to run and secure.
- **Fewer point-to-point interfaces isn't always better.** For transactions between systems, a point-to-point interface with a confirmed response is often the safest option.

OEE is a good example of the history point. You can publish the current OEE to a UNS, but you can't aggregate OEE figures by order or shift. For that you have to go back to the raw data, stored somewhere that keeps it.

So a UNS can be used to share real-time data with systems that only need the latest value. For anything that must arrive, such as orders, consumption or quality status, use an integration that confirms it did.

## Where MES/MOM fits

Connectivity moves data. MES/MOM gives it meaning.

A UNS can tell you a machine's state changed. MES/MOM knows which order was running, which material, which shift, and that the operator just entered the reason as a jam. That contextualised data is often exactly what other systems want to subscribe to.

Where a UNS is used, MES/MOM can consume machine data from it and publish contextualised operational data to it. More on why that context matters in [Raw machine data is worthless](/post/contextualised-manufacturing-data).

## A few practical rules

- **Don't connect ERP directly to machines.** ERP needs aggregated data at sensible intervals, not raw machine signals.
- **Start with what you'll use.** Connect bottleneck assets and the signals you need for counts, states and key parameters first.
- **Agree a naming standard early.** Asset hierarchies and tag names are dull, and they decide whether the data is usable later.
- **Treat OT security as part of the design.** Not an afterthought once everything's connected.

## What to ask vendors

- Which protocols do you support natively: OPC UA, MQTT, others?
- Can you consume and publish to a unified namespace?
- How do you handle older equipment without modern interfaces?
- How are connections configured: by your team through configuration, or through custom development?

How connected is your shopfloor today, and how much of that data has context?
