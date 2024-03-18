import os
import json
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import norm

# 存储数据的列表
cluster_breath_lists = []
cluster_heart_rate_lists = []

# 文件夹路径
folder_path = "clusters"

# 遍历每个簇文件夹
for i in range(4):
    cluster_breath_list = []
    cluster_heart_rate_list = []
    cluster_folder = os.path.join(folder_path, f"cluster_{i}")
    
    # 遍历簇文件夹中的每个JSON文件
    for filename in os.listdir(cluster_folder):
        if filename.endswith(".json"):
            file_path = os.path.join(cluster_folder, filename)
            
            # 加载JSON数据
            with open(file_path) as f:
                data = json.load(f)
            
            # 提取数据
            breath = data["breath"]
            heart_rate = data["heart_rate"]
            
            # 将数据添加到列表中
            cluster_breath_list.append(breath)
            cluster_heart_rate_list.append(heart_rate)
    
    cluster_breath_lists.append(cluster_breath_list)
    cluster_heart_rate_lists.append(cluster_heart_rate_list)

# 创建子图布局
fig, axes = plt.subplots(2, 1, figsize=(10,12))

# 定义颜色列表
colors = ["blue", "green", "orange", "red"]

# 分别处理每个簇的数据
for i in range(4):
    cluster_breath_data = cluster_breath_lists[i]
    cluster_heart_rate_data = cluster_heart_rate_lists[i]
    
    # 从列表创建DataFrame
    breath_df = pd.DataFrame({
        "breath": cluster_breath_data
    })
    heart_rate_df = pd.DataFrame({
        "heart_rate": cluster_heart_rate_data
    })
    
    # 拟合概率密度函数（PDF）
    breath_params = norm.fit(breath_df["breath"])
    heart_rate_params = norm.fit(heart_rate_df["heart_rate"])
    
    # 生成PDF曲线的值
    x_breath = np.linspace(breath_df["breath"].min(), breath_df["breath"].max(), 100)
    breath_pdf = norm.pdf(x_breath, *breath_params)
    
    x_heart_rate = np.linspace(heart_rate_df["heart_rate"].min(), heart_rate_df["heart_rate"].max(), 100)
    heart_rate_pdf = norm.pdf(x_heart_rate, *heart_rate_params)
    
    # 绘制直方图和PDF曲线
    sns.histplot(data=breath_df, x="breath", kde=True, ax=axes[0], label=f"Cluster {i}", color=colors[i])
    axes[0].plot(x_breath, breath_pdf, color=colors[i])
    
    sns.histplot(data=heart_rate_df, x="heart_rate", kde=True, ax=axes[1], label=f"Cluster {i}", color=colors[i])
    axes[1].plot(x_heart_rate, heart_rate_pdf, color=colors[i])

# 设置图例
axes[0].legend()
axes[1].legend()

# 调整子图布局
plt.tight_layout()
plt.show()
