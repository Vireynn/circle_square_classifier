from figure import Figure
from random import choices
import json

# Прописываем пути к изображениям
circle_filename = 'img/circle/*.png'
square_filename = 'img/square/*.png'
img_size = 63

# ======== Создание векторов ========
desc_len = 9  # длина дескриптора
coords = []
for i in range(desc_len):
    coords.append([choices(range(img_size), k=2) for x in range(2)])
# сохранение координат
data_filename = "data/coords.json"
try:
    with open(data_filename) as f_obj:
        coords = json.load(f_obj)
except FileNotFoundError:
    with open(data_filename, 'w') as f_obj:
        json.dump(coords, f_obj)

# ===== Создание экземпляра Circle =====
circle = Figure(circle_filename, coords)
circle_fern = circle.create_fern()
c_prob_table = circle.prob_table(circle_fern)

# сохранение c_prob_table
data_c_path = 'data/c_prob_table.json'
with open(data_c_path, 'w') as f_obj:
    json.dump(c_prob_table, f_obj)

print(f"Таблица вероятностей класса Circle:\n{c_prob_table}\n")

# ===== Создание экземпляра Square =====
square = Figure(square_filename, coords)
square_fern = square.create_fern()
s_prob_table = square.prob_table(square_fern)

# сохранение/загрузка s_prob_table
data_s_path = 'data/s_prob_table.json'
with open(data_s_path, 'w') as f_obj:
    json.dump(s_prob_table, f_obj)

print(f"Таблица вероятностей класса Square:\n{s_prob_table}\n")