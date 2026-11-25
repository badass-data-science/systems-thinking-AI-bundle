---
id: recurring-causes-mean-structure
type: heuristic
title: Recurring, differently-caused failures point at structure
summary: If each incident has a different, correctly fixed root cause but the overall metric doesn't improve, the cause is in the structure connecting the parts, not in any part.
chapters: [1, 5]
when: Every postmortem finds a real, different proximate cause, every fix works, and the aggregate failure rate stays flat or worsens.
then: Stop treating incidents one at a time. Line them up as a pattern and ask which unchanged interconnection keeps stressing a different part each period (the iceberg model's pattern and structure bands).
links:
  diagnoses: [fixes-that-fail]
  uses: [iceberg-model, system]
  related: [reduction]
series: [unintended-consequences]
mnemonic: "Four quarters, four 'ROOT CAUSE IDENTIFIED AND RESOLVED' stamps, and the miss rate went up."
---

A run of correct fixes that doesn't move the aggregate is evidence, not bad luck. The elements that broke changed every time; something that didn't change kept transmitting stress to whichever element was weakest. In the book's running example, urgency at the assembly end of a supply chain fed back into corner-cutting at the refining end, whichever link happened to break.

The heuristic applies equally to a deployment pipeline whose every outage has a different real cause, a forecasting model retrained after each drift and drifting again for a new reason, or a hiring funnel patched at whichever stage leaked worst last month.

It stops holding when the incidents really are independent: different systems, no shared resource, no shared schedule pressure. Check for a shared interconnection before concluding there is one.
