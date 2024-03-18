import os
import json
import numpy as np
import matplotlib.pyplot as plt

data_folder = 'clusters'
n_clusters = 4  # 聚类的数量，根据你的数据设置

# 初始化呼吸特征列表
breath_features = [[] for _ in range(n_clusters)]

# 循环遍历每个聚类文件夹
for cluster_id in range(n_clusters):
    cluster_folder = os.path.join(data_folder, f'cluster_{cluster_id}')
    signal_files = os.listdir(cluster_folder)

    # 遍历每个信号文件
    for file_name in signal_files:
        file_path = os.path.join(cluster_folder, file_name)

        with open(file_path) as json_file:
            data = json.load(json_file)
            breath = data['breath']

            # 将呼吸特征添加到对应聚类的列表中
            breath_features[cluster_id].append(breath)

# 计算每个聚类的平均呼吸特征和方差
avg_breath_features = [np.mean(breath_features[i]) for i in range(n_clusters)]
var_breath_features = [np.var(breath_features[i]) for i in range(n_clusters)]

# 绘制条形图和直方图
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, figsize=(8, 10))

# 绘制条形图
x = np.arange(n_clusters)
width = 0.35

rects1 = ax1.bar(x, avg_breath_features, width, label='Average')
rects2 = ax1.bar(x + width, var_breath_features, width, label='Variance')

ax1.set_xlabel('Cluster')
ax1.set_ylabel('Breath Feature')
ax1.set_title('Average and Variance of Breath Feature by Cluster')
ax1.set_xticks(x)
ax1.legend()

# 在每个条形上方添加平均呼吸特征和方差标签
for i, rect in enumerate(rects1):
    height = rect.get_height()
    ax1.text(rect.get_x() + rect.get_width() / 2, height, f'{avg_breath_features[i]:.2f}', ha='center', va='bottom')

for i, rect in enumerate(rects2):
    height = rect.get_height()
    ax1.text(rect.get_x() + rect.get_width() / 2, height, f'{var_breath_features[i]:.2f}', ha='center', va='bottom')

# 绘制直方图
ax2.hist(breath_features, bins=10, edgecolor='black', alpha=0.7)
ax2.set_xlabel('Breath Feature')
ax2.set_ylabel('Frequency')
ax2.set_title('Distribution of Breath Feature')
ax2.legend(['Cluster 0', 'Cluster 1', 'Cluster 2', 'Cluster 3'])

plt.tight_layout()
plt.show()
