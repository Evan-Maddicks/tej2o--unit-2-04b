"""
Created by: Evan M
Created on: Sep 2024
This module is a Micro:bit MicroPython program
This program will tell the current temperature
"""

basic.clear_screen()
basic.show_icon(IconNames.Happy)
basic.pause(1000)

input.temperature()

def on_button_pressed_a():
    pass
input.on_button_pressed(Button.A, on_button_pressed_a)
input.temperature()
basic.show_string("The current temperature is:")
basic.show_number(input.temperature())