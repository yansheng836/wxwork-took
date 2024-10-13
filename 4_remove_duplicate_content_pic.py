import re
import os
import hashlib

directory = r'D:\WXWork\1688850205828112\Cache\Image\2023-07'

# 遍历目录下的所有文件
file_list = os.listdir(directory)
dup_list = []
for filename in file_list:
    # 获取文件的完整路径
    full_path = os.path.join(directory, filename)
    # print(f"外层循环的文件:{filename}")
    with open(full_path, 'rb') as f:
        file_hash = hashlib.md5(f.read()).hexdigest()

    for filename2 in file_list:
        if filename == filename2:
            continue
        # 获取文件的完整路径
        full_path2 = os.path.join(directory, filename2)
        # print(f" 内层循环的文件:{filename2}")
        with open(full_path2, 'rb') as f2:
            file_hash2 = hashlib.md5(f2.read()).hexdigest()
        if file_hash == file_hash2:
            print(f'{filename} 和 {filename2} 相同')
            # 比较两个文件的创建时间
            print(os.path.getctime(full_path))
            print(os.path.getctime(full_path2))
            if os.path.getmtime(full_path) == os.path.getmtime(full_path2):
                print()
            else:
                print()
        else:
            # print(f'{filename} 和 {filename2} 不相同')
            # print()
            continue
