![image](https://raw.githubusercontent.com/mytechnotalent/MicroPython-micro-bit_Talking_LED_Blink/main/MicroPython-micro-bit%20Talking%20LED%20Blink.jpg)

# MicroPython-micro-bit
# Talking LED Blink
The micro:bit Talking LED Blink is a micro:bit Electronic Educational Engagement Tool designed to help students create a talking LED blink application.

## Schematic
![image](https://raw.githubusercontent.com/mytechnotalent/MicroPython-micro-bit_Talking_LED_Blink/main/schematic.png | width=50)<br>
*** NOTE *** USE PIN1 INSTEAD OF PIN0 (GREEN WIRE)

## Parts
[micro:bit](https://microbit.org/buy/?location=US&version=microbitV2)<br>
[Ks0360 Keyestudio Sensor Shield V2 for BBC micro:bit](https://www.amazon.com/gp/product/B08H7VSLZH/)<br>
* Keyestudio Micro bit sensor V2 shield * 1
* keyestudio Digital White LED Module * 1
* Dupont jumper wire * 3

## STEP 1: Navigate To The FREE micro:bit Python Web Editor
[micro:bit Python Web Editor](https://python.microbit.org/v/beta)<br><br>
![image](https://raw.githubusercontent.com/mytechnotalent/MicroPython-micro-bit_Talking_LED_Blink/main/STEP%201.png)

## STEP 2: Plug micro:bit V2 Into Computer
***PLUG IN USB CABLE TO COMPUTER AND DEVICE***

## STEP 3: Click CONNECT
![image](https://raw.githubusercontent.com/mytechnotalent/MicroPython-micro-bit_Talking_LED_Blink/main/STEP%203.png)

## STEP 4: Click "BBC micro:bit CMSIS-DAP" & CONNECT
![image](https://raw.githubusercontent.com/mytechnotalent/MicroPython-micro-bit_Talking_LED_Blink/main/STEP%204.png)

## STEP 5: Highlight Sample Code - Select All
![image](https://raw.githubusercontent.com/mytechnotalent/MicroPython-micro-bit_Talking_LED_Blink/main/STEP%205.png)

## STEP 6: Click Backspace On Keyboard To Delete Sample Code
![image](https://raw.githubusercontent.com/mytechnotalent/MicroPython-micro-bit_Talking_LED_Blink/main/STEP%206.png)

## STEP 7: Copy Study Buddy Python Code Template Into Python Web Editor

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


## STEP 8: Rename Script Name To talking_led_blink

## STEP 9: Click Save
![image](https://raw.githubusercontent.com/mytechnotalent/MicroPython-micro-bit_Talking_LED_Blink/main/STEP%209.png)

## STEP 10: Click Download Python Script
![image](https://raw.githubusercontent.com/mytechnotalent/MicroPython-micro-bit_Talking_LED_Blink/main/STEP%2010.png)

## STEP 11: Click Flash
![image](https://raw.githubusercontent.com/mytechnotalent/MicroPython-micro-bit_Talking_LED_Blink/main/STEP%2011.png)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)
