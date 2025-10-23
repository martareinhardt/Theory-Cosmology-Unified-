import numpy as np
import matplotlib.pyplot as plt
from coupled_solver import system_of_equations, solve_ivp, params, Y0, t_span # Importe o solver

def plot_cosmic_evolution(sol, H0):
    """Gera gráficos da evolução cósmica do modelo AAD."""
    
    # Extração de dados da solução
    t = sol.t
    a = sol.y[0]
    H = sol.y[1]
    phi = sol.y[2]
    phi_dot = sol.y[3]
    
    # 1. Gráfico da Expansão: Fator de Escala a(t)
    plt.figure(figsize=(10, 6))
    plt.plot(t, a, label='Fator de Escala a(t)')
    plt.xlabel('Tempo Cósmico (t)')
    plt.ylabel('Fator de Escala (a)')
    plt.title('Evolução da Expansão do Universo (Modelo AAD)')
    plt.legend()
    plt.grid(True)
    plt.show()

    # 2. Gráfico da Evolução do Campo: phi(t)
    plt.figure(figsize=(10, 6))
    plt.plot(t, phi, label='Campo Escalar $\phi(t)$')
    plt.xlabel('Tempo Cósmico (t)')
    plt.ylabel('Valor do Campo ($\phi$)')
    plt.title('Evolução do Campo Dinâmico (Modulador dos Padrões Subatômicos)')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    # A maneira ideal seria rodar o solver aqui ou importá-lo já resolvido:
    
    # Exemplo: Chame a função solve_ivp do seu módulo coupled_solver
    # Solução = solve_ivp(..., ...)
    
    # Assumindo que você já tem o objeto 'sol' resolvido:
    # plot_cosmic_evolution(sol, H0)
    
    # OBS: Substitua 'sol' e 'H0' pelos valores reais do seu solver.
    print("Módulo plot_results.py pronto. Execute-o após rodar o coupled_solver.")

