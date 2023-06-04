import re

# 读取单元格中的值
cell_value = "Área Costera: Cielo poco nuboso a nuboso. Viento de dirección Noreste rolando a Este,, con velocidades de 5 a 15 nudos (Fuerza 2-4). Temperatura ambiente oscilará entre 24°C, a 29°C., , Área Marítima: Viento de dirección Noreste rolando a Este-noreste, con velocidades de, 17 a 28 nudos (Fuerza 5-7). Altura del oleaje oscilará entre 1.0 a 1.6 metros (Mar 3-4)."

# 提取区域天气等信息
area_pattern = r"Área Costera: (.*?), , Área Marítima: (.*)"
area_match = re.search(area_pattern, cell_value)
if area_match:
    coastal_area = area_match.group(1)
    marine_area = area_match.group(2)
    print("Coastal Area:", coastal_area)
    print("Marine Area:", marine_area)

    # 提取海浪高度信息
    wave_pattern = r"Altura del oleaje oscilará entre (\d+\.\d+) a (\d+\.\d+) metros \(Mar (\d+-\d+)\)"
    wave_match = re.search(wave_pattern, marine_area)
    if wave_match:
        min_wave_height = wave_match.group(1)
        max_wave_height = wave_match.group(2)
        wave_mar = wave_match.group(3)
        print("Wave Height:", min_wave_height, "-", max_wave_height, "meters (Mar", wave_mar, ")")
    
    # 提取其他信息
    other_pattern = r"Cielo (.*?). Viento de dirección (.*?), con velocidades de, (\d+) a (\d+) nudos .*?Temperatura ambiente oscilará entre (\d+)°C, a (\d+)°C"
    other_match = re.search(other_pattern, coastal_area)
    if other_match:
        sky = other_match.group(1)
        wind_direction = other_match.group(2)
        min_wind_speed = other_match.group(3)
        max_wind_speed = other_match.group(4)
        min_temp = other_match.group(5)
        max_temp = other_match.group(6)
        print("Sky:", sky)
        print("Wind Direction:", wind_direction)
        print("Wind Speed:", min_wind_speed, "-", max_wind_speed, "nudos")
        print("Temperature:", min_temp, "°C -", max_temp, "°C")
