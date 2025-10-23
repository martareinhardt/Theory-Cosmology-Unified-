import coupled_solver 
import analysis
import plot_results
import numpy as np

def main_execution_flow():
    print("--- Executando o Fluxo de Simulações do Modelo Unified-Theory (AAD) ---")

    # 1. Configurar Parâmetros (Use os parâmetros definidos no coupled_solver)
    # Exemplo: Importe diretamente as variáveis de configuração do solver
    initial_params = coupled_solver.params 
    Y0 = coupled_solver.Y0 
    t_span = coupled_solver.t_span 
    
    # 2. Definir Cenários de Teste (Análise)
    test_alphas = [0.0, 0.1, 0.5] 
    print(f"Testando coeficientes de acoplamento alpha: {test_alphas}")

    # 3. Rodar as Simulações e Comparar Resultados
    results_data = analysis.run_comparison(test_alphas, initial_params, Y0, t_span)
    
    # 4. Análise e Métricas (Exemplo)
    print("\n--- Resultados da Análise ---")
    for alpha_val, data in results_data.items():
        age = analysis.calculate_cosmic_age(data['t'], data['a'])
        print(f"Alpha={alpha_val}: Idade Cósmica Estimada = {age:.2f} unidades de tempo.")
        # Você pode adicionar mais métricas de análise aqui

    # 5. Visualização
    print("\n--- Gerando Gráficos de Resultados ---")
    plot_results.plot_cosmic_evolution(results_data[0.0], coupled_solver.H0) # Plota o cenário padrão
    analysis.plot_hubble_comparison(results_data) # Plota a comparação H(z)

    print("--- Simulação Concluída. Verifique os gráficos gerados. ---")

if __name__ == '__main__':
    # Certifique-se de que todas as dependências estão configuradas
    # (Ex: garantir que H0 e as funções de potencial estão definidas no coupled_solver)
    main_execution_flow()
