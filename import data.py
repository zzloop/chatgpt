import os
from PyPDF2 import PdfReader  # 导入PdfReader类
import pandas as pd

# 设置路径
path = r"C:\Users\Alize\Desktop\weather in Barranquilla"

# 创建一个Excel文件
writer = pd.ExcelWriter(os.path.join(path, 'weather_data.xlsx'), engine='xlsxwriter')

# 循环遍历指定路径内的所有PDF文件
for file_name in os.listdir(path):
    if file_name.endswith('.pdf'):
        try:
            # 打开PDF文件并读取第一页和第二页
            with open(os.path.join(path, file_name), 'rb') as pdf_file:
                reader = PdfReader(pdf_file)
                if len(reader.pages) >= 2:
                    first_page_text = reader.pages[0].extract_text().split('\n')[0].strip()

                    # 提取第二页的表格数据
                    table_data = []
                    for row in reader.pages[1].extract_text().split('\n'):
                        table_data.append(row.split('\t'))

                    # 将表格数据转换为DataFrame
                    df = pd.DataFrame(table_data[1:], columns=table_data[0])

                    # 将第一页的首段文字和第二页的表格数据保存在Excel文件中
                    df.to_excel(writer, sheet_name=file_name[:-4], index=False)
                    worksheet = writer.sheets[file_name[:-4]]
                    worksheet.write(0, 0, first_page_text)
                else:
                    print(f"File {file_name} does not have enough pages.")

        except Exception as e:
            print(f"Error processing file {file_name}: {str(e)}")

# 关闭Excel文件
writer.save()






