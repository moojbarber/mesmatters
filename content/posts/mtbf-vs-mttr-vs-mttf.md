---
title: "MTBF vs MTTR vs MTTF: maintenance metrics explained"
short: "MTBF vs MTTR vs MTTF"
description: "MTBF measures how long a repairable asset runs between failures, MTTR how long it takes to fix, and MTTF how long a non-repairable item lasts. How to calculate each, how they relate to availability, and where the data comes from."
published: 2026-10-24
category: education
art: wheel
---

MTBF, MTTR and MTTF are the standard reliability metrics in maintenance. They're often quoted together, and often calculated from data nobody quite trusts.

Each one measures something different.

## MTBF: how long it runs between failures

**MTBF** (mean time between failures) is the average time a repairable asset runs before it fails.

**MTBF = total operating time ÷ number of failures**

If a filler runs for 1,000 hours in a quarter and fails five times, its MTBF is 200 hours. Higher is better: the asset is more reliable.

## MTTR: how long it takes to fix

**MTTR** (mean time to repair) is the average time it takes to get a failed asset running again.

**MTTR = total repair time ÷ number of repairs**

If those five failures took 15 hours to fix in total, MTTR is three hours. Lower is better: you recover faster.

Be clear what's included. Some sites measure only hands-on repair time. Others include waiting for a technician and spare parts. The second is what production actually feels, so it's usually more useful.

## MTTF: how long it lasts

**MTTF** (mean time to failure) is the average time a non-repairable item lasts before it fails and is replaced. Think bearings, seals, sensors or light sources.

**MTTF = total operating time ÷ number of items that failed**

It helps you plan replacement intervals and spare parts stock.

## Side by side

| | MTBF | MTTR | MTTF |
| --- | --- | --- | --- |
| **Measures** | Reliability of repairable assets | Speed of recovery | Life of non-repairable items |
| **Better when** | Higher | Lower | Higher |
| **Typical use** | Machines and critical equipment | Any repair | Components, parts, consumables |
| **Helps you** | Target reliability improvements | Improve response and spares | Plan replacements and spares |

## How they relate to availability

MTBF and MTTR combine into a simple measure of availability:

**Availability = MTBF ÷ (MTBF + MTTR)**

With an MTBF of 200 hours and an MTTR of three hours, availability is about 98.5%. Improve either side and availability goes up. That's the same availability that feeds OEE. More in [What is OEE?](/post/what-is-oee-overall-equipment-effectiveness)

## Where the data comes from

All of them depend on knowing exactly how long each stop lasted and why it happened. If downtime is written on a sheet at the end of the shift, short stops vanish and the reasons are guesses.

MES/MOM records each stop from the machine as it happens, with the reason and the order attached. That gives MTBF and MTTR a reliable basis, and gives a CMMS or EAM the data it needs to plan maintenance. More in [CMMS vs EAM vs MES](/post/cmms-vs-eam-vs-mes) and [maintenance strategies](/post/preventive-vs-predictive-maintenance).

Do your maintenance and production teams calculate MTBF from the same downtime data?
