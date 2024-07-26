# initialize_parameters.py

def get_initial_parameters():
    # 手动输入的初始数据
    params = {
        # 氢气生产量，基于5:3的比例
        "production_quantity": 2250,  # 5部分
        # 氢气运输量，单次运输量设置为1350公斤
        "transport_quantity": 1350,  # 3部分
        # 绿氢的单位生产成本
        "unit_cost_green": 31.56,
        # SMR制氢的单位生产成本
        "unit_cost_smr": 12.8,
        # ATR制氢的单位生产成本
        "unit_cost_atr": 12.8,
        # CCS制氢的单位生产成本
        "unit_cost_ccs": 9.75,
        # 管道运输的单位运输成本
        "unit_cost_pipeline": 6.44,
        # 汽车运输的单位运输成本
        "unit_cost_truck": 20.45,
        # 液氢罐车运输的单位运输成本
        "unit_cost_liquefied": 13.79,
        # 管道运输的距离
        "distance_pipeline": 500,  # 这里假设为500公里
        # 汽车运输的距离
        "distance_truck": 300,  # 这里假设为300公里
        # 液氢罐车运输的距离
        "distance_liquefied": 260,  # 这里假设为260公里
        # 绿氢的单位环境成本
        "unit_cost_environment_green": 0,
        # SMR制氢的单位环境成本
        "unit_cost_environment_smr": 0.84,
        # ATR制氢的单位环境成本
        "unit_cost_environment_atr": 0.84,
        # CCS制氢的单位环境成本
        "unit_cost_environment_ccs": 9.75,
        # 管道运输的单位环境成本
        "unit_cost_environment_pipeline": 0.05,
        # 汽车运输的单位环境成本
        "unit_cost_environment_truck": 74,
        # 液氢罐车运输的单位环境成本
        "unit_cost_environment_liquefied": 132
    }
    return params

if __name__ == "__main__":
    params = get_initial_parameters()
    print(params)
