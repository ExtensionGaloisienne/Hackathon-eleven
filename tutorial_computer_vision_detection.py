# %%
from PIL import Image
from torchvision import models
from torchvision import transforms as T
import matplotlib.pyplot as plt
import cv2

import os
import random

# %%
# Loading the model and the dataset
# Loads pretrained VGG model and sets it to eval mode

model = models.detection.fasterrcnn_resnet50_fpn(pretrained=True)
model = model.eval()
# %%
COCO_INSTANCE_CATEGORY_NAMES = [
    "__background__",
    "person",
    "bicycle",
    "car",
    "motorcycle",
    "airplane",
    "bus",
    "train",
    "truck",
    "boat",
    "traffic light",
    "fire hydrant",
    "N/A",
    "stop sign",
    "parking meter",
    "bench",
    "bird",
    "cat",
    "dog",
    "horse",
    "sheep",
    "cow",
    "elephant",
    "bear",
    "zebra",
    "giraffe",
    "N/A",
    "backpack",
    "umbrella",
    "N/A",
    "N/A",
    "handbag",
    "tie",
    "suitcase",
    "frisbee",
    "skis",
    "snowboard",
    "sports ball",
    "kite",
    "baseball bat",
    "baseball glove",
    "skateboard",
    "surfboard",
    "tennis racket",
    "bottle",
    "N/A",
    "wine glass",
    "cup",
    "fork",
    "knife",
    "spoon",
    "bowl",
    "banana",
    "apple",
    "sandwich",
    "orange",
    "broccoli",
    "carrot",
    "hot dog",
    "pizza",
    "donut",
    "cake",
    "chair",
    "couch",
    "potted plant",
    "bed",
    "N/A",
    "dining table",
    "N/A",
    "N/A",
    "toilet",
    "N/A",
    "tv",
    "laptop",
    "mouse",
    "remote",
    "keyboard",
    "cell phone",
    "microwave",
    "oven",
    "toaster",
    "sink",
    "refrigerator",
    "N/A",
    "book",
    "clock",
    "vase",
    "scissors",
    "teddy bear",
    "hair drier",
    "toothbrush",
]


# %%
def get_prediction(img_path, threshold):
    img = Image.open(img_path)  # Load the image
    transform = T.Compose([T.ToTensor()])  # Defining PyTorch Transform
    img = transform(img)  # Apply the transform to the image
    pred = model([img])  # Pass the image to the model
    pred_class = [
        COCO_INSTANCE_CATEGORY_NAMES[i]
        for i in list(pred[0]["labels"].numpy())
    ]  # Get the Prediction Score
    pred_boxes = [
        [(i[0], i[1]), (i[2], i[3])]
        for i in list(pred[0]["boxes"].detach().numpy())
    ]  # Bounding boxes
    pred_score = list(pred[0]["scores"].detach().numpy())
    pred_t = [pred_score.index(x) for x in pred_score if x > threshold][
        -1
    ]  # Get list of index with score greater than threshold.
    pred_boxes = pred_boxes[: pred_t + 1]
    pred_class = pred_class[: pred_t + 1]
    return pred_boxes, pred_class


# %%
def object_detection_api(
        img_path, threshold=0.5, rect_th=3, text_size=3, text_th=3
):
    boxes, pred_cls = get_prediction(img_path, threshold)  # Get predictions
    img = cv2.imread(img_path)  # Read image with cv2
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert to RGB
    for i in range(len(boxes)):
        cv2.rectangle(
            img, (int(boxes[i][0][0]), int(boxes[i][0][1])), (int(boxes[i][1][0]), int(boxes[i][1][1])),
            color=(0, 255, 0), thickness=rect_th
        )  # Draw Rectangle with the coordinates
        cv2.putText(
            img,
            pred_cls[i],
            (int(boxes[i][0][0]), int(boxes[i][0][1])),
            cv2.FONT_HERSHEY_SIMPLEX,
            text_size,
            (0, 255, 0),
            thickness=text_th,
        )  # Write the prediction class
    print(boxes)
    plt.figure()  # display the output image
    plt.imshow(img)
    plt.xticks([])
    plt.yticks([])
    plt.show()



# GET A RANDOM IMAGE PATH IN FOLDER dir
def choose_random_image(directory):
    img_extension = ["png", "jpeg", "jpg"]  # Image Extensions to be chosen from
    all_images = list()
    for img in os.listdir(directory):  # Lists all files
        ext = img.split(".")[len(img.split(".")) - 1]
        if ext in img_extension:
            all_images.append(img)
    # choice = random.randint(0, len(allImages) - 1)
    # chosen_image = allImages[choice]  # Do Whatever you want with the image file
    random_image = random.choice(all_images)
    return os.path.join(directory, random_image)


# MAIN

# %%
# Try the detection model for the image of your choice
# Example to help, if I have a folder named data with a jpeg format picture called test, the result would be:


#dir_path = "/Users/redabendjellountouimi/Git/Hackathon-eleven/data/Detection_Train_Set/Detection_Train_Set/Detection_Train_Set_Img"
# dir_path = "C:\\Users\\Léonard\\Downloads\\data\\Detection_Test_Set\\Detection_Test_Set_Img"
dir_path = "C:/Users/dimit/hackathon/Hackathon-eleven/Datasets/Detection_Train_Set/Detection_Train_Set_Img"
test_img_path = choose_random_image(dir_path)
print(test_img_path)
object_detection_api(test_img_path)

# %%
