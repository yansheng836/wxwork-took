#!/usr/bin/env python3

import os

# 设置目标目录
# directory = r'D:\WXWork\1688850205828112\Cache\Image\2023-11'
# directory = r'D:\WXWork\1688850205828112\Cache\Image\2023-12'
# directory = r'D:\WXWork\1688850205828112\Cache\Image\2024-02'
# F:\Program Files (x86)\Tencent\WeChat\WeChat Files\wxid_pj5d1j5jff0021\FileStorage\File\2024-10
# D:\WXWork\1688850205828112\Cache\Image\2023-11
directory = r'D:\WXWork\1688850205828112\Cache\Image\2023-07'

# 用于存储找到的jpg文件名
jpg_files = {}

# 遍历目录下的所有文件
for filename in os.listdir(directory):
    # 获取文件的完整路径
    full_path = os.path.join(directory, filename)
    if os.path.isdir(full_path):
        # print(f'存在目录：{full_path}')
        if len(os.listdir(full_path)) == 0:
            # print(f'存在空目录：{full_path}')
            os.removedirs(full_path)
            print(f'删除空目录：{full_path} 成功')
    else:
        # getsize单位是字节，例如：80.0 KB 即：80502
        # print(f'{full_path} 的大小为：{os.path.getsize(full_path)}')
        if os.path.getsize(full_path) < 15000:
            os.remove(full_path)
            print(f'删除小于15KB的图片：{full_path} 成功')
        if 'charset' in filename or '.WeDrive' in filename:
            os.remove(full_path)
            print(f'删除特殊文件：{full_path} 成功')
