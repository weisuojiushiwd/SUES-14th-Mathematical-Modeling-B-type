import json
import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
#设置字体为楷体
matplotlib.rcParams['font.sans-serif'] = ['KaiTi']
plt.rc('axes', unicode_minus=False)
json_dir = 'clusters/cluster_3'
json_files = os.listdir(json_dir)
embedding_dim = 3  # 设置相空间重构的维度

# 存储相空间重构后的轨迹
trajectories = []
def calculate_lyapunov_exponent(trajectory):
    n = len(trajectory)
    d = len(trajectory[0])
    epsilon = 1e-6  # 设置扰动大小

    # 初始化初始扰动向量
    initial_perturbation = np.random.randn(d)

    # 计算初始状态的李雅普诺夫指数
    x0 = trajectory[0]
    v0 = initial_perturbation / np.linalg.norm(initial_perturbation)
    l0 = 0.0

    # 迭代计算李雅普诺夫指数
    for i in range(1, n):
        x = trajectory[i]
        v = v0 / np.linalg.norm(v0)
        delta_x = x - x0
        delta_v = v - v0
        norm_delta_x = np.linalg.norm(delta_x)
        norm_delta_v = np.linalg.norm(delta_v)
        l0 += np.log(norm_delta_x / norm_delta_v)

        # 更新初始状态
        x0 = x
        v0 = delta_v * (epsilon / norm_delta_v)

    # 计算平均李雅普诺夫指数
    lyapunov_exponent = l0 / (n - 1)

    return lyapunov_exponent
for file in json_files:
    with open(os.path.join(json_dir, file), 'r') as f:
        data = json.load(f)
        optical_power = data['opticalpower']
        
        # 相空间重构
        trajectory = []
        for i in range(len(optical_power) - embedding_dim + 1):
            point = optical_power[i:i+embedding_dim]
            trajectory.append(point)
        
        trajectories.append(trajectory)

# 转换为NumPy数组
trajectories = np.array(trajectories)
lyapunov_exponents = []
for trajectory in trajectories:
    lyapunov_exponent = calculate_lyapunov_exponent(trajectory)
    lyapunov_exponents.append(lyapunov_exponent)

# 打印每个轨迹的李雅普诺夫指数
for i, lyapunov_exponent in enumerate(lyapunov_exponents):
    print(f"轨迹 {i+1} 的李雅普诺夫指数: {lyapunov_exponent}")
# 绘制相空间重构后的轨迹
fig = plt.figure(figsize=(12, 10))  # 设置图的尺寸
ax = fig.add_subplot(111, projection='3d')

for trajectory in trajectories:
    ax.plot(trajectory[:, 0], trajectory[:, 1], trajectory[:, 2])

ax.set_xlabel('维度1')
ax.set_ylabel('维度2')
ax.set_zlabel('维度3')
ax.set_title('相空间重构后的轨迹')

plt.show()
