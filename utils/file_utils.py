#!/usr/bin/env python3

"""
文件工具
"""

import hashlib
import os
import re


def remove_emoji(directory):
    """
    删除特殊文件
    :return:
    """

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
            # 11.docx 编辑中的文件 ~$11.docx
            if '~$' in filename:
                print(f'文件：{full_path} ')
                # 2024年11月2日 这里需要注意，这类文件可能是只读的，不特殊处理会报错：PermissionError: [WinError 5] 拒绝访问。
                print(os.system(f"attrib -r +s {full_path}"))
                os.remove(full_path)
                print(f'删除特殊文件：{full_path} 成功')
            # sign = '; charset=UTF-8'
            # if sign in filename:
            #     new_path = full_path.replace(sign, '')
            #     # os.rename(full_path, new_path)
            #     print(f'重命名特殊文件：{full_path} to {new_path} 成功')


def remove_duplicate_has_brackets(directory):
    """
    删除带括号的重复文件
    :return:
    """

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
                        # os.remove(full_path)
                        print(f'删除重复图片：{full_path} 成功')
                    else:
                        # print(f'有括号的比较大，保留有括号的（实际上是删除无括号的，然后将有括号的重命名为无括号的）')
                        # os.remove(base_path)
                        # os.rename(full_path, base_path)
                        print(f'删除重复图片：{full_path} 成功')
                    print()


def remove_duplicate_name_jpg(directory):
    """
    删除名称重复的图片
    :return:
    """

    # 遍历目录下的所有文件
    for filename in os.listdir(directory):
        # 获取文件的完整路径
        full_path = os.path.join(directory, filename)

        # 如果是png文件
        if filename.endswith('.png') or filename.endswith('.gif'):
            # 去掉.png后缀并添加.jpg
            jpg_name = filename[:-4] + '.jpg'
            jpg_path = os.path.join(directory, jpg_name)
            # 检查是否有同名的jpg文件
            if os.path.exists(jpg_path):
                print(f'找到 {filename} 同名的 JPG 文件: {jpg_name}')
                # print(os.path.getsize(full_path))
                # print(os.path.getsize(jpg_path))
                # 删除空间比较小的文件，发现好像都是jpg比较小
                if os.path.getsize(full_path) >= os.path.getsize(jpg_path):
                    # print(f'JPG比较小')
                    # os.remove(jpg_path)
                    print(f'删除重复图片：{jpg_name} 成功')
                else:
                    # print(f'JPG比较大')
                    # os.remove(full_path)
                    print(f'删除重复图片：{full_path} 成功')
                print()


def remove_duplicate_content_file(directory):
    """
    删除内容重复（名称不同）的文件
    :return:
    """

    # 遍历目录下的所有文件
    file_list = os.listdir(directory)
    # print(file_list)
    # 移除目录，目录不能进行hash计算
    # i = 0
    dir_list = []
    for fname in file_list:
        # i = i+1
        n_fn = os.path.join(directory, fname)
        # print(f'fname: {fname}')
        if os.path.isdir(n_fn):
            # print(f'目录 {n_fn}')
            # print(f'file_list 长度 {len(file_list)}')
            # file_list.remove(fname)
            dir_list.append(fname)
            # print(f'file_list 长度 {len(file_list)}')
            # print(file_list)
    # 从 file_list 移除 dir_list 中的元素
    file_list = [x for x in file_list if x not in dir_list]
    # print(f'i的值为；{i}')
    # print(file_list)
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

        for j in range(i + 1, len(file_list)):
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

                # 如果其中一个文件含有特殊字符:'(' ,'- 副本'，直接删除，不再比较时间
                sign_arr = ['(', '- 副本']
                contains = any(element in filename for element in sign_arr)
                contains2 = any(element in filename2 for element in sign_arr)
                # 存在关键字时
                if contains or contains2:
                    if (contains and contains2) or contains:
                        print(os.system(f"attrib -r +s {full_path}"))
                        os.remove(full_path)
                        print(f'删除重复文件(1含关键字)：{full_path} 成功')
                    # elif contains:
                    #     # os.remove(full_path)
                    #     print(f'删除重复文件：{full_path} 成功')
                    elif contains2:
                        os.remove(full_path2)
                        print(f'删除重复文件(2含关键字2)：{full_path2} 成功')
                else:
                    # 如果都不包含关键字，走下面的逻辑
                    # 比较两个文件的创建时间
                    # print(os.path.getctime(full_path))
                    # print(os.path.getctime(full_path2))

                    # 取创建时间和修改时间之中的小者当做 “文件的创建时间”
                    # 这里用问号表达式不知道为什么不可以？？？
                    # filetime = (os.path.getctime(full_path) > os.path.getmtime(full_path)) ? (os.path.getctime(full_path)) :(os.path.getmtime(full_path))
                    filetime = os.path.getctime(full_path)
                    if filetime > os.path.getmtime(full_path):
                        filetime = os.path.getmtime(full_path)

                    filetime2 = os.path.getctime(full_path2)
                    if filetime2 > os.path.getmtime(full_path2):
                        filetime2 = os.path.getmtime(full_path2)

                    # print(f'filetime ：{filetime} ')
                    # print(f'filetime2：{filetime2} ')
                    if filetime <= filetime2:
                        # print(f'创建时间比较晚的是：{full_path2}，需删除')
                        os.remove(full_path2)
                        print(f'删除重复文件：{full_path2} 成功')
                    else:
                        # print(f'创建时间比较晚的是：{full_path}，需删除')
                        os.remove(full_path)
                        print(f'删除重复文件：{full_path} 成功')
                print()
            else:
                # print(f'{filename} 和 {filename2} 不相同')
                # print()
                continue


if __name__ == '__main__':

    # 设置目标目录
    # directory = r'D:\WXWork\1688850205828112\Cache\Image\2024-02'
    default_directory = r'D:\WXWork\1688850205828112\Cache\File'
    parent_directory = r'D:\WXWork\1688850205828112\Cache\File'
    parent_directory = r'D:\WXWork\1688850205828112\Cache\Video'
    parent_directory = r'F:\Program Files (x86)\Tencent\WeChat\WeChat Files\wxid_pj5d1j5jff0021\FileStorage\File'

    if os.path.isdir(parent_directory):
        # print(f'存在目录：{full_path}')
        sub_dirs = os.listdir(parent_directory)
        # print(type(sub_dirs))
        if len(sub_dirs) > 0:
            for sub_dir in sub_dirs:
                # print(f'打印目录内容： {sub_dir} ')
                full_path = os.path.join(parent_directory, sub_dir)
                if os.path.isdir(full_path):
                    print(f'打印目录中的目录： {full_path}')
                    # 调用逻辑删除文件
                    remove_emoji(full_path)
                    # # remove_duplicate_has_brackets(full_path)
                    # # remove_duplicate_name_jpg(full_path)
                    remove_duplicate_content_file(full_path)
                    # exit(0)
        else:
            print(f'该目录 {full_path}  为空，请输入正确的路径，可参考：{default_directory}')
    else:
        raise Exception(f'{parent_directory} 不是目录，请输入目录！')
