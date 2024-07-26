% matlab_script_model1.m

% 设置Python环境
pyenv('Version', 'D:\Program Files\Python311\python.exe');

% 调用初始化参数文件
params = py.initialize_parameters.get_initial_parameters();

% 调用生成初始解集文件
initial_solutions = py.generate_initial_solutions.generate_initial_solutions(params);

% 获取初始解集的长度
num_solutions = int32(length(initial_solutions));  % 确保是整数类型

% 调用自适应初始温度调整文件
target_acceptance_rate = 0.66;
T_0 = py.adaptive_initial_temperature.adaptive_initial_temperature(num_solutions, target_acceptance_rate, params);
fprintf('Adjusted Initial Temperature: %f\n', T_0);

% 调用自适应冷却速率调整文件
alpha_0 = 0.995;  % 调整冷却速率，使温度下降更平缓
r_min = 0.1;
r_max = 0.9;
current_acceptance_rate = 0.5;
t = int32(10);  % 确保是整数类型
N = int32(100);  % 确保是整数类型
d = int32(500);  % 确保是整数类型
D_max = int32(1000);  % 确保是整数类型
alpha = py.adaptive_cooling_rate.adaptive_cooling_rate(alpha_0, r_min, r_max, current_acceptance_rate, t, N, d, D_max);
fprintf('Adjusted Cooling Rate: %f\n', alpha);

% 计算适应度
fitness_values = py.list();
for i = 1:num_solutions
    solution = initial_solutions{i};
    fitness = py.calculate_fitness_model1.calculate_fitness_wrapper(solution, params);
    fitness_values.append(fitness);
    solution_str = char(py.json.dumps(solution));  % 将solution转换为字符串
    fprintf('Solution %d: %s, Fitness: %f\n', i, solution_str, fitness);
end

% 调用模拟退火萤火虫算法文件
optimal_solution = py.simulated_annealing_firefly_model1.run_simulated_annealing_firefly(initial_solutions, params, T_0, alpha);
disp('Optimal Solution:');
disp(optimal_solution);

% 调用目标函数健康检查文件
objective_values = py.list();  % 存储目标函数值
num_iterations = int32(1000);  % 确保是整数类型

% 计算当前最优解的适应度值
current_fitness = py.calculate_fitness_model1.calculate_fitness_wrapper(optimal_solution, params);

for i = 1:num_iterations
    objective_values.append(current_fitness);
    
    % 每4次迭代监控一次目标函数的变化
    if mod(i, 4) == 0
        converged = py.objective_function_health_check.check_health(objective_values);
        if converged
            fprintf('Iteration: %d, Converged with Best Fitness: %f\n', i, current_fitness);
            break;
        end
    end
    
    % 输出调试信息
    if mod(i, 10) == 0  % 每10次迭代输出调试信息
        fprintf('Iteration: %d, Current Best Fitness: %f, Temperature: %f\n', i, current_fitness, T_0 * alpha^i);
    end
end

fprintf('Final Optimal Solution: %s\n', char(py.json.dumps(optimal_solution)));
fprintf('Total Iterations: %d\n', i);
