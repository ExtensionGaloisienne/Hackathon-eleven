# script generant la heatmap a partir des donnees json

import os
import random
import json


# Choix d'un fichier aléatoire
def choose_random_file(directory):
    return random.choice(os.listdir(directory))


# Choix d'un fichier json aléatoire
def get_random_json_path(directory):
    return os.path.join(directory, choose_random_file(directory))


def get_all_json_paths(directory):
    return [os.path.join(directory, json_file) for json_file in os.listdir(directory)]


def heatmap():
    random.seed()
    directory = "C:\\Users\\Léonard\\Downloads\\data\\Detection_Test_Set\\Detection_Test_Set_Json"
    json_files = get_all_json_paths(directory)
    json_data_list = []
    for json_file in json_files:
        with open(json_file) as f:
            try:
                json_data = json.load(f)
                json_data_list.append(json_data)
            except json.JSONDecodeError:
                print("Couldn't decode file {}".format(json_file))
    return 0

heatmap()