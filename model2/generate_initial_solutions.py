# generate_initial_solutions.py

import numpy as np

def generate_initial_solutions(params):
    initial_solutions = []
    production_methods = ['Green', 'SMR', 'ATR', 'CCS']
    transport_methods = ['Pipeline', 'Truck', 'LiquefiedTruck']

    for prod_method in production_methods:
        for trans_method in transport_methods:
            solution = {
                'production_method': prod_method,
                'transport_method': trans_method,
                'production_quantity': params['production_quantity'],  # 固定生产量
                'transport_quantity': params['transport_quantity']     # 固定运输量
            }
            initial_solutions.append(solution)
    
    return initial_solutions

if __name__ == "__main__":
    from initialize_parameters import get_initial_parameters
    params = get_initial_parameters()
    initial_solutions = generate_initial_solutions(params)
    for i, solution in enumerate(initial_solutions):
        print(f"Solution {i + 1}: {solution}")
