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
    # Setup channel
    gpio.setup(button_ch, gpio.IN, pull_up_down=gpio.PUD_DOWN)
    gpio.setup(auto_flash_LED_ch, gpio.OUT, initial=False)
    # Main Loop
    n_clicks = 0
    click_timeout = 5
    while n_clicks < click_timeout:
        if gpio.input(button_ch):
            print("Button Clicked - {}".format(n_clicks))
            gpio.output(auto_flash_LED_ch, True)
            time.sleep(2)
            gpio.output(auto_flash_LED_ch, False)
            n_clicks += 1
    # Teardown gpio
    gpio.cleanup()
    

if __name__ == "__main__":
    main()
