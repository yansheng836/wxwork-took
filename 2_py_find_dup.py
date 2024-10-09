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
# 遍历目录下的所有文件
for filename in os.listdir(directory):
    # 获取文件的完整路径
    full_path = os.path.join(directory, filename)
    # 如果是带有数字括号的文件名
    #match = re.match(r'^(.*?)(\s*\(\d+\))\.jpg$', filename)
    match = re.match(r'^(.*?)(\s*\(\d+\))(\.\w+)$', filename)
    if match:
        base_name = match.group(1) + '.jpg'  # 获取不带括号的文件名
        base_path = os.path.join(directory, base_name)
        if os.path.exists(base_path):
            print(f'找到无括号的 JPG 文件: {base_name}')
            print(f'找到带括号的 JPG 文件: {filename}')
            #os.remove(full_path)  # 删除带有括号的JPG文件
            #print()

