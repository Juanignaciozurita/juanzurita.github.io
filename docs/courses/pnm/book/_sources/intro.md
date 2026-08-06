---
title: Programming & Numerical Methods for Economics
subtitle: University of Edinburgh
---

# Programming & Numerical Methods for Economics

**University of Edinburgh -- School of Economics**\
**Instructor:** Juan Zurita

## About This Course

This course provides a practical introduction to programming and numerical methods for economics. Students learn to write Python code for data analysis, build economic models, and solve them computationally. The first half of the course covers Python fundamentals, data manipulation with pandas, and the transition from data to economic models. The second half introduces core numerical methods used in macroeconomics and computational economics: root-finding algorithms, numerical optimisation, function approximation, and dynamic programming via value function iteration.

The materials are designed to be self-contained and hands-on. Each week pairs a lecture notebook with worked examples, and lab exercises give students the opportunity to apply the techniques to realistic economic problems. The final module uses Julia to illustrate value function iteration for a neoclassical growth model, exposing students to a second scientific computing language widely used in quantitative economics.

## Prerequisites

- **Mathematics:** Calculus (single and multivariable), linear algebra, basic probability and statistics.
- **Economics:** Intermediate microeconomics and macroeconomics. Familiarity with constrained optimisation problems is helpful.
- **Programming:** No prior programming experience is required. The course starts from the basics.

## How to Use These Materials

### Run in Google Colab

The simplest way to work with the notebooks is to open them directly in Google Colab. Each notebook page includes a launch button (rocket icon) in the top toolbar -- click it and select **Colab** to open a live, runnable copy in your browser. No local installation is needed.

### Run locally

To run the notebooks on your own machine:

1. Install [Python 3.10+](https://www.python.org/downloads/) (or use [Anaconda](https://www.anaconda.com/download)).
2. Clone the course repository:
   ```bash
   git clone https://github.com/Juanignaciozurita/juanzurita.github.io.git
   ```
3. Install the required packages:
   ```bash
   pip install numpy scipy pandas matplotlib jupyter
   ```
4. Launch Jupyter:
   ```bash
   jupyter notebook
   ```
5. Navigate to the `courses/pnm/notebooks/` directory and open any notebook.

For the Julia notebook (Week 8), you will also need [Julia 1.9+](https://julialang.org/downloads/) and the IJulia kernel.

## Course Outline

| Week | Topic |
|------|-------|
| 1 | Introduction to Programming |
| 2 | Fundamentals of Programming in Python |
| 3 | Data Manipulation with pandas; Case Study |
| 4 | From Data to Models |
| 5 | Numerical Methods I: Root-Finding & Optimisation |
| 6 | Numerical Methods II: Optimisation in Economics |
| 7 | Numerical Methods III: Function Approximation; Examples |
| 8 | Economic Models: Value Function Iteration (Julia) |

## References

- Judd, K. L. (1998). *Numerical Methods in Economics*. MIT Press.
- Fernandez-Villaverde, J. *Computational Methods for Economists*. Lecture notes, University of Pennsylvania.
- Sargent, T. J. and J. Stachurski. [*QuantEcon*](https://quantecon.org/). Open-source lectures on quantitative economics.
- Miranda, M. J. and P. L. Fackler (2002). *Applied Computational Economics and Finance*. MIT Press.

## Contact

Juan Zurita\
School of Economics, University of Edinburgh\
Email: [juan.zurita@ed.ac.uk](mailto:juan.zurita@ed.ac.uk)\
GitHub: [github.com/Juanignaciozurita](https://github.com/Juanignaciozurita)
