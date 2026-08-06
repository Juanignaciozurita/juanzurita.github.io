---
title: Deep Learning for Macroeconomics
subtitle: University of Edinburgh
---

# Deep Learning for Macroeconomics

**University of Edinburgh**

## About this course

Modern macroeconomic models -- featuring high-dimensional state spaces,
occasionally binding constraints, and heterogeneous agents -- routinely
exceed the reach of traditional numerical methods such as value-function
iteration on discrete grids. This course introduces deep learning as a
practical tool for solving, simulating, and estimating these models. Starting
from the link between classical function approximation and neural networks,
we build up to deep equilibrium networks (DEQNs) that enforce economic
equilibrium conditions directly inside the training loop, and to
physics-informed neural networks (PINNs) that embed differential-equation
structure into the loss function.

By the end of the ten weeks, students will be able to implement neural-network
solvers for stochastic growth models, Aiyagari-type heterogeneous-agent
economies, and models with inequality constraints. The course also covers
surrogate-assisted estimation, climate--economy integrated assessment models,
and the current research frontier connecting deep learning with structural
macroeconometrics.

## Prerequisites

Students should have completed **Programming for Numerical Methods (PNM)** or
an equivalent course covering:

- Python programming (NumPy, basic plotting)
- Function approximation (polynomials, splines)
- Value-function iteration and policy-function iteration
- Basic optimisation (gradient descent, Newton's method)

No prior experience with deep learning frameworks is required; PyTorch will be
introduced from scratch in Week 1.

## How to use these materials

Each week's notebook is self-contained and can be run in two ways:

1. **Google Colab** (recommended for most students) -- click the
   "Open in Colab" badge at the top of each notebook. No local installation is
   needed.
2. **Local installation** -- clone the repository and install the dependencies:

   ```bash
   git clone https://github.com/Juanignaciozurita/juanzurita.github.io.git
   cd juanzurita.github.io/courses/dlmacro
   pip install torch numpy matplotlib jupyter
   ```

## A note on compute

Weeks 1--4 run comfortably on a laptop CPU. **Weeks 5--8** train larger
networks and benefit significantly from GPU acceleration. If you do not have a
local GPU, switch your Colab runtime to **GPU** (Runtime > Change runtime type
> T4 GPU). Week 9 (surrogate estimation) can be CPU-only but is faster on GPU.
Week 10 is discussion-oriented and does not require heavy computation.

## References

- Scheidegger, S. (2025). *Deep Learning in Economics*. Cambridge University
  Press.
- Azinovic, M., Gaegauf, L., & Scheidegger, S. (2022). Deep equilibrium nets.
  *International Economic Review*, 63(4), 1471--1525.
- Fernandez-Villaverde, J., Hurtado, S., & Nuno, G. (2023). Financial frictions
  and the wealth distribution. *Econometrica*, 91(5), 1843--1886.
- QuantEcon (https://quantecon.org) -- open-source lectures on computational
  economics.
- Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. MIT
  Press.

## Contact

Juan Zurita\
University of Edinburgh\
[juan.zurita@ed.ac.uk](mailto:juan.zurita@ed.ac.uk)
