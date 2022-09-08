import numpy as np

def area_rect(rect):
    return np.abs((rect[0][0]-rect[0][1])*(rect[0][1]-rect[1][1]))


def area_inter2(rect_pred, rect_json):
    area_inter, area_union = 0, area_rect(rect_pred)+area_rect(rect_json)

    x_pred, x_json = rect_pred[:][0], rect_json[:][0]
    y_pred, y_json = rect_pred[:][1], rect_json[:][1]

    if x_pred[1] > x_json[0]:
        area_inter = (x_pred[1] - x_json[0])*(y_pred[1] - y_json[0])
    if x_json[1] > x_pred[0]:
        area_inter = (x_json[1] - x_pred[0])*(y_pred[0] - y_json[1])
    if y_pred[1] > y_json[0]:
        area_inter = (y_pred[1] - y_json[0])*(x_pred[1] - x_json[0])
    if y_json[1] > y_pred[0]:
        area_inter = (y_json[1] - y_pred[0])*(x_json[1] - x_pred[0])
    return area_inter

def area_inter_n(rect_pred_list, rect_json_list):
    area = 0
    for rect_pred in rect_pred_list:
        for rect_json in rect_json_list:
            area += area_inter2(rect_pred, rect_json)
    return area


def area_union(rect_list):
    return np.sum(area_rect(rect_list))

