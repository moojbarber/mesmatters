---
title: "Cloud vs on-premises MES: how they compare"
short: "Cloud vs on-premises MES"
description: "Cloud vs on-premises MES/MOM compared on security, scalability, upgrades and cost, and why most multi-site MES already depends on the network."
published: 2026-07-09
category: education
art: cloud
---

Where should your MES/MOM run? A few years ago most manufacturers ran it on servers they owned. Today more and more of them run it in the cloud, and the question comes up in almost every evaluation.

This article sets out how the two compare.

## What each one means

**On-premises** means you run the MES/MOM software on servers you own or rent, either in the factory or in your own data centre. Your team, or a partner, looks after the servers, databases, backups and upgrades.

**Cloud** means the software runs on a cloud platform, usually delivered by the vendor as software as a service (SaaS). The vendor runs the infrastructure and keeps the application up to date. Most cloud MES/MOM also includes an edge component at each site, close to the machines.

## Most "on-premises" MES isn't on the premises

One point often gets missed. When MES/MOM serves several sites from one instance, it usually sits in a central data centre. Every site except perhaps one already reaches it over a wide-area network or the internet.

So the dependency on connectivity that people associate with cloud often exists already. The real difference is who runs the infrastructure, and how the system is kept up to date.

## Side by side

| | On-premises | Cloud |
| --- | --- | --- |
| **Who runs the infrastructure** | You, or a partner | The vendor and cloud provider |
| **Security** | Depends on your own team and processes | Large-scale monitoring and patching, with certifications such as ISO 27001 and SOC 2 |
| **Adding a site or capacity** | Buy and set up servers | Mostly configuration |
| **Upgrades** | Periodic projects, often years apart | Frequent, smaller updates |
| **New features, including AI** | Arrive when you upgrade | Arrive as they're released |
| **If the network drops** | Sites using a central instance are affected | Edge components keep critical functions running |
| **Control over timing of changes** | Full | Shared with the vendor, usually with test environments |
| **Typical licensing** | Perpetual licence plus maintenance | Subscription |

## What cloud brings

**Security.** Major cloud platforms invest in security at a scale few manufacturers can match: continuous monitoring and rapid patching, backed by independent certifications. Patches are applied as standard rather than waiting for a maintenance window.

**Scalability.** Adding a new site or line is mostly configuration, with no servers to buy. Capacity can grow as data volumes climb with machine connectivity and AI.

**Staying current.** Updates arrive regularly and in small steps, so there's no large upgrade project every few years. On-premises customers often put those upgrades off, and fall behind.

**Access to new capabilities.** New features, including AI and analytics, reach customers as they're released.

**Less infrastructure to run.** The vendor looks after servers, databases, backups and disaster recovery. Your team can spend that time on processes and improvement.

**Resilience.** Cloud platforms offer redundancy across data centres, which would be expensive to build yourself.

## What on-premises brings

**Full control over timing.** You decide exactly when changes happen, which some regulated sites value. If you've recently invested in data centre capacity and skills, on-premises also makes use of them.

**Working without connectivity.** A site with no reliable connection, or an air-gapped environment in defence and some critical infrastructure, may need everything on site.

## Handling the common concerns about cloud

**What if the connection drops, or latency matters?** Critical shopfloor functions and machine data can run on a local edge component that buffers data and keeps production moving, then catches up when the connection returns. Internet connectivity is now close to as reliable as power for most sites, so the edge covers a rare gap. That's the same design question a central on-premises instance raises. Real-time machine connectivity also sits at the edge, so latency isn't an issue for the equipment. The cloud handles the operational application and analytics, where milliseconds don't matter.

**Data residency and regulation.** Cloud regions let you keep data in the country or region you need, though some data residency requirements, and many aerospace and defence programmes, still call for your own data centre. In regulated industries, look for vendors with a validated cloud approach and clear documentation for quality and compliance teams.

## Questions to ask a cloud MES vendor

- How is machine data buffered, and how does it catch up?
- Which security certifications do you hold, and how often is the platform patched?
- How often are updates released, and can we test them before they reach production?
- Which regions can our data be held in?
- What does a new site cost to stand up, in time and effort?

## Licensing

Cloud usually comes with subscription licensing, and on-premises with a perpetual licence plus annual maintenance. Compare the total cost over the life of the system, including infrastructure and the upgrade projects each model involves.

## My view

I think cloud is now the right default for most manufacturers. If your MES/MOM already runs in a central data centre, you carry the network dependency without the security and scalability benefits the cloud adds. Subscription licensing also gives vendors the predictable revenue to keep investing in a product you'll rely on for a decade or more.

On-premises still has a place where connectivity really isn't available. Many aerospace and defence programmes, and some data residency rules, also call for your own data centre. For everyone else, I'd want a good reason not to choose cloud.

If your MES/MOM already runs in a central data centre, what's keeping it out of the cloud?
