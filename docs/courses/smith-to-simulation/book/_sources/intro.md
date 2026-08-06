---
title: "From Smith to Simulation"
subtitle: "Computing the Ideas that Built Economics"
---

# From Smith to Simulation

**Computing the Ideas that Built Economics**

*University of Edinburgh -- School of Economics*

---

## Course Description

This ten-week course traces the intellectual history of economics from Adam
Smith's *Wealth of Nations* (1776) to Thomas Piketty's *Capital in the
Twenty-First Century* (2013), pairing each major idea with a computational
exercise in Python. Students will build working simulations of supply-and-demand
equilibria, Ricardian trade models, Marxian reproduction schemes, Keynesian
multipliers, Solow growth dynamics, rational-expectations economies, and
Markov-chain wealth distributions.

No prior programming experience is assumed. Each module introduces the
necessary Python tools -- arrays, plotting, optimisation, simulation -- as they
arise naturally from the economics.

By the end of the course, students will be able to:

- Explain the core contribution of each major school of economic thought.
- Translate verbal and mathematical economic arguments into executable code.
- Use simulation to test theoretical predictions and explore parameter sensitivity.
- Communicate quantitative findings through well-documented computational essays.

---

## How to Use These Materials

### Run in the cloud (recommended for beginners)

Every notebook can be launched directly in Google Colab -- look for the
**"Open in Colab"** badge at the top of each page. No local installation
required; just sign in with your University Google account.

### Run locally

1. Install [Anaconda](https://www.anaconda.com/download) (Python 3.11+).
2. Clone the repository:
   ```bash
   git clone https://github.com/Juanignaciozurita/juanzurita.github.io.git
   cd juanzurita.github.io/courses/smith-to-simulation
   ```
3. Create the course environment:
   ```bash
   conda create -n smith-sim python=3.11 numpy matplotlib scipy pandas jupyter
   conda activate smith-sim
   ```
4. Launch Jupyter:
   ```bash
   jupyter notebook
   ```

---

## Assessment

| Component              | Weight |
|------------------------|--------|
| Weekly quizzes         | 20%    |
| Computational essays   | 40%    |
| Final project          | 30%    |
| Participation          | 10%    |

**Weekly quizzes** test comprehension of both the economic ideas and the Python
concepts introduced each week.

**Computational essays** (three over the semester) ask students to extend a
module's model, run new experiments, and write up findings in a Jupyter
notebook combining code, visualisations, and narrative.

**Final project** is an independent computational investigation of an economic
question of the student's choosing, presented as a polished Jupyter notebook
with full documentation.

---

## References

- Smith, Adam. *An Inquiry into the Nature and Causes of the Wealth of Nations* (1776).
- Heilbroner, Robert L. *The Worldly Philosophers: The Lives, Times, and Ideas of the Great Economic Thinkers*. 7th ed., Simon & Schuster, 1999.
- Broadie, Alexander. *The Scottish Enlightenment: The Historical Age of the Historical Nation*. Birlinn, 2001.
- Romer, David. *Advanced Macroeconomics*. 5th ed., McGraw-Hill, 2018.
- Piketty, Thomas. *Capital in the Twenty-First Century*. Translated by Arthur Goldhammer, Harvard University Press, 2014.

---

## Contact

**Instructor:** Juan Zurita\
**Email:** [juan.zurita@ed.ac.uk](mailto:juan.zurita@ed.ac.uk)\
**Office hours:** By appointment
