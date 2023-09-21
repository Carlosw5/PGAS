import time
import board
import neopixel
import random
np = neopixel.NeoPixel(board.D2, 30, auto_write = False, brightness = 0.5)
red = [255, 0, 0]
blue = [0, 43, 255]
pink = [255, 0, 255]
green = [0, 153, 0]
turq = [0, 255, 255]
purple = [255, 0, 255]
orange = [255, 128, 0]
color = [255,156,127]

times = 1
'''

Function: Fade Out

Description: This function decreases the brightness of the neopixel from its original brightness by lowering RGB value

Parameters: color and speed

Return value: None

'''
def fadeOut(color, speed=0.001):
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

Function: Fade In

Description: This function increases brighteness of a neopixel by raising RGB value

Parameters: color, speed

Return value: none

'''
def fadeIn(color, speed=0.001):
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

Function: Chase

Description: Takes in a background color and a set color moves in intervals of 2

Parameters: color and speed

Return value: background color

'''
def chase(color = [0,0,0], speed = 0.01):
    for j in range(30):
        np.show()
        for i in range(30):
            if i % 3 != 0:
                led = (i+j) % 30 
                np[led] = [255,0,255]
                print("bColor",i,np[i])
            elif i % 3 == 0:
                led = (i+j) % 30
                np[led] = color
                print("fColor",i,np[i])
            time.sleep(speed)
'''

Function: Sparkle

Description: This function takes in a background color and then uses a random integer to pop a random color

Parameters: color and times

Return value: None

'''
def sparkle(color = [0,0,0], times = 1):
    for i in range(times):
        np.fill(color)
        led1 = random.randint(0, 28)
        led2 = random.randint(0, 28)
        led3 = random.randint(0, 28)
        np[led1] = [12,124,42]
        np[led2] = [255,255,255]
        np[led3] = [255,255,255]
        np.show()
        time.sleep(0.7)

while True:
    sparkle(pink, 5)
    fadeIn(blue)
    fadeOut(blue)
    fadeIn(red)
    fadeOut(red)
    chase(turq)
    fadeIn(purple)
    fadeOut(purple)
    fadeIn(orange)
    fadeOut(orange)
    chase(orange)
    sparkle(red, 5)

import time
import board
import neopixel
import random
np = neopixel.NeoPixel(board.D2, 30, auto_write = False, brightness = 0.5)
red = [255, 0, 0]
blue = [0, 43, 255]
pink = [255, 0, 255]
green = [0, 153, 0]
turq = [0, 255, 255]
purple = [255, 0, 255]
orange = [255, 128, 0]
color = [255,156,127]
black = [0, 0, 0]

times = 1

def sparkle(color = [0,0,0], times = 1):
    for i in range(times):
        np.fill(color)
        for i in range(3):
            np[random.randint(0, 28)] = [102,0,204]
            np[random.randint(0, 28)] = [255, 255, 255]
            np.show()
            time.sleep(random.random())
    
        
while True:
    sparkle(black, 8)

    
