import os
import json
import numpy as np
import matplotlib.pyplot as plt
import pywt

data_folder = 'clusters'
n_clusters = 4  # 聚类的数量，根据你的数据设置

# 初始化小波频谱列表
wavelet_spectrums = [[] for _ in range(n_clusters)]

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

            # 进行小波变换
            coeffs = pywt.wavedec(signal, 'db1')

            # 提取近似系数作为频谱
            approx_coeffs = coeffs[0]

            # 将频谱添加到对应聚类的频谱列表中
            wavelet_spectrums[cluster_id].append(approx_coeffs)

# 计算平均小波频谱
avg_wavelet_spectrums = [np.mean(np.abs(np.array(wavelet_spectrums[i])), axis=0) for i in range(n_clusters)]

# 绘制平均小波频谱图

plt.figure(figsize=(8, 6))  # 调整图像尺寸
for cluster_id in range(n_clusters):
    plt.plot(avg_wavelet_spectrums[cluster_id], label=f'Cluster {cluster_id}')
plt.xlabel('Scale')
plt.ylabel('Magnitude')
plt.title('Average Wavelet Spectrum')
plt.legend()
plt.tight_layout()  # 调整子图布局
plt.show()

