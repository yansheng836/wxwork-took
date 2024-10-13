#!/usr/bin/python3
# coding=utf-8

"""
删除带括号的重复图片
"""

import os
import re

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
    # 如果是带有数字括号的文件名
    # match = re.match(r'^(.*?)(\s*\(\d+\))\.jpg$', filename)
    match = re.match(r'^(.*?)(\s*\(\d+\))(\.\w+)$', filename)
    # print(match)
    if match:
        for suffix in ['.jpg', '.png', '.gif']:
            # print(suffix)
            # exit(0)
            # continue
            # base_name = match.group(1) + '.jpg'  # 获取不带括号的文件名
            base_name = match.group(1) + suffix  # 获取不带括号的文件名
            base_path = os.path.join(directory, base_name)
            if os.path.exists(full_path) and os.path.exists(base_path):
                print(f'找到带括号的 JPG 文件: {filename}')
                print(f'存在无括号的 JPG 文件: {base_name}')
                # print(os.path.getsize(full_path))
                # print(os.path.getsize(base_path))
                # os.remove(full_path)  # 删除带有括号的JPG文件
                # 删除空间比较小的文件，发现好像都是jpg比较小
                if os.path.getsize(full_path) <= os.path.getsize(base_path):
                    # print(f'没有括号的比较大，或者是一样的，保留没有括号的')
                    os.remove(full_path)
                    print(f'删除重复图片：{full_path} 成功')
                else:
                    # print(f'有括号的比较大，保留有括号的（实际上是删除无括号的，然后将有括号的重命名为无括号的）')
                    os.remove(base_path)
                    os.rename(full_path, base_path)
                    print(f'删除重复图片：{full_path} 成功')
                print()
