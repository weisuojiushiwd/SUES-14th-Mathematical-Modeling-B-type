import os
import json
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft

data_folder = 'clusters'
n_clusters = 4  # 聚类的数量，根据你的数据设置

# 初始化傅里叶频谱列表
fourier_spectrums = [[] for _ in range(n_clusters)]

# 循环遍历每个聚类文件夹
for cluster_id in range(n_clusters):
    cluster_folder = os.path.join(data_folder, f'cluster_{cluster_id}')
    signal_files = os.listdir(cluster_folder)

    # 遍历每个信号文件
    for file_name in signal_files:
        file_path = os.path.join(cluster_folder, file_name)

        with open(file_path) as json_file:
            data = json.load(json_file)
            signal = data['opticalpower']

            # 进行傅里叶变换
            spectrum = np.abs(fft(signal))

            # 将频谱添加到对应聚类的频谱列表中
            fourier_spectrums[cluster_id].append(spectrum)

# 计算平均傅里叶频谱
avg_fourier_spectrums = [np.mean(np.array(fourier_spectrums[i]), axis=0) for i in range(n_clusters)]

# 绘制平均傅里叶频谱图
plt.figure(figsize=(8, 6))  # 调整图像尺寸
for cluster_id in range(n_clusters):
    plt.plot(avg_fourier_spectrums[cluster_id], label=f'Cluster {cluster_id}')
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.title('Average Fourier Spectrum')
plt.xlim(0, 1)  # 调整x轴范围，放大低频区域
plt.legend()
plt.tight_layout()  # 调整子图布局
plt.show()
