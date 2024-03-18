import os
import shutil
import json
from threading import ThreadError
import numpy as np

# 文件夹路径
folder_path = "clusters"

# 创建用于存储高方差文件的文件夹
output_folder = "high_variance_files"
os.makedirs(output_folder, exist_ok=True)

# 初始化计数器
total_files = 0
high_variance_files = 0
cluster_counts = {}
threshold = 0.5
# 遍历文件夹
for i in range(4):
    cluster_folder = os.path.join(folder_path, f"cluster_{i}")
    cluster_total_files = 0
    cluster_high_variance_files = 0
    for filename in os.listdir(cluster_folder):
        if filename.endswith(".json"):
            file_path = os.path.join(cluster_folder, filename)
            with open(file_path) as f:
                data = json.load(f)
            optical_power = data["opticalpower"]
            variance = np.var(optical_power)
            total_files += 1
            cluster_total_files += 1

            # 判断方差是否超过阈值
            if variance > threshold:
                high_variance_files += 1
                cluster_high_variance_files += 1
                # 复制文件到输出文件夹
                output_file_path = os.path.join(output_folder, filename)
                shutil.copy(file_path, output_file_path)

    # 记录每个 cluster 的文件数量和高方差文件数量
    cluster_counts[f"cluster_{i}"] = {
        "total_files": cluster_total_files,
        "high_variance_files": cluster_high_variance_files
    }

# 打印各个 cluster 的比例
print("Cluster Proportions:")
for cluster, counts in cluster_counts.items():
    proportion = counts["high_variance_files"] / counts["total_files"]
    print(f"{cluster}: {proportion:.2%}")

# 打印总体结果
total_proportion = high_variance_files / total_files
print(f"\nTotal files: {total_files}")
print(f"High variance files: {high_variance_files}")
print(f"Total Proportion: {total_proportion:.2%}")
