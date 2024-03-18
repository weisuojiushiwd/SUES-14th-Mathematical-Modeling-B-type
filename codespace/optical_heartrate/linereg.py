import os
import json
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# ��� JSON �ļ����ļ���·��
folder_path = "clusters"

# ��ʼ�����б���������е�����������Ŀ�����
all_optical_power = []
all_heart_rate = []

# �����ļ���
for i in range(4):
    cluster_folder = os.path.join(folder_path, f"cluster_{i}")

    # �����ļ����е��ļ�
    for filename in os.listdir(cluster_folder):
        if filename.endswith(".json"):
            file_path = os.path.join(cluster_folder, filename)

            # ��ȡ JSON �ļ�
            with open(file_path) as f:
                data = json.load(f)

            # ��ȡ optical_power ��ƽ��ֵ
            optical_power = data["opticalpower"]
            optical_power_avg = np.mean(optical_power)

            heart_rate = data["heart_rate"]

            # ��ӵ����б���
            all_optical_power.append(optical_power_avg)
            all_heart_rate.append(heart_rate)

# ת������Ϊ NumPy ����
X = np.array(all_optical_power).reshape(-1, 1)
y = np.array(all_heart_rate)

# ����ѵ�����Ͳ��Լ�
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# �������Իع�ģ��
model = LinearRegression()

# ���ģ��
model.fit(X_train, y_train)
print("Model training completed.")

# �ڲ��Լ��Ͻ���Ԥ��
y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
rmse = np.sqrt(mse)

print("Mean Squared Error:", mse)
print("R2 Score:", r2)
print("Root Mean Squared Error:", rmse)

# ����ģ��
joblib.dump(model, "linear_regression_model.joblib")
