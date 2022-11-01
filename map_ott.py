import matplotlib as plt
import cv2
import time
import sys

from coordinates import * 


img = cv2.imread('test_map.png', cv2.IMREAD_COLOR)


# Indicate the Stations 1-5

img = cv2.circle(img, Divert_SPS01_HighwayFeeder, radius=15, color=(0, 0, 255), thickness=-1)
img = cv2.circle(img, Divert_SPS02_HighwayFeeder, radius=15, color=(0, 0, 255), thickness=-1)
img = cv2.circle(img, Divert_SPS03_HighwayFeeder, radius=15, color=(0, 0, 255), thickness=-1)
img = cv2.circle(img, Divert_SPS04_HighwayFeeder, radius=15, color=(0, 0, 255), thickness=-1)
img = cv2.circle(img, Divert_SPS05_HighwayFeeder, radius=15, color=(0, 0, 255), thickness=-1)

# Indicate the Stations 6-10

img = cv2.circle(img, Divert_SPS06_HighwayFeeder, radius=15, color=(0, 0, 255), thickness=-1)
img = cv2.circle(img, Divert_SPS07_HighwayFeeder, radius=15, color=(0, 0, 255), thickness=-1)
img = cv2.circle(img, Divert_SPS08_HighwayFeeder, radius=15, color=(0, 0, 255), thickness=-1)
img = cv2.circle(img, Divert_SPS09_HighwayFeeder, radius=15, color=(0, 0, 255), thickness=-1)
img = cv2.circle(img, Divert_SPS10_HighwayFeeder, radius=15, color=(0, 0, 255), thickness=-1)


# Indicate the Diverts

img = cv2.circle(img, Divert_ToteLoop_Recirc1, radius=15, color=(255, 0, 255), thickness=-1)
img = cv2.circle(img, Divert_ToteLoop_Recirc2, radius=15, color=(255, 0, 255), thickness=-1)
img = cv2.circle(img, Divert_ToteLoop_Recirc3, radius=15, color=(255, 0, 255), thickness=-1)
img = cv2.circle(img, Divert_ToteLoop_Recirc4, radius=15, color=(255, 0, 255), thickness=-1)
img = cv2.circle(img, Divert_ToteLoop_Recirc5, radius=15, color=(255, 0, 255), thickness=-1)
img = cv2.circle(img, Divert_ToteLoop_Recirc6, radius=15, color=(255, 0, 255), thickness=-1)

# Indicate the Discharges

img = cv2.circle(img, Divert_ToteLoop_Discharge1, radius=15, color=(0, 255, 255), thickness=-1)
img = cv2.circle(img, Divert_ToteLoop_Discharge2, radius=15, color=(0, 255, 255), thickness=-1)


station_coordinates = {
    "Divert_SPS01_HighwayFeeder": (1070, 590),
    "Divert_SPS02_HighwayFeeder": (890, 590),
    "Divert_SPS03_HighwayFeeder": (700, 590),
    "Divert_SPS04_HighwayFeeder": (525, 590),
    "Divert_SPS05_HighwayFeeder": (340, 590),
    "Divert_SPS06_HighwayFeeder": (340, 220),
    "Divert_SPS07_HighwayFeeder": (525, 220),
    "Divert_SPS08_HighwayFeeder": (700, 220),
    "Divert_SPS09_HighwayFeeder": (890, 220),
    "Divert_SPS10_HighwayFeeder": (1070, 220),
    "Divert_ToteLoop_Recirc1": (730, 680),
    "Divert_ToteLoop_Recirc6": (660, 680),
    "Divert_ToteLoop_Recirc3": (660, 140),
    "Divert_ToteLoop_Recirc4": (730, 140),
    "Divert_ToteLoop_Recirc2": (180, 640),
    "Divert_ToteLoop_Recirc5": (240, 180),
    "Divert_ToteLoop_Discharge1": (1080, 110),
    "Divert_ToteLoop_Discharge2": (1280, 110),
}

# [x_1,y_1,x_2,y_2]
box_position_coordinates = {
    "Divert_SPS01_HighwayFeeder": [-20,-100,40,-160],
    "Divert_SPS02_HighwayFeeder": [-20,-100,40,-160],
    "Divert_SPS03_HighwayFeeder": [-20,-100,40,-160],
    "Divert_SPS04_HighwayFeeder": [-20,-100,40,-160],
    "Divert_SPS05_HighwayFeeder": [-20,-100,40,-160],
    
    "Divert_SPS06_HighwayFeeder": [-20,100,40,160],
    "Divert_SPS07_HighwayFeeder": [-20,100,40,160],
    "Divert_SPS08_HighwayFeeder": [-20,100,40,160],
    "Divert_SPS09_HighwayFeeder": [-20,100,40,160],
    "Divert_SPS10_HighwayFeeder": [-20,100,40,160],

    "Divert_ToteLoop_Recirc1": [40,0,100,60],
    "Divert_ToteLoop_Recirc6": [-40,0,-100,60],
    "Divert_ToteLoop_Recirc3": [-40,0,-100,-60],
    "Divert_ToteLoop_Recirc4": [40,0,100,-60],
    "Divert_ToteLoop_Recirc2": [-120,20,-60,-40],
    "Divert_ToteLoop_Recirc5": [-120,0,-60,-60],
    "Divert_ToteLoop_Discharge1": [-120,20,-60,-40],
    "Divert_ToteLoop_Discharge2": [60,20,120,-40],
}

divert_name = 'Divert_ToteLoop_Discharge2'
x_1 = box_position_coordinates[divert_name][0]
x_2 = box_position_coordinates[divert_name][2]
y_1 = box_position_coordinates[divert_name][1]
y_2 = box_position_coordinates[divert_name][3]

img = cv2.rectangle(img, (station_coordinates[divert_name][0]+x_1,station_coordinates[divert_name][1]+y_1),
						 (station_coordinates[divert_name][0]+x_2,station_coordinates[divert_name][1]+y_2), (0,0,0), -1)


cv2.imshow('Station Map',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
