import cv2
import csv
import time
import sys
import pandas as pd
from datetime import datetime
import re
import numpy as np
import glob
from common_helper import *
from matplotlib import pyplot as plt
RAW_FILE_NAME = "raw_data/time_measure.csv"
data = read_csv(RAW_FILE_NAME)

dataFrame = pd.read_csv(RAW_FILE_NAME)

all_locations = ['Divert_SPS01_HighwayFeeder', 'Divert_SPS02_HighwayFeeder',
                 'Divert_SPS03_HighwayFeeder', 'Divert_SPS04_HighwayFeeder',
                 'Divert_SPS05_HighwayFeeder', 'Divert_SPS06_HighwayFeeder',
                 'Divert_SPS07_HighwayFeeder', 'Divert_SPS08_HighwayFeeder',
                 'Divert_SPS09_HighwayFeeder', 'Divert_SPS10_HighwayFeeder',
                 'Divert_ToteLoop_Recirc1', 'Divert_ToteLoop_Recirc6',
                 'Divert_ToteLoop_Recirc3', 'Divert_ToteLoop_Recirc4',
                 'Divert_ToteLoop_Recirc2', 'Divert_ToteLoop_Recirc5',
                 'Divert_ToteLoop_Discharge1', 'Divert_ToteLoop_Discharge2']


df_names = ['df_Divert_SPS01_HighwayFeeder', 'df_Divert_SPS02_HighwayFeeder',
            'df_Divert_SPS03_HighwayFeeder', 'df_Divert_SPS04_HighwayFeeder',
            'df_Divert_SPS05_HighwayFeeder', 'df_Divert_SPS06_HighwayFeeder',
            'df_Divert_SPS07_HighwayFeeder', 'df_Divert_SPS08_HighwayFeeder',
            'df_Divert_SPS09_HighwayFeeder', 'df_Divert_SPS10_HighwayFeeder',
            'df_Divert_ToteLoop_Recirc1', 'df_Divert_ToteLoop_Recirc6',
            'df_Divert_ToteLoop_Recirc3', 'df_Divert_ToteLoop_Recirc4',
            'df_Divert_ToteLoop_Recirc2', 'df_Divert_ToteLoop_Recirc5',
            'df_Divert_ToteLoop_Discharge1', 'df_Divert_ToteLoop_Discharge2']

for loc_idx in range(len(all_locations)):
    # printing the data frame for all locations
    df_names[loc_idx] = dataFrame[dataFrame['location_id'].str.contains(
        all_locations[loc_idx])]


def find_time(df):
    time_stamps = df["@timestamp"].tolist()
    time_stamps.reverse()
    return time_stamps

# print dataframes


for loc_idx in range(len(all_locations)):
    # printing the data frame for all locations
    df_names[loc_idx] = dataFrame[dataFrame['location_id'].str.contains(
        all_locations[loc_idx])]

# fucntion to extract the timestamps and reverse it and return the reversed list


def find_time(df):
    time_stamps = df["@timestamp"].tolist()
    time_stamps.reverse()
    return time_stamps


all_average_time_dic = {}

for location_iterator in range(len(all_locations)):

    time_stamp_list = find_time(df_names[location_iterator])

    # now doing the time delta calculation

    average_time_list = []
    for time_list_iterator in range(len(time_stamp_list)):
    	# appending seconds instead of minutes
        average_time_list.append(find_time_delta(time_stamp_list, time_list_iterator)*60)

    all_average_time_dic[all_locations[location_iterator]] = average_time_list

    # converting average time to seconds

    average_time_seconds = (sum(average_time_list)/len(average_time_list))
    print('Average time taken between totes at ',
          all_locations[location_iterator], ' is : ', average_time_seconds, ' seconds')

    # redoing it for every point, so setting iterator back to 0
    average_time_list = []
    time_list_iterator = 0

all_average_time_dic_keys = []
for k, v in all_average_time_dic.items():
    all_average_time_dic_keys.append(k)


# subplot properties

axis_rows = 3
axis_columns = 6
fig, axs = plt.subplots(axis_rows, axis_columns)
# set the super title for the matplotlib plot

fig.suptitle('Time between Totes across all cells')
fig.text(0.5, 0.04, 'number of totes', ha='center')
fig.text(0.04, 0.5, 'time between totes in seconds', va='center', rotation='vertical')
# count to iterate through all dictionary keys

count = 0

# to create a r x c sized subplot
for r in range(axis_rows):
    for c in range(axis_columns):

        # drawing the subplot

        axs[r, c].plot(all_average_time_dic[all_average_time_dic_keys[count]])
        axs[r, c].set_title(all_average_time_dic_keys[count],fontsize=9)
        count += 1

# show the matplotlib plot
plt.show()
