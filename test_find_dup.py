import os
import hashlib


def find_duplicate_jpg_files(folder_path):
    file_hashes = {}
    duplicates = []
    print("进来了")
    # print(os.listdir(folder_path))
    for root, dirs, files in os.walk(folder_path):
        print(root)
        print(dirs)
        print(files)
        for file in files:
            if file.endswith('.png'):
                print(file)
                print(dirs)
                print(files)
                file_path = os.path.join(root, file)
                with open(file_path, 'rb') as f:
                    file_hash = hashlib.md5(f.read()).hexdigest()
                if file_hash in file_hashes:
                    duplicates.append((file_path, file_hashes[file_hash]))
                else:
                    file_hashes[file_hash] = file_path
    return duplicates


folder_path = f'D:\\WXWork\\1688850205828112\\Cache\\Image\\2023-111'
duplicate_files = find_duplicate_jpg_files(folder_path)

if duplicate_files:
    print("找到重复的 JPG 文件：")
    for file1, file2 in duplicate_files:
        print(f"{file1} 和 {file2} 内容相同。")
else:
    print("未找到内容相同的 JPG 文件。")
