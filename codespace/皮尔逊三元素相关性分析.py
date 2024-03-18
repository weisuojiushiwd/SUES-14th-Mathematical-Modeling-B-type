import os
import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

breath_list = []
heart_rate_list = []
total_motion_list = []

folder_path = "clusters"
for i in range(5):
    cluster_folder = os.path.join(folder_path, f"cluster_{i}")
    for filename in os.listdir(cluster_folder):
        if filename.endswith(".json"):
            file_path = os.path.join(cluster_folder, filename)
            with open(file_path) as f:
                data = json.load(f)
            breath = data["breath"]
            heart_rate = data["heart_rate"]
            total_motion = data["totalMotion"]
            breath_list.append(breath)
            heart_rate_list.append(heart_rate)
            total_motion_list.append(total_motion)

df = pd.DataFrame({
    "breath": breath_list,
    "heart_rate": heart_rate_list,
    "totalMotion": total_motion_list
})

correlation = df.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap="coolwarm", annot_kws={"fontsize": 12})
plt.title("Correlation Heatmap", fontsize=14)
plt.show()
