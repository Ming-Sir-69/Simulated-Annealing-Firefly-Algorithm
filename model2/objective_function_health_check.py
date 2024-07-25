# objective_function_health_check.py

def check_health(objective_values, threshold=1e-2, window=40):
    """
    检查目标函数的健康状况，如果目标函数在最近的 window 次迭代中变化小于 threshold，则返回 True，否则返回 False。
    
    :param objective_values: list, 目标函数值的历史记录
    :param threshold: float, 判断收敛的阈值
    :param window: int, 滑动窗口大小
    :return: bool, 如果目标函数收敛，则返回 True，否则返回 False
    """
    if len(objective_values) < window:
        return False
    
    recent_values = objective_values[-window:]
    max_value = max(recent_values)
    min_value = min(recent_values)
    
    return (max_value - min_value) < threshold
