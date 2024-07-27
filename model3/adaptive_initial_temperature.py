# adaptive_initial_temperature.py

import numpy as np
from calculate_fitness_model3 import calculate_fitness

def adaptive_initial_temperature(num_solutions, target_acceptance_rate, params, tolerance=0.01):
    initial_temperature = 5000  # 初始猜测的温度
    current_acceptance_rate = 0
    
    production_methods = ['Green', 'SMR', 'ATR', 'CCS']
    transport_methods = ['Pipeline', 'Truck', 'LiquefiedTruck']
    
    while abs(current_acceptance_rate - target_acceptance_rate) > tolerance:
        accepted_count = 0
        solutions = []
        
        for _ in range(num_solutions):
            production_method = np.random.choice(production_methods)
            transport_method = np.random.choice(transport_methods)
            production_quantity = np.random.uniform(100, 1000)
            transport_quantity = np.random.uniform(100, 1000)
            
            solution = {
                'production_method': production_method,
                'transport_method': transport_method,
                'production_quantity': production_quantity,
                'transport_quantity': transport_quantity
            }
            solutions.append(solution)
        
        for solution in solutions:
            old_fitness = calculate_fitness(
                solution['production_method'],
                solution['production_quantity'],
                solution['transport_method'],
                solution['transport_quantity'],
                params
            )
            new_solution = {
                'production_method': np.random.choice(production_methods),
                'transport_method': np.random.choice(transport_methods),
                'production_quantity': np.random.uniform(100, 1000),
                'transport_quantity': np.random.uniform(100, 1000)
            }
            new_fitness = calculate_fitness(
                new_solution['production_method'],
                new_solution['production_quantity'],
                new_solution['transport_method'],
                new_solution['transport_quantity'],
                params
            )
            if new_fitness < old_fitness or np.random.rand() < np.exp((old_fitness - new_fitness) / initial_temperature):
                accepted_count += 1
        
        current_acceptance_rate = accepted_count / num_solutions
        
        if current_acceptance_rate < target_acceptance_rate:
            initial_temperature *= 1.5  # 增大初始温度，更多解被接受，迭代次数增加
        else:
            initial_temperature *= 0.9  # 减小初始温度，较少解被接受，迭代次数减少
    
    return initial_temperature

if __name__ == "__main__":
    from initialize_parameters import get_initial_parameters
    params = get_initial_parameters()

    #！！！ 增大 增加解的多样性，可能需要更多迭代来收敛！！！
    num_solutions = 1000  
    
    #！！！ 增大  会接受更多较差解，温度增加，迭代次数增加！！！
    target_acceptance_rate = 0.9  
    T_0 = adaptive_initial_temperature(num_solutions, target_acceptance_rate, params)
    print(f"Adjusted Initial Temperature: {T_0}")
