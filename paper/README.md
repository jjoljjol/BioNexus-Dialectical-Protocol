# Manuscript & Reproducibility Assets

This directory contains the source files and high-resolution figures for the paper:

> **"The Dialectical Protocol: Self-Evolving AI via Bio-Inspired Vibe Coding and Adversarial Agent Synthesis"**

## 📂 Contents

- `manuscript/`: LaTeX source files (`.tex`, `.bib`, `sections/`).
- `figures/`: High-resolution figures (Fig 1-5) as used in the submission.
- `tables/`: Supplementary technical tables.

## 📄 Submission Information

- **Target Journal**: IEEE Transactions on Neural Networks and Learning Systems (TNNLS).
- **Status**: Submitted.
- **Reference URL**: [Link to pre-print if available].

## 🔬 Reproducing Figures

To regenerate the figures using the latest evolutionary data, run:
```bash
python scripts/generate_figures.py --input results/ --output paper/figures/
```
