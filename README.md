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
│   ├── matlab_script_model0_modified.m  # 适用于模型0的修改版MATLAB脚本
│   ├── objective_function_health_check.py  # 目标函数健康检查
│   └── simulated_annealing_firefly_model0.py  # 适用于模型0的模拟退火萤火虫算法文件
├── model1/  # 模型1专用文件夹
│   ├── __pycache__/  # Python 缓存文件夹
│   ├── adaptive_cooling_rate.py  # 自适应冷却速率调整
│   ├── adaptive_initial_temperature.py  # 自适应初始温度调整
│   ├── calculate_fitness_model1.py  # 适用于模型1的适应度计算文件
│   ├── generate_initial_solutions.py  # 生成初始解集
│   ├── initialize_parameters.py  # 参数初始化
│   ├── matlab_script_model1.m  # 适用于模型1的MATLAB脚本
│   ├── matlab_script_model1_modified.m  # 适用于模型1的修改版MATLAB脚本
│   ├── objective_function_health_check.py  # 目标函数健康检查
│   └── simulated_annealing_firefly_model1.py  # 适用于模型1的模拟退火萤火虫算法文件
├── model2/  # 模型2专用文件夹
│   ├── __pycache__/  # Python 缓存文件夹
│   ├── adaptive_cooling_rate.py  # 自适应冷却速率调整
│   ├── adaptive_initial_temperature.py  # 自适应初始温度调整
│   ├── calculate_fitness_model2.py  # 适用于模型2的适应度计算文件
│   ├── generate_initial_solutions.py  # 生成初始解集
│   ├── initialize_parameters.py  # 参数初始化
│   ├── matlab_script_model2.m  # 适用于模型2的MATLAB脚本
│   ├── matlab_script_model2_modified.m  # 适用于模型2的修改版MATLAB脚本
│   ├── objective_function_health_check.py  # 目标函数健康检查
│   └── simulated_annealing_firefly_model2.py  # 适用于模型2的模拟退火萤火虫算法文件
├── model3/  # 模型3专用文件夹
│   ├── __pycache__/  # Python 缓存文件夹
│   ├── adaptive_cooling_rate.py  # 自适应冷却速率调整
│   ├── adaptive_initial_temperature.py  # 自适应初始温度调整
│   ├── calculate_fitness_model3.py  # 适用于模型3的适应度计算文件
│   ├── generate_initial_solutions.py  # 生成初始解集
│   ├── initialize_parameters.py  # 参数初始化
│   ├── matlab_script_model3.m  # 适用于模型3的MATLAB脚本
│   ├── matlab_script_model3_modified.m  # 适用于模型3的修改版MATLAB脚本
│   ├── objective_function_health_check.py  # 目标函数健康检查
│   └── simulated_annealing_firefly_model3.py  # 适用于模型3的模拟退火萤火虫算法文件
├── 初始值.md  # 初始值说明文档
├── 清空命令窗口.m  # 清空命令窗口的MATLAB脚本
├── 文件夹结构.txt  # 文件夹结构说明文件
|── README.md  # 项目介绍文档
├── 实验数据/
│   ├──model0/
│       ├── optimal_solutions/
│   ├──model1/
│       ├── optimal_solutions/
│   ├──model2/
│       ├── optimal_solutions/
|   └──model3/
└       └── optimal_solutions/


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


### Update Version 1.1

#### Update Content
- Corrected and updated the calculation formula for Model 1, adding the `subsidy_amount` parameter for calculating direct financial subsidies. 🚀
- Data modification process:
  1. Added the `subsidy_amount` parameter in `initialize_parameters.py`. 📝
  2. Used the `subsidy_amount` parameter in `calculate_fitness_model1.py` to calculate subsidies and updated the fitness calculation function. 🔄
- Usage:
  1. Ensure all parameters are initialized in `initialize_parameters.py`. 📂
  2. When performing fitness calculations in `calculate_fitness_model1.py`, ensure the subsidy parameter is used correctly. ✅
  3. Run `matlab_script_model1.m` to conduct the experiment. 🔍

### Update Version 1.2

#### Update Content
- Added a control group model without subsidies (Model 0). 🎉
- Reasons and functions of adding Model 0:
  1. The control group model provides a baseline comparison without subsidies to evaluate the effects of different subsidy policies. 📊
  2. By comparing with the subsidy models, analyze the impact of subsidies on the cost of the hydrogen supply chain to identify the optimal subsidy policies and plans. 🔬
- Usage:
  1. Initialize all parameters in `initialize_parameters.py`. 📂
  2. Use `calculate_fitness_model0.py` for fitness calculation, which does not consider any subsidies, only calculating the total production and transportation costs. 🔄
  3. Run `matlab_script_model0.m` to conduct the experiment and obtain baseline data without subsidies. 🔍

### Update Version 1.3

#### Update Content
- Corrected and updated the calculation formulas for Models 0, 1, and 2 to ensure correct extraction of `production_quantity` and `distance_pipeline` parameters from `params`. 🔧
- Optimized the result saving paths and file naming formats to ensure correct saving of experimental data and optimal solution tables. 📁
- Data modification process:
  1. Defined initial production quantity and pipeline transportation distance in `initialize_parameters.py` and calculated other related parameters based on proportions. 📝
  2. Ensured consistent parameter sources in the fitness calculation files for each model (`calculate_fitness_model0.py`, `calculate_fitness_model1.py`, `calculate_fitness_model2.py`). 🔄
  3. Modified the relevant MATLAB script files (`matlab_script_model0_modified.m`, `matlab_script_model1_modified.m`, `matlab_script_model2_modified.m`) to ensure correct extraction and use of parameters, and optimized the result saving paths and file naming formats. 🔍
  4. Updated the file structure.

- Usage:
  1. Ensure all parameters are initialized in `initialize_parameters.py`. 📂
  2. When performing fitness calculations in the fitness calculation files for each model, ensure the parameters are used correctly. ✅
  3. Run the corresponding MATLAB script files to conduct experiments and obtain experimental data and optimal solution tables for each model. 📊
