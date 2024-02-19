import os

# 定义要合并的文件夹路径
folder_path = "wallet"

# 定义要输出的合并后的文件路径
output_file_path = "wallet/bera_private_keys_hcy_auto_all.txt"
output_file_path2 = "wallet/bera_private_keys_hcy_auto_all2.txt"

# 打开要输出的文件，使用 'a' 模式以便追加内容
with open(output_file_path, 'a') as output_file:
    # 遍历文件夹中的所有文件
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        # 检查是否为文件
        if os.path.isfile(file_path) and 'auto_all' not in file_path and 'hcy_auto_' in file_path:
            print(file_path)
            # 打开文件并将内容写入输出文件
            with open(file_path, 'r') as input_file:
                output_file.write(input_file.read())

with open(output_file_path2, 'a') as output_file:
    # 遍历文件夹中的所有文件
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        # 检查是否为文件
        if os.path.isfile(file_path) and 'auto_all' not in file_path and 'hcy_auto_' not in file_path:
            print(file_path)
            # 打开文件并将内容写入输出文件
            with open(file_path, 'r') as input_file:
                output_file.write(input_file.read())