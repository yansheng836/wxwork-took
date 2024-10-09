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
    # 检查带有数字括号的文件名
    match = re.match(r'^(.*?)(\s*\(\d+\))(\.\w+)$', filename)
    
    if match:
        base_name = match.group(1) + match.group(3)  # 获取不带括号的基础文件名
        base_path = os.path.join(directory, base_name)
        
        if os.path.exists(base_path):
            print(f'找到带括号的文件: {filename}')
            # 收集同一基础名的所有相关文件
            files_to_compare = [full_path, base_path]
            
            # 查找所有带数字括号的相关文件
            for file in os.listdir(directory):
                if re.match(rf'^{re.escape(match.group(1))}(\s*\(\d+\))(\.\w+)$', file):
                    files_to_compare.append(os.path.join(directory, file))
            
            # 找出最大文件
            max_file = None
            max_size = -1
            
            for file in files_to_compare:
                size = os.path.getsize(file)
                
                if size > max_size:
                    max_size = size
                    max_file = file
                elif size == max_size:
                    # 如果大小相同，优先选择带有数字括号的文件
                    if re.search(r'\s*\(\d+\)', os.path.basename(file)) and max_file and not re.search(r'\s*\(\d+\)', os.path.basename(max_file)):
                        print(f'相同  {max_file}')
                        print(f'相同1 {file}')
                        max_file = file
            
            # 删除较小的文件
            for file in files_to_compare:
                if file != max_file:
                    print(f'删除较小的文件: {file}')
                    #os.remove(file)

# 结束
print("文件处理完成。")