# initialize_parameters.py

def get_initial_parameters():
    # 初始化生产量和管道运输距离
    production_quantity = 2250  # 单位：千克
    distance_pipeline = 2500  # 单位：公里

    # 根据输入参数计算其他比例数据
    transport_quantity = production_quantity * 3 / 5  # 单位：千克
    distance_truck = distance_pipeline * 3 / 5  # 单位：公里
    distance_liquefied = distance_pipeline * 2.6 / 5  # 单位：公里

    # 手动输入的初始数据
    params = {
        # 氢气生产量，基于5:3的比例
        "production_quantity": production_quantity,  # 5部分
        # 氢气运输量
        "transport_quantity": transport_quantity,  # 3部分
        # 管道运输的距离5：3：2.6
        "distance_pipeline": distance_pipeline,  # 5部分
        # 汽车运输的距离
        "distance_truck": distance_truck,  # 3部分
        # 液氢罐车运输的距离
        "distance_liquefied": distance_liquefied,  # 2.6部分
        # 绿氢的单位生产成本，单位：元/千克
        "unit_cost_green": 31.56,
        # SMR制氢的单位生产成本，单位：元/千克
        "unit_cost_smr": 12.8,
        # ATR制氢的单位生产成本，单位：元/千克
        "unit_cost_atr": 12.8,
        # CCS制氢的单位生产成本，单位：元/千克
        "unit_cost_ccs": 9.75,
        # 管道运输的单位运输成本，单位：元/千克/公里
        "unit_cost_pipeline": 6.44,
        # 汽车运输的单位运输成本，单位：元/千克/公里
        "unit_cost_truck": 20.45,
        # 液氢罐车运输的单位运输成本，单位：元/千克/公里
        "unit_cost_liquefied": 13.79,
        # 绿氢的单位环境成本，单位：元/千克
        "unit_cost_environment_green": 0,
        # SMR制氢的单位环境成本，单位：元/千克
        "unit_cost_environment_smr": 0.84,
        # ATR制氢的单位环境成本，单位：元/千克
        "unit_cost_environment_atr": 0.84,
        # CCS制氢的单位环境成本，单位：元/千克
        "unit_cost_environment_ccs": 9.75,
        # 管道运输的单位环境成本，单位：元/千克/公里
        "unit_cost_environment_pipeline": 0.05,
        # 汽车运输的单位环境成本，单位：元/千克/公里
        "unit_cost_environment_truck": 74,
        # 液氢罐车运输的单位环境成本，单位：元/千克/公里
        "unit_cost_environment_liquefied": 132,
        # 直接资金补贴，单位：元/千克
        "subsidy_amount": 1.5,
        # 比例分担成本，百分比
        "cost_sharing_ratio": 0.2,  # 例如分担20%的成本
        # 绿色度补贴系数，单位：元/千克
        "green_subsidy_coefficient": 100,
        # 碳排放减少补贴，单位：元/吨CO2
        "carbon_emission_reduction": 0.5
    }

    return params

if __name__ == "__main__":
    params = get_initial_parameters()
    print(params)
