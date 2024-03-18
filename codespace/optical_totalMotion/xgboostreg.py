import os
import json
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# 存放 JSON 文件的文件夹路径
folder_path = "clusters"

# 初始化空列表来存放所有的输入特征和目标变量
all_optical_power = []
all_total_motion = []

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
            optical_power = data["opticalpower"]
            total_motion = data["totalMotion"]

            # 添加到总列表中
            all_optical_power.append(optical_power)
            all_total_motion.append(total_motion)

# 转换数据为 NumPy 数组
X = np.array(all_optical_power)
y = np.array(all_total_motion)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建 XGBoost 回归模型
model = xgb.XGBRegressor()

# 拟合模型
model.fit(X_train, y_train)
print("Model training completed.")

# 在测试集上进行预测
y_pred = model.predict(X_test)

# 计算均方根误差
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# 计算R2分数
r2 = r2_score(y_test, y_pred)
print("R2 Score:", r2)

# 计算均方根误差
rmse = np.sqrt(mse)
print("Root Mean Squared Error:", rmse)

# 保存模型
joblib.dump(model, "xgboost_model.joblib")
