# -*- coding: utf-8 -*-
# Project: ProjectRobot1_2025
# File: speed_control.py
# Description:
#   Control the Tiny:bit robot's movement speed using PWM values.
#   The robot gradually accelerates from low to high speed and then stops.

from microbit import display, sleep, Image
import tinybit

# --- Speed levels (PWM values) ---
speed_levels = [50, 100, 150, 200, 255]

# --- Display introduction ---
display.scroll("Speed Ctrl")

# --- Gradual acceleration demo ---
for speed in speed_levels:
    display.show(Image.ARROW_N)  # Arrow points forward
    tinybit.setMotorPWM(speed, speed, 1000)
    sleep(1000)
    display.show(str(int(speed / 28)))  # Display approximate level (0–9)
    sleep(500)

# --- Gradual deceleration demo ---
for speed in reversed(speed_levels):
    display.show(Image.ARROW_S)  # Arrow points backward
    tinybit.setMotorPWM(speed, speed, 1000)
    sleep(1000)
    display.show(str(int(speed / 28)))
    sleep(500)

# --- Stop the car at the end ---
tinybit.car_stop()
display.show(Image.NO)
sleep(1000)
display.clear()
