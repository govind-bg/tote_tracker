import matplotlib as plt
import cv2
import time
import sys
from pandas import *
from datetime import datetime
import re
import numpy as np
import glob


# OPEN_CV Image Properties

COLOR_BLACK = (0, 0, 0)
COLOR_GREY = (100, 100, 100)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (0, 200, 255)
COLOR_GREEN = (0, 255, 0)
COLOR_DARK_GREEN = (80, 220, 80)
COLOR_RED = (0, 0, 255)
CIRCLE_RAD_SMALL = 15
CIRCLE_RAD_BIG = 30
TEXT_FONT_SIZE = 1
TEXT_FONT_THICKNESS = 2

# OPEN_CV Video Properties

# Video will be saved at 2 FPS. Slow to properly track the tote
FRAME_RATE = 2
# 200 ms was found to be a good balance 
WAIT_KEY_PARAM= 200 
# Video format
VIDEO_FORMAT = cv2.VideoWriter_fourcc(*'MP4V')

# Manually sourced coordinates of the stations

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

# Manually sourced coordinates for the box to be drawn, these are added to the posiitons
# of the stations listed above

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


def get_tote_number(raw_data):
	"""
	Gets the tote name from the logs
	"""
	# we only need one of the messages
	first_message = raw_data["message"].tolist() [0]
	print(first_message)
	processing_first_message = first_message.split("for ", 1)[1]
	tote_number = processing_first_message.split(" @",1)[0]
	return (tote_number)

def find_time_delta(time_stamp_list,main_iterator):
	"""
	Gets the time difference between 2 timestampts whie
	iterating through the loop in main script. Not 
	returning in string format because we need to add it
	in the main loop
	"""
	if main_iterator== 0:
		return 0
		
	time_stamp_prev = time_stamp_list[main_iterator-1]
	time_stamp_current = time_stamp_list[main_iterator]
	time_stamp_prev = datetime.strptime(time_stamp_prev, "%b %d, %Y @ %H:%M:%S.%f")
	time_stamp_current = datetime.strptime(time_stamp_current, "%b %d, %Y @ %H:%M:%S.%f")
	time_delta = time_stamp_current - time_stamp_prev

	# returns (minutes, seconds) tuple format
	time_minutes = divmod(time_delta.total_seconds(), 60)

	# this returns the time in minutes
	time_minutes = time_minutes[0] + (time_minutes [1]/60)
	return time_minutes

def find_time_spent(raw_data):
	"""
	function to calculate the time spent by a tote in the system
	"""

	time_stamps = raw_data["@timestamp"].tolist()

	time_stamp_exit = time_stamps[0]
	time_stamp_entry = time_stamps[-1]

	print('Time of Entry : ', time_stamp_entry)
	print('Time of Exit : ', time_stamp_exit)
	print('\n')

	tote_entry = datetime.strptime(time_stamp_entry, "%b %d, %Y @ %H:%M:%S.%f")
	tote_exit = datetime.strptime(time_stamp_exit, "%b %d, %Y @ %H:%M:%S.%f")
	time_delta = tote_exit - tote_entry

	# returns (minutes, seconds) tuple format
	time_minutes = divmod(time_delta.total_seconds(), 60)

	if time_minutes[0] >= 60:
		print('Total time spent by tote in the system: ', time_minutes[0] / 60,
			  ' hours')
	else:
		print('Total time spent by tote in the system: ', time_minutes[0],
			  'minutes', time_minutes[1], 'seconds')


def print_summary(summary_dictionary):
	"""
	Prints the summary of the tote journey in the console when the 
	tote leaves the system or at the end of the record of the tote in
	the BG system
	"""

	print('\n')
	print('Summary of the tote : ')
	print('\n')
	for k, v in summary_dictionary.items():
		print(k, end=" >>> ")
		for k2, v2 in v.items():
			print(k2, ':', v2, end=" | ")
		print('\n')
	print('\n')


def prepare_positions_list(raw_data):
	"""
	returns the positions of the tote (scanner wise)
	the list is reversed because the data is obtained in reverse
	chronological order and we want to display the animationin 
	chronological order
	"""

	messages = raw_data["message"].tolist()
	positions_list_func = [msg.split("@ ", 1)[1] for msg in messages]

	# Reversing the list as to be in the reverse chronological order

	positions_list_func.reverse()
	reversed_positions_list = positions_list_func

	return reversed_positions_list


def prepare_divert_truth(raw_data):
	"""
	returns the diver TRUE/FALSE of divert decision
	the list is reversed because the data is obtained in reverse
	chronological order and we want to display the animationin 
	chronological order
	"""

	messages = raw_data["message"].tolist()
	divert_truth_list_func = [msg.split("for", 1)[0] for msg in messages]

	# Reversing the list as to be reverse chronological

	divert_truth_list_func.reverse()
	reversed_divert_truth_list = divert_truth_list_func

	for idx in range(len(reversed_divert_truth_list)):

		# Extraction TRUE/FALSE from the divert decision

		divert_truth = re.findall('\((.*?)\)', reversed_divert_truth_list[idx])

		# rewrites the reversed divert list, adding 0 index because
		# the raw data is a list of length 1

		reversed_divert_truth_list[idx] = divert_truth[0]

	return reversed_divert_truth_list

