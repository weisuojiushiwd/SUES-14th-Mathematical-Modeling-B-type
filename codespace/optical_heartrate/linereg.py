import os
import json
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# 存放 JSON 文件的文件夹路径
folder_path = "clusters"

# 初始化空列表来存放所有的输入特征和目标变量
all_optical_power = []
all_heart_rate = []

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

            # 提取 optical_power 的平均值
            optical_power = data["opticalpower"]
            optical_power_avg = np.mean(optical_power)

            heart_rate = data["heart_rate"]

            # 添加到总列表中
            all_optical_power.append(optical_power_avg)
            all_heart_rate.append(heart_rate)

# 转换数据为 NumPy 数组
X = np.array(all_optical_power).reshape(-1, 1)
y = np.array(all_heart_rate)

# 划分训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建线性回归模型
model = LinearRegression()

# 拟合模型
model.fit(X_train, y_train)
print("Model training completed.")

# 在测试集上进行预测
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mse)

print("Mean Squared Error:", mse)
print("R2 Score:", r2)
print("Root Mean Squared Error:", rmse)

# 保存模型
joblib.dump(model, "linear_regression_model.joblib")
