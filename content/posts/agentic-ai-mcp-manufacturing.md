---
title: "Agentic AI and MCP, explained for people who run factories"
short: "Agentic AI and MCP"
description: "Agentic AI and MCP are all over LinkedIn. What they actually are, what they could mean for the shopfloor, and what has to be in place before any agent touches production."
published: 2026-08-27
category: thought-leadership
art: network
---

My feed has been full of agentic AI for months. Then MCP. Everyone has an opinion. I'm not convinced everyone has an accurate understanding.

So if your feed is blowing up too and you want some context, this one's for you. I'm still learning on this topic myself, so treat it as a practical starting point rather than the final word.

## What is agentic AI?

Most of the AI people have used is conversational. You ask, it answers, and you decide what to do with the answer.

Agentic AI goes further. An agent is given an objective and works towards it with some autonomy. Broadly, it:

- **Perceives.** Gathers information about the situation.
- **Reasons.** Works out what the information means.
- **Plans.** Decides what needs to happen to reach the objective.
- **Acts.** Carries out the steps, often by using other software tools.
- **Learns.** Reviews the result and gets better over time.

The important word is *acts*. An agent doesn't just tell you the line is running behind. It might re-sequence the schedule, raise a maintenance request or notify the planner. That's powerful. It's also why you need to think hard before you let one loose.

## What is MCP?

MCP stands for Model Context Protocol. It's an open, standardised way for AI agents to connect to other systems: applications, databases and APIs.

Why does it matter?

- It gives agents a common way to talk to software, without a custom integration for every pairing.
- It describes what data and functions a system offers, so an agent understands what it can do there.
- Agents can discover and use tools in connected systems without everything being hard-coded in advance.
- The system stays in control of what's exposed, so you decide which data and actions an agent can reach.

MCP is the interoperability layer that lets agents work in real, messy IT landscapes. Which, if you've ever looked at a factory's application landscape, is exactly what's needed.

## What could agents do on the shopfloor?

Some plausible examples, roughly in order of risk:

- **Prepare.** Pull together the data for the morning meeting and draft the agenda from yesterday's losses.
- **Investigate.** Trace a customer complaint back through batches, inspections and process parameters, and present a likely root cause for a person to confirm.
- **Recommend.** Suggest a revised schedule after a breakdown, showing the impact on each order.
- **Act within limits.** Raise a maintenance work order when a condition threshold is crossed, or put a suspect lot on hold pending inspection.

Notice that the first three still end with a person making the call. That's where I'd start.

## The catch: agents are only as good as what they connect to

An agent that acts on bad data acts badly, and quickly.

If it's reading downtime that was typed in at the end of a shift, inventory that's only roughly right, and quality results sitting in a spreadsheet, its decisions will reflect that. The speed that makes agents attractive also makes their mistakes expensive.

That's why agentic operations sit at the very top of the [maturity model](/post/smart-manufacturing-maturity-model). They need:

- **Trustworthy, real-time data.** Captured automatically where possible, validated at the point of work.
- **Context.** Which order, which material, which machine, which shift. That context lives in [MES/MOM](/post/what-is-mes-and-why-is-it-important-in-manufacturing).
- **Systems that enforce rules.** If an agent tries to consume a quarantined lot, the operational system should stop it, just as it would stop a person.
- **Clear guardrails and audit trails.** What the agent may do on its own, what needs approval, and a record of every action it took and why.

A well-implemented MES/MOM already error-proofs what people do. The same validation protects you from what agents do.

## My advice

Be curious, not credulous.

Start with agents that prepare and investigate rather than act. Make sure every action is logged and reviewable. And keep investing in the foundation, because the factories that get the most from agents will be the ones with clean, connected, contextualised data already in place.

What's the first task you'd trust an agent with in your factory, and what would you never let it touch?
