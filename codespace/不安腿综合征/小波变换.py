import json
import os
import pywt
import numpy as np

json_dir = 'clusters/cluster_3'
json_files = os.listdir(json_dir)

for file in json_files:
    with open(os.path.join(json_dir, file), 'r') as f:
        data = json.load(f)
        optical_power = data['opticalpower']
        
        # 执行小波变换
        coeffs = pywt.wavedec(optical_power, 'db1')  
        
        # 打印每个 cA
        print(f"JSON 文件 {file} 的 cA:")
        for i, cA in enumerate(coeffs[:-1]):
            print(f"cA{len(coeffs)-i}: {cA}")
        print("-------------------")
