import pandas as pd
import os
import glob

# 获取指定文件夹中的所有xyz文件路径
folder_path = r'C:\Users\Alize\Desktop\负水深转换'
file_paths = glob.glob(folder_path + '/*.xyz')

# 创建存储修改后文件的文件夹
output_folder_path = os.path.join(folder_path, 'modified')
os.makedirs(output_folder_path, exist_ok=True)

# 遍历所有文件进行处理
for file_path in file_paths:
    # 读取XYZ文件
    df = pd.read_csv(file_path, delimiter=' ', header=None, dtype=str)

    # 修改最后一个数字为负数
    df.iloc[:, -1] = '-' + df.iloc[:, -1]

    # 提取文件名
    file_name = os.path.basename(file_path)

    # 构建输出文件路径
    output_file_path = os.path.join(output_folder_path, file_name)

    # 保存修改后的结果到新文件
    df.to_csv(output_file_path, sep=' ', index=False, header=False)
