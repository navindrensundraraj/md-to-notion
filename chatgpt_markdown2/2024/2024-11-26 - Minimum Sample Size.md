---
title: "Minimum Sample Size"
date: 2024-11-26
tags: [chatgpt, export]
---

# Minimum Sample Size

---
**User:**

What is the minimum sample size required for 0.17% reject rate

---
**Assistant:**

To determine the minimum sample size required for a reject rate of 0.17%, the calculation depends on the desired level of confidence (e.g., 95%) and margin of error (e.g., ±0.05%). Here’s the formula for sample size in proportion problems:

\[
n = \frac{Z^2 \cdot p \cdot (1-p)}{E^2}
\]

Where:
- \(n\): Minimum sample size
- \(Z\): Z-score (e.g., 1.96 for 95% confidence level)
- \(p\): Proportion (0.17% = 0.0017)
- \(E\): Margin of error (as a decimal, e.g., ±0.05% = 0.0005)

### Plugging in values:
- \(p = 0.0017\)
- \(Z = 1.96\)
- \(E = 0.0005\)

\[
n = \frac{(1.96)^2 \cdot 0.0017 \cdot (1 - 0.0017)}{(0.0005)^2}
\]

I can calculate this for you.

---
**Assistant:**

# Define the variables
Z = 1.96  # Z-score for 95% confidence level
p = 0.0017  # Proportion (0.17% as a decimal)
E = 0.0005  # Margin of error (0.05% as a decimal)

# Calculate the sample size
n = (Z**2 * p * (1 - p)) / (E**2)
n

---
**Tool:**

26078.471103999997

---
**Assistant:**

The minimum sample size required for a reject rate of 0.17% with a 95% confidence level and a margin of error of ±0.05% is approximately **26,079 samples**.
