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
    directory = r'C:\Users\Léonard\Downloads\data\Detection_Train_Set\Detection_Train_Set_Json'
    json_files = get_all_json_paths(directory)
    devisubox_files = [x for x in json_files if "Devisubox" in x]
    marseille_files = [x for x in json_files if "Marseille" in x]
    biosav_files = [x for x in json_files if "BioSAV" in x]
    nouveaucampus_files = [x for x in json_files if "Nouveau" in x]
    roissy_files = [x for x in json_files if "Roissy" in x]
    print("Total: {}, BioSAV: {}, Devisubox: {}, Marseille: {}\
, Nouveau Campus: {}, Roissy: {}".format(len(json_files),
                                             len(biosav_files),
                                             len(devisubox_files),
                                             len(marseille_files),
                                             len(nouveaucampus_files),
                                             len(roissy_files)))
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