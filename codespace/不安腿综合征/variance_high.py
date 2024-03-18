import json
import os
import shutil
import statistics
json_dir = 'clusters/cluster_3'
output_dir = 'clusters/cluster_3_high_variance'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

json_files = os.listdir(json_dir)

for file in json_files:
    with open(os.path.join(json_dir, file), 'r') as f:
        data = json.load(f)
        optical_power = data['opticalpower']
        variance = statistics.variance(optical_power)
        
        if variance > 0.5:
            output_file = os.path.join(output_dir, file)
            shutil.copyfile(os.path.join(json_dir, file), output_file)
            print(f'复制文件 {file} 到目标文件夹')

print('复制完成')
