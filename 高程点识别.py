import ezdxf
import os

def extract_layer_inserts(filename, layer_name):
    doc = ezdxf.readfile(filename)
    modelspace = doc.modelspace()
    inserts = []

    for entity in modelspace:
        if entity.dxftype() == 'INSERT' and entity.dxf.layer == layer_name:
            inserts.append(entity)

    return inserts

# 文件信息
folder_path = r"C:\Users\Alize\Desktop\项目投标"
filename = "高程点.dxf"
file_path = os.path.join(folder_path, filename)

# 图层名称
layer_name = "V-NODE-TEXT"

# 提取图层内的块参照
layer_inserts = extract_layer_inserts(file_path, layer_name)

# 构建保存数据的文件路径
output_file_path = os.path.join(folder_path, "块参照位置信息.xyz")

# 保存块参照的位置信息
with open(output_file_path, 'w') as file:
    for insert in layer_inserts:
        location = insert.dxf.insert
        x, y, z = location
        file.write(f"{x} {y} {z}\n")

print(f"位置信息已保存至文件: {output_file_path}")
