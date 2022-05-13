# this library comes with python and will pause for us
import time
# this library is for our cpe
from adafruit_circuitplayground import cp

# set the overall brightness
cp.pixels.brightness = 0.5

# this is always going to run, waiting for a response
while True:
    # for each touch sensor, we specify a wave file
    # and a pixel that turns on to a color
    # as the chosen sound plays
    # and then off (0,0,0) after 1/4 second
    if cp.touch_A1:
        cp.pixels[6] = (255, 0, 0)
        cp.play_file("electro1.mp4")
        time.sleep(0.25)
        cp.pixels[6] = (0, 0, 0)
    if cp.touch_A2:
        cp.pixels[7] = (0, 255, 0)
        cp.play_file("electro2.mp4")
        time.sleep(0.25)
        cp.pixels[7] = (0, 0, 0)
    if cp.touch_A3:
        cp.pixels[8] = (0, 255, 0)
        cp.play_file("electro3.mp4")
        time.sleep(0.25)
        cp.pixels[8] = (0, 0, 0)
    if cp.touch_A4:
        cp.pixels[0] = (40, 15, 210)
        cp.play_file("electro4.mp4")
        time.sleep(0.25)
        cp.pixels[0] = (0, 0, 0)
    if cp.touch_A5:
        cp.pixels[1] = (255, 50, 55)
        cp.play_file("electro5.mp4")
        time.sleep(0.25)
        cp.pixels[1] = (0, 0, 0)
    if cp.touch_A6:
        cp.pixels[3] = (125, 0, 255)
        cp.play_file("electro6.mp4")
        time.sleep(0.25)
        cp.pixels[3] = (0, 0, 0)
    if cp.touch_A7:
        cp.pixels[4] = (0, 255, 55)
        cp.play_file("electro7.mp4")
        time.sleep(0.25)
        cp.pixels[4] = (0, 0, 0)
