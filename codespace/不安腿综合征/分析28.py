import json
import os
import matplotlib.pyplot as plt

json_dir = 'signal_precheck'
json_files = os.listdir(json_dir)

total_motion_values = []

for file in json_files:
    with open(os.path.join(json_dir, file), 'r') as f:
        data = json.load(f)
        total_motion = data['totalMotion']
        total_motion_values.append(total_motion)

# 绘制分布图
plt.hist(total_motion_values, bins=10)
plt.xlabel('totalMotion')
plt.ylabel('Frequency')
plt.title('Total Motion Distribution')
plt.show()
