import os
import glob
import subprocess
import pandas as pd

# 定义PDF所在文件夹路径
pdf_folder_path = r"C:\Users\Alize\Desktop\weather in Barranquilla"

# 定义Excel文件名
excel_file_name = "converted_files.xlsx"

# 定义Adobe Acrobat软件路径
acrobat_path = r"D:\Program Files (x86)\Adobe\Acrobat DC\Acrobat\Acrobat.exe"

# 调用Adobe Acrobat命令行工具将PDF文件转换为Excel文件
for pdf_file_path in glob.glob(os.path.join(pdf_folder_path, "*.pdf")):
    excel_file_path = os.path.splitext(pdf_file_path)[0] + ".xlsx"
    command = [acrobat_path, "/N", "/T", excel_file_path, pdf_file_path, "Excel Worksheet"]
    subprocess.run(command, shell=True, check=True)

# 将所有Excel文件读取为DataFrame对象，并合并到一个DataFrame中
df_list = []
for excel_file_path in glob.glob(os.path.join(pdf_folder_path, "*.xlsx")):
    df = pd.read_excel(excel_file_path)
    df_list.append(df)
merged_df = pd.concat(df_list, ignore_index=True)

# 将合并后的DataFrame存储到一个Excel文件中
merged_df.to_excel(excel_file_name, index=False)

print("所有PDF文件已成功转换成Excel文件并保存在{}中".format(excel_file_name))
