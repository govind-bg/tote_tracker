from site_params.sunflower_ott_params import *
# from site_params.washington_phx_params import *
# from site_params.britton_jax_params import *
# from site_params.huron_lan_params import *

from common_helper import *

# reading the blank image

print(MAP_NAME)
img = cv2.imread(MAP_NAME, cv2.IMREAD_COLOR)


# Looping to draw the circles where the stations will be
# displayed

for sys_name, coords in system_coordinates.items():

    img = cv2.circle(img, coords, radius=15, color=COLOR_BLACK, thickness=-1)

# Looping to draw the black rectangles where the scores will be
# displayed

for divert_name, _ in box_position_coordinates.items():

    # get station position coordinates
    x_1 = box_position_coordinates[divert_name][0]
    x_2 = box_position_coordinates[divert_name][2]

    y_1 = box_position_coordinates[divert_name][1]
    y_2 = box_position_coordinates[divert_name][3]

    # Adding offset to station coords to display the rectangle
    rectangle_corner_1 = (system_coordinates[divert_name][0] + x_1,
                          system_coordinates[divert_name][1] + y_1)
    rectangle_corner_2 = (system_coordinates[divert_name][0] + x_2,
                          system_coordinates[divert_name][1] + y_2)

    # Draw a rectangle
    img = cv2.rectangle(img, rectangle_corner_1,
                        rectangle_corner_2, color=COLOR_DARK_GREEN, thickness=-1)

# To display the rectangle that will show the time

img = cv2.rectangle(img, (time_map_rect_coords[0], time_map_rect_coords[1]),
                    (time_map_rect_coords[2], time_map_rect_coords[3]), COLOR_BLACK, -1)

# To display the rectangle that will show the tote_title

img = cv2.rectangle(img, (tote_title_rect_coords[0], tote_title_rect_coords[1]),
                    (tote_title_rect_coords[2], tote_title_rect_coords[3]), COLOR_BLACK, -1)


cv2.imshow('System Map', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
