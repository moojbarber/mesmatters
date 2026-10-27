---
title: "Historians, data lakes and data fabric: where shopfloor data lives"
short: "Manufacturing data platforms"
description: "Historians, data warehouses, data lakes, data fabric. Which one holds what, how they relate to MES/MOM, and which layer AI actually reads from."
published: 2026-07-28
category: education
art: pipeline
---

MES/MOM generates enormous quantities of data. So do PLCs, sensors, historians and IIoT platforms. Then ERP, quality and maintenance systems add their own.

Where should it all live? It depends what you want to do with it, so let's go through the main options.

## Historians

Historians are databases built for time-series data at very high volume: machine signals, process variables, sensor readings, often every second or faster.

They've been part of manufacturing IT for decades and they're still widely used, especially by engineers for troubleshooting and long-term trending. "What was the oven temperature doing in the two hours before that batch failed?"

MES/MOM also reads time-series values from the machines, usually over OPC UA, and adds the context: which order, material and machine each value belongs to. It isn't designed to hold the same volume of data as a historian, or to capture it at the same frequency. But for most manufacturers, what MES/MOM captures is absolutely fine, and it removes the need for a separate historian. Only in rare cases do you need both. More in [Historian vs MES](/post/historian-vs-mes).

## Data warehouses

Structured databases optimised for reporting. They pull data from MES/MOM, ERP, quality and other systems, and organise it for business intelligence tools.

Best for well-structured, aggregated data that answers known questions: output by site by month, scrap cost by product family.

## Data lakes

Large stores of raw, unstructured or semi-structured data. Anything can go in: machine data from historians, transactions from MES/MOM and ERP, IIoT streams, logs, images.

Data lakes are often the raw material for advanced analytics and machine learning. The risk is obvious: without structure and context, a lake becomes a swamp.

## Data fabric and data mesh

More recent architectural ideas. Rather than physically copying everything into one place, they focus on making data discoverable and usable across the enterprise wherever it lives.

It weaves data together rather than moving it all. Useful in large organisations with many systems and sites.

## How it typically fits together

A common pattern in mature factories:

1. **MES/MOM** captures operational events and gives them context: order, material, machine, shift, reason, result.
2. **A historian**, in the rare cases it's needed, keeps very high-frequency machine data.
3. **A data platform** (lake, warehouse or fabric) brings MES/MOM, ERP and other data together for analytics and AI.

The lines between these categories are blurring, and vendors increasingly offer platforms that cover more of the stack. But the roles stay roughly the same.

## Which layer does AI read from?

Usually the data platform. That's where data from many sources can be combined, at scale, for training models.

But the *context* that makes the data valuable is created upstream, at the point of work, by MES/MOM. A data lake full of uncontextualised machine signals won't give a model much to learn from. One that includes which order, which material and which shift was involved, linked to quality outcomes and maintenance history, will.

I explain why in [Raw machine data is worthless](/post/contextualised-manufacturing-data).

## Don't start with the platform

I've seen manufacturers build impressive data platforms before they have reliable data to put in them. The lake fills up. Nobody trusts what's in it. The data science team spends most of its time cleaning.

Start at the source. Get accurate, contextualised data captured on the shopfloor. Then build the platform to make it available.

Where does most of your shopfloor data live today?
