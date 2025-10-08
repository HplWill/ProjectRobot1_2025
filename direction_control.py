# Micro:bit Tiny:bit Robot – Direction Control Demo
# Project: ProjectRobot1_2025
# Description:
#   Demonstrates direction control for the Tiny:bit robot.
#   The robot moves forward, backward, turns left/right, and spins.
#   Each motion lasts 1 second, showing corresponding LED arrows.

from microbit import display, Image, sleep
import tinybit

# --- Configuration ---
SPEED = 150       # Motor speed (0–255)
DURATION = 1000   # Duration for each movement (in milliseconds)

# --- Movement Functions ---
def move_forward():
    display.show(Image.ARROW_N)
    tinybit.car_run(SPEED)
    sleep(DURATION)

def move_backward():
    display.show(Image.ARROW_S)
    tinybit.car_back(SPEED)
    sleep(DURATION)

def turn_left():
    display.show(Image.ARROW_W)
    tinybit.car_left(SPEED)
    sleep(DURATION)

def turn_right():
    display.show(Image.ARROW_E)
    tinybit.car_right(SPEED)
    sleep(DURATION)

def spin_left():
    display.show(Image.ARROW_W)
    tinybit.car_spinleft(SPEED)
    sleep(DURATION)

def spin_right():
    display.show(Image.ARROW_E)
    tinybit.car_spinright(SPEED)
    sleep(DURATION)

def stop_car():
    tinybit.car_stop()
    display.clear()
    sleep(500)

# --- Main Loop ---
while True:
    try:
        move_forward()
        stop_car()

        move_backward()
        stop_car()

        turn_left()
        stop_car()

        turn_right()
        stop_car()

        spin_left()
        stop_car()

        spin_right()
        stop_car()

    except Exception as e:
        # Handle unexpected issues safely
        display.show(Image.NO)
        tinybit.car_stop()
        sleep(2000)
        display.clear()

