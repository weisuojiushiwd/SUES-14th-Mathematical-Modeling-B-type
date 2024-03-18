import os
import json
import numpy as np
import xgboost as xgb
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

            # ��ȡ����������Ŀ�����
            optical_power = data["opticalpower"]
            heart_rate = data["heart_rate"]

            # ���ӵ����б���
            all_optical_power.append(optical_power)
            all_heart_rate.append(heart_rate)

# ת������Ϊ NumPy ����
X = np.array(all_optical_power)
y = np.array(all_heart_rate)

# ����ѵ�����Ͳ��Լ�
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ���� XGBoost �ع�ģ��
model = xgb.XGBRegressor()

# ���ģ��
model.fit(X_train, y_train)
print("Model training completed.")

# �ڲ��Լ��Ͻ���Ԥ��
y_pred = model.predict(X_test)

# ������������
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

# ����R2����
r2 = r2_score(y_test, y_pred)
print("R2 Score:", r2)

# ������������
rmse = np.sqrt(mse)
print("Root Mean Squared Error:", rmse)

# ����ģ��
joblib.dump(model, "xgboost_model.joblib")