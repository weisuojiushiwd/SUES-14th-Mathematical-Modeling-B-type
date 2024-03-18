import json
import os
import statistics
import matplotlib.pyplot as plt
import matplotlib
# 设置字体为楷体
matplotlib.rcParams['font.sans-serif'] = ['KaiTi']
plt.rc('axes', unicode_minus=False)

json_dir = 'clusters/cluster_3'
json_files = os.listdir(json_dir)

medians = []
averages = []
variances = []

for file in json_files:
    with open(os.path.join(json_dir, file), 'r') as f:
        data = json.load(f)
        optical_power = data['opticalpower']
        median = statistics.median(optical_power)
        average = statistics.mean(optical_power)
        variance = statistics.variance(optical_power)
        medians.append(median)
        averages.append(average)
        variances.append(variance)

# 创建一个画布和三个子图
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 10))

# 绘制中位数散点图
ax1.scatter(range(len(medians)), medians)
ax1.set_xlabel('JSON文件编号')
ax1.set_ylabel('中位数')
ax1.set_title('每个JSON的中位数')

# 绘制平均数散点图
ax2.scatter(range(len(averages)), averages)
ax2.set_xlabel('JSON文件编号')
ax2.set_ylabel('平均数')
ax2.set_title('每个JSON的平均数')

# 绘制方差散点图
ax3.scatter(range(len(variances)), variances)
ax3.set_xlabel('JSON文件编号')
ax3.set_ylabel('方差')
ax3.set_title('每个JSON的方差')

# 调整子图之间的间距
plt.tight_layout()

# 显示图形
plt.show()
