import joblib
import numpy as np
import os
import json
from sklearn.metrics import mean_squared_error, r2_score

folder_path = "clusters"
# 初始化空列表来存放所有的输入特征和目标变量
all_heart_rate = []
all_total_motion = []
all_optical_power = []
predicted_all_total_motion = []

# 遍历文件夹
for i in range(4):
    cluster_folder = os.path.join(folder_path, f"cluster_{i}")

    # 遍历文件夹中的文件
    for filename in os.listdir(cluster_folder):
        if filename.endswith(".json"):
            file_path = os.path.join(cluster_folder, filename)

            # 读取 JSON 文件
            with open(file_path) as f:
                data = json.load(f)

            # 提取输入特征和目标变量
            heart_rate = data["heart_rate"]
            total_motion = data["totalMotion"]
            optical_power = data["opticalpower"]

            # 添加到总列表中
            all_heart_rate.append(heart_rate)
            all_total_motion.append(total_motion)
            all_optical_power.append(optical_power)

# 加载模型
heart_rate_model = joblib.load("random_forest_model.joblib")
total_motion_model = joblib.load("random_forest_model_ht_tm.joblib")

# 转换数据为 NumPy 数组
optical_power = np.array(all_optical_power)
actual_heart_rate = np.array(all_heart_rate)
actual_total_motion = np.array(all_total_motion)

# 使用 "optical_power" 预测 "heart_rate"
predicted_heart_rate = heart_rate_model.predict(optical_power).reshape(-1, 1)

predicted_total_motion = total_motion_model.predict(predicted_heart_rate)
predicted_all_total_motion.extend(predicted_total_motion.flatten())  # 将预测结果转换为一维数组

# 进行性能评估
mse_total_motion = mean_squared_error(actual_total_motion, predicted_all_total_motion)
r2_total_motion = r2_score(actual_total_motion, predicted_all_total_motion)
rmse_total_motion = np.sqrt(mse_total_motion)

# 打印评估结果
print("Total Motion Model - Mean Squared Error:", mse_total_motion)
print("Total Motion Model - R2 Score:", r2_total_motion)
print("Total Motion Model - Root Mean Squared Error:", rmse_total_motion)
