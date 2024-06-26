from figure import Figure
from random import choices
from yaml.loader import FullLoader
import logging
import yaml
import json
import os

# Config load
with open('config.yaml', 'r') as f_obj:
    config = yaml.load(f_obj, Loader=FullLoader)

# Config
img_size = config['image_size']
desc_len = config['desc_length']
circle_filepath = config['circle.path']['circle_filepath']
data_c_path = config['circle.path']['circle_data_path']
square_filepath = config['square.path']['square_filepath']
data_s_path = config['square.path']['square_data_path']
coords_filepath = config['coords_filepath']

# Logging settings
logging.basicConfig(level=logging.INFO, filename='prog1_log.log', filemode='w',
                    format="%(asctime)s %(levelname)s %(message)s")

# Create vector
coords = []
for i in range(desc_len):
    coords.append([choices(range(img_size), k=2) for x in range(2)])

# Saving coordinates
try:
    with open(coords_filepath) as f_obj:
        coords = json.load(f_obj)
except FileNotFoundError as err:
    logging.warning(f"File was not found at path <{coords_filepath}>.")
    with open(coords_filepath, 'w') as f_obj:
        json.dump(coords, f_obj)
        logging.info(f"File '{os.path.basename(f_obj.name)}' was created.")

# Circle probability table
circle = Figure(circle_filepath, coords)
circle_fern = circle.create_fern()
c_prob_table = circle.prob_table(circle_fern)

# Saving c_prob_table
with open(data_c_path, 'w') as f_obj:
    json.dump(c_prob_table, f_obj)
    logging.info(f"Circle probability table have been created on path <{data_c_path}>")

print(f"Probability table of Circle class:\n{c_prob_table}\n")

# Square probability table
square = Figure(square_filepath, coords)
square_fern = square.create_fern()
s_prob_table = square.prob_table(square_fern)

# Saving c_prob_table
with open(data_s_path, 'w') as f_obj:
    json.dump(s_prob_table, f_obj)
    logging.info(f"Square probability table have been created on path <{data_s_path}>")

print(f"Probability table of Square class:\n{s_prob_table}\n")
