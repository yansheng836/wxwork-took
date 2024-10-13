#!/usr/bin/python3
# coding=utf-8

"""
删除内容重复的图片
"""

import os
import hashlib

directory = r'D:\WXWork\1688850205828112\Cache\Image\2023-11'

# 遍历目录下的所有文件
file_list = os.listdir(directory)
# 移除目录，目录不能进行hash计算
for fname in file_list:
    n_fn = os.path.join(directory, fname)
    if os.path.isdir(n_fn):
        file_list.remove(fname)
dup_list = []

# 用简单的for循环，方便控制
file_hashs = []
for i in range(0, len(file_list)):
    # print(i)
    filename = file_list[i]
    # print(filename)
    # 获取文件的完整路径
    full_path = os.path.join(directory, filename)
    # print(f"外层循环的文件:{filename}")
    if i == 0:
        with open(full_path, 'rb') as f:
            file_hash = hashlib.md5(f.read()).hexdigest()
        file_hashs.append(file_hash)
    else:
        file_hash = file_hashs[i]
    # 记录

    for j in range(i+1, len(file_list)):
        # 获取文件的完整路径
        filename2 = file_list[j]
        full_path2 = os.path.join(directory, filename2)
        # print(f" 内层循环的文件:{filename2}")
        if i == 0:
            with open(full_path2, 'rb') as f2:
                file_hash2 = hashlib.md5(f2.read()).hexdigest()
            file_hashs.append(file_hash2)
        else:
            file_hash2 = file_hashs[j]

        if file_hash == file_hash2:
            print(f'{filename} 和 {filename2} 相同')
            # 因为后面会删除文件，需要保证两个文件都不为空，不然查看和处理文件会报错
            if os.path.exists(full_path) is False:
                break
            if os.path.exists(full_path2) is False:
                continue
            # 比较两个文件的创建时间
            # print(os.path.getctime(full_path))
            # print(os.path.getctime(full_path2))
            if os.path.getctime(full_path) == os.path.getctime(full_path2):
                # 如果创建时间相同，再比较修改时间
                # 其实不会相等，时间可以精确到小数点后7位，如：1720612917.2837794，1720612917.408793
                if os.path.getmtime(full_path) <= os.path.getmtime(full_path2):
                    # print(f'创建时间比较晚的是：{full_path2}，需删除')
                    os.remove(full_path2)
                    print(f'删除重复图片：{full_path2} 成功')
                else:
                    # print(f'创建时间比较晚的是：{full_path}，需删除')
                    os.remove(full_path)
                    print(f'删除重复图片：{full_path} 成功')
            elif os.path.getctime(full_path) < os.path.getctime(full_path2):
                # print(f'创建时间比较晚的是：{full_path2}，需删除')
                os.remove(full_path2)
                print(f'删除重复图片：{full_path2} 成功')
            else:
                # print(f'创建时间比较晚的是：{full_path}，需删除')
                os.remove(full_path)
                print(f'删除重复图片：{full_path} 成功')
            print()
        else:
            # print(f'{filename} 和 {filename2} 不相同')
            # print()
            continue
