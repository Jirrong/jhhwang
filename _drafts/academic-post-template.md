---
title: "Post title"
description: "Summarize the question or main point in one or two sentences."
categories: [Study notes]
tags: [Chemistry]
lang: en
math: true
toc: true
---
Start with the question or context. This file is an unpublished writing template. To publish, move it to `_posts/YYYY-MM-DD-your-title.md` and add the corresponding date to the front matter.

<!--more-->

## Question

What is the question? Distinguish source results from your interpretation.

## Methods and conditions

Record methods, units, software versions, and assumptions where relevant.

## Equations

The following is a formatting example, not a research result:

$$
\Delta G = \Delta H - T\Delta S
$$

Use $\Delta G$ for an inline expression.

## Code

```python
# Illustrative arithmetic in kJ mol^-1.
enthalpy = -20.0
entropy = -0.05
temperature = 298.15
free_energy = enthalpy - temperature * entropy
print(f"Delta G = {free_energy:.2f} kJ mol^-1")
```

## Figures and tables

Upload a figure to `images/posts/`, then replace the path below and remove the comment.

{% raw %}
<!--
![Describe what the figure shows]({{ '/images/posts/your-figure.png' | relative_url }})
-->
{% endraw %}

| Condition | Method | Observation |
| :--- | :--- | :--- |
| A | Method and settings | Result with units |

## Interpretation and open questions

Explain what follows from the result and what still needs checking. Footnotes are supported.[^note]

[^note]: Additional context or a reference.

## References

1. Authors, *Title*, Journal, year. DOI or original URL.
