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
alpha_0 = 0.999;  % 调整冷却速率，使温度下降更平缓
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
results = {};
fitness_values = py.list();
iteration_step = 10; % 每次迭代步长

for i = 1:num_solutions
    solution = initial_solutions{i};
    fitness = py.calculate_fitness_model0.calculate_fitness_wrapper(solution, params);
    fitness_values.append(fitness);
    solution_str = char(py.json.dumps(solution));  % 将solution转换为字符串
    fprintf('Solution %d: %s, Fitness: %f\n', i, solution_str, fitness);
    % 将结果保存到results数组
    production_method = char(solution{'production_method'});
    transport_method = char(solution{'transport_method'});
    production_quantity = double(solution{'production_quantity'});
    transport_quantity = double(solution{'transport_quantity'});
    results = [results; {i, iteration_step * i, fitness, production_method, transport_method, production_quantity, transport_quantity}];
end

% 调用模拟退火萤火虫算法文件
optimal_solution = py.simulated_annealing_firefly_model0.run_simulated_annealing_firefly(initial_solutions, params, T_0, alpha);
disp('Optimal Solution:');
disp(optimal_solution);

% 调用目标函数健康检查文件
objective_values = py.list();  % 存储目标函数值
num_iterations = int32(1000);  % 确保是整数类型

% 计算当前最优解的适应度值
current_fitness = py.calculate_fitness_model0.calculate_fitness_wrapper(optimal_solution, params);

% 记录迭代过程中的适应度值
initial_iteration = num_solutions + 1; % 设置初始迭代为初始解集长度加一
for i = 1:num_iterations
    objective_values.append(current_fitness);
    iteration_values = initial_iteration + i - 1;
    fitness_over_iterations = current_fitness;
    
    % 每4次迭代监控一次目标函数的变化
    if mod(i, 4) == 0
        converged = py.objective_function_health_check.check_health(objective_values);
        if converged
            fprintf('Iteration: %d, Converged with Best Fitness: %f\n', initial_iteration + i - 1, current_fitness);
            results = [results; {initial_iteration + i - 1, (initial_iteration + i - 1) * iteration_step, current_fitness, char(optimal_solution{'production_method'}), char(optimal_solution{'transport_method'}), double(optimal_solution{'production_quantity'}), double(optimal_solution{'transport_quantity'})}];
            break;
        end
    end
    
    % 输出调试信息
    if mod(i, 10) == 0  % 每10次迭代输出调试信息
        fprintf('Iteration: %d, Current Best Fitness: %f, Temperature: %f\n', initial_iteration + i - 1, current_fitness, T_0 * alpha^i);
    end
    
    % 保存每次迭代的结果
    results = [results; {initial_iteration + i - 1, (initial_iteration + i - 1) * iteration_step, current_fitness, char(optimal_solution{'production_method'}), char(optimal_solution{'transport_method'}), double(optimal_solution{'production_quantity'}), double(optimal_solution{'transport_quantity'})}];
end

% 最终的迭代次数
total_iterations = initial_iteration + i - 1;

fprintf('Final Optimal Solution: %s\n', char(py.json.dumps(optimal_solution)));
fprintf('Total Iterations: %d\n', total_iterations);

% 将results转换为表格
resultsTable = cell2table(results, 'VariableNames', {'Iteration', 'Step', 'Fitness', 'ProductionMethod', 'TransportMethod', 'ProductionQuantity', 'TransportQuantity'});

% 确保所有列都是数值类型
% 确保 ProductionQuantity 是元胞数组
if ~iscell(resultsTable.ProductionQuantity)
    resultsTable.ProductionQuantity = num2cell(resultsTable.ProductionQuantity);
end
resultsTable.ProductionQuantity = cellfun(@double, resultsTable.ProductionQuantity);

% 确保 TransportQuantity 是元胞数组
if ~iscell(resultsTable.TransportQuantity)
    resultsTable.TransportQuantity = num2cell(resultsTable.TransportQuantity);
end
resultsTable.TransportQuantity = cellfun(@double, resultsTable.TransportQuantity);

% 确保 Fitness 是元胞数组
if ~iscell(resultsTable.Fitness)
    resultsTable.Fitness = num2cell(resultsTable.Fitness);
end
resultsTable.Fitness = cellfun(@double, resultsTable.Fitness);

% 在导出文件和获取当前时间之前提取生产量和管道运输距离
production_quantity_final = double(params{'production_quantity'});
distance_pipeline_final = double(params{'distance_pipeline'});

% 获取当前时间并格式化为字符串
currentTime = datetime('now', 'Format', 'yyyyMMdd_HHmmss');
filename = sprintf('../实验数据/model0/result_model0_生产量_%d_管道运输距离_%d_时间_%s.xlsx', production_quantity_final, distance_pipeline_final, char(currentTime));

% 导出数据到Excel
writetable(resultsTable, filename);
fprintf('Data has been written to %s\n', filename);

% 添加最终决策结果到Excel
final_solution = {'Final Optimal Solution', char(py.json.dumps(optimal_solution))};
iterations_info = {'Total Iterations', total_iterations};
final_data = [final_solution; iterations_info];
final_data_range = size(resultsTable, 1) + 2; % 确定写入的位置

% 写入最终决策结果到Excel
writecell(final_data, filename, 'Sheet', 1, 'Range', sprintf('A%d', final_data_range));

% 绘制适应度值的直方图
figure;
histogram(resultsTable.Fitness, 'Normalization', 'pdf');
title('Fitness Value Distribution - Histogram', 'FontSize', 14, 'FontWeight', 'bold', 'Color', 'k');
xlabel('Fitness', 'FontSize', 12, 'FontWeight', 'bold', 'Color', 'k');
ylabel('Probability Density', 'FontSize', 12, 'FontWeight', 'bold', 'Color', 'k');
grid on;

% 绘制适应度值的核密度估计图
figure;
ksdensity(resultsTable.Fitness);
title('Fitness Value Distribution - Kernel Density Estimate', 'FontSize', 14, 'FontWeight', 'bold', 'Color', 'k');
xlabel('Fitness', 'FontSize', 12, 'FontWeight', 'bold', 'Color', 'k');
ylabel('Density', 'FontSize', 12, 'FontWeight', 'bold', 'Color', 'k');
grid on;

% 绘制适应度值的箱线图
figure;
boxplot(resultsTable.Fitness, 'Colors', 'b', 'Symbol', 'o', 'Widths', 0.5);
title('Distribution of Fitness Values', 'FontSize', 14, 'FontWeight', 'bold', 'Color', 'k');
ylabel('Fitness', 'FontSize', 12, 'FontWeight', 'bold', 'Color', 'k');
grid on;
ylim([min(resultsTable.Fitness) - 0.1 * range(resultsTable.Fitness), max(resultsTable.Fitness) + 0.1 * range(resultsTable.Fitness)]);

% 绘制适应度值的热图
figure;
heatmapData = groupsummary(resultsTable, {'ProductionQuantity', 'TransportQuantity'}, 'mean', 'Fitness');
h = heatmap(heatmapData, 'ProductionQuantity', 'TransportQuantity', 'ColorVariable', 'mean_Fitness');
h.Title = 'Fitness Value Heatmap';
h.XLabel = 'Production Quantity';
h.YLabel = 'Transport Quantity';
colorbar;
grid on;

% 根据实验结果生成最佳匹配表格
optimalSolutions = [];
production_methods = unique(resultsTable.ProductionMethod);
transport_methods = unique(resultsTable.TransportMethod);
quantities = unique(resultsTable.TransportQuantity);

for p = 1:length(production_methods)
    for t = 1:length(transport_methods)
        for q = 1:length(quantities)
            subset = resultsTable(strcmp(resultsTable.ProductionMethod, production_methods{p}) & strcmp(resultsTable.TransportMethod, transport_methods{t}) & [resultsTable.TransportQuantity] == quantities(q), :);
            [~, minIdx] = min(subset.Fitness);
            if ~isempty(minIdx)
                optimalSolutions = [optimalSolutions; production_methods(p), transport_methods(t), quantities(q), subset.ProductionQuantity(minIdx), subset.TransportQuantity(minIdx), subset.Fitness(minIdx)];
            end
        end
    end
end

optimalSolutionsTable = array2table(optimalSolutions, 'VariableNames', {'ProductionMethod', 'TransportMethod', 'Quantity', 'ProductionQuantity', 'TransportQuantity', 'Fitness'});

% 获取当前时间并格式化为字符串
optimal_filename = sprintf('../实验数据/model0/optimal_solutions/生产量_%d_管道运输距离_%d_时间_%s.xlsx', production_quantity_final, distance_pipeline_final, char(currentTime));

% 将最佳匹配表格保存为Excel文件
writetable(optimalSolutionsTable, optimal_filename);
fprintf('Optimal solutions have been written to %s\n', optimal_filename);
