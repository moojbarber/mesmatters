---
title: "Maintenance strategies: reactive, preventive, condition-based or predictive?"
short: "Maintenance strategies"
description: "Reactive, preventive, condition-based and predictive maintenance compared. What each costs, what data it needs, and how to choose the right strategy for each asset."
published: 2026-09-16
category: education
art: signal
---

There are four broad maintenance strategies, from fixing things when they break to forecasting failures from data. Most factories use a mix, chosen asset by asset.

## Four strategies

**Reactive.** Fix it when it breaks. Cheap to plan, expensive when it happens: unplanned downtime, emergency repairs, knock-on damage and missed deliveries.

**Preventive.** Maintain on a schedule, by calendar time or by usage such as running hours or cycles. Much better than reactive, but blunt. Sometimes you service too early and waste parts and labour. Sometimes too late, and it fails anyway.

**Condition-based.** Maintain when the equipment's actual condition says so: vibration, temperature, current draw, pressure, oil quality. You act on what's happening rather than on the calendar.

**Predictive.** Use patterns in condition data and failure history to forecast a failure before it happens, often with machine learning. The goal is to act at the last sensible moment, planned around production.

## Side by side

| | Reactive | Preventive | Condition-based | Predictive |
| --- | --- | --- | --- | --- |
| **Trigger** | A breakdown | Time or usage | A measured condition crossing a limit | A forecast of failure |
| **Planned downtime** | None | Regular | When needed | When needed, scheduled ahead |
| **Unplanned downtime** | High | Lower | Low | Lowest, when the model is good |
| **Data needed** | Very little | Asset register and usage counters | Sensors on the right components | Condition data, failure history, maintenance actions and operating context |
| **Best for** | Cheap, non-critical assets with spares on the shelf | Assets with predictable wear | Critical assets with a measurable sign of wear | Bottleneck and high-value assets with enough history |

## Choosing per asset

Ask these about each asset:

- **What does a failure cost?** Include lost output on the bottleneck, scrap, safety and customer impact.
- **Does it give warning?** Some failures show signs weeks ahead. Others are sudden.
- **Can you measure that warning?** If there's no sensor and no practical way to add one, condition-based and predictive aren't options yet.
- **Do you have the history?** Predictive models learn from past failures. Without failure history, start with condition-based limits.

A light bulb in a corridor runs to failure. A gearbox on the bottleneck with a vibration signature is a good candidate for condition-based maintenance, and later predictive.

## Why everything starts with downtime data

You can't predict failures you don't record accurately. Most factories still log downtime at the end of the shift, from memory, with a reason chosen from a list that's too long or too vague. Short stops aren't recorded at all.

Get that right first: stops detected automatically from the equipment, with operators adding the reason while it's fresh, and production and maintenance working from the same record. [MES/MOM](/post/mes-functionality-maintenance) does that, and usage counters from production can drive preventive maintenance straight away. More in [Predictive maintenance needs data you probably aren't collecting yet](/post/predictive-maintenance-data).

## Where operators fit

Operators notice problems first. Autonomous maintenance, such as cleaning and routine inspections, catches a lot before any sensor would. Give operators a fast way to raise a fault from the screen they already use, and those observations become data too.

## My view

Predictive maintenance gets the headlines, but I think the right answer for most factories is a mix. Some equipment should simply be run until it fails. A few critical assets are worth predicting. And none of it works without accurate downtime data.

Which of your assets are you maintaining on a schedule that would be better served by condition, or the other way round?
