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
    
    # 找到数据开始的行（跳过说明行和空行）
    start_row = None
    for i in range(len(df)):
        if df.iloc[i, 1] == "Light read":
            start_row = i + 1
            break
    
    if start_row is None:
        raise ValueError(f"在 {sheet_name} 中未找到表头")
    
    # 找到平均值所在行（通常包含 "Average"）
    end_row = None
    for i in range(start_row, len(df)):
        if isinstance(df.iloc[i, 1], str) and "Average" in str(df.iloc[i, 1]):
            end_row = i
            break
    
    if end_row is None:
        # 如果没有找到 Average，取到数据末尾
        end_row = len(df)
    
    # 读取数据区域
    data_df = df.iloc[start_row:end_row, 1:11].copy()
    data_df.columns = ["Light_read", "Light_colour",
                       "0_min_read", "0_min_colour",
                       "3_min_read", "3_min_colour",
                       "6_min_read", "6_min_colour",
                       "9_min_read", "9_min_colour"]
    
    # 转换为数值，非数值变成 NaN
    data_df = data_df.apply(pd.to_numeric, errors='coerce')
    
    return data_df

def plot_metric(data_df, metric_name, sheet_name):
    """
    metric_name: 'read' 或 'colour'
    """
    times = [0, 3, 6, 9]
    
    if metric_name == 'read':
        cols = [f"{t}_min_read" for t in times]
        ylabel = "Read value"
        title_suffix = "Read"
    else:
        cols = [f"{t}_min_colour" for t in times]
        ylabel = "Colour value"
        title_suffix = "Colour"
    
    means = []
    stds = []
    for col in cols:
        valid_data = data_df[col].dropna()
        means.append(valid_data.mean())
        stds.append(valid_data.std())
    
    means = np.array(means)
    stds = np.array(stds)
    
    plt.figure(figsize=(5, 4))
    plt.errorbar(times, means, yerr=stds, fmt='o-', capsize=5,
                 color='black', ecolor='gray', elinewidth=1, markeredgewidth=1)
    plt.xlabel("Time (minutes)")
    plt.ylabel(ylabel)
    plt.title(f"{sheet_name} - {title_suffix} (mean ± SD)")
    plt.xticks(times)
    plt.grid(True, linestyle='--', alpha=0.5)
    
    # 图注说明，符合 Q&A 要求
    plt.figtext(0.5, -0.1,
                f"Figure. {sheet_name} {title_suffix} values over time. "
                "Points show mean, error bars show ±1 standard deviation. "
                "Data collected by IBMS1 students.",
                wrap=True, ha='center', fontsize=9)
    
    plt.tight_layout()
    plt.show()

# 主程序
for sheet in ["Morning", "Afternoon"]:
    print(f"\n处理工作表: {sheet}")
    data = process_sheet(sheet)
    plot_metric(data, "read", sheet)
    plot_metric(data, "colour", sheet)