import os
import json
import numpy as np
from sklearn.cluster import KMeans
import shutil

data_folder = 'signal_precheck'
output_folder = 'clusters'  # 存放聚类结果的文件夹路径
n_clusters = 4  # 聚类的数量，根据你的需求设置

# 创建存放聚类结果的文件夹
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 读取数据
data = []
file_names = []
for file_name in os.listdir(data_folder):
    file_path = os.path.join(data_folder, file_name)
    with open(file_path) as json_file:
        json_data = json.load(json_file)
        optical_power = json_data['opticalpower']
        data.append(optical_power)
        file_names.append(file_name)

# 转换为NumPy数组
data = np.array(data)

# 进行聚类
kmeans = KMeans(n_clusters=n_clusters)
kmeans.fit(data)

# 获取每个样本所属的聚类标签
labels = kmeans.labels_

# 将文件移动到每个簇中
for i, label in enumerate(labels):
    cluster_folder = os.path.join(output_folder, f'cluster_{label}')
    if not os.path.exists(cluster_folder):
        os.makedirs(cluster_folder)
    file_name = file_names[i]
    file_path = os.path.join(data_folder, file_name)
    shutil.move(file_path, cluster_folder)

# 输出每个样本的聚类标签和移动后的文件路径
for i, label in enumerate(labels):
    file_name = file_names[i]
    cluster_folder = os.path.join(output_folder, f'cluster_{label}')
    new_file_path = os.path.join(cluster_folder, file_name)
    print(f"Sample {i+1}: Cluster {label}, File moved to: {new_file_path}")

# 输出聚类中心
centroids = kmeans.cluster_centers_
for i, centroid in enumerate(centroids):
    print(f"Cluster {i} centroid: {centroid}")
