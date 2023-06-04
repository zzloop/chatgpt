import os
import pandas as pd
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter, PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
import openpyxl
from openpyxl.utils.dataframe import dataframe_to_rows

# 定义函数将 PDF 文件转换为文本
def pdf_to_text(path):
    rsrcmgr = PDFResourceManager()
    codec = 'utf-8'
    laparams = LAParams()
    with StringIO() as output:
        with TextConverter(rsrcmgr, output, codec=codec, laparams=laparams) as converter:
            with open(path, 'rb') as file:
                interpreter = PDFPageInterpreter(rsrcmgr, converter)
                for page in PDFPage.get_pages(file):
                    interpreter.process_page(page)
        text = output.getvalue()
    return text

# 定义函数将文本转换为 Excel 表格
def text_to_excel(text, ws):
    data = []
    for line in text.split('\n'):
        row = [cell.strip() for cell in line.split('\t')]
        data.append(row)
    df = pd.DataFrame(data)
    for r in dataframe_to_rows(df, index=False, header=False):
        ws.append(r)

# 批量转换
folder_path = "C:\\Users\\Alize\\Desktop\\weather in Barranquilla"
output_path = "C:\\Users\\Alize\\Desktop\\weather in Barranquilla\\output.xlsx"
wb = openpyxl.Workbook()

# 遍历文件夹中的所有 PDF 文件并转换为 Excel 表格
for filename in os.listdir(folder_path):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(folder_path, filename)
        sheet_name = os.path.splitext(filename)[0]
        ws = wb.create_sheet(sheet_name)
        text = pdf_to_text(pdf_path)
        text_to_excel(text, ws)

# 删除默认的工作表
wb.remove(wb.worksheets[0])

# 保存 Excel 文件
wb.save(output_path)



