"""

"""

import os

# 设置目标目录
# directory = r'D:\WXWork\1688850205828112\Cache\Image\2023-11'
# directory = r'D:\WXWork\1688850205828112\Cache\Image\2023-12'
# directory = r'D:\WXWork\1688850205828112\Cache\Image\2024-02'
# F:\Program Files (x86)\Tencent\WeChat\WeChat Files\wxid_pj5d1j5jff0021\FileStorage\File\2024-10
# D:\WXWork\1688850205828112\Cache\Image\2023-11
directory = r'D:\WXWork\1688850205828112\Cache\Image\2023-10'

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
            # print(f'找到同名的 JPG 文件: {jpg_name}')
            print(f'找到 {filename} 同名的 JPG 文件: {jpg_name}')
            # print(os.path.getsize(full_path))
            # print(os.path.getsize(jpg_path))
            # 删除空间比较小的文件，发现好像都是jpg比较小
            if os.path.getsize(full_path) >= os.path.getsize(jpg_path):
                # print(f'JPG比较小')
                os.remove(jpg_path)  # 删除JPG文件
            else:
                print(f'JPG比较大')
