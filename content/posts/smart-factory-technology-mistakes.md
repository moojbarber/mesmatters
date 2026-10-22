---
title: "Six technology mistakes that sink smart factory projects"
short: "Six technology mistakes"
description: "ERP wired to machines, homegrown platforms, point solutions, over-customisation, connected worker overlap and IIoT sold as MES. Six avoidable mistakes I see again and again."
published: 2026-07-21
category: advice
art: gates
---

I've seen all of these, repeatedly. Every one is avoidable if you know what to look for.

## 1. Connecting ERP directly to machines

This is a huge no-no.

ERP isn't designed for real-time communication with shopfloor equipment. It doesn't have the data model, the transaction speed or the user interface for it. It needs aggregated data at a sensible frequency, not thousands of signals a second from a PLC.

People who try it end up with custom interfaces between ERP and the equipment. They're fragile, expensive to maintain, and they make every ERP upgrade a nightmare.

MES/MOM exists precisely to sit between ERP and the shopfloor. Use it. And if it isn't in place yet, buffer the machine data in an IIoT platform or historian, not ERP.

## 2. Building a homegrown platform

I have a strong opinion on this one.

It's irresponsible to suggest that building an entire MES/MOM platform from scratch is better, faster or less risky than buying one. Homegrown systems start small. Someone builds a database, adds some screens, connects a couple of machines. It works, for a while.

Then requirements grow. The person who built it becomes the single point of failure. Eventually, they leave. No vendor support, no upgrade path, no roadmap. When it breaks, you're on your own. I cover replacing them in [Replacing a homegrown MES](/post/replacing-a-homegrown-mes).

## 3. Buying point solutions that can't scale

Too many people start with something small to fill a gap: an OEE tool, a checklist app, a standalone quality system, an energy dashboard.

It solves the immediate problem. Then requirements grow. You need quality connected to production, inventory connected to quality, maintenance connected to downtime. The point solution can't do it.

Now you're either replacing it, wasting the original investment, or bolting on more point solutions and creating an integration mess. Start with the end in mind. Choose a platform that can grow with you, even if you only use part of it on day one.

## 4. Over-customising

The more custom work you do, the bigger the budget you need now and later. Custom code needs maintaining and retesting with every upgrade. And it often means you've encoded a bad process into software instead of fixing it.

Configure, don't customise. More in [Configure, don't customise](/post/configure-dont-customise).

## 5. A lightweight connected worker platform that collides with MES/MOM

Connected worker platforms are everywhere. They solve real problems: checklists, tasks, shift handover, skills.

But operators don't just manage checklists. They run production orders, perform inspections, consume material and do autonomous maintenance. A standalone connected worker tool does none of that. So you add MES/MOM later, and now operators use two systems and the data is split.

Choose MES/MOM with connected worker built in. Same quick wins, one platform. More in [Connected worker: one app, not five](/post/connected-worker-one-app-not-five).

## 6. Treating IIoT as a replacement for MES/MOM

IIoT is trendier. But it's the connectivity layer, not operational management.

I've seen manufacturers connect hundreds of sensors and build beautiful dashboards, then realise they still can't manage a production order, track an inspection or trace a lot. IIoT feeds MES/MOM. It doesn't replace it. See [IIoT doesn't replace MES](/post/iiot-vs-mes).

## The common thread

Every one of these mistakes comes from solving today's problem without thinking about where you're heading. The quick fix that looks cheap and turns out expensive.

Before any technology decision, ask: will this still be the right choice when we're three times bigger and want production, quality, inventory and maintenance on the same data?

Which of these six have you seen up close?
