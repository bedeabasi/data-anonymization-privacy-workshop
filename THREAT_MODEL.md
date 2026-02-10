# Threat Model

This document defines the adversary assumptions, capabilities, and limitations used throughout the workshop.

All privacy analyses, attacks, and defenses are evaluated **within this threat model**.

---

## Why a Threat Model Matters

Privacy guarantees are **meaningless without assumptions**.

A method is not “secure” or “private” in isolation — it is secure **against a specific adversary** with defined capabilities.

This workshop explicitly models the adversary to:

- Avoid ambiguous claims
- Enable fair comparisons between methods
- Ground discussions in realistic scenarios

---

## Adversary Profile

We assume a **passive, data-centric adversary**.

The adversary:

- Has access to the released dataset or trained model
- Does **not** tamper with data generation
- Does **not** control the training process
- Operates offline (no adaptive query interface unless stated)

---

## Adversary Capabilities

The adversary **can**:

- Access auxiliary datasets from public or semi-public sources
- Perform arbitrary computation
- Apply statistical, machine learning, and linkage techniques
- Know the anonymization or privacy mechanism used
- Know all parameters **except random seeds**

This follows **Kerckhoffs’ principle**: security must not rely on secrecy of the method.

---

## Adversary Limitations

The adversary **cannot**:

- Access direct identifiers removed prior to release
- Observe internal randomness of mechanisms
- Modify the released dataset
- Query the system adaptively unless explicitly stated
- Compromise the data collection pipeline

---

## Data Assumptions

All datasets used in this workshop are:

- Synthetic
- Tabular unless stated otherwise
- Structured with direct identifiers removed

Sensitive attributes remain present to model realistic disclosure risk.

---

## Attack Goals

Depending on the session, the adversary may attempt to:

- Re-identify individuals
- Infer sensitive attributes
- Determine membership in a dataset
- Exploit distributional leakage
- Measure privacy loss empirically

Success is measured probabilistically — **not** by certainty.

---

## Defense Assumptions

Defensive mechanisms are assumed to:

- Be implemented correctly
- Follow standard definitions (e.g., k-anonymity, ε-DP)
- Use properly calibrated parameters
- Avoid undocumented heuristics

Incorrect implementations are treated as **failures**, not defenses.

---

## Out-of-Scope Threats

The following are **explicitly out of scope**:

- Side-channel attacks
- Timing attacks
- Hardware compromise
- Malicious data poisoning
- Insider threats
- Active adaptive querying systems

These threats are important but require separate analysis.

---

## Evaluation Philosophy

Privacy is evaluated using:

- Empirical attack success
- Theoretical guarantees (when applicable)
- Utility degradation
- Failure case analysis

No single metric is treated as definitive.

---

## Ethical Constraints

This workshop is for **education and research only**.

Participants must not:

- Apply attacks to real, personal, or proprietary data
- Use methods to bypass legal or ethical protections
- Misrepresent results or guarantees

All work should comply with institutional review and ethics guidelines.

---

## Final Note

If an attack succeeds, the system failed — not the user.

Understanding **why** it failed is the objective.

Privacy is a system property, not a feature.
