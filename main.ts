/** 
Created by: Evan M
Created on: Sep 2024
This module is a Micro:bit MicroPython program
This program will tell the current temperature

 */
basic.clearScreen()
basic.showIcon(IconNames.Happy)
basic.pause(1000)
input.temperature()
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
})
input.temperature()
basic.showString("The current temperature is:")
basic.showNumber(input.temperature())
