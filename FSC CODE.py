import time
import board
import neopixel
import random
np = neopixel.NeoPixel(board.D2, 30, auto_write = False, brightness = 0.5)

color = [255,156,127]
speed = 6
times = 1
def fadeOut(color, speed=1):
    if speed <= 0:
        speed = 1
    fadeR = color[0]/256.0
    fadeG = color[1]/256.0
    fadeB = color[2]/256.0
    color1 = [color[0],color[1],color[2]]
    np.fill(color1)
    np.show()
    for i in range(255):
        color1[0] = int (color[0] - (fadeR*i))
        color1[1] = int (color[1] - (fadeG*i))
        color1[2] = int (color[2] - (fadeB*i))
        np.fill(color1)
        np.show()
        print(color1)
        time.sleep(speed)
'''

Function: Fade Out

Description: This function decreases the brightness of the neopixel from its original brightness by lowering RGB value

Parameters: color and speed

Return value: None

'''
def fadeIn(color, speed=1):
    if speed <= 0:
        speed = 1
    fadeR = color[0]/256.0
    fadeG = color[1]/256.0
    fadeB = color[2]/256.0
    color1 = [0,0,0]
    np.fill(color1)
    np.show()
    print(color1)
    for i in range(255):
        color1[0] = int (fadeR*i)
        color1[1] = int (fadeG*i)
        color1[2] = int (fadeB*i)
        np.fill(color1)
        np.show()
        time.sleep(speed)
        print(color1)
'''

Function: Fade In

Description: This function increases brighteness of a neopixel by raising RGB value

Parameters: color, speed

Return value: none

'''

def chase(color = [0,0,0], speed = 0.1):
    for j in range(30):
        np.show()
        for i in range(30):
            if i % 3 != 0:
                led = (i+j) % 30 
                np[led] = [0,0,255]
                print("bColor",i,np[i])
            elif i % 3 == 0:
                led = (i+j) % 30
                np[led] = color
                print("fColor",i,np[i])
            time.sleep(speed)
'''

Function: Chase

Description: Takes in a background color and a set color moves in intervals of 2

Parameters: color and speed

Return value: none

'''
def sparkle(color = [0,0,0], times = 1):
    for i in range(times):
        np.fill(color)
        led1 = random.randint(0, 28)
        led2 = random.randint(0, 28)
        led3 = random.randint(0, 28)
        np[led1] = [12,124,42]
        np[led2] = [12,124,42]
        np[led3] = [12,124,42]
        np.show()
        time.sleep(0.01)
'''

Function: Sparkle

Description: This function uses a random integer to pop a random color

Parameters: color and times

Return value: None

'''
while True:
    sparkle(color, 0.001)
    fadeIn(color, 0.01)
    fadeOut(color, 0.01)
