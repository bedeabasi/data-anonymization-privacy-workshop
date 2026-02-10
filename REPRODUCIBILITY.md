# Reproducibility Guidelines

This document defines the standards for producing reproducible results in this workshop.

All reported results must follow these guidelines.

---

## Why Reproducibility Matters

Privacy research is especially sensitive to:

- Randomness
- Implementation details
- Parameter choices

Without reproducibility, comparisons between methods are meaningless.

---

## Sources of Randomness

The following sources of randomness are present in this workshop:

- Dataset generation
- Sampling and shuffling
- Noise addition (e.g., differential privacy)
- Model initialization
- Train–test splits

All randomness **must be controlled** unless explicitly stated otherwise.

---

## Random Seed Policy

Unless instructed otherwise, use the following global seed:

```
SEED = 42
```

Seeds must be set for all relevant libraries, including:

- Python `random`
- NumPy
- Machine learning frameworks (when applicable)

Example (Python):

```python
import random
import numpy as np

SEED = 42
random.seed(SEED)
np.random.seed(SEED)
```

---

## Deterministic vs Stochastic Results

- **Deterministic methods** must produce identical outputs across runs
- **Stochastic methods** must report:
  - Mean performance
  - Variance or confidence intervals
  - Number of runs

Single-run stochastic results are **not sufficient**.

---

## Parameter Reporting

All experiments must report:

- Privacy parameters (e.g., `k`, `t`, `ε`)
- Dataset size
- Feature set used
- Attack configuration
- Evaluation metrics

Hidden parameters invalidate results.

---

## Result Storage

All results should be saved in structured form:

- Machine-readable (CSV, JSON)
- Versioned
- Timestamped

Plots must include:

- Axis labels
- Units
- Parameter values in captions

---

## Acceptable Variance

Small numeric differences are expected.

Large discrepancies require explanation, such as:

- Different library versions
- Hardware differences
- Changed random seeds
- Modified preprocessing

Unexplained variance is treated as an error.

---

## What Counts as a Valid Result

A result is valid if:

- The setup matches the documented environment
- The correct seed policy is followed
- Parameters are fully reported
- The attack or defense executes as intended

“Looks right” is not a validation criterion.

---

## Re-running Experiments

Before reporting results, you should be able to:

- Restart the kernel
- Re-run the notebook top to bottom
- Obtain statistically consistent outcomes

If this fails, the experiment is not reproducible.

---

## Final Principle

If someone else cannot reproduce your result using this repository and documentation, the result does not exist.

Reproducibility is part of correctness.
