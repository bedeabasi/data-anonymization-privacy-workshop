# Workshop Session Index

This document outlines the structure, goals, and expected outcomes of each workshop session.

Sessions are designed to be completed **in order**.

---

## Session 1: Re-identification Attacks

**Notebook:**  
```
notebooks/session1_reidentification.ipynb
```

### Objectives
By the end of this session, you will be able to:

- Understand quasi-identifiers and linkage attacks
- Perform basic record linkage using auxiliary data
- Measure re-identification risk
- Explain why naïve anonymization fails

### Key Concepts
- Direct identifiers vs quasi-identifiers
- Linkage attacks
- Uniqueness
- Adversary background knowledge

### Output
- Re-identification rate
- Risk metrics
- Discussion of failure modes

---

## Session 2: k-Anonymity and Extensions

**Notebook:**  
```
notebooks/session2_k_anonymity.ipynb
```

### Objectives
By the end of this session, you will be able to:

- Implement k-anonymity
- Apply generalization and suppression
- Evaluate privacy vs utility tradeoffs
- Identify homogeneity and background knowledge attacks

### Key Concepts
- k-anonymity
- Generalization hierarchies
- Suppression
- Attribute disclosure

### Output
- k-anonymized dataset
- Utility metrics
- Attack demonstration

---

## Session 3: t-Closeness and Distributional Privacy

**Notebook:**  
```
notebooks/session3_t_closeness.ipynb
```

### Objectives
By the end of this session, you will be able to:

- Explain why k-anonymity is insufficient
- Apply t-closeness constraints
- Compare distributional distance metrics
- Analyze residual disclosure risk

### Key Concepts
- t-closeness
- Earth Mover’s Distance
- Distribution leakage
- Group privacy

### Output
- t-close dataset
- Distance metrics
- Comparative analysis

---

## Session 4: Differential Privacy (Mechanisms)

**Notebook:**  
```
notebooks/session4_differential_privacy.ipynb
```

### Objectives
By the end of this session, you will be able to:

- Define ε-differential privacy
- Apply Laplace and Gaussian mechanisms
- Calibrate noise correctly
- Reason about privacy budgets

### Key Concepts
- ε (epsilon)
- Sensitivity
- Composition
- Privacy loss

### Output
- Noisy query results
- Accuracy vs privacy plots

---

## Session 5: Privacy Attacks on ML Models

**Notebook:**  
```
notebooks/session5_membership_inference.ipynb
```

### Objectives
By the end of this session, you will be able to:

- Execute membership inference attacks
- Interpret attack accuracy
- Understand memorization in ML models
- Connect model behavior to privacy risk

### Key Concepts
- Membership inference
- Overfitting
- Shadow models
- Adversarial evaluation

### Output
- Attack accuracy
- ROC curves
- Risk interpretation

---

## Session 6: Defenses and Practical Tradeoffs

**Notebook:**  
```
notebooks/session6_defenses.ipynb
```

### Objectives
By the end of this session, you will be able to:

- Apply differential privacy to learning
- Compare anonymization vs DP
- Identify real-world deployment constraints
- Make defensible privacy design decisions

### Key Concepts
- DP-SGD
- Utility degradation
- Policy constraints
- System-level privacy

### Output
- Defended model
- Comparative evaluation
- Final discussion

---

## Expectations

- Sessions build on each other — do not skip ahead
- Run notebooks top to bottom
- Read markdown explanations carefully
- Be prepared to explain *why* an approach fails

Understanding failure is the goal.

---

## Completion Criteria

You have successfully completed the workshop if you can:

- Explain at least one privacy failure mode
- Demonstrate one attack
- Justify a privacy defense choice
- Articulate tradeoffs clearly

---

This workshop emphasizes **thinking like an adversary** and **designing like a defender**.
