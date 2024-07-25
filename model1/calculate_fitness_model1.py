# calculate_fitness_model1.py

def calculate_fitness(production_method, production_quantity, transport_method, transport_quantity, params):
    # 计算生产成本
    production_cost = 0  # 初始化生产成本
    if production_method == 'Green':
        production_cost = params['unit_cost_green'] * production_quantity
    elif production_method == 'SMR':
        production_cost = params['unit_cost_smr'] * production_quantity
    elif production_method == 'ATR':
        production_cost = params['unit_cost_atr'] * production_quantity
    elif production_method == 'CCS':
        production_cost = params['unit_cost_ccs'] * production_quantity

    # 计算运输成本
    transport_cost = 0  # 初始化运输成本
    if transport_method == 'Pipeline':
        transport_cost = params['unit_cost_pipeline'] * params['distance_pipeline'] * transport_quantity
    elif transport_method == 'Truck':
        transport_cost = params['unit_cost_truck'] * params['distance_truck'] * transport_quantity
    elif transport_method == 'LiquefiedTruck':
        transport_cost = params['unit_cost_liquefied'] * params['distance_liquefied'] * transport_quantity

    # 计算总成本
    total_cost = production_cost + transport_cost
    
    return total_cost

def calculate_fitness_wrapper(solution, params):
    return calculate_fitness(
        solution['production_method'],
        solution['production_quantity'],
        solution['transport_method'],
        solution['transport_quantity'],
        params
    )

if __name__ == "__main__":
    from initialize_parameters import get_initial_parameters
    params = get_initial_parameters()
    initial_solution = {
        'production_method': 'Green',
        'production_quantity': 500,
        'transport_method': 'Pipeline',
        'transport_quantity': 300
    }
    fitness = calculate_fitness_wrapper(initial_solution, params)
    print(f"Initial Solution Fitness: {fitness}")
