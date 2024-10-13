#!/usr/bin/env python3
import hashlib
import os
import re


def remove_emoji(directory):
    """
    删除表情包
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
            # getsize单位是字节，例如：80.0 KB 即：80502
            # print(f'{full_path} 的大小为：{os.path.getsize(full_path)}')
            if os.path.getsize(full_path) < 15000:
                os.remove(full_path)
                print(f'删除小于15KB的图片：{full_path} 成功')
            if '.WeDrive' in filename:
                os.remove(full_path)
                print(f'删除特殊文件：{full_path} 成功')
            sign = '; charset=UTF-8'
            if sign in filename:
                new_path = full_path.replace(sign, '')
                os.rename(full_path, new_path)
                print(f'重命名特殊文件：{full_path} to {new_path} 成功')


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
                if os.path.exists(base_path):
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
                    os.remove(jpg_path)
                    print(f'删除重复图片：{jpg_name} 成功')
                else:
                    # print(f'JPG比较大')
                    os.remove(full_path)
                    print(f'删除重复图片：{full_path} 成功')
                print()


def remove_duplicate_content_pic(directory):
    """
    删除内容重复（名称不同）的文件
    :return:
    """

    # 遍历目录下的所有文件
    file_list = os.listdir(directory)

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


if __name__ == '__main__':

    # 设置目标目录
    # directory = r'D:\WXWork\1688850205828112\Cache\Image\2024-02'
    default_directory = r'D:\WXWork\1688850205828112\Cache\Image'
    parent_directory = r'D:\WXWork\1688850205828112\Cache\Image'

    if os.path.isdir(parent_directory):
        # print(f'存在目录：{full_path}')
        sub_dirs = os.listdir(parent_directory)
        print(type(sub_dirs))
        if len(sub_dirs) > 0:
            for sub_dir in sub_dirs:
                # print(f'打印目录内容： {sub_dir} ')
                full_path = os.path.join(parent_directory, sub_dir)
                if os.path.isdir(full_path):
                    print(f'打印目录中的目录： {full_path}')
                    # 调用逻辑删除文件
                    remove_emoji(full_path)
                    remove_duplicate_has_brackets(full_path)
                    # remove_duplicate_name_jpg(full_path)
                    # remove_duplicate_content_pic(full_path)
                    # exit(0)
        else:
            print(f'该目录 {full_path}  为空，请输入正确的路径，可参考：{default_directory}')
    else:
        raise Exception(f'{parent_directory} 不是目录，请输入目录！')
