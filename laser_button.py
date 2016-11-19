#!/usr/bin/env python3
"""
Trying to make Rpi3 flash for 5 seconds on button click
"""

import time

def main():
    # Import GPIO
    try:
        import RPi.GPIO as gpio
    except RuntimeError:
        print("Error importing RPi.GPIO!  This is probably because you need superuser privileges. ",
              "You can achieve this by using 'sudo' to run your script")
    
    # Set gpio board mode
    gpio.setmode(gpio.BOARD)
    gpio.setwarnings(False)
    # Set gpio pin numbers
    auto_flash_LED_ch = 12
    button_ch = 7
    laser_ch = 16
    # Setup channel
    gpio.setup(button_ch, gpio.IN)
    gpio.setup(auto_flash_LED_ch, gpio.OUT, initial=False)
    gpio.setup(laser_ch, gpio.OUT, initial=True)
    # Main Loop
    n_clicks = 0
    n_max = 5
    
    prev_state = False
    while n_clicks < n_max:
        if not gpio.input(button_ch):
            n_clicks = n_clicks + 1 if not prev_state else n_clicks
            prev_state = True
            print("Button clicked {}".format(n_clicks))
            gpio.output(laser_ch, False)
        else:
            gpio.output(laser_ch, True)
            prev_state = False
        time.sleep(0.1)  # To prevent runaway CPU usage, scan on 0.1s intervals
    # Teardown gpio
    gpio.cleanup()
    

if __name__ == "__main__":
    main()
