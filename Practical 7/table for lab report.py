import matplotlib.pyplot as plt
import pandas as pd

# 重新组织数据：时间点作为行，Morning和Afternoon作为列
data = {
    'Time point': ['Light', '0 min', '3 min', '6 min', '9 min'],
    'Morning Visual acuity': ['2.51 ± 0.37', '12.30 ± 5.71', '8.93 ± 3.13', '7.69 ± 2.57', '7.00 ± 2.31'],
    'Morning Colour': ['1.52 ± 0.13', '11.58 ± 9.20', '6.71 ± 6.24', '5.03 ± 4.76', '4.53 ± 4.52'],
    'Afternoon Visual acuity': ['2.50 ± 0.32', '15.71 ± 5.63', '10.48 ± 3.23', '8.66 ± 2.39', '7.70 ± 2.36'],
    'Afternoon Colour': ['1.58 ± 0.29', '17.24 ± 8.33', '8.55 ± 5.58', '5.70 ± 3.45', '4.43 ± 2.82']
}

df = pd.DataFrame(data)

# 创建图形
fig, ax = plt.subplots(figsize=(12, 4))
ax.axis('off')

# 创建表格
table = ax.table(cellText=df.values,
                 colLabels=df.columns,
                 cellLoc='center',
                 loc='center',
                 colWidths=[0.12, 0.22, 0.22, 0.22, 0.22])

# 设置字体
table.auto_set_font_size(False)
table.set_fontsize(9.5)

# 设置边框
for key, cell in table.get_celld().items():
    cell.set_edgecolor('black')
    cell.set_linewidth(0.5)

# 表头加粗
for i in range(5):
    table[(0, i)].set_text_props(weight='bold')

# 添加标题
plt.title('Table 1. Summary of visual acuity and colour discrimination thresholds (mean ± SD)\nfor morning and afternoon groups', 
          fontsize=11, pad=20)

# 添加注释
plt.figtext(0.5, 0.01, 'Note: Lower font size values indicate better performance.', 
            ha='center', fontsize=9, style='italic')

plt.tight_layout()
plt.savefig('dark_adaptation_table.png', dpi=300, bbox_inches='tight')
plt.show()