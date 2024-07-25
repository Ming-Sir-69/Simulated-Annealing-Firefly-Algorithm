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
        # 绿氢的单位环境成本
        "unit_cost_environment_green": 0.1,
        # SMR制氢的单位环境成本
        "unit_cost_environment_smr": 0.4,
        # ATR制氢的单位环境成本
        "unit_cost_environment_atr": 0.3,
        # CCS制氢的单位环境成本
        "unit_cost_environment_ccs": 0.2,
        # 管道运输的单位环境成本
        "unit_cost_environment_pipeline": 0.05,
        # 汽车运输的单位环境成本
        "unit_cost_environment_truck": 0.2,
        # 液氢罐车运输的单位环境成本
        "unit_cost_environment_liquefied": 0.3,
        # 绿色度补贴系数
        "green_subsidy_coefficient": 100,
        # 碳排放减少量
        "carbon_emission_reduction": 0.5
    }
    return params

if __name__ == "__main__":
    params = get_initial_parameters()
    print(params)
