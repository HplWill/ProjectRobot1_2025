# -*- coding: utf-8 -*-
# Project: ProjectRobot1_2025
# File: path_control.py
# Description:
#   Tiny:bit Robot Path Control — Draw preset paths ("L", "O", "D", "Z")
#   by combining motion commands. Controlled via buttons A and B.

from microbit import display, Image, sleep, button_a, button_b
import tinybit

# --- Custom LED letter images ---
LETTER_IMAGES = {
    "L": Image("90000:90000:90000:90000:99999"),
    "O": Image("09990:90009:90009:90009:09990"),
    "D": Image("99000:90900:90090:90009:99999"),
    "Z": Image("99999:00090:00900:09000:99999"),
}

# --- Movement sequences for each letter ---
LETTER_MOVEMENTS = {
    "L": [
        ("run", 100, 1000),
        ("spinleft", 150, 500),
        ("run", 100, 1000),
        ("stop", 0, 0),
    ],
    "O": [
        ("run", 100, 1000),
        ("spinleft", 180, 400),
        ("run", 100, 1000),
        ("spinleft", 180, 400),
        ("run", 100, 1000),
        ("spinleft", 180, 400),
        ("run", 100, 1000),
        ("stop", 0, 0),
    ],
    "D": [
        ("run", 100, 1000),
        ("spinleft", 150, 600),
        ("run", 100, 1500),
        ("spinleft", 150, 600),
        ("run", 100, 1000),
        ("stop", 0, 0),
    ],
    "Z": [
        ("run", 100, 1000),
        ("spinright", 120, 600),
        ("run", 100, 1300),
        ("spinleft", 120, 600),
        ("run", 100, 1000),
        ("stop", 0, 0),
    ],
}

# --- Initialization ---
display.show(Image.HAPPY)
sleep(500)

current_letter = 0
letter_keys = list(LETTER_IMAGES.keys())
execute_flag = False


def execute_movement_sequence(letter):
    """
    Execute the Tiny:bit movement pattern corresponding to a given letter.
    """
    display.show(LETTER_IMAGES[letter])
    sleep(1000)  # Show letter before movement

    for action, speed, duration in LETTER_MOVEMENTS[letter]:
        if action == "run":
            tinybit.car_run(speed)
        elif action == "spinleft":
            tinybit.car_spinleft(speed)
        elif action == "spinright":
            tinybit.car_spinright(speed)
        elif action == "stop":
            tinybit.car_stop()

        if duration > 0:
            sleep(duration)

    tinybit.car_stop()
    display.show(Image.YES)
    sleep(800)
    display.clear()


# --- Main loop ---
while True:
    # Button A: switch to next letter
    if button_a.was_pressed():
        current_letter = (current_letter + 1) % len(letter_keys)
        display.show(LETTER_IMAGES[letter_keys[current_letter]])

    # Button B: execute path for current letter
    if button_b.was_pressed():
        execute_flag = True

    if execute_flag:
        execute_movement_sequence(letter_keys[current_letter])
        execute_flag = False
        display.show(LETTER_IMAGES[letter_keys[current_letter]])
