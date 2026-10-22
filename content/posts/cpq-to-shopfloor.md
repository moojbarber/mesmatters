---
title: "From CPQ to the shopfloor: building what the customer actually configured"
short: "CPQ to shopfloor"
description: "Configured and engineer-to-order products start in CPQ. How the configuration reaches the operator through ERP, and when PLM gets involved too."
published: 2026-09-03
category: education
art: tiles
---

If you make configured products, every order is slightly different. Different motor. Different colour. Different control panel. A bracket that only exists for one customer.

The sale is won in **CPQ** (Configure, Price, Quote). The product is built on the shopfloor. In between, a lot can get lost.

## What CPQ does

CPQ lets sales, or the customer directly, configure a product from a set of options and rules. It knows that option A rules out option B, that the large frame needs the heavy-duty base, and what the whole thing costs. It produces a valid, priced quote.

When the quote is accepted, you have a configuration. A list of choices. That's not something the shopfloor can build from. Yet.

## Configuration to order: ERP sits in the middle

In most setups the accepted quote becomes a sales order in **ERP**, with the configuration attached. ERP then does the heavy lifting:

- Resolves the configuration into an order-specific BOM, using variant rules on a configurable "super BOM"
- Selects the matching routing operations, and drops the ones this variant doesn't need
- Plans materials and capacity
- Releases a production order for that exact variant

That order, with its specific BOM and routing, goes to **MES/MOM**. From the operator's point of view, it's just an order. The configuration has already been turned into something buildable.

This is the most common pattern, and for configure-to-order products with well-defined options, it works well. ERP is where the configuration has to become cost, stock and capacity anyway.

## Where it gets harder: engineer-to-order

Configure-to-order means every option already exists. Engineer-to-order (ETO) means some of it doesn't. The customer wants something the rules don't cover, and engineering has to design it.

Now the flow has a second path. Sales hands over to engineering. Engineering designs the special parts in **PLM**. Those release to ERP, which updates the order BOM and routing. Only then can the order go to MES/MOM.

Two things I'd watch for here:

- **Partial release.** ETO products often start production before engineering is finished. Long-lead items and standard sub-assemblies go first. MES/MOM needs to handle an order whose later operations aren't defined yet.
- **Order-specific documents.** A one-off bracket has a one-off drawing. The operator needs it, at the right revision, at the operation. ERP usually won't carry it.

That second point is where some manufacturers add a direct link from PLM to MES/MOM for drawings and instructions, while the order itself still comes through ERP. I go through the options in [PLM, ERP and MES: where the digital thread actually runs](/post/plm-erp-mes-digital-thread).

## What the operator needs to see

The configuration should change what the operator sees. Not as a list of option codes, but as instructions for *this* unit:

- Only the steps that apply to this variant
- The right component, with its picture, at each step
- Option-specific checks, such as wiring tests for the export voltage
- Clear flags for anything unusual, like a customer-special part

That's where [digital work instructions that know what's running](/post/digital-work-instructions) earn their keep. If every operator reads a generic instruction and mentally filters it for the options on the traveller, you're relying on memory. Error-proof it instead: let MES/MOM show only what applies, and scan components against the order BOM.

## Options at a glance

| Product type | Typical flow | Direct PLM to MES/MOM? |
| --- | --- | --- |
| Configure-to-order, simple options | CPQ → ERP → MES/MOM | Rarely needed |
| Configure-to-order, complex visual assembly | CPQ → ERP → MES/MOM | Often useful for option-specific instructions |
| Engineer-to-order | CPQ → ERP and PLM → ERP → MES/MOM | Common, for order-specific drawings |

Some manufacturers also feed the configuration straight to MES/MOM so it can select instructions by option code. That works, but keep ERP's order BOM as the authority. Two systems interpreting the same configuration independently will, eventually, disagree.

## Closing the loop

Configured products give you a goldmine of data, if you capture it. Which options take longest to build? Which combinations cause the most rework? Which options get changed after the order is placed? Which "standard" options are really bespoke every time?

That's MES/MOM data. Feed it back to the people who maintain the CPQ rules and the product range. How many of your options are priced as if they're easy to build, when the shopfloor knows otherwise?
