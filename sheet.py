import os
import tabula
import pandas as pd

# 设置路径
path = r"C:\Users\Alize\Desktop\weather in Barranquilla"

# 创建一个Excel文件
writer = pd.ExcelWriter(os.path.join(path, 'weather_data.xlsx'), engine='xlsxwriter')

# 循环遍历指定路径内的所有PDF文件
for file_name in os.listdir(path):
    if file_name.endswith('.pdf'):
        try:
            # 提取PDF文件中的表格数据
            tables = tabula.read_pdf(os.path.join(path, file_name), pages='all', encoding='gbk')

            # 将每个表格数据保存为单独的Excel工作表
            for i, df in enumerate(tables):
                sheet_name = f"{file_name[:-4]}_{i+1}"
                df.to_excel(writer, sheet_name=sheet_name, index=False)

        except Exception as e:
            print(f"Error processing file {file_name}: {str(e)}")

# 关闭Excel文件
writer.save()
