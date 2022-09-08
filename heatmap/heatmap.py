# script generant la heatmap a partir des donnees json

import os
import random
import json
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


# Choix d'un fichier aléatoire
def choose_random_file(directory):
    return random.choice(os.listdir(directory))


def show_json_data(json_list):
    for x in json_list:
        print(x)


# Choix d'un fichier json aléatoire
def get_random_json_path(directory):
    return os.path.join(directory, choose_random_file(directory))


def get_all_json_paths(directory):
    return [os.path.join(directory, json_file) for json_file in os.listdir(directory)]


def filter_by_chantier(json_files, name):
    return [x for x in json_files if name in x]
def heatmap():
    random.seed()
    directory = r'C:\Users\Léonard\Downloads\data\Detection_Train_Set\Detection_Train_Set_Json'
    json_files = get_all_json_paths(directory)
    devisubox_files = filter_by_chantier(json_files, "Devisubox")
    marseille_files = filter_by_chantier(json_files, "Marseille")
    biosav_files = filter_by_chantier(json_files, "BioSAV")
    nouveaucampus_files = filter_by_chantier(json_files, "Nouveau")
    roissy_files = filter_by_chantier(json_files, "Roissy")
    print("Total: {}, BioSAV: {}, Devisubox: {}, Marseille: {}\
, Nouveau Campus: {}, Roissy: {}".format(len(json_files),
                                             len(biosav_files),
                                             len(devisubox_files),
                                             len(marseille_files),
                                             len(nouveaucampus_files),
                                             len(roissy_files)))
    chantiers = [devisubox_files, marseille_files, biosav_files, nouveaucampus_files, roissy_files]
    data_by_chantier = [[] for x in chantiers]
    for i in range(len(chantiers)):
        for json_file in chantiers[i]:
            with open(json_file) as f:
                try:
                    json_data = json.load(f)
                    data_by_chantier[i].append(json_data)
                except json.JSONDecodeError:
                    print("Couldn't decode file {}".format(json_file))
    return data_by_chantier


def main():
    data_by_chantier = heatmap()
    objects_density = [0 for i in range(60)]
    for chantier in data_by_chantier:
        for picture_data in chantier:
            # print(picture_data.keys())
            objects_density[len(picture_data["objects"])] += 1
    plt.figure()
    plt.xlabel("N° of objects detected")
    plt.ylabel("N° of pictures")
    plt.title("Object detection density in data set")
    plt.bar(np.arange(len(objects_density)), objects_density)
    plt.show()
    return 0


if __name__ == "__main__":
    main()
