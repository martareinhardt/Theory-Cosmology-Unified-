![Python](https://img.shields.io/badge/python-3.11-blue)
![Astropy](https://img.shields.io/badge/astropy-6.0+-green)
![Testes](https://github.com/martareinhardt/Theory-Cosmology-Unified-/actions/workflows/python_tests.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.11-blue) ![Status](https://img.shields.io/badge/status-active-success) 
![Build Status](https://github.com/martareinhardt/Theory-Cosmology-Unified-/actions/workflows/python_tests.yml/badge.svg)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

from ipywidgets import interact
@interact(alpha=(0.0, 0.1, 0.01))
def plot_hz(alpha):
    # Seu código de H(z) aqui
    plt.plot(z, H_seu); plt.show()

# 🪐 Theory Cosmology Unified

A numerical model to test hypotheses of **cosmological unification**, simulating the variation of physical constants over time.  
This project combines *theoretical physics*, *numerical analysis*, and *scientific visualization* in Python.

<p align="center">
  <img src="results/sample_cosmology_plot.png" width="500" alt="Cosmological Simulation Preview">
</p>

---

## 🚀 How to Run the Project

###  Clone the repository  

```bash
git clone https://github.com/martareinhardt/Theory-Cosmology-Unified-.git
cd Theory-Cosmology-Unified-
'''
pip install -r requirements.txt

'''
python run_simulations.py --example

'''
notebooks/example_simulation.ipynb

---
[Open in Colab](https://colab.research.google.com/github/martareinhardt/Theory-Cosmology-Unified-/blob/main/notebooks/example_simulation.ipynb)
>
├── run_simulations.py      # Main simulation script  
├── results/                # Generated plots and data  
├── notebooks/              # Interactive experiments (Jupyter)  
├── paper/                  # Scientific notes and drafts  
├── requirements.txt        # Project dependencies  
└── README.md               # This documentation file

```

## 📊 Scientific Goal

This project investigates:

Cosmological models with variable physical constants (e.g., H₀(t), G(t))

Expansion and energy density equations

Visualization of the temporal evolution of the observable universe


Partial results and visualizations are stored in the results/ folder and documented in paper/.

## 📚 References & Scientific Credits

The theoretical foundation of this project stands on the work of many brilliant scientists whose research and ideas have shaped modern cosmology and fundamental physics.

Special acknowledgment is due to:

Albert Einstein (1879–1955) – for the General Theory of Relativity, the cornerstone of modern cosmology.

Edwin Hubble (1889–1953) – for the observational evidence of an expanding Universe.

Stephen Hawking (1942–2018) – for his contributions to black hole thermodynamics and quantum cosmology.

Roger Penrose (1931–) – for his pioneering work in mathematical physics and spacetime singularities.

Alan Guth (1947–) – for the theory of cosmic inflation.

Andrei Linde (1948–) – for the development of the chaotic and eternal inflation models.

George Ellis (1939–) and Dennis Sciama (1926–1999) – for contributions to relativistic cosmology.

Planck Collaboration (2018) – for precision cosmological data and parameters.


This repository aims to unify theoretical insights and computational methods in cosmology, inspired by their legacy and guided by the ongoing quest to understand the Universe as a coherent whole.




## 🔭 Next Steps

Implement models with dynamic dark energy

Automate testing and code quality checks using GitHub Actions

Add scientific documentation in LaTeX or PDF format

Create an interactive web visualization with Plotly or Bokeh





## 🤝 Contributing

1. Fork this repository


2. Create a branch for your modification (git checkout -b feature/your-feature-name)


3. Commit your changes (git commit -m 'description of modification')


4. Submit a Pull Request 🚀



See also: CONTRIBUTING.md


---

📜 License

Licensed under Creative Commons Attribution (CC BY 4.0).
© 2025 Marta Reinhardt

---

