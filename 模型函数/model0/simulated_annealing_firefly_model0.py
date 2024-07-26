# simulated_annealing_firefly_model1.py

import numpy as np
from calculate_fitness_model0 import calculate_fitness_wrapper
from adaptive_initial_temperature import adaptive_initial_temperature
from adaptive_cooling_rate import adaptive_cooling_rate
from objective_function_health_check import check_health
from generate_initial_solutions import generate_initial_solutions

def run_simulated_annealing_firefly(initial_solutions, params, T_0, alpha):
    num_iterations = 1000  # 最大迭代次数
    best_solution = None
    best_fitness = float('inf')
    
    current_temperature = T_0
    iteration = 0
    objective_values = []

    while iteration < num_iterations:
        for solution in initial_solutions:
            current_fitness = calculate_fitness_wrapper(solution, params)
            
            # 生成新的解，仅更新运输方式和制氢方式，保持生产量和运输量不变
            new_solution = {
                'production_method': np.random.choice(['Green', 'SMR', 'ATR', 'CCS']),
                'transport_method': np.random.choice(['Pipeline', 'Truck', 'LiquefiedTruck']),
                'production_quantity': solution['production_quantity'],  # 固定生产量
                'transport_quantity': solution['transport_quantity']   # 固定运输量
            }
            new_fitness = calculate_fitness_wrapper(new_solution, params)
            if new_fitness < current_fitness or np.random.rand() < np.exp((current_fitness - new_fitness) / current_temperature):
                solution.update(new_solution)
                current_fitness = new_fitness
                if current_fitness < best_fitness:
                    best_fitness = current_fitness
                    best_solution = solution
        
        # 记录当前最优适应度值
        objective_values.append(best_fitness)
        
        # 调整温度
        current_temperature = current_temperature * alpha
        iteration += 1

        # 增加对目标函数变化的监控
        if iteration % 4 == 0:  # 每4次迭代监控一次
            converged = check_health(objective_values, threshold=1e-4, window=200)  # 增加阈值并扩大窗口大小
            if converged:
                print(f"Iteration: {iteration}, Converged with Best Fitness: {best_fitness}")
                break

        
        # 输出调试信息
        if iteration % 10 == 0:  # 每10次迭代输出调试信息
            print(f"Iteration: {iteration}, Current Best Fitness: {best_fitness}, Temperature: {current_temperature}")

    print(f'Total Iterations: {iteration}')
    return best_solution

if __name__ == "__main__":
    from initialize_parameters import get_initial_parameters
    params = get_initial_parameters()
    initial_solutions = generate_initial_solutions(params)

    # 调用自适应初始温度调整函数
    num_solutions = len(initial_solutions)
    target_acceptance_rate = 0.66
    T_0 = adaptive_initial_temperature(num_solutions, target_acceptance_rate, params)
    
    # 调用自适应冷却速率调整函数
    alpha_0 = 0.95
    r_min = 0.1
    r_max = 0.9
    current_acceptance_rate = 0.5
    t = 10
    N = 100
    d = 500
    D_max = 1000
    alpha = adaptive_cooling_rate(alpha_0, r_min, r_max, current_acceptance_rate, t, N, d, D_max)

    best_solution = run_simulated_annealing_firefly(initial_solutions, params, T_0, alpha)
    print('Optimal Solution:')
    print(best_solution)
