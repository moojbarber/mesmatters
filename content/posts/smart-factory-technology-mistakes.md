---
title: "Six technology mistakes that sink smart factory projects"
short: "Six technology mistakes"
description: "ERP wired to machines, homegrown platforms, point solutions, over-customisation and more: six avoidable smart factory technology mistakes."
published: 2026-07-21
category: advice
art: gates
---

I've seen all of these, repeatedly. Every one is avoidable if you know what to look for.

## 1. Connecting ERP directly to machines

This is a huge no-no.

ERP isn't designed for real-time communication with shopfloor equipment. It doesn't have the data model, the transaction speed or the user interface for it. It needs aggregated data at a sensible frequency, not thousands of signals a second from a PLC.

People who try it end up with custom interfaces between ERP and the equipment. They're expensive to maintain and add work to every ERP upgrade, because ERP was never meant to handle machine signals.

MES/MOM exists precisely to sit between ERP and the shopfloor. Use it. And if it isn't in place yet, buffer the machine data in a connectivity layer you can later feed into MES/MOM, not ERP.

## 2. Underestimating what it takes to code your own

Building your own can be an OK option in some cases, usually for smaller companies with a narrow scope and the right expertise. Coding an entire MES/MOM platform from scratch is a much bigger commitment than it looks.

Homegrown systems start small. Someone builds a database, adds some screens, connects a couple of machines. It works, for a while. A system of any real scale takes years to build well, and the gaps are easy to miss: user experience, industry best practice, standard KPIs such as ISO 22400, and integrations.

Then requirements grow. The person who built it becomes the single point of failure, and eventually they leave. Every upgrade and every new capability is yours to build. I cover replacing these systems in [Replacing a homegrown MES](/post/replacing-a-homegrown-mes).

## 3. Buying point solutions with no destination in mind

Plenty of projects start with something small to fill a gap: an OEE tool, a checklist app, a standalone quality system, an energy dashboard.

It solves the immediate problem. Then requirements grow. You need quality connected to production, inventory connected to quality, maintenance connected to downtime. The point solution can't do it.

Now you're either replacing it, or adding more tools and connecting them. Stitching best-of-breed applications together can work, especially with a well-governed unified namespace, but every boundary is an interface to own and some context is lost at each one. It's fine to start small, but start small on the right path, with the destination in mind. Whichever route you take, know how it grows, and what connecting the pieces will cost. I compare the options in [Code, build, stitch or configure](/post/build-vs-buy-mes).

## 4. Over-customising

The more custom work you do, the bigger the budget you need now and later. Custom code needs maintaining and retesting with every upgrade. And it often means you've encoded a bad process into software instead of fixing it.

Configure, don't customise. More in [Configure, don't customise](/post/configure-dont-customise).

## 5. A lightweight connected worker platform that collides with MES/MOM

Connected worker platforms are everywhere. They solve real problems: checklists, tasks, shift handover, skills.

But operators don't just manage checklists. They run production orders, perform inspections, consume material and do autonomous maintenance. A standalone connected worker tool doesn't cover those on its own. So you add MES/MOM later, and now operators use two systems and the data is split, unless you plan how they connect.

MES/MOM with connected worker built in gives you similar quick wins on one platform. If you go standalone, decide up front how it will connect to everything else. More in [Connected worker: one app, not five](/post/connected-worker-one-app-not-five).

## 6. Treating IIoT as a replacement for MES/MOM

IIoT is trendier, and IoT platforms are the right choice in some cases. But they're the connectivity layer, not operational management. If you need MES functionality, you need an MES.

I've seen manufacturers connect hundreds of sensors and build beautiful dashboards, then realise they still can't manage a production order, track an inspection or trace a lot. IIoT feeds MES/MOM. It doesn't replace it. See [IIoT doesn't replace MES](/post/iiot-vs-mes).

## The common thread

Every one of these mistakes comes from solving today's problem without thinking about where you're heading. The quick fix that looks cheap and turns out expensive.

Before any technology decision, ask: will this still be the right choice when we're three times bigger and want production, quality, inventory and maintenance on the same data?

Which of these six have you seen up close?
