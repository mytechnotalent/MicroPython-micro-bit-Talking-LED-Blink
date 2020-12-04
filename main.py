from time import sleep

from microbit import pin1, display, Image
from speech import say

# Customize bot speaking speed
SPEED = 95

while True:
    # Here we write a digital 1 or True to our pin1
    # as this will turn the LED on
    pin1.write_digital(1)
    display.show(Image.SURPRISED)
    say('The light is on!', speed=SPEED)
    display.show(Image.HAPPY)
    sleep(5)
    # Here we write a digital 0 or False to our pin1
    # as this will turn the LED on
    pin1.write_digital(0)
    display.show(Image.SURPRISED)
    say('The light is off!', speed=SPEED)
    display.show(Image.HAPPY)
    sleep(5)
