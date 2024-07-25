# initialize_parameters.py

def get_initial_parameters():
    # 手动输入的初始数据
    params = {
        # 氢气生产量
        "production_quantity": 500,
        # 氢气运输量
        "transport_quantity": 300,
        # 绿氢的单位生产成本
        "unit_cost_green": 2.0,
        # SMR制氢的单位生产成本
        "unit_cost_smr": 1.8,
        # ATR制氢的单位生产成本
        "unit_cost_atr": 1.6,
        # CCS制氢的单位生产成本
        "unit_cost_ccs": 2.2,
        # 管道运输的单位运输成本
        "unit_cost_pipeline": 0.5,
        # 管道运输的距离
        "distance_pipeline": 100,
        # 汽车运输的单位运输成本
        "unit_cost_truck": 1.0,
        # 汽车运输的距离
        "distance_truck": 150,
        # 液氢罐车运输的单位运输成本
        "unit_cost_liquefied": 1.5,
        # 液氢罐车运输的距离
        "distance_liquefied": 200,
        # 成本分担比例（用于模型2）
        "cost_sharing_ratio": 0.3
    }
    return params

if __name__ == "__main__":
    params = get_initial_parameters()
    print(params)
