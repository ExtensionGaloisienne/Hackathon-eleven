# script generant la heatmap a partir des donnees json

import os
import random
import json
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import torchvision.ops as tvo


NAMES = ["BioSAV", "Devisubox", "Marseille", "Nouveau Campus", "Roissy"]
SIZES = [[720, 1280], [720, 1280], [720, 1280], [1080, 1920], [1080, 1920]]


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
    #directory = r'C:\Users\Léonard\Downloads\data\Detection_Train_Set\Detection_Train_Set_Json'
    directory = r'C:\Users\dimit\hackathon\Hackathon-eleven\Datasets\Detection_Train_Set\Detection_Train_Set_Json'
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
    chantiers = [biosav_files,  devisubox_files, marseille_files, nouveaucampus_files, roissy_files]
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


def display_objects_density(data_by_chantier):
    objects_density = [[0 for i in range(60)] for i in range(5)]
    plt.figure(figsize=(10, 2))
    for i in range(5):
        for picture_data in data_by_chantier[i]:
            objects_density[i][len(picture_data["objects"])] += 1
        plt.subplot(1, 5, i + 1)
        plt.bar(np.arange(len(objects_density[i])), objects_density[i])
        plt.title(NAMES[i])
    plt.show()


def display_people_density(people_by_chantier):
    objects_density = [[0 for i in range(60)] for i in range(5)]
    plt.figure(figsize=(10, 2))
    for i in range(5):
        for picture_data in people_by_chantier[i]:
            objects_density[i][len(picture_data)] += 1
        plt.subplot(1, 5, i + 1)
        plt.bar(np.arange(len(objects_density[i])), objects_density[i])
        plt.title(NAMES[i])
    plt.show()


def extract_people(picture_data):
    people_boxes = []
    for detected_obj in picture_data["objects"]:
        if detected_obj["classTitle"] == "People":
            people_boxes.append(detected_obj)
    return people_boxes


def compute_center(a, b):
    return np.array([(a[0]+b[0]) // 2, (a[1]+b[1]) // 2])

def compute_radius(a, b):
    return np.mean([abs(b[0]-a[0]) / 2, abs(b[1]-a[1]) / 2])


def get_boxes_from_people_list(people_list):
    return np.array([guy['points']['exterior'] for guy in people_list], dtype=np.int64)


def main():
    data_by_chantier = heatmap()
    # display_objects_density(data_by_chantier)
    people_by_chantier = [[] for _ in range(5)]
    for i in range(5):
        for picture_data in data_by_chantier[i]:
            people_in_picture = extract_people(picture_data)
            if len(people_in_picture) > 0:
                people_by_chantier[i].append(people_in_picture)
    # display_people_density(people_by_chantier)
    for i in range(5):
        plt.figure()
        plt.title(NAMES[i])
        all_the_people = np.empty((0, 2, 2))
        for people_list in people_by_chantier[i]:
            people_boxes = get_boxes_from_people_list(people_list)
            all_the_people = np.concatenate((all_the_people, people_boxes))
        box_count = len(all_the_people)
        centers = np.zeros((box_count, 2), dtype=np.int64)
        radii = np.zeros(box_count, dtype=np.int64)
        for j in range(box_count):
            centers[j] = compute_center(all_the_people[j][0], all_the_people[j][1])
            radii[j] = compute_radius(all_the_people[j][0], all_the_people[j][1])
        limits = [[0, SIZES[i][0]], [0, SIZES[i][1]]]
        plt.hist2d(centers[:, 0], centers[:, 1], bins=50, weights=radii,
                   range=limits, cmap='Blues')
        plt.show()
    return 0


if __name__ == "__main__":
    main()
