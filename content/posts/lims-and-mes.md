---
title: "LIMS and MES: getting lab results to the line before the batch moves on"
short: "LIMS and MES"
description: "In process industries, LIMS runs the lab and MES/MOM runs the batch. How sampling, results and release flow between them, with ERP holding batch status."
published: 2026-10-16
category: education
art: tanks
---

In process manufacturing, a lot of quality happens away from the line. Samples go to the lab. Results come back. Sometimes hours later.

If those results arrive after the batch has already moved to the next stage, or worse, been packed and shipped, the lab might as well not exist.

## What LIMS does

A **LIMS** (Laboratory Information Management System) runs the lab. It manages:

- Samples, their labels and chain of custody
- Test methods, specifications and instrument data
- Analyst workload and lab scheduling
- Certificates of analysis (CoA) and stability studies

It's essential in food and beverage, chemicals, pharmaceuticals, cosmetics and plenty of discrete industries with materials testing.

## What MES/MOM does in the same process

**MES/MOM** runs the batch. Which recipe, which equipment, which raw material lots, what the process conditions were at each phase, and what the operator did. In-process checks done at the line, such as weight, pH or viscosity at a station, often sit in MES/MOM directly.

The two meet at the sample.

## The flow that should happen

1. **MES/MOM triggers sampling.** The batch reaches a phase that needs a sample. MES/MOM tells the operator, prints the label and tells LIMS a sample is coming, with the batch, phase and equipment attached.
2. **LIMS tests it.** The lab receives the sample, runs the methods and records results against the specification.
3. **Results come back.** Pass, fail or out-of-spec values flow back to MES/MOM against the batch and phase.
4. **MES/MOM acts.** A pass releases the next step. A fail holds the batch, or triggers an adjustment such as adding more of an ingredient, then a re-sample.

The key is that the sample is born with its context. If the lab has to type in the batch number from a handwritten label, you've lost both time and traceability.

## Where ERP fits

**ERP** usually owns batch status for the business: quarantined, released, rejected. It needs that to plan, to ship and to report stock.

Final batch release is often a QA decision that draws on LIMS results and the batch record from MES/MOM. Where that decision is recorded varies:

- **Release in ERP**, with LIMS and MES/MOM feeding the evidence. Common, and keeps stock status in one place.
- **Release in LIMS**, which then updates ERP. Common where the lab owns the release decision.
- **Release in a QMS**, which then updates ERP. Common where QA runs a formal disposition process.
- **Release in MES/MOM**, as part of [review by exception](/post/mes-in-regulated-industries) on the electronic batch record, then posted to ERP.

## Integration options

Raw material testing usually flows LIMS ↔ ERP. Goods are received in ERP, quarantined, sampled, tested in LIMS, and released in ERP. MES/MOM only needs to know the lot is released before it can be used.

In-process testing is where the options appear:

| | Through ERP | Direct LIMS ↔ MES/MOM |
| --- | --- | --- |
| Sample request | MES/MOM → ERP → LIMS | MES/MOM → LIMS |
| Results | LIMS → ERP → MES/MOM | LIMS → MES/MOM, and LIMS → ERP for status |
| Good for | Few in-process samples, slow processes | Frequent in-process samples that gate the next step |

When a reactor sits waiting for a result, every minute counts. The direct link is usually worth it for in-process testing. For raw materials and final release, the ERP path is often perfectly adequate.

## Watch out for

- **Specifications defined twice.** If the spec lives in both LIMS and MES/MOM, they'll drift. Pick one owner, usually LIMS for lab tests and MES/MOM for line checks, and don't duplicate.
- **Results without process context.** A failed test is far more useful when you can see the temperature profile of the phase it came from. That's MES/MOM data. [Context](/post/contextualised-manufacturing-data) turns a lab result into a root cause.
- **Manual transcription.** Any result keyed by hand from one system into another is a data integrity risk, and in regulated industries an audit finding waiting to happen.
- **Units that don't match.** One system reports mg/kg, the other expects ppm. Or one rounds to one decimal place and the limit is set to two. Test the edge cases before go-live, not after the first false pass.

How long does a batch in your plant sit waiting for a lab result? And how much of that wait is the test, versus the paperwork around it?
