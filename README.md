
Theory Cosmology Unified

Author: Marta Reinhardt

License: Creative Commons Attribution 4.0 International (CC BY 4.0)


---

🪐 Overview

Theory Cosmology Unified is a structured cosmological framework that aims to unify the major epochs of the universe—from the primordial Big Bang to the ultimate cosmic asymptote—under a consistent mathematical and conceptual model.

This project combines theoretical cosmology, Friedmann dynamics, and numerical simulation to visualize and explore the evolution of the scale factor, energy densities, and cosmic transitions between radiation, matter, and dark energy domination.

Repository: https://github.com/martareinhardt/Theory-Cosmology-Unified-


---

🔭 Scientific Motivation

The model presented here follows an alphabetic cosmological taxonomy, organizing cosmic evolution into stages designated by Greek letters — from Alpha (the primordial origin) to Omega (the ultimate fate). Each stage introduces new physical components, equations, and symmetries extending the standard Friedmann–Lemaître–Robertson–Walker (FLRW) formulation.

Major Phases:

Symbol	Phase	Description

Alpha	Primordial Origin	Initial singularity; homogeneous and isotropic FLRW start.
Beta	Early Expansion	Radiation and matter-dominated eras; curvature and dark energy terms emerge.
Gamma	Structural Alignment	Growth of anisotropies and early structures.
Delta	Perturbations	Jeans instability and density fluctuation growth.
Epsilon	Dark Matter	Non-baryonic matter and gravitational halo formation.
Zeta	Dark Energy	Accelerated expansion; equation of state .
Eta → Omega	Advanced & Final Eras	Entropy growth, tensor modes, unification attempts, and asymptotic end states.


Each equation in the sequence generalizes the Friedmann equation:

\left( \frac{\dot{a}(t)}{a(t)} \right)^2 = \frac{8\pi G}{3} \rho(t) - \frac{k c^2}{a(t)^2} + \frac{\Lambda c^2}{3} + \text{perturbative terms}
## 🚀 Executando as Simulações do Modelo AAD

Para rodar o solver de acoplamento dinâmico e gerar os gráficos comparativos, siga os passos abaixo no seu terminal:

### 1. Pré-requisitos
Certifique-se de que você tem o Git e o Python (3.x) instalados.

### 2. Instalação (Clonar e Configurar)
```bash
git clone [https://github.com/martareinhardt/Theory-Cosmology-Unified-](https://github.com/martareinhardt/Theory-Cosmology-Unified-)
cd Theory-Cosmology-Unified-
pip install -r requirements.txt
python run_simulations.py




---

🧮 Numerical Simulation

The Python module provided implements the numerical integration of the Friedmann equation, computing the scale factor  and corresponding density components for radiation, matter, and dark energy.

Dependencies

pip install numpy scipy matplotlib

Running the Simulation

python cosmology_friedmann.py

Output

The script produces two primary plots:

Scale Factor vs. Time 

Density Evolution vs. Redshift 


Both
![Theory Cosmology Unified Banner](figures/banner_cosmology.png)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)]()
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)]()
[![Made with ❤️ by Marta Reinhardt](https://img.shields.io/badge/Made%20with%20%E2%9D%A4%EF%B8%8F-Marta%20Reinhardt-pink.svg)]()


