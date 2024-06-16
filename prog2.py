from figure import Figure
from yaml.loader import FullLoader
import logging
import cv2
import json
import yaml
import math
import os

# Config load
with open('config.yaml', 'r') as f_obj:
    config = yaml.load(f_obj, Loader=FullLoader)

data_filename = config['coords_filepath']
data_c_path = config['circle.path']['circle_data_path']
data_s_path = config['square.path']['square_data_path']

# Logging settings
logging.basicConfig(level=logging.INFO, filename="prog2_log.log", filemode='w',
                    format="%(asctime)s %(levelname)s %(message)s")

def file_load(path: str | os.PathLike):
    try:
        with open(path) as f_obj:
            var = json.load(f_obj)
            return var
    except FileNotFoundError as error:
        logging.error(f"{error.strerror}: '{error.filename}'")
        raise error


def prob_list(list_, result):
    prob_l = []
    for index, elem in enumerate(list_):
        prob_l.append(elem[result[index]])
    return prob_l

# Vector load
coords = file_load(data_filename)

# Circle prob. table load
c_prob_table = file_load(data_c_path)

print(f"Probability table of Circle class:\n{c_prob_table}\n")

# Square prob. table load
s_prob_table = file_load(data_s_path)

print(f"Probability table of Square class:\n{s_prob_table}\n")

# ====== Тестовое изображение ======
img = cv2.imread('img/test_square.png', cv2.IMREAD_GRAYSCALE)
test_fern = Figure.bin_attr_fern(img, coords)
test_split = Figure.fern_split(test_fern, 3)
res = list(map(lambda x: int(x, 2), test_split))

p_circle = round(math.prod(prob_list(c_prob_table, res)), 3)
p_square = round(math.prod(prob_list(s_prob_table, res)), 3)

if p_circle > p_square:
    print("Изображение относится к классу 'Круг'.")
else:
    print("Изображение относится к классу 'Квадрат'.")
