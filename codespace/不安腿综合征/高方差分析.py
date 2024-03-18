import json
import os
import statistics
import pandas as pd

json_dir = 'clusters/cluster_3_high_variance'
json_files = os.listdir(json_dir)

# 创建空的DataFrame
data_frame = pd.DataFrame(columns=['dataname', 'opticalpower', 'totalMotion'])

for file in json_files:
    with open(os.path.join(json_dir, file), 'r') as f:
        data = json.load(f)
        optical_power = data['opticalpower']
        total_motion = data['totalMotion']
        optical_power_average = statistics.mean(optical_power)
        
        # 将每个文件的数据添加到DataFrame中
        data_frame = data_frame.append({
            'dataname': file,
            'opticalpower': optical_power_average,
            'totalMotion': total_motion
        }, ignore_index=True)

# 保存DataFrame为CSV文件
data_frame.to_csv('结果表格.csv', index=False)
