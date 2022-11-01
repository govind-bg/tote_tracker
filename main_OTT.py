from helper_functions_OTT import *

# read the raw data from kibana (exported in CSV format)
data = read_csv("raw_file.csv")

positions_list = prepare_positions_list(data)
divert_truth_list = prepare_divert_truth(data)

# A variable to iterate until

total_scans = len(divert_truth_list)

looping_counters = {}

# read the map of the system
img = cv2.imread("test_map.png", cv2.IMREAD_COLOR)

# choose codec according to format needed
# frame size is WIDTH, HEIGHT
FRAME_SIZE = (img.shape[1], img.shape[0])
FRAME_RATE = 8
video_output = cv2.VideoWriter('tote_traversal.avi',cv2.VideoWriter_fourcc(*'DIVX'), FRAME_RATE, FRAME_SIZE)

for idx in range(total_scans):

	# Checking for the name of the divert and if the divert was TRUE/FALSE

	divert_name = positions_list[idx]
	divert_truth = divert_truth_list[idx]
	# Updating dictionary values to have a good data
	# of everything

	if divert_name not in looping_counters:
		looping_counters[divert_name] = {}
		looping_counters[divert_name]['instances_visitied'] = 1
		if divert_truth == 'True':
			print('tote divert requested to: ', divert_name)
			looping_counters[divert_name]['diverted'] = 1

			# Draw filled rectangles to display the station divert TRUE Score


			# get station position coordinates
			x_1 = box_position_coordinates[divert_name][0]
			x_2 = box_position_coordinates[divert_name][2]

			y_1 = box_position_coordinates[divert_name][1]
			y_2 = box_position_coordinates[divert_name][3]

			# Adding offset to station coords to display the rectangle
			rectangle_corner_1 = (station_coordinates[divert_name][0] + x_1,
								  station_coordinates[divert_name][1] + y_1)
			rectangle_corner_2 = (station_coordinates[divert_name][0] + x_2,
								  station_coordinates[divert_name][1] + y_2)

			# Draw a rectangle
			img = cv2.rectangle(img, rectangle_corner_1, rectangle_corner_2,
								COLOR_DARK_GREEN, -1)

			# Text coordinates

			text_corner_x = int(
				(station_coordinates[divert_name][0] + x_1 +
				 station_coordinates[divert_name][0] + x_2) / 2)
			text_corner_y = int(
				(station_coordinates[divert_name][1] + y_1 +
				 station_coordinates[divert_name][1] + y_2) / 2)
			

			# added as a manual param to center the text in the rectangle
			text_offset = 20 

			# adding the text to the rectangle 
			cv2.putText(
				img, str(looping_counters[divert_name]['diverted']),
				(text_corner_x - text_offset, text_corner_y + text_offset),
				cv2.FONT_HERSHEY_SIMPLEX, TEXT_FONT_SIZE, COLOR_BLACK, TEXT_FONT_THICKNESS)

		elif divert_truth == 'False':
			looping_counters[divert_name]['diverted'] = 0

	else:
		looping_counters[divert_name]['instances_visitied'] += 1
		if divert_truth == 'True':
			print('tote divert requested AGAIN to: ', divert_name)

			# this new updated value will now go inside the rectangle

			looping_counters[divert_name]['diverted'] += 1

			# Draw filled rectangles to display the station divert TRUE Score

			# get station position coordinates
			x_1 = box_position_coordinates[divert_name][0]
			x_2 = box_position_coordinates[divert_name][2]

			y_1 = box_position_coordinates[divert_name][1]
			y_2 = box_position_coordinates[divert_name][3]

			# Adding offset to station coords to display the rectangle
			rectangle_corner_1 = (station_coordinates[divert_name][0] + x_1,
								  station_coordinates[divert_name][1] + y_1)
			rectangle_corner_2 = (station_coordinates[divert_name][0] + x_2,
								  station_coordinates[divert_name][1] + y_2)

			# Draw a rectangle
			img = cv2.rectangle(img, rectangle_corner_1, rectangle_corner_2,
								COLOR_DARK_GREEN, -1)

			# Text coordinates

			text_corner_x = int(
				(station_coordinates[divert_name][0] + x_1 +
				 station_coordinates[divert_name][0] + x_2) / 2)
			text_corner_y = int(
				(station_coordinates[divert_name][1] + y_1 +
				 station_coordinates[divert_name][1] + y_2) / 2)
			
			# added as a manual param to center the text in the rectangle
			text_offset = 20 

			# adding the text to the rectangle 
			cv2.putText(
				img, str(looping_counters[divert_name]['diverted']),
				(text_corner_x - text_offset, text_corner_y + text_offset),
				cv2.FONT_HERSHEY_SIMPLEX, TEXT_FONT_SIZE, COLOR_BLACK, TEXT_FONT_THICKNESS)

	# change color of the circle based on divert truth.
	# if divert == true, circle color == green
	# if divert == false, circle color == red

	if divert_truth == 'False':

		img = cv2.circle(img,
						 station_coordinates[divert_name],
						 radius=CIRCLE_RAD_SMALL,
						 color=COLOR_RED,
						 thickness=-1)
		cv2.imshow("Station Map", img)
		cv2.waitKey(100)

	else:

		img = cv2.circle(img,
						 station_coordinates[divert_name],
						 radius=CIRCLE_RAD_SMALL,
						 color=COLOR_GREEN,
						 thickness=-1)
		cv2.imshow("Station Map", img)
		cv2.waitKey(100)

	# saving the video output here so that the circle colors show up

	video_output.write(img)
	
	# resetting back to black circle

	img = cv2.circle(img,
					 station_coordinates[divert_name],
					 radius=CIRCLE_RAD_BIG,
					 color=COLOR_BLACK,
					 thickness=-1)

	cv2.imshow("Station Map", img)
	cv2.waitKey(100)
	

video_output.release()

cv2.destroyAllWindows()
# print the summary of the tote

print_summary(looping_counters)

# Check the duration the tote spent in the system

find_time_spent(data)
print('\n')
