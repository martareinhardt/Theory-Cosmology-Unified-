import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

Parâmetros cosmológicos (Planck 2018)

H0 = 67.74  # km/s/Mpc — usaremos unidades normalizadas (H0 = 1)
Omega_m0 = 0.3089
Omega_L0 = 0.6911
Omega_r0 = 9.04e-5  # radiação (fótons + neutrinos)

Função para a equação de Friedmann: da/dt / a = H(a)

def H(a):
return np.sqrt(Omega_r0 / a4 + Omega_m0 / a3 + Omega_L0)

Equação diferencial: da/dt = a * H(a)

def da_dt(a, t):
return a * H(a)

Tempo (em unidades de 1/H0)

t = np.linspace(1e-10, 2.0, 1000)  # de t~0 até o futuro

Condição inicial: a(0) ≈ 0 → usar valor pequeno

a0 = 1e-10

Integra numericamente a(t)

a = odeint(da_dt, a0, t)[:, 0]

Calcula densidades vs. a (ou z = 1/a - 1)

z = 1 / a - 1
rho_r = Omega_r0 / a4
rho_m = Omega_m0 / a3
rho_L = Omega_L0 * np.ones_like(a)

Redshifts de transição

z_rm = Omega_m0 / Omega_r0 - 1       # radiação-matéria (~3400)
z_mL = (Omega_L0 / Omega_m0)**(1/3) - 1  # matéria-energia escura (~0.33)

---------- PLOTS ----------

fig, ax = plt.subplots(2, 1, figsize=(10, 8))

Plot 1: a(t)

ax[0].plot(t, a)
ax[0].set_xlabel('Tempo normalizado (t * H0)')
ax[0].set_ylabel('Fator de escala a(t)')
ax[0].set_title('Evolução do Fator de Escala a(t)')
ax[0].grid(True)

Plot 2: Densidades vs z

ax[1].semilogx(z, rho_r, label='Radiacao (Omega_r / a^4)')
ax[1].semilogx(z, rho_m, label='Materia (Omega_m / a^3)')
ax[1].semilogx(z, rho_L, label='Energia Escura (Omega_L)')
ax[1].axvline(z_rm, color='r', linestyle='--', label=f'Transicao Rad-Mat (z≈{z_rm:.0f})')
ax[1].axvline(z_mL, color='g', linestyle='--', label=f'Transicao Mat-DE (z≈{z_mL:.2f})')
ax[1].set_xlabel('Redshift z')
ax[1].set_ylabel('Densidades Normalizadas')
ax[1].set_title('Transicoes de Eras: Densidades vs Redshift')
ax[1].legend()
ax[1].grid(True)
ax[1].set_xlim(1e-1, 1e4)

plt.tight_layout()
plt.show()

---------- RESULTADOS ----------

print(f"Transicao Radiacao–Materia: z ≈ {z_rm:.0f}")
print(f"Transicao Materia–Energia Escura: z ≈ {z_mL:.2f}")

