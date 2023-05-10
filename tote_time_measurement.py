# Data from https://sunflower.kb.us-central1.gcp.cloud.es.io:9243/app/discover#/?_g=(filters:!(),refreshInterval:(pause:!t,value:0),time:(from:now-1h,to:now))&_a=(columns:!(message,tote_id,location_id),filters:!(),index:ce572630-0f58-11ed-bd81-e7f3585b181b,interval:auto,query:(language:kuery,query:'%22arrived%22%20'),sort:!(!('@timestamp',desc)))
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
RAW_FILE_NAME = "raw_data/time_measure_2.csv"
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

main_avg = []
total_totes = 0
y_lim = 0
for location_iterator in range(len(all_locations)):

    time_stamp_list = find_time(df_names[location_iterator])
    # now doing the time delta calculation

    average_time_list = []
    for time_list_iterator in range(len(time_stamp_list)):
        # appending seconds instead of minutes
        average_time_list.append(find_time_delta(
            time_stamp_list, time_list_iterator)*60)

    all_average_time_dic[all_locations[location_iterator]] = average_time_list



    if len(average_time_list) != 0: 

        # Dynamically change y_lim for every instance. So we set y_lim as the highest time interval we see
        if max(average_time_list) > y_lim:
            y_lim = max(average_time_list)
        average_time_seconds = (sum(average_time_list)/len(average_time_list))
        main_avg.append(average_time_seconds)
        print('Average time taken between totes at ',
              all_locations[location_iterator], ' is : ', average_time_seconds, ' seconds | Totes processed : ', len(average_time_list))
        # redoing it for every point, so setting iterator back to 0
        total_totes += len(average_time_list)
        # average_time_list = []
        # time_list_iterator = 0
    else:
        print('No totes went past ', all_locations[location_iterator])
        main_avg.append(0)

all_average_time_dic_keys = []
for k, v in all_average_time_dic.items():
    all_average_time_dic_keys.append(k)

print ('\n')
print(' ====== Overall Tote Loop Average time between totes at every point is : ',
      (sum(main_avg)/len(main_avg)), ' seconds  ====== ')
print(' ====== Total Totes processed (repeated)  : ', total_totes, ' ====== ')
# subplot properties
print(' ====== Total Unique Totes processed : ', len(set(dataFrame["tote_id"].tolist())), ' ====== ')
axis_rows = 3
axis_columns = 6
fig, axs = plt.subplots(axis_rows, axis_columns)
# set the super title for the matplotlib plot

fig.suptitle('Time between Totes across all cells')
fig.text(0.5, 0.04, 'number of totes', ha='center')
fig.text(0.04, 0.5, 'time between totes in seconds',
         va='center', rotation='vertical')
# count to iterate through all dictionary keys

count = 0

# to create a r x c sized subplot
for r in range(axis_rows):
    for c in range(axis_columns):

        # drawing the subplot

        axs[r, c].plot(all_average_time_dic[all_average_time_dic_keys[count]])
        axs[r, c].set_ylim([0, y_lim + 25])
        axs[r, c].set_title(all_average_time_dic_keys[count], fontsize=9)
        count += 1

# show the matplotlib plot
plt.show()
