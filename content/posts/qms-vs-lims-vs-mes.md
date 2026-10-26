---
title: "QMS vs LIMS vs MES: which quality system does what?"
short: "QMS vs LIMS vs MES"
description: "A QMS runs the quality system, a LIMS runs the lab and MES/MOM runs quality on the line. What each one does, where they meet, and which you actually need."
published: 2026-10-24
category: education
art: badge
---

Quality lives in more than one system. QMS and LIMS both sit under "quality", and both usually get bought by the quality team. Then MES/MOM arrives with inspections and SPC of its own, and people reasonably ask which system should do what.

They overlap in places. But each is built for different work, and different people.

A quick note on terms. Strictly, MES covers production. MOM, manufacturing operations management, covers production, quality, inventory and maintenance. Most people search for "MES", so I use MES/MOM here, but it's the quality capability of MOM that matters.

## What a QMS does

A **QMS** (Quality Management System) runs the processes that keep quality under control across the business. It works over weeks and months, and across sites and suppliers:

- Root cause investigations, CAPA (corrective and preventive action) and non-conformances
- Customer complaints
- Audits and certifications, such as ISO 9001, IATF 16949 or GMP
- Document control, change control and training records
- Supplier qualification and supplier quality

Its users are quality managers, QA, auditors and process owners. Its output is evidence that the system works, and actions that make it work better.

## What a LIMS does

A **LIMS** (Laboratory Information Management System) runs the lab. It works in hours and days, sample by sample:

- Samples, labels and chain of custody
- Test methods, specifications and limits
- Results, often captured directly from lab instruments
- Analyst workload and lab scheduling
- Certificates of analysis (CoA) and stability studies

Its users are lab analysts and lab managers, with QA reviewing the results. Its output is a trustworthy result for every sample.

## What MES/MOM does for quality

**MES/MOM** runs quality at the point of production, in real time and against the order that's running:

- Inspection plans and sampling, triggered by what's actually happening on the line
- In-process checks and SPC on critical characteristics
- Goods-in inspection of incoming material
- Non-conformances recorded at the source, with the order, lot, machine and operator attached
- Holding and releasing lots, so suspect material can't be consumed
- Batch release, drawing on the batch record and the test results

Its users are operators, team leaders, supervisors and quality technicians on the floor. Its output is quality data with full production context, captured as it happens.

### Sampling triggered by events

This is one of the strongest reasons to run quality in MOM. Because MOM sees production, quality, inventory and maintenance events as they happen, any of them can add a check to the operator's list:

- An order starts, or the first part comes off after a changeover
- A tool is changed, or a mould goes back in after maintenance
- Inventory is created, or a new lot of material is consumed
- An out-of-spec measurement or a critical defect is recorded
- A process parameter trends above a threshold

The check arrives with everything already filled in: the order, material, lot, machine and operator. Nobody has to type any of it, and nobody has to remember to do the check.

## Side by side

| | QMS | LIMS | MES/MOM |
| --- | --- | --- | --- |
| **Main job** | Manage and improve the quality system | Manage samples and test results in the lab | Control quality during production |
| **Typical users** | QA, quality managers, auditors, process owners | Lab analysts, lab managers | Operators, team leaders, supervisors, quality technicians |
| **Time scale** | Weeks and months | Hours and days | Seconds to shifts |
| **Core records** | CAPAs, complaints, audits, documents | Samples, tests, results, CoAs | Inspections, sampling, SPC, holds, non-conformances, genealogy |
| **Connects to** | ERP, MES/MOM, suppliers, document systems | Instruments, ERP, MES/MOM | Equipment, ERP, and a QMS or LIMS where one is used |
| **Who needs it** | Some regulated or certified manufacturers, though MOM plus ERP often covers it | A minority, mainly lab-heavy industries | Any plant that wants quality built into the process |

## Where they meet

**Non-conformances and CAPA.** A non-conformance is found on the line and recorded in MES/MOM with full context. Serious or repeat issues, and the CAPA that follows, are best escalated into ERP, where the cost, supplier and customer sides are handled. They shouldn't be managed entirely inside MES/MOM, or a QMS on its own.

**Incoming material.** Goods-in inspection can run in MES/MOM. Results that affect how the supplier is paid, or that need taking up with the supplier, pass to ERP, which handles the commercial side. You don't need a LIMS for that.

**Batch release.** MES/MOM can release batches, drawing on the batch record and the test results, and an open deviation can block release. Pick one system for the decision and stick to it.

**Specifications.** Where a LIMS is used, it holds the lab test limits. MES/MOM holds the in-process limits. Agree which system is the master for each.

## When you need a LIMS

The main reason for a LIMS is a lab with a heavy sample load, many instruments and strict regulations around them. That's mostly found in a few industries:

- Pharmaceuticals and biotech
- Chemicals and petrochemicals
- Food and dairy plants with their own microbiology labs
- Metals, mining and materials testing

Even there, a LIMS isn't always needed. Where the testing is simple, or done by an external lab, MOM can record the samples and results itself.

There's more on the boundaries with MES/MOM in [QMS and MES: closing the quality loop](/post/qms-and-mes-quality) and [LIMS and MES: getting lab results to the line](/post/lims-and-mes).

## Which do you need?

- **Defects found too late, or quality data without context?** Start with quality in MOM.
- **Certified or regulated?** MOM, with non-conformances and CAPA escalated into ERP. A separate QMS rarely adds enough to justify it.
- **Testing incoming materials?** Goods-in inspection in MOM, with supplier issues passed to ERP.
- **A large regulated lab?** That's when a LIMS earns its place.

## My view

A good MOM platform is the place to run quality. It manages the inspection plan, triggers checks from what's actually happening, captures every result with full context, and holds and releases material. Serious non-conformances and CAPA then escalate into ERP, where the business side is handled. With MOM and ERP working together, a separate QMS adds little.

If you run an MES that covers production only, it can feed a separate QMS with non-conformances and results, and that works. But a full MOM is the better overall solution.

A LIMS is a specialist tool for a heavy, regulated lab, in a handful of industries. Most manufacturers don't need one.

Where does an out-of-spec result go in your business today, and how long does it take to get there?
