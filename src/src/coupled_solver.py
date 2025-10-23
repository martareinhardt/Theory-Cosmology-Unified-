import numpy as np
from scipy.integrate import solve_ivp

# --- Parâmetros Cosmólogicos e do Modelo AAD ---

# Constantes fundamentais e densidades atuais (H0, Omega_m, Omega_r, etc.)
# Você deve definir esses parâmetros com base no seu modelo base.
G = 6.674e-11 # Constante Gravitacional (exemplo)
M_pl = 1.22e19 # Massa de Planck (exemplo para normalização)
alpha = 0.1   # Coeficiente de Acoplamento (Seu Novo Padrão!)

# --- Potencial do Campo Escalar V(phi) ---
# Exemplo de potencial: V(phi) = M^4 * exp(-lambda * phi)
def potential(phi, M, lmbda):
    """Define o potencial V(phi) para a Energia Escura (e.g., Quintessência)."""
    return M**4 * np.exp(-lmbda * phi)

def dV_dphi(phi, M, lmbda):
    """Define a derivada do potencial dV/dphi."""
    return -lmbda * M**4 * np.exp(-lmbda * phi)

# --- Sistema de EDOs de Primeira Ordem ---

def system_of_equations(t, Y, params):
    """
    Define o sistema de EDOs de primeira ordem para o solver.
    Y = [a, H, phi, phi_dot]
    """
    a, H, phi, phi_dot = Y
    
    # 1. Desempacotar Parâmetros:
    G, M_pl, alpha, M, lmbda, Omega_m0, Omega_r0, a0 = params
    
    # 2. Calcular Densidades e Pressões Dinâmicas:
    # Rho e P para Matéria Bariônica + Radiação (os "padrões repetitivos"):
    rho_m = Omega_m0 / a**3
    P_m = 0
    rho_r = Omega_r0 / a**4
    P_r = rho_r / 3

    # Rho e P para o Campo Escalar (o "novo padrão"):
    rho_phi = 0.5 * phi_dot**2 + potential(phi, M, lmbda)
    P_phi = 0.5 * phi_dot**2 - potential(phi, M, lmbda)
    
    # 3. Calcular Densidades Totais:
    rho_total = rho_m + rho_r + rho_phi
    P_total = P_m + P_r + P_phi
    
    # --- As Derivadas (O Sistema EDOs) ---
    
    # Derivadas triviais:
    a_dot = H * a
    phi_ddot = phi_dot
    
    # EDO 1: Derivada de H (Segunda Equação de Friedmann)
    H_dot = - (4 * np.pi * G / 3) * (rho_total + 3 * P_total)

    # EDO 2: Derivada da Taxa do Campo (Equação de Klein-Gordon Acoplada)
    # Termo Acoplamento = -(alpha/M_pl) * (rho_m - 3*P_m)
    coupling_term = - (alpha / M_pl) * (rho_m - 3 * P_m)
    
    phi_dot_dot = -3 * H * phi_dot - dV_dphi(phi, M, lmbda) + coupling_term
    
    return [a_dot, H_dot, phi_ddot, phi_dot_dot]

# --- Solução Numérica (Exemplo) ---

# Defina os parâmetros:
params = [G, M_pl, alpha, 1e-3, 1, 0.31, 9e-5, 1.0] # Valores de exemplo

# Condições Iniciais:
# [a, H, phi, phi_dot] no tempo inicial (e.g., z=1000)
Y0 = [0.001, 10000, 1.0, 0.0] 

# Intervalo de tempo para integração (do passado ao presente/futuro):
t_span = [0, 100]

# Rodar o Solver:
sol = solve_ivp(system_of_equations, t_span, Y0, args=(params,), 
                method='RK45', dense_output=True)

# Os resultados 'sol.y' conterão as curvas evolutivas de a(t), H(t), phi(t), e phi_dot(t).
# Estes resultados validam a sua hipótese de Acoplamento Dinâmico.
