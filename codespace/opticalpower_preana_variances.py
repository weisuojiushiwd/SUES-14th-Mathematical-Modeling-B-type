import os
import json
import numpy as np

folder_path = "clusters"

for i in range(4):
    cluster_folder = os.path.join(folder_path, f"cluster_{i}")
    file_variances = []

    for filename in os.listdir(cluster_folder):
        if filename.endswith(".json"):
            file_path = os.path.join(cluster_folder, filename)
            with open(file_path) as f:
                data = json.load(f)
            opticalpower = data["opticalpower"]
            variance = np.var(opticalpower)
            file_variances.append(variance)

    # 打印每个文件的方差
    for j, variance in enumerate(file_variances):
        print(f"File {j+1} variance: {variance}")
