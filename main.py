from common_helper import *
# from sunflower_ott_params import *
# from washington_phx_params import *
from britton_jax_params import *

# read the raw data from kibana (exported in CSV format)
data = read_csv(RAW_FILE_NAME)

# extracting the time column
time_stamps = data["@timestamp"].tolist()
time_stamps.reverse()

positions_list = prepare_positions_list(data)
divert_truth_list = prepare_divert_truth(data)

# Checks for how many times a scanner saw the tote and
# iterates that many times in the loop

total_scans = len(divert_truth_list)

looping_counters = {}

# read the map of the system
img = cv2.imread(MAP_NAME, cv2.IMREAD_COLOR)

# Adding title to the image

# get tote name
tote_name = get_tote_number(data)
# Draw TITLE rectangle
img = cv2.rectangle(img, (tote_title_rect_coords[0], tote_title_rect_coords[1]),
                    (tote_title_rect_coords[2], tote_title_rect_coords[3]), COLOR_BLACK, -1)

# adding the text to the TITLE  - Trial and error method to get rectangle coordinates
cv2.putText(img, "Tote : " + str(tote_name), (520, 30),
            cv2.FONT_HERSHEY_SIMPLEX, TEXT_FONT_SIZE, COLOR_WHITE,
            TEXT_FONT_THICKNESS)

# choose codec according to format needed
# frame size is WIDTH, HEIGHT
FRAME_SIZE = (img.shape[1], img.shape[0])
video_output = cv2.VideoWriter(
    'videos/' + str(tote_name) +
    '_tote_traversal.mp4', VIDEO_FORMAT, FRAME_RATE,
    FRAME_SIZE)

# will be iterated after getting data from the find_time_delta func

time_counter = 0.0

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

            # Draw filled rectangles to display the systems divert TRUE Score

            # get systems position coordinates
            x_1 = box_position_coordinates[divert_name][0]
            x_2 = box_position_coordinates[divert_name][2]

            y_1 = box_position_coordinates[divert_name][1]
            y_2 = box_position_coordinates[divert_name][3]

            # Adding offset to systems coords to display the rectangle
            rectangle_corner_1 = (system_coordinates[divert_name][0] + x_1,
                                  system_coordinates[divert_name][1] + y_1)
            rectangle_corner_2 = (system_coordinates[divert_name][0] + x_2,
                                  system_coordinates[divert_name][1] + y_2)

            # Draw a rectangle
            img = cv2.rectangle(img, rectangle_corner_1, rectangle_corner_2,
                                COLOR_DARK_GREEN, -1)

            # Text coordinates

            text_corner_x = int(
                (system_coordinates[divert_name][0] + x_1 +
                 system_coordinates[divert_name][0] + x_2) / 2)
            text_corner_y = int(
                (system_coordinates[divert_name][1] + y_1 +
                 system_coordinates[divert_name][1] + y_2) / 2)

            # added as a manual param to center the text in the rectangle
            text_offset = 20

            # adding the text to the rectangle
            cv2.putText(
                img, str(looping_counters[divert_name]['diverted']),
                (text_corner_x - text_offset, text_corner_y + text_offset),
                cv2.FONT_HERSHEY_SIMPLEX, TEXT_FONT_SIZE, COLOR_BLACK,
                TEXT_FONT_THICKNESS)

        elif divert_truth == 'False':
            looping_counters[divert_name]['diverted'] = 0

    else:
        looping_counters[divert_name]['instances_visitied'] += 1
        if divert_truth == 'True':
            print('tote divert requested AGAIN to: ', divert_name)

            # this new updated value will now go inside the rectangle

            looping_counters[divert_name]['diverted'] += 1

            # Draw filled rectangles to display the systems divert TRUE Score

            # get systems position coordinates
            x_1 = box_position_coordinates[divert_name][0]
            x_2 = box_position_coordinates[divert_name][2]

            y_1 = box_position_coordinates[divert_name][1]
            y_2 = box_position_coordinates[divert_name][3]

            # Adding offset to systems coords to display the rectangle
            rectangle_corner_1 = (system_coordinates[divert_name][0] + x_1,
                                  system_coordinates[divert_name][1] + y_1)
            rectangle_corner_2 = (system_coordinates[divert_name][0] + x_2,
                                  system_coordinates[divert_name][1] + y_2)

            # Draw a rectangle
            img = cv2.rectangle(img, rectangle_corner_1, rectangle_corner_2,
                                COLOR_DARK_GREEN, -1)

            # Text coordinates

            text_corner_x = int(
                (system_coordinates[divert_name][0] + x_1 +
                 system_coordinates[divert_name][0] + x_2) / 2)
            text_corner_y = int(
                (system_coordinates[divert_name][1] + y_1 +
                 system_coordinates[divert_name][1] + y_2) / 2)

            # added as a manual param to center the text in the rectangle
            text_offset = 20

            # adding the text to the rectangle
            cv2.putText(
                img, str(looping_counters[divert_name]['diverted']),
                (text_corner_x - text_offset, text_corner_y + text_offset),
                cv2.FONT_HERSHEY_SIMPLEX, TEXT_FONT_SIZE, COLOR_BLACK,
                TEXT_FONT_THICKNESS)

    # change color of the circle based on divert truth.
    # if divert == true, circle color == green
    # if divert == false, circle color == red

    if divert_truth == 'False':

        img = cv2.circle(img,
                         system_coordinates[divert_name],
                         radius=CIRCLE_RAD_SMALL,
                         color=COLOR_RED,
                         thickness=-1)
        cv2.imshow("System Map", img)
        cv2.waitKey(WAIT_KEY_PARAM)

    else:

        img = cv2.circle(img,
                         system_coordinates[divert_name],
                         radius=CIRCLE_RAD_MEDIUM,
                         color=COLOR_GREEN,
                         thickness=-1)
        cv2.imshow("System Map", img)
        cv2.waitKey(WAIT_KEY_PARAM)

    # saving the video output here so that the circle colors show up

    video_output.write(img)

    # resetting back to black circle

    img = cv2.circle(img,
                     system_coordinates[divert_name],
                     radius=CIRCLE_RAD_BIG,
                     color=COLOR_BLACK,
                     thickness=-1)

    # to display live time spent in the system
    img = cv2.rectangle(img, (time_map_rect_coords[0], time_map_rect_coords[1]),
                        (time_map_rect_coords[2], time_map_rect_coords[3]), COLOR_BLACK, -1)

    # formatting the time
    time_difference = float(find_time_delta(time_stamps, idx))
    time_counter += time_difference
    time_counter = float('{:.2f}'.format(time_counter))

    # # adding the text to the TITLE  - Trial and error method to get rectangle coordinates
    cv2.putText(img,
                str(time_counter) + " minutes", (1150, 25),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, COLOR_YELLOW, 2)

    cv2.imshow("System Map", img)
    cv2.waitKey(WAIT_KEY_PARAM)

video_output.release()

cv2.destroyAllWindows()
# print the summary of the tote

print_summary(looping_counters)

# Check the duration the tote spent in the system

find_time_spent(data)
print('\n')
