import os
import glob
import shutil

# 定义文件夹路径
folder_path = r'C:\Users\Alize\Desktop\1800耙迹线'
output_folder_path = os.path.join(folder_path, 'updated_files')

# 创建输出文件夹
os.makedirs(output_folder_path, exist_ok=True)

# 获取文件夹中所有.ppl文件的路径
file_paths = glob.glob(os.path.join(folder_path, '*.ppl'))

# 循环处理每个文件
for file_path in file_paths:
    # 读取原始文件内容
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # 保留第一行
    first_line = lines[0]
    lines = lines[1:]

    # 对每一行进行减一运算并替换数字
    updated_lines = []
    for line in lines:
        values = line.split(',')

        # 获取要减一的数字
        number_start = line.find('   ') + 3  # 找到3个连续空格的位置并加上3
        number_end = line.find(',', number_start)
        if number_end == -1:
            number_end = len(line)
        number_str = line[number_start:number_end].strip()

        # 减一运算并判断是否小于等于8
        if number_str != '':
            number = float(number_str)
            updated_number = number - 1
            if updated_number <= 8:
                continue  # 跳过此行
            updated_number_str = '{:.2f}'.format(updated_number)
        else:
            updated_number_str = ''
        
        # 替换原有数字并更新行数据
        line = line[:number_start] + updated_number_str + line[number_end:]
        updated_lines.append(line)

    # 如果所有行都小于等于8，则不生成更新后的文件
    if len(updated_lines) == 0:
        continue

    # 构建更新后的文件路径，保持原文件名不变
    file_name = os.path.basename(file_path)
    new_file_path = os.path.join(output_folder_path, file_name)

    # 将更新后的内容写入新文件
    with open(new_file_path, 'w') as new_file:
        new_file.write(first_line)  # 保留第一行
        new_file.writelines(updated_lines)

# 移动输出文件夹到目标路径
target_folder_path = os.path.join(folder_path, 'updated_files')
shutil.move(output_folder_path, target_folder_path)


