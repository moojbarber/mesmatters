---
title: "Predictive maintenance needs data you probably aren't collecting yet"
short: "Predictive maintenance"
description: "From reactive to preventive to condition-based. What predictive maintenance really needs, why downtime data comes first, and where operators fit in."
published: 2026-07-22
category: thought-leadership
art: spc
---

Predictive maintenance is one of the most talked-about AI use cases in manufacturing. It's also one of the most proven.

But it's usually sold as a technology you switch on. It isn't. It's the end of a journey, and most factories are still near the start.

## Three ways to maintain equipment

**Reactive.** Fix it when it breaks. The most expensive approach by a distance: unplanned downtime, emergency repairs, knock-on damage, missed deliveries.

**Preventive.** Maintain on a schedule, by time or cycle count. Better. But schedules are blunt. Sometimes you maintain too early and waste parts and labour. Sometimes too late, and it breaks anyway.

**Condition-based and predictive.** Maintain based on the actual condition of the equipment. Vibration, temperature, current draw, pressure, cycle counts. Predictive goes a step further and uses those patterns to forecast a failure before it happens.

That last one is the goal. But you can't jump to it.

## Why downtime is where it starts

Downtime is usually the biggest loss when you look at [OEE](/post/what-is-oee-overall-equipment-effectiveness). For most manufacturers, it's the single largest area for improvement.

Before you can predict failures, you need to know your failures. Accurately. Which machine, how long, how often, for what reason, during which order.

Most factories don't have that yet. Downtime is recorded at the end of the shift, from memory, with a reason code chosen from a list that's too long or too vague. Short stops aren't recorded at all.

Get that right first. Automatic stop detection from the equipment, with operators adding the reason while it's fresh. It's not glamorous, but it's the foundation everything else stands on.

## What the models need

Predictive maintenance models learn the patterns that come before a failure. That means collecting the right data, over time:

- **Condition data.** The sensor readings that change as a component degrades. You may need new sensors for this, so start with your bottleneck assets.
- **Failure history.** When things actually failed, and why. Without it, the model has nothing to learn from.
- **Maintenance actions.** What was actually done each time: the part replaced, the adjustment made. Otherwise the model can't tell a repaired machine from a degrading one.
- **Operating context.** What the machine was doing at the time: which product, which speed, which material. A spike in temperature during a heavy product run means something different from the same spike on a light one.

Condition data and failure history are often in separate places. Operating context usually only exists in [MES/MOM](/post/what-is-mes-and-why-is-it-important-in-manufacturing). That's why I'm wary of predictive maintenance projects that sit in a silo, disconnected from what production was doing.

## Production and maintenance on the same data

This is a point I come back to often.

Production and maintenance both care about downtime. If production records stops in one system and maintenance works from another, they'll disagree about what happened. The morning meeting turns into an argument rather than a plan.

When maintenance lives in the same platform as production, both teams see the same stops, the same reasons and the same equipment history. Repair windows can be planned around the schedule. And the data that predictive models need is already joined up.

I cover how maintenance fits into MES/MOM in [MES functionality: maintenance](/post/mes-functionality-maintenance).

## Don't forget the operator

Asset care is increasingly the operator's job too. Autonomous maintenance: cleaning, lubrication, visual checks, tightening, spotting early signs of wear.

Operators often notice problems long before a sensor does. A new noise. A different smell. A machine that "doesn't feel right". Give them a quick, easy way to log it from the screen they already use, and you add a source of early warning no model can replicate.

## Start small

You don't need sensors on every machine on day one.

1. Get accurate downtime data, automatically, on your bottleneck assets.
2. Move maintenance into the same system as production, so everyone sees the same picture.
3. Add condition sensors where the cost of failure is highest.
4. Collect failure history consistently for a period before you train anything.
5. Then pilot a predictive model on one asset type, and measure the result.

Every step pays back on its own. And by the time you reach step five, you'll have the data a model actually needs.

Which asset in your factory would you most like to see failing a week before it does?
