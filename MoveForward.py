# -*- coding: utf-8 -*-
# Micro:bit Robot Basic Movement Example
# Author: [Your Name]
# Project: ProjectRobot1_2025
# Description:
#   This program displays an arrow on the LED screen and drives the
#   Tiny:bit robot forward at a defined speed. It also includes
#   optional directional and stop functions for testing.

from microbit import display, Image, button_a, button_b, sleep
import tinybit

# --- Configuration ---
SPEED = 150  # Speed range: 0–255

# --- Initialization ---
display.show(Image.HAPPY)
sleep(1000)
display.show(Image.ARROW_S)

# --- Main Control Loop ---
while True:
    # Press button A to move forward
    if button_a.is_pressed():
        display.show(Image.ARROW_N)
        tinybit.car_run(SPEED)
        sleep(2000)  # move for 2 seconds
        tinybit.car_stop()
        display.show(Image.HAPPY)

    # Press button B to move backward
    elif button_b.is_pressed():
        display.show(Image.ARROW_S)
        tinybit.car_back(SPEED)
        sleep(2000)
        tinybit.car_stop()
        display.show(Image.HAPPY)

    # If no button pressed, stay idle
    else:
        tinybit.car_stop()
        display.show(Image.ASLEEP)
        sleep(200)

