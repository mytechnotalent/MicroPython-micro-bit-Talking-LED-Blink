from time import sleep

from microbit import pin1, display, Image
from speech import say

while True:
    pin1.write_digital(1)
    display.show(Image.SURPRISED)
    say('The light is on!')
    display.show(Image.HAPPY)
    sleep(5)
    pin1.write_digital(0)
    display.show(Image.SURPRISED)
    say('The light is off!')
    display.show(Image.HAPPY)
    sleep(5)
