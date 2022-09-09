#Worksite Safety Monitoring

Hackathon challenge : eleven strategy x École des Ponts ParisTech  
Septembre 2022  

**Groupe 2 (Matthieu, Dimitri, Leonard, Reda)**


## Présentation

Le projet est expliqué dans la présentation "**Présentation_Groupe_2.pdf**"

## Modèle de détection

La première itération a été d'exploiter le fichier de tutoriel fourni par les examinateurs. Il s'agit de **basic_faster_rcnn.py**.  
Il est possible de l'exécuter directement (à une correction de directory_path près) pour obtenir l'analyse d'une image aléatoire du Training_set par le modèle Faster R-CNN tel qu'il est distribué.
On y observe en général une détection partielle des ouvriers sur l'image et une détection aléatoire de "boat", "car" et autres classes courantes du *COCO Dataset*.

La seconde itération a été de d'effectuer du *Transfer Learning* à l'aide du modèle précédent. Il se trouve dans le fichier **finetuning_faster_rcnn.py**. N'ayant pas réussi à créer un modèle étendu composé de Faster R-CNN + 1 couche de 7 neurones réprésentant les nouvelles classes à détecter (structures verticales, échafaudages, etc.), **nous avons laissé le code non fonctionnel tel quel.**

La troisième itération consistait à entraîner un modèle à reconnaitre nos 7 classes. La base de données à fournir devait être sous format *ImageFolder* : un dossier par classe à reconnaître, et un grand nombre d'images illustrant cette classe dans chaque dossier.
Il s'agit de **resnet18.py**. Nous avons abandonné cette piste car elle nécessitait un travail important de fragmentation de l'image en petits rectangles à faire passer par le réseau de neurones, puis de reconstruction de l'image finale.

La quatrième et dernière itération correspond à l'utilisation du modèle Detectron2 pour une détection performante des ouvriers uniquement.
Cette partie a été réalisée sur Google Colaboratory. Afin de l'ouvrier, télécharger le fichier **basic_detectron2.ipynb** et l'ouvrir aveec Google Colaboratory. Il a déjà tourné, et le dernier résultat est visible.
Pour obtenir d'autres résultats, modifier la cellule "directory path".

## Modèle d'analyse

Le dossier *heatmap* contient le fichier **heatmap.py** dont la fonction main produit la heatmap souhaitée.

## Compte-rendu

Le dossier *metrics* contient un début de code pour implémenter le *IoU* : **iou.py**.



