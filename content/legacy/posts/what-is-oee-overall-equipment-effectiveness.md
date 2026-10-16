---
title: "What is OEE (Overall Equipment Effectiveness)"
slug: "what-is-oee-overall-equipment-effectiveness"
legacyUrl: "https://www.mesmatters.com/post/what-is-oee-overall-equipment-effectiveness"
description: "What is OEEOverall Equipment Effectiveness (OEE) is a global standard used across all industries in manufacturing to measure the effectiveness of a production line. It takes into account how much good material was created on the production line, compared to the amount of good material that theoretically could have been created. Factors like scrap, downtime, and slow running equipment negatively affect the OEE figure, which can be used for continuous improvement activities, and to benchmark equip"
published: "2023-06-08T15:40:10.900Z"
updated: "2026-10-16T09:00:00.000Z"
author: "Matthew Barber"
categories: ["MES Education"]
heroImage: "/images/legacy/b75fc5_2367592c66354089963cc1ae2120014b-mv2.jpg"
wordCount: 1872
---

## What is OEE

Overall Equipment Effectiveness (OEE) is a global standard used across all industries in manufacturing to measure the effectiveness of a production line. It takes into account how much good material was created on the production line, compared to the amount of good material that theoretically could have been created. Factors like scrap, downtime, and slow running equipment negatively affect the OEE figure, which can be used for continuous improvement activities, and to benchmark equipment and processes.

> OEE asks the question: Are we producing good quality product, at the fastest rate we can, 100% of the available time?

## OEE Calculation

The calculation for OEE is:

> **OEE** = Availability x Performance x Quality

An industry standard for OEE exists, it is the ISO 22400 standard. This standard defines the definition of the components of OEE and other key KPIs. The full ISO definition is available to be purchased, but a sub-section of information is available [here](https://www.iso.org/obp/ui/#iso:std:iso:22400:-2:ed-1:v1:en). The standard includes more KPIs than just OEE and it's components, I'd strongly recommend purchasing for additional information. I'll use my own more descriptive terms for the calculations in this article, rather than those defined by ISO.

#### Availability

The availability figure represents the percentage of time that equipment is running, compared to the time it was planned to run. If the equipment was not planning to run, for example if the factory does not operate during weekend hours, then this time is excluded from the calculation.

> **Availability** = Production Time / Planned Production Time

Definitions:

- **Production Time** = The time the production line actually ran.
- **Planned Production Time** = The total time the production line was planned to run for.

In an 8 hour shift, if the production line stopped for 2 hours then the Availability figure is 6 (hours) / 8 (hours) = 0.75 = 75%. Meaning the production line was running for 75% of the time, and stopped for 25% of the time.

Production lines often comprise multiple machines, where each machine is performing a different manufacturing operation.

The only machine that is interesting for the OEE calculation is the bottleneck machine. The bottleneck is the machine with the lowest throughput in the line.

If other machines in the line operate faster than the bottleneck, then they may be able to stop for short periods of time without affecting the bottleneck machine. If other machines in the line incur downtime, but the bottleneck is not impacted and still runs 100% of the time, then the production line can not produce any faster, so the machine stops from other machines do not impact the OEE figure.

If the other machines stop for long enough they will impact the bottleneck machine and cause it to stop. If machines before the bottleneck stop the bottleneck will eventually be starved of material. If the machines after the bottleneck stop then the bottleneck will become blocked, as it can not process any more materials.

#### Performance

The performance figure defines whether the the production line is producing at the target speed for the equipment. Each operation in the routing defines the "Target Cycle Time" which is how long it takes to make a quantity of 1 unit. The actual cycle time is based on the production volumes on the line, and compared to the target cycle time to calculate the performance figure.

> **Performance** = (Quantity Produced x Target Cycle Time) / (Target Quantity Produced x Target Cycle Time)

Definitions:

- **Quantity Produced** = The total quantity produced, including any scrap produced.
- **Target Quantity Produced** = The quantity that could have been produced in the same time period, if the production line had produced at the rate defined by the "Target Cycle Time".
- **Target Cycle Time** = The time it takes to make a quantity of 1.

All parts of the OEE calculation relate back to a "time" unit. Including the target cycle time in the equation allows comparison across items with different target cycle times. In reality the calculation can be simplified to remove the target cycle time:

> **Performance** = Quantity Produced / Target Quantity Produced

If the production line can make 6 pieces per minute then the target cycle time for 1 piece is 10 seconds. If the production line actually produces 4 pieces per minute, then the actual cycle time is 15 seconds. The performance figure is 10/15 = 66.6%.

If you get a production performance figure of more than 100%, this means that you need to review your target cycle time because your machines can produce at a higher rate than you have defined in the master data. It can be tempting to leave the master data as it is to score a higher OEE result, but this is counterproductive as it doesn't drive continuous improvement. Recognise the achievement of the operators, adjust the target cycle time, and aim for better.

#### Quality

The quality rate is the percentage of good quantity produced compared to the total quantity produced.

> **Quality** = (Good Quantity x Target Cycle Time) / (Quantity Produced x Target Cycle Time)

Definitions:

- **Good Quantity** = The total good quantity produced.
- **Quantity Produced** = The total quantity produced, including any scrap produced.
- **Target Cycle Time** = The time it takes to make a quantity of 1.

All parts of the OEE calculation relate back to a "time" unit. Including the target cycle time in the equation allows comparison across items with different target cycle times. In reality the calculation can be simplified to remove the target cycle time:

> **Quality** = Good Quantity / Quantity Produced

If the line produces 100 pieces, but only 95 of them are good, then the quality rate is 95%.

Scrap has a negative impact on the quality figure, but rework doesn't. Rework does affect OEE though, as it takes more time to process the same number of pieces because some pieces need to be processed multiple times. This affects the performance figure, not the quality figure.

Sometimes processes create an expected quantity of waste as a by-product of the process. This doesn't contribute to the quality rate, as it is planned as part of the process.

#### Final Calculation

So, the high-level OEE calculation is:

> **OEE** = Availability x Performance x Quality

Which equates to:

> **OEE** = (Production Time / Planned Production Time) x (Quantity Produced / Target Quantity Produced) x (Good Quantity / Quantity Produced )

This can be simplified to:

> **OEE** = Good Quantity / (Planned Production Time / Target Cycle Time)

This basically says, what is the total good quantity made compared to the amount we could have made in the planned time, based on the target cycle time.

So, you may ask why it's broken down into the 3 components of Availability, Performance, and Quality....?

The answer is.....to identify where in the process the losses are occurring for continuous improvement activities.

## Data Capture

To get the most accurate OEE figure it's crucial to invest in automatic data capture in real-time directly from the shopfloor equipment. This is usually captured via OPC.

In the absence of automated OPC data, operators can capture this data manually but be aware that this will always give you a more positive view of your OEE figure because operators are unable to collect the detailed data, for example very short machine stops, sometimes only a few seconds will not be captured by operators, and sometimes short stops can have the biggest impact on production.

If you are migrating from manual data collection to automated data collection then you should expect to see much lower OEE figures than you have been used to. Initially this can be a cause for concern, but it's important to effectively communicate with operations, supervisors, and management to explain the situation and try to assess a new bench mark. Once the new benchmark is in place, this gives you a good baseline for continuous improvement activities. You can't improve what you don't measure.

## Analogy

OEE can actually be used to determine the effectiveness of anything, if you aren't familiar with OEE then lets go over a non-manufacturing analogy.

Imagine you are a person typing.

You plan to type for 1 hour, but you take a 10 minute coffee break and finish 5 minutes earlier than planned for lunch. Your availability is 75% because you planned to type for 1 hour, but you only typed for 45 minutes.

You can type at a rate of 50 words per minute, but it's difficult to keep this up for prolonged periods of time. Instead you average 40 words per minute. This is only 80% of your top performance, so you experience a loss here.

Intermittently you make typing errors and have to spend time correcting, this loss of quality affects your overall effectiveness by 5%, making your quality rate 95%.

Overall, the best you could have done in 1 hour is 60 (minutes) x 50 (words) = 3000 words.

> Your OEE was 57% (75% x 80% x 95%) which is 1710 words.


## Where you count changes where the losses show

Here's a weird one. Move the sensor that counts production on a line, and your Performance and Quality figures can swing wildly while OEE stays exactly the same.

It isn't a glitch. OEE is fundamentally (good units × target cycle time) / planned production time. If good units and planned time don't change, OEE doesn't either. But where you count shifts the blame between Availability, Performance and Quality.

**Counting before the bottleneck**, the bottleneck looks like it's hitting its speed because it's being fed well, scrap inside the bottleneck is invisible, and downstream back-ups show up as idle time, making Availability look worse than it is.

**Counting after the bottleneck** gives you reality: if the machine struggled to keep up, it shows as a speed loss, and Availability measures the time it was actually producing sellable parts.

So be strategic about your data points:

- **Downtime:** if you only monitor one machine, make it the bottleneck. Track the others to see whether it's being starved or blocked.
- **Scrap:** ideally after every operation that can produce scrap. Prioritise where you can't do them all.
- **Counts:** the more places the better, ideally an "in" and "out" for the line, so you can see losses by operation.

And remember the micro-stops. Short stops of a few seconds are almost never recorded manually, but they add up, and they're often the real killer. Automatic data capture is usually the first time people see them.

## Benchmarking

As mentioned earlier, OEE is always calculated based on a unit of "time". This means that benchmarking can be performed across different materials, manufacturing processes, manufacturing plants, and even across industries.

OEE rates vary massively across industries, it's not a "one size fits all". Typically 85% OEE is considered "world class", many manufacturers operate closer to 60%, or lower.

## How to improve OEE

The first step to improving anything is to start measuring it. Once it is being accurately measured, continuous improvement initiatives can be put in place to mitigate the biggest losses.

The most significant loss is often downtime, for most manufacturers this is the biggest challenge. Interestingly, it's small frequent stops that can have as big an impact (if not bigger) than long stops which happen less frequently, but continually stop the production line. Common causes of downtime are, short stops for machine settings and issues, breakdowns, lack of resources. Consider implementing maintenance within your MES to proactively complete asset care procedures to reduce your breakdowns.

Product quality can also have an impact. Implementing quality and SPC within your MES to identify issues before they become a problem is a great way to improve your quality rate.

Manufacturers who manually collect data on the shopfloor, and then switch to an automated approach are often staggered by their "real" OEE figure. This is primarily down to the fact that the data collected automatically is so much more accurate. For example, if the machine stops for a few seconds then it's unlikely that would be recorded manually, but automatic data capture will record all of these stops in detail, giving a more accurate figure.

## Summary

OEE is a measure of the productivity of production equipment. OEE is calculated by multiplying availability, performance, and quality rates. Availability is the percentage of time that equipment is available for production. Performance is the percentage of the maximum possible production rate achieved by equipment. Quality is the percentage of good units produced by equipment. MES systems provide real-time visibility into OEE, enabling manufacturers to monitor and optimise equipment productivity. By analysing OEE over time, manufacturers can identify trends and patterns in equipment performance, enabling them to take proactive measures to improve productivity and reduce costs. OEE is critical for monitoring production performance, benchmarking across processes and factories, and for continuous improvement activities.

## Related reading

- [Manufacturing KPIs beyond OEE](/post/manufacturing-kpis-beyond-oee)
- [MES functionality: production monitoring](/post/mes-functionality-production-monitoring)
- [Predictive maintenance needs data you probably aren't collecting yet](/post/predictive-maintenance-data)
