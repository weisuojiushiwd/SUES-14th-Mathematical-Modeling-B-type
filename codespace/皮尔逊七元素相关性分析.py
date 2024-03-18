import os
import json
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pywt
from scipy.fft import fft
from sklearn.svm import SVC
from sklearn.feature_selection import SelectFromModel

svm_model = SVC(kernel='rbf')

breath_list = []
heart_rate_list = []
total_motion_list = []
average_optical_power_list = []
optical_power_wavelet_listCA = []
optical_power_wavelet_listCD = []
optical_power_fft_list = []

folder_path = "clusters"
for i in range(4):
    cluster_folder = os.path.join(folder_path, f"cluster_{i}")
    for filename in os.listdir(cluster_folder):
        if filename.endswith(".json"):
            file_path = os.path.join(cluster_folder, filename)
            with open(file_path) as f:
                data = json.load(f)
            breath = data["breath"]
            heart_rate = data["heart_rate"]
            total_motion = data["totalMotion"]
            optical_power = data["opticalpower"]
            # 进行傅里叶变换
            optical_power_fft = fft(optical_power)
            average_optical_power_fft = np.mean(optical_power_fft)
            optical_power_fft_list.append(average_optical_power_fft)
            # 进行小波变换
            coeffs = pywt.dwt(optical_power, 'db1')  # 使用db1小波基
            cA, cD = coeffs  # cA是近似系数，cD是细节系数
            # 求细节系数cD的平均值作为特征
            average_optical_power_waveletCA = np.mean(cA)
            average_optical_power_waveletCD = np.mean(cD)
            optical_power_wavelet_listCA.append(average_optical_power_waveletCA)
            optical_power_wavelet_listCD.append(average_optical_power_waveletCD)
            average_optical_power = np.mean(optical_power)
            average_optical_power_list.append(average_optical_power)
            breath_list.append(breath)
            heart_rate_list.append(heart_rate)
            total_motion_list.append(total_motion)

df_wavelet = pd.DataFrame({
    "bt": breath_list,
    "h_t": heart_rate_list,
    "tM": total_motion_list,
    "a_o": average_optical_power_list,
    "a_o_wl_CA": optical_power_wavelet_listCA,
    "a_o_wl_CD": optical_power_wavelet_listCD,
    "a_o_fft": optical_power_fft_list
})

correlation = df_wavelet.corr()
plt.figure(figsize=(10, 10))
sns.heatmap(correlation, annot=True, cmap="coolwarm", annot_kws={"fontsize": 14})
plt.tick_params(axis='x', labelsize=12)  # 设置横轴元素字体大小为
plt.tick_params(axis='y', labelsize=12)  # 设置纵轴元素字体大小为
plt.title("Elements Correlation Heatmap", fontsize=14)

plt.show()


