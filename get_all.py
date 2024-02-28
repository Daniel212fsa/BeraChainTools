import os
import math

# 定义要合并的文件夹路径
folder_path = "wallet"


# 定义要输出的合并后的文件路径
# output_file_path = "wallet/bera_private_keys_hcy_auto_all.txt"
# # output_file_path2 = "wallet/bera_private_keys_hcy_auto_all_key.txt"

# 打开要输出的文件，使用 'a' 模式以便追加内容

def get_content():
    content_list = []
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        # 检查是否为文件
        if os.path.isfile(file_path) and 'auto_all' not in file_path and 'hcy_auto_' in file_path:
            with open(file_path, 'r') as input_file:
                content_list.append(input_file.read())
    return content_list
            # arr[f'wallet/bera_private_keys_hcy_auto_all_{t}.txt'].append(input_file.read())
            # #     output_file.write(input_file.read())
    # return output_file_path, content_list,arr


def group_list(lst, size):
    return [lst[i:i+size] for i in range(0, len(lst), size)]


result = group_list(get_content(), 10)
for group_index, group in enumerate(result):
    file_name = f"wallet/bera_private_keys_hcy_auto_all_{group_index}.txt"
    # a 追加模式
    # w 非追加模式
    with open(file_name, 'w') as output_file:
        for item_index, item in enumerate(group):
            output_file.write(item)






# with open(output_file_path2, 'a') as output_file:
#     # 遍历文件夹中的所有文件
#     for file_name in os.listdir(folder_path):
#         file_path = os.path.join(folder_path, file_name)
#         # 检查是否为文件
#         if os.path.isfile(file_path) and 'auto_all' not in file_path and 'hcy_auto_' not in file_path:
#             print(file_path)
#             # 打开文件并将内容写入输出文件
#             with open(file_path, 'r') as input_file:
#                 output_file.write(input_file.read())
