import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 设置字体和大小，符合 lab report 要求
plt.rcParams.update({
    'font.size': 11,
    'axes.titlesize': 12,
    'axes.labelsize': 11,
    'legend.fontsize': 10,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10
})

# 读取 Excel 文件
file_path = r"C:\Users\lenovo\Desktop\lab report（dark adaption）\dark adaptation statistics.xlsx"

def process_sheet(sheet_name):
    df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)
    
    # 找到数据开始的行
    start_row = None
    for i in range(len(df)):
        if df.iloc[i, 1] == "Light read":
            start_row = i + 1
            break
    
    if start_row is None:
        raise ValueError(f"在 {sheet_name} 中未找到表头")
    
    # 找到平均值所在行
    end_row = None
    for i in range(start_row, len(df)):
        if isinstance(df.iloc[i, 1], str) and "Average" in str(df.iloc[i, 1]):
            end_row = i
            break
    
    if end_row is None:
        end_row = len(df)
    
    # 读取数据区域
    data_df = df.iloc[start_row:end_row, 1:11].copy()
    data_df.columns = ["Light_read", "Light_colour",
                       "0_min_read", "0_min_colour",
                       "3_min_read", "3_min_colour",
                       "6_min_read", "6_min_colour",
                       "9_min_read", "9_min_colour"]
    
    # 转换为数值
    data_df = data_df.apply(pd.to_numeric, errors='coerce')
    
    return data_df

def plot_combined(data_df, sheet_name):
    """
    为单个 sheet 生成一张组合图，包含 Read 和 Colour 两条曲线
    """
    times = [0, 3, 6, 9]
    
    # 计算 Read 的均值和标准差
    read_cols = [f"{t}_min_read" for t in times]
    read_means = []
    read_stds = []
    for col in read_cols:
        valid_data = data_df[col].dropna()
        read_means.append(valid_data.mean())
        read_stds.append(valid_data.std())
    
    # 计算 Colour 的均值和标准差
    colour_cols = [f"{t}_min_colour" for t in times]
    colour_means = []
    colour_stds = []
    for col in colour_cols:
        valid_data = data_df[col].dropna()
        colour_means.append(valid_data.mean())
        colour_stds.append(valid_data.std())
    
    read_means = np.array(read_means)
    read_stds = np.array(read_stds)
    colour_means = np.array(colour_means)
    colour_stds = np.array(colour_stds)
    
    # 创建图表
    plt.figure(figsize=(6, 5))
    
    # 绘制 Read 曲线
    plt.errorbar(times, read_means, yerr=read_stds, fmt='o-', capsize=5,
                 color='black', ecolor='gray', elinewidth=1, 
                 markeredgewidth=1, label='Read threshold')
    
    # 绘制 Colour 曲线
    plt.errorbar(times, colour_means, yerr=colour_stds, fmt='s--', capsize=5,
                 color='red', ecolor='lightcoral', elinewidth=1,
                 markeredgewidth=1, label='Colour threshold')
    
    plt.xlabel("Time in darkness (minutes)")
    plt.ylabel("Threshold value (lower = better performance)")
    plt.title(f"{sheet_name} - Dark adaptation over time (mean ± SD)")
    plt.xticks(times)
    plt.legend(loc='upper right')
    plt.grid(True, linestyle='--', alpha=0.5)
    
    # 图注说明
    plt.figtext(0.5, -0.08,
                f"Figure. {sheet_name} visual performance during dark adaptation. "
                "Points show mean, error bars show ±1 standard deviation. "
                "Lower threshold values indicate better visual performance. "
                "Data collected by IBMS1 students.",
                wrap=True, ha='center', fontsize=9)
    
    plt.tight_layout()
    plt.show()

# 主程序
for sheet in ["Morning", "Afternoon"]:
    print(f"\n处理工作表: {sheet}")
    data = process_sheet(sheet)
    plot_combined(data, sheet)