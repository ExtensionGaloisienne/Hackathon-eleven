# script generant la heatmap a partir des donnees json

import os
import random


#Choix d'un fichier aléatoire
def choose_random_file(directory):
    return random.choice(os.listdir(directory))

# Choix d'un fichier json aléatoire
def choose_random_json(directory):
    return os.path.join(directory, choose_random_file(directory))

def heatmap():
    directory = "C:\\Users\\Léonard\\Downloads\\data\\Detection_Test_Set\\Detection_Test_Set_Json"
    json_file = choose_random_json(directory)
    print(json_file)
    return 0
