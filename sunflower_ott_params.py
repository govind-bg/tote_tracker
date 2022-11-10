# Coordinates for Sunflower-Ottawa
# Link to get data: 
# https://sunflower.kb.us-central1.gcp.cloud.es.io:9243/app/discover#/?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-7d%2Fd,to:now))&_a=(columns:!(message,system_name),filters:!(),index:ce572630-0f58-11ed-bd81-e7f3585b181b,interval:auto,query:(language:kuery,query:'%22Divert%20decision%22%20%20and%20%22770000601205%22'),sort:!(!('@timestamp',desc)))

MAP_NAME = "Images/sunflower_ottawa_map.png"
RAW_FILE_NAME = "raw_data/raw_file_ott.csv"

# Manually sourced coordinates of the systems 

system_coordinates = {
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

# Manually sourced coordinates for the box to be drawn, these are added to the posiitons
# of the systems listed above

# x_1, y_1, x_2, y_2

box_position_coordinates = {
    "Divert_SPS01_HighwayFeeder": [-20, -100, 40, -160],
    "Divert_SPS02_HighwayFeeder": [-20, -100, 40, -160],
    "Divert_SPS03_HighwayFeeder": [-20, -100, 40, -160],
    "Divert_SPS04_HighwayFeeder": [-20, -100, 40, -160],
    "Divert_SPS05_HighwayFeeder": [-20, -100, 40, -160],
    "Divert_SPS06_HighwayFeeder": [-20, 100, 40, 160],
    "Divert_SPS07_HighwayFeeder": [-20, 100, 40, 160],
    "Divert_SPS08_HighwayFeeder": [-20, 100, 40, 160],
    "Divert_SPS09_HighwayFeeder": [-20, 100, 40, 160],
    "Divert_SPS10_HighwayFeeder": [-20, 100, 40, 160],
    "Divert_ToteLoop_Recirc1": [40, 0, 100, 60],
    "Divert_ToteLoop_Recirc6": [-40, 0, -100, 60],
    "Divert_ToteLoop_Recirc3": [-40, 0, -100, -60],
    "Divert_ToteLoop_Recirc4": [40, 0, 100, -60],
    "Divert_ToteLoop_Recirc2": [-120, 20, -60, -40],
    "Divert_ToteLoop_Recirc5": [-120, 0, -60, -60],
    "Divert_ToteLoop_Discharge1": [-120, 20, -60, -40],
    "Divert_ToteLoop_Discharge2": [60, 20, 120, -40],
}

# Tote title coordinates on the image

tote_title_rect_coords = [510, 0, 880, 40]

# Time display coordinates on the image

time_map_rect_coords = [1150, 0, 1500, 40]
