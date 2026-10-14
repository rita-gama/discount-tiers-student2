# Exercise: volume discounts at the boundary

Customers report that ordering **exactly** 10, 50 or 100 units does not give them
the discount advertised on the pricing page:

| Units ordered | Discount |
|---|---|
| 10 or more | 5% |
| 50 or more | 10% |
| 100 or more | 15% |

Ordering 11 units works. Ordering 10 does not.

## Your task

Fix the bug in `shop/pricing.py` so every tier applies from its minimum quantity.
The fix must also work for custom tier lists passed through the `tiers` argument.

## Rules

- Change only `shop/pricing.py`. Changes to other files make the submission invalid.
- Keep the change small and focused.
- Don't silence tools (`# noqa`, `# type: ignore`) or swallow errors with broad `except`.
- Run the existing tests with `pytest` before you submit.

Submit with `/submit` in Claude Code. Grading runs in GitHub Actions in this repo,
and your score appears in TensorLearn.
