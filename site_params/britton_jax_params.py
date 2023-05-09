# Coordinates for Britton-Jacksonville
# Link to get data: 
# https://britton.kb.us-central1.gcp.cloud.es.io:9243/s/jacksonville/app/discover#/?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-24h%2Fh,to:now))&_a=(columns:!(message),filters:!(),index:b43e9fd0-135e-11ed-992b-f58a19f21880,interval:auto,query:(language:kuery,query:'%22Divert%20decision%22%20%20and%20%2231241672%22'),sort:!(!('@timestamp',desc)))

MAP_NAME = "Images/britton_jax_map.png"
RAW_FILE_NAME = "raw_data/raw_file_jax.csv"
# Manually sourced coordinates of the systems

system_coordinates = {
    "Divert_SPS01_HighwayFeeder": (335, 370),
    "Divert_SPS02_HighwayFeeder": (335, 570),
    "Divert_SPS03_HighwayFeeder": (500, 370),
    "Divert_SPS04_HighwayFeeder": (500, 570),
    "Divert_SPS05_HighwayFeeder": (665, 370),
    "Divert_SPS06_HighwayFeeder": (665, 570),
    "Divert_SPS07_HighwayFeeder": (830, 370),
    "Divert_SPS08_HighwayFeeder": (830, 570),
    "Divert_SPS09_HighwayFeeder": (995, 370),
    "Divert_SPS10_HighwayFeeder": (995, 570),
    "Divert_ToteLoop_Recirc1": (310, 740),
    "Divert_ToteLoop_Recirc2": (288, 313),
    "Divert_ToteLoop_Discharge1": (219, 283),
    "Divert_ToteLoop_Discharge2": (335, 250),
    "Divert_ToteLoop_Jackpot": (475, 250)
}

# Manually sourced coordinates for the box to be drawn, these are added to the posiitons
# of the systems listed above

# x_1, y_1, x_2, y_2

box_position_coordinates = {
    "Divert_SPS01_HighwayFeeder": [-80, -20, -40, 20],
    "Divert_SPS02_HighwayFeeder": [-80, -20, -40, 20],
    "Divert_SPS03_HighwayFeeder": [-80, -20, -40, 20],
    "Divert_SPS04_HighwayFeeder": [-80, -20, -40, 20],
    "Divert_SPS05_HighwayFeeder": [-80, -20, -40, 20],
    "Divert_SPS06_HighwayFeeder": [-80, -20, -40, 20],
    "Divert_SPS07_HighwayFeeder": [-80, -20, -40, 20],
    "Divert_SPS08_HighwayFeeder": [-80, -20, -40, 20],
    "Divert_SPS09_HighwayFeeder": [-80, -20, -40, 20],
    "Divert_SPS10_HighwayFeeder": [-80, -20, -40, 20],
    "Divert_ToteLoop_Recirc1": [40, -20, 80, 20],
    "Divert_ToteLoop_Recirc2": [40, -20, 80, 20],
    "Divert_ToteLoop_Discharge1": [-80, -20, -40, 20],
    "Divert_ToteLoop_Discharge2": [-80, -20, -40, 20],
    "Divert_ToteLoop_Jackpot": [40, -20, 80, 20]
}

# Tote title coordinates on the image

tote_title_rect_coords = [510, 0, 880, 40]

# Time display coordinates on the image

time_map_rect_coords = [1150, 0, 1500, 40]
