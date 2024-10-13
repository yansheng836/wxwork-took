#!/usr/bin/env python3

import os
import re

# 设置目标目录
#directory = r'D:\WXWork\1688850205828112\Cache\Image\2023-11'
#directory = r'D:\WXWork\1688850205828112\Cache\Image\2023-12'
directory = r'D:\WXWork\1688850205828112\Cache\Image\2024-02'

# 用于存储找到的jpg文件名
jpg_files = {}

# 遍历目录下的所有文件
for filename in os.listdir(directory):
    # 获取文件的完整路径
    full_path = os.path.join(directory, filename)

    # 如果是png文件
    if filename.endswith('.png'):
        # 检查是否有同名的jpg文件
        jpg_name = filename[:-4] + '.jpg'  # 去掉.png后缀并添加.jpg
        jpg_path = os.path.join(directory, jpg_name)
        if os.path.exists(jpg_path):
            #print(f'找到同名的 JPG 文件: {jpg_name}')
            print(f'找到 {filename} 同名的 JPG 文件: {jpg_name}')
            os.remove(jpg_path)  # 删除JPG文件

    #continue

for filename in os.listdir(directory):
    # 获取文件的完整路径
    full_path = os.path.join(directory, filename)
    match = re.match(r'^(.*?)(\s*\(\d+\))(\.\w+)$', filename)
    if match:
        base_name = match.group(1) + match.group(3)  # 获取不带括号的文件名
        base_path = os.path.join(directory, base_name)
        
        if os.path.exists(base_path):
            print(f'找到带括号的文件: {filename}')
            # 对同一基础名的文件进行比较，找出最大文件
            files_to_compare = [full_path, base_path]
            
            max_file = max(files_to_compare, key=os.path.getsize)
            
            # 删除较小的文件
            for file in files_to_compare:
                #if file != max_file:
                if file < max_file:
                    print(f'max_file的文件: {max_file}')
                    print(f'删除较小的文件: {file}')
                    #os.remove(file)
                    print()
                if file == max_file:
                    print('大小相同，删除带括号的')
                    print(f'max_file的文件: {max_file}')
                    print(f'file的文件: {file}')
                    if '(' in file:
                        print(f'带括号的文件: {file}')
                    else:
                        print(f'带括号的文件: {max_file}')
                    #os.remove(file)
                    print()

