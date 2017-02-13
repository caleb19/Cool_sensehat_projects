#!/usr/bin/python
import sys
from sense_hat import SenseHat

# To get good results with the magnetometer you must first calibrate it using
# the program in RTIMULib/Linux/RTIMULibCal
# The calibration program will produce the file RTIMULib.ini
# Copy it into the same folder as your Python code

led_loop = [4,5,7,17,27,37,47,57,77,75,74,73,72,71,70,50,40,30,20,10,0,1,2,3]

sense = SenseHat()
sense.set_rotation(0)
sense.clear()

prev_x = 0
prev_y = 0

#led_degree_ratio = len(led_loop) / 360.0

while True:
    dir = sense.get_compass()
    if dir < 0.49:
        dir = 360
    led_index = dir / 15 # Gives 24 steps => led_loop

    offset = led_loop[led_index]

    y = offset // 8  # row
    x = offset % 8  # column

    if x != prev_x or y != prev_y:
        sense.set_pixel(prev_x, prev_y, 0, 0, 0)

    sense.set_pixel(x, y, 0, 0, 255)

    prev_x = x
    prev_y = y
