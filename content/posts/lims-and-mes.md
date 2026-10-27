---
title: "LIMS and MES: getting lab results to the line before the batch moves on"
short: "LIMS and MES"
description: "A good MOM handles sampling, lab tests, SPC and certificates of analysis itself. When a separate LIMS earns its place, and how the flow works with and without one."
published: 2026-09-22
category: education
art: tanks
---

In process manufacturing, a lot of quality happens away from the line. Samples go to the lab. Results come back. Sometimes hours later.

If those results arrive after the batch has already moved to the next stage, or worse, been packed and shipped, the lab might as well not exist.

## What a LIMS does

A **LIMS** (Laboratory Information Management System) runs the lab. It manages:

- Samples, their labels and chain of custody
- Test methods, specifications and instrument data
- Analyst workload and lab scheduling
- Certificates of analysis (CoA) and stability studies

## What MOM can do in the lab

A good MOM covers a lot of this itself. It triggers checks and samples from what's happening on the line, records results against the batch and phase, runs SPC on them, and produces certificates of analysis. Because it's running the batch, every result comes with the recipe, equipment, raw material lots and process conditions attached.

There are many good reasons to keep as much of this inside the MOM as possible: one system for the operator and the lab technician, no interface to maintain, and results that act on the batch the moment they're recorded.

## When a separate LIMS earns its place

A LIMS is an option in some cases, and in certain industries there's more of a case for a separate LIMS than for a separate QMS. It's typically a heavy, regulated lab with many instruments, analysts and stability studies, such as in pharmaceuticals and biotech, chemicals, food and dairy plants with their own microbiology labs, and materials testing. Even there, check how much the MOM already covers before adding another system.

## The flow when MOM handles the lab

This is the simpler option:

1. **MOM triggers the sample.** The batch reaches a phase that needs testing. MOM tells the operator, prints the label and adds the test to the lab's work list, with the batch, phase and equipment already attached.
2. **The lab tests it in MOM.** Results are recorded against the specification, by hand or straight from the instrument.
3. **MOM acts.** A pass releases the next step. A fail holds the batch, or triggers an adjustment such as adding more of an ingredient, then a re-sample.

No interface, no waiting for a message to arrive, and nothing typed twice.

## The flow when a LIMS is used

This works too, but it needs integration:

1. **MES/MOM triggers sampling.** It tells the operator, prints the label and tells the LIMS a sample is coming, with the batch, phase and equipment attached.
2. **The LIMS tests it.** The lab receives the sample, runs the methods and records results against the specification.
3. **Results come back.** Pass, fail or out-of-spec values flow back to MES/MOM against the batch and phase.
4. **MES/MOM acts.** A pass releases the next step. A fail holds the batch, or triggers an adjustment and a re-sample.

The sample needs to be born with its context. If the lab has to type in the batch number from a handwritten label, you've lost both time and traceability. And when a reactor sits waiting for a result, a direct link between the LIMS and MES/MOM is usually worth having, rather than routing results through ERP.

## Where ERP fits

**ERP** usually owns batch status for the business: quarantined, released, rejected. It needs that to plan, to ship and to report stock.

Incoming materials can be tested in MES/MOM too. Results that affect how the supplier is paid, or that need raising with the supplier, pass to ERP.

Final batch release draws on the test results and the batch record. MES/MOM can release the batch, as part of [review by exception](/post/mes-in-regulated-industries) on the electronic batch record, and post the status to ERP. Where a LIMS is used, release sometimes sits there instead. Pick one place and stick to it.

## Watch out for

- **Specifications defined twice.** Where a LIMS is used, the spec must not live in both systems, or they'll drift. Pick one owner and don't duplicate.
- **Results without process context.** A failed test is far more useful when you can see the temperature profile of the phase it came from. [Context](/post/contextualised-manufacturing-data) turns a lab result into a root cause.
- **Manual transcription.** Any result keyed by hand from one system into another is a data integrity risk, and in regulated industries an audit finding waiting to happen.
- **Units that don't match.** One system reports mg/kg, the other expects ppm. Or one rounds to one decimal place and the limit is set to two. Test the edge cases before go-live, not after the first false pass.

How long does a batch in your plant sit waiting for a lab result? And how much of that wait is the test, versus the paperwork around it?
