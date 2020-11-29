![image](https://raw.githubusercontent.com/mytechnotalent/MicroPython-micro-bit_Talking_LED_Blink/main/MicroPython-micro-bit%20Talking%20LED%20Blink.jpg)

# MicroPython-micro-bit
# Talking LED Blink
The micro:bit Talking LED Blink is a micro:bit Electronic Educational Engagement Tool designed to help students create a talking LED blink application.

# CODE
```python
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
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)
