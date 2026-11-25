# Eval results: new, old, without

18 items. Cost $3.01 (including any reused runs).

| | new | old | without |
|---|---|---|---|
| Mean score | 0.97 | 0.89 | 0.88 |
| Pitfalls committed | 0 | 0 | 0 |
| Skill loaded | 17 of 18 | 0 of 18 | 0 of 18 |

- **new vs without:** mean difference +0.09 (95% paired bootstrap +0.03 to +0.17); better on 5, worse on 0, tied on 13.
  - loaded (17 items): 0.97 vs 0.88
  - not loaded (1 items): 1.00 vs 1.00
- **old vs without:** mean difference +0.01 (95% paired bootstrap -0.04 to +0.07); better on 1, worse on 2, tied on 15.
  - not loaded (18 items): 0.89 vs 0.88

## By kind

| Kind | n | new | old | without |
|---|---|---|---|---|
| apply | 6 | 0.94 | 0.92 | 0.92 |
| critique | 3 | 1.00 | 0.83 | 0.89 |
| discriminate | 2 | 0.92 | 0.62 | 0.62 |
| procedure | 4 | 1.00 | 0.96 | 1.00 |
| recognize | 3 | 1.00 | 1.00 | 0.83 |

## By item (score, and * if the skill was loaded)

| Item | Kind | new | old | without |
|---|---|---|---|---|
| ai-002 | recognize | 1.00* | 1.00 | 0.50 |
| ai-010 | apply | 1.00* | 0.83 | 0.83 |
| ai-011 | procedure | 1.00* | 1.00 | 1.00 |
| ai-012 | critique | 1.00* | 0.83 | 1.00 |
| ai-014 | discriminate | 0.83* | 0.50 | 0.50 |
| arch-003 | recognize | 1.00* | 1.00 | 1.00 |
| arch-005 | recognize | 1.00* | 1.00 | 1.00 |
| found-004 | procedure | 1.00* | 1.00 | 1.00 |
| found-005 | apply | 1.00* | 1.00 | 1.00 |
| found-010 | critique | 1.00* | 1.00 | 1.00 |
| found-011 | apply | 1.00 | 1.00 | 1.00 |
| found-012 | discriminate | 1.00* | 0.75 | 0.75 |
| model-002 | procedure | 1.00* | 0.83 | 1.00 |
| model-005 | critique | 1.00* | 0.67 | 0.67 |
| model-006 | procedure | 1.00* | 1.00 | 1.00 |
| model-007 | apply | 1.00* | 1.00 | 1.00 |
| model-008 | apply | 1.00* | 1.00 | 1.00 |
| model-009 | apply | 0.67* | 0.67 | 0.67 |
