import os
import json
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

folder_path = "clusters"
# ��ʼ�����б���������е�����������Ŀ�����
all_heart_rate = []
all_total_motion = []

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

            # ��ȡ����������Ŀ�����
            heart_rate = data["heart_rate"]
            total_motion = data["totalMotion"]

            # ��ӵ����б���
            all_heart_rate.append(heart_rate)
            all_total_motion.append(total_motion)

# ת������Ϊ NumPy ����
X = np.array(all_heart_rate).reshape(-1, 1)
y = np.array(all_total_motion)

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
