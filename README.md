# Research on Government Subsidies and Hydrogen Energy Supply Chain Based on Simulated Annealing Firefly Algorithm

## Introduction

This repository contains the research and implementation of a study on government subsidies and the hydrogen energy supply chain, utilizing the Simulated Annealing Firefly Algorithm. The project aims to optimize the hydrogen energy supply chain by considering various factors such as production costs, transportation costs, environmental costs, and government subsidies.

## Research Background

Hydrogen energy is a promising alternative to fossil fuels due to its high energy density and environmental benefits. However, the production and distribution of hydrogen involve significant costs and logistical challenges. Government subsidies play a crucial role in promoting the adoption of hydrogen energy by offsetting some of these costs.

This research focuses on three key models to analyze and optimize the hydrogen energy supply chain:

1. **Model 1**: Examines the production and transportation costs.
2. **Model 2**: Incorporates cost-sharing ratios.
3. **Model 3**: Integrates environmental costs and government subsidies.

The Simulated Annealing Firefly Algorithm is used to find optimal solutions for these models, balancing cost efficiency and environmental impact.

## Project Structure

The project is organized into the following directories and files:

```

模型函数/
├── model0/  # 模型0专用文件夹
│   ├── __pycache__/  # Python 缓存文件夹
│   ├── adaptive_cooling_rate.py  # 自适应冷却速率调整
│   ├── adaptive_initial_temperature.py  # 自适应初始温度调整
│   ├── calculate_fitness_model0.py  # 适用于模型0的适应度计算文件
│   ├── generate_initial_solutions.py  # 生成初始解集
│   ├── initialize_parameters.py  # 参数初始化
│   ├── matlab_script_model0.m  # 适用于模型0的MATLAB脚本
│   ├── objective_function_health_check.py  # 目标函数健康检查
│   └── simulated_annealing_firefly_model0.py  # 适用于模型0的模拟退火萤火虫算法文件
│
├── model1/  # 模型1专用文件夹
│   ├── __pycache__/  # Python 缓存文件夹
│   ├── adaptive_cooling_rate.py  # 自适应冷却速率调整
│   ├── adaptive_initial_temperature.py  # 自适应初始温度调整
│   ├── calculate_fitness_model1.py  # 适用于模型1的适应度计算文件
│   ├── generate_initial_solutions.py  # 生成初始解集
│   ├── initialize_parameters.py  # 参数初始化
│   ├── matlab_script_model1.m  # 适用于模型1的MATLAB脚本
│   ├── objective_function_health_check.py  # 目标函数健康检查
│   └── simulated_annealing_firefly_model1.py  # 适用于模型1的模拟退火萤火虫算法文件
│
├── model2/  # 模型2专用文件夹
│   ├── __pycache__/  # Python 缓存文件夹
│   ├── adaptive_cooling_rate.py  # 自适应冷却速率调整
│   ├── adaptive_initial_temperature.py  # 自适应初始温度调整
│   ├── calculate_fitness_model2.py  # 适用于模型2的适应度计算文件
│   ├── generate_initial_solutions.py  # 生成初始解集
│   ├── initialize_parameters.py  # 参数初始化
│   ├── matlab_script_model2.m  # 适用于模型2的MATLAB脚本
│   ├── objective_function_health_check.py  # 目标函数健康检查
│   └── simulated_annealing_firefly_model2.py  # 适用于模型2的模拟退火萤火虫算法文件
│
├── model3/  # 模型3专用文件夹
│   ├── __pycache__/  # Python 缓存文件夹
│   ├── adaptive_cooling_rate.py  # 自适应冷却速率调整
│   ├── adaptive_initial_temperature.py  # 自适应初始温度调整
│   ├── calculate_fitness_model3.py  # 适用于模型3的适应度计算文件
│   ├── generate_initial_solutions.py  # 生成初始解集
│   ├── initialize_parameters.py  # 参数初始化
│   ├── matlab_script_model3.m  # 适用于模型3的MATLAB脚本
│   ├── objective_function_health_check.py  # 目标函数健康检查
│   └── simulated_annealing_firefly_model3.py  # 适用于模型3的模拟退火萤火虫算法文件
│
├── 初始值.md  # 初始值说明文档
├── 清空命令窗口.m  # 清空命令窗口的MATLAB脚本
├── 文件夹结构.txt  # 文件夹结构说明文件
└── README.md  # 项目介绍文档


```

## Files Description

### model1 Directory

- **adaptive_cooling_rate.py**: Adjusts the cooling rate for the simulated annealing algorithm.
- **adaptive_initial_temperature.py**: Adjusts the initial temperature for the simulated annealing algorithm.
- **calculate_fitness_model1.py**: Calculates the fitness value for Model 1.
- **generate_initial_solutions.py**: Generates initial solutions for the optimization algorithm.
- **initialize_parameters.py**: Initializes the parameters required for the simulation, including production and transportation costs, environmental costs, and subsidy coefficients.
- **matlab_script_model1.m**: MATLAB script to run Model 1 with the Simulated Annealing Firefly Algorithm.
- **objective_function_health_check.py**: Checks the health of the objective function to determine if the algorithm has converged.
- **simulated_annealing_firefly_model1.py**: Implements the Simulated Annealing Firefly Algorithm for Model 1.

### model2 Directory

- **adaptive_cooling_rate.py**: Adjusts the cooling rate for the simulated annealing algorithm.
- **adaptive_initial_temperature.py**: Adjusts the initial temperature for the simulated annealing algorithm.
- **calculate_fitness_model2.py**: Calculates the fitness value for Model 2, including cost-sharing ratios.
- **generate_initial_solutions.py**: Generates initial solutions for the optimization algorithm.
- **initialize_parameters.py**: Initializes the parameters required for the simulation, including production and transportation costs, environmental costs, and subsidy coefficients.
- **matlab_script_model2.m**: MATLAB script to run Model 2 with the Simulated Annealing Firefly Algorithm.
- **objective_function_health_check.py**: Checks the health of the objective function to determine if the algorithm has converged.
- **simulated_annealing_firefly_model2.py**: Implements the Simulated Annealing Firefly Algorithm for Model 2.

### model3 Directory

- **adaptive_cooling_rate.py**: Adjusts the cooling rate for the simulated annealing algorithm.
- **adaptive_initial_temperature.py**: Adjusts the initial temperature for the simulated annealing algorithm.
- **calculate_fitness_model3.py**: Calculates the fitness value for Model 3, integrating environmental costs and government subsidies.
- **generate_initial_solutions.py**: Generates initial solutions for the optimization algorithm.
- **initialize_parameters.py**: Initializes the parameters required for the simulation, including production and transportation costs, environmental costs, and subsidy coefficients.
- **matlab_script_model3.m**: MATLAB script to run Model 3 with the Simulated Annealing Firefly Algorithm.
- **objective_function_health_check.py**: Checks the health of the objective function to determine if the algorithm has converged.
- **simulated_annealing_firefly_model3.py**: Implements the Simulated Annealing Firefly Algorithm for Model 3.

### Other Files

- **初始值.md**: Documentation of initial values.
- **清空命令窗口.m**: MATLAB script to clear the command window.
- **文件夹结构.txt**: Description of the directory structure.
- **README.md**: Introduction and overview of the project.

## How to Run

1. **Download the repository as a ZIP file**:
    - Click the "Code" button on the repository page and select "Download ZIP".

2. **Extract the ZIP file**:
    - Extract the contents to a desired location on your computer.

3. **Set up the Python environment**:
    Ensure you have Python installed. Create a virtual environment and install the required packages.
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    pip install -r requirements.txt  # Ensure you have a requirements.txt file with necessary packages
    ```

4. **Run the MATLAB scripts**:
    - Open MATLAB 2023b (or your installed version).
    - Navigate to the directory containing the extracted files.
    - Run the scripts `matlab_script_model1.m`, `matlab_script_model2.m`, and `matlab_script_model3.m` one by one.

## Results

The results of the simulations will provide insights into the optimal strategies for hydrogen production and transportation under various subsidy policies. The project demonstrates the effectiveness of the Simulated Annealing Firefly Algorithm in optimizing complex supply chain problems.

## PS

**Note**: When running the MATLAB scripts, you may encounter an issue where running one script causes another to fail due to conflicts in the Python environment setup. To resolve this:
- After running a MATLAB script, close the current MATLAB session.
- Open a new MATLAB session and run the next script.

This ensures that each script runs with a fresh Python environment setup.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Contact

If you have any questions or suggestions, please feel free to contact me at [1254406948@qq.com](mailto:1254406948@qq.com).

好的，以下是包含GitHub常用表情包的更新版本说明：

### 更新后的 README.md

#### 更新版本1.1

##### 更新内容
- 修正并更新了模型1的计算公式，添加了 `subsidy_amount` 参数用于计算直接资金补贴。🚀
- 数据修改过程：
  1. 在 `initialize_parameters.py` 中添加了 `subsidy_amount` 参数。📝
  2. 在 `calculate_fitness_model1.py` 中使用 `subsidy_amount` 参数计算补贴并更新适应度计算函数。🔄
- 使用方法：
  1. 确保所有参数已在 `initialize_parameters.py` 中初始化。📂
  2. 在 `calculate_fitness_model1.py` 中进行适应度计算时，确保正确使用补贴参数。✅
  3. 运行 `matlab_script_model1.m` 进行实验。🔍

#### 更新版本1.2

##### 更新内容
- 加入了无补贴的对照组模型（model0）。🎉
- model0的加入原因和作用：
  1. 对照组模型用于提供无补贴情况下的基准对比，以评估不同补贴政策的效果。📊
  2. 通过与补贴模型对比，分析补贴对氢能供应链成本的影响，找出最优的补贴政策和方案。🔬
- 使用方法：
  1. 在 `initialize_parameters.py` 中初始化所有参数。📂
  2. 使用 `calculate_fitness_model0.py` 进行适应度计算，该文件不考虑任何补贴，仅计算生产成本和运输成本的总和。🔄
  3. 运行 `matlab_script_model0.m` 进行实验，获得无补贴情况下的基准数据。🔍
