---
title: "ISA-95 vs ISA-88: which standard covers what"
short: "ISA-95 vs ISA-88"
description: "ISA-88 standardises batch control: recipes, equipment and procedures. ISA-95 standardises how manufacturing operations connect to the business. What each covers, where they meet, and which one you need to know."
published: 2026-10-23
category: education
art: stack
---

If you work in process manufacturing, you'll hear both of these standards quoted, sometimes in the same sentence. They're related, they come from the same organisation, and they're easy to mix up.

They answer different questions.

## ISA-88: how to control a batch

ISA-88, often called S88, is the standard for batch control. Its first part was published in 1995, and it's also adopted internationally as IEC 61512.

It gives you a common way to describe batch manufacturing:

- **A physical model** of the plant, from site and area down to process cells, units, equipment modules and control modules.
- **A procedural model** of how a batch is made, from the procedure down to unit procedures, operations and phases.
- **A process model** describing the stages and operations of the process itself, independent of the equipment.
- **A recipe model** that separates what to make from the equipment it's made on, so the same recipe can run on different units.

The big idea is separating the recipe from the equipment. Engineers build reusable phases once, such as charge, heat, agitate or transfer, and recipes combine them. That makes recipes far easier to change and reuse.

ISA-88 lives mostly at the control level, inside the DCS or batch manager.

## ISA-95: how operations connect to the business

ISA-95 is the standard for integrating enterprise and control systems. Work on it began in the mid-1990s, Part 1 was published in 2000, and its core parts are adopted internationally as IEC 62264.

It's best known for the functional hierarchy, the familiar levels 0 to 4, and for defining the four areas of manufacturing operations: production, quality, inventory and maintenance. It also defines the objects that ERP and MES/MOM exchange: orders, materials, equipment, personnel and performance.

ISA-95 lives mostly at level 3 and the boundary with level 4. More in [ISA-95 explained](/post/what-is-the-isa-95-model-and-where-does-mes-fit).

## Side by side

| | ISA-88 | ISA-95 |
| --- | --- | --- |
| **Focus** | Batch control | Enterprise and control system integration |
| **First published** | 1995 | 2000 |
| **International version** | IEC 61512 | IEC 62264 |
| **Main level** | Control, levels 1 and 2 | Operations, level 3, and the boundary with level 4 |
| **Key models** | Physical, procedural and recipe models | Functional hierarchy, operations activities, exchanged objects |
| **Typical users** | Control and process engineers | MES/MOM, ERP and integration teams |
| **Applies to** | Mainly batch processes | All types of manufacturing |

## Where they meet

The two standards were designed to fit together, and they overlap in a few places.

**Equipment hierarchy.** Both describe the plant as a hierarchy. ISA-88's process cells and units sit neatly under ISA-95's areas and work centres, so you can use one consistent model from ERP down to the control module.

**Recipes and batch execution.** ISA-88 defines general, site, master and control recipes. The upper ones are closer to product definitions in ISA-95, which MES/MOM manages, while the control recipe runs in the batch manager. MES/MOM handles the order and the materials, and the batch manager runs the phases. ISA-95 describes the exchange between them, and ISA-88 describes what happens inside.

## Which do you need to know?

- **Batch process plants:** both. ISA-88 for how the control system runs the recipe, and ISA-95 for how that connects to MES/MOM and ERP.
- **Discrete manufacturers:** ISA-95 is the one that matters most. ISA-88's ideas about separating product from equipment are still worth knowing.
- **Anyone integrating ERP and MES/MOM:** start with ISA-95. It gives everyone a common vocabulary, which saves weeks of arguments about what "batch" and "lot" mean.
- **Vendors and integrators serving process industries:** both, because your customers will expect you to speak each one.

For the control side of the boundary, see [DCS vs MES](/post/dcs-vs-mes).

Do your control engineers and your MES team use the same names for the same equipment?
