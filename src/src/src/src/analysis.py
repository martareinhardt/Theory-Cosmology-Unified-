import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Assumindo que você tem seu sistema de equações e parâmetros definidos aqui ou importáveis
# from coupled_solver import system_of_equations, initial_params, Y0 

def calculate_cosmic_age(t_array, a_array, a_today=1.0):
    """Estima a idade do Universo (tempo onde a(t) = a_today)."""
    # Encontra o índice onde a é mais próximo de 1.0 (presente)
    idx = np.argmin(np.abs(a_array - a_today))
    return t_array[idx]

def calculate_weff(H, H_dot):
    """Calcula o parâmetro de equação de estado efetivo w_eff."""
    # w_eff = -1 - (2 * H_dot) / (3 * H**2)
    # Evita divisão por zero se H for muito pequeno
    return -1.0 - (2.0 * H_dot) / (3.0 * H**2 + 1e-10)

def calculate_redshift(a):
    """Calcula o redshift z a partir do fator de escala a, assumindo a_today=1."""
    return (1.0 / a) - 1.0

def run_comparison(alphas, initial_params, Y0, t_span):
    """Roda o solver para diferentes coeficientes de acoplamento alpha."""
    results = {}
    
    for alpha_val in alphas:
        # Cria a lista de parâmetros para este teste de alpha
        current_params = list(initial_params)
        
        # Encontra o índice de alpha no seu array de parâmetros
        # (Você precisa saber qual índice corresponde ao alpha no seu `initial_params`)
        alpha_index = 2 # Exemplo: assumindo que alpha é o 3º parâmetro
        current_params[alpha_index] = alpha_val
        
        # Resolve o sistema
        sol = solve_ivp(system_of_equations, t_span, Y0, args=(current_params,), method='RK45')
        
        # Armazena os resultados para análise
        H_dot = np.gradient(sol.y[1], sol.t) # Calcula a derivada de H (H_dot)
        
        results[alpha_val] = {
            't': sol.t,
            'a': sol.y[0],
            'H': sol.y[1],
            'phi': sol.y[2],
            'weff': calculate_weff(sol.y[1], H_dot)
        }
        
    return results

def plot_hubble_comparison(results):
    """Plota a taxa de Hubble H(z) para diferentes valores de alpha."""
    plt.figure(figsize=(10, 6))
    
    for alpha_val, data in results.items():
        z = calculate_redshift(data['a'])
        # Plota H(z) apenas para redshifts razoáveis (e.g., z < 5)
        mask = z < 5
        plt.plot(z[mask], data['H'][mask], label=f'Alpha = {alpha_val}')

    plt.xlabel('Redshift (z)')
    plt.ylabel('Taxa de Hubble H(z)')
    plt.title('Impacto do Acoplamento Dinâmico ($\alpha$) na Expansão')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    # --- Configuração de Teste (Valores Fictícios) ---
    # VOCÊ DEVE DEFINIR: system_of_equations, initial_params, Y0, t_span
    
    # Exemplo de Coeficientes para Comparação:
    test_alphas = [0.0, 0.1, 0.5] 
    
    # results_data = run_comparison(test_alphas, initial_params, Y0, t_span)
    
    # Exemplo de Análise:
    # age_lambda = calculate_cosmic_age(results_data[0.0]['t'], results_data[0.0]['a'])
    # age_alpha_high = calculate_cosmic_age(results_data[0.5]['t'], results_data[0.5]['a'])
    
    # print(f"Idade do Universo (Lambda CDM): {age_lambda}")
    # print(f"Idade do Universo (AAD Alpha=0.5): {age_alpha_high}")
    
    # plot_hubble_comparison(results_data)
    
    print("Módulo analysis.py pronto para rodar testes comparativos!")
  
