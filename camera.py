import picamera
import RPi.GPIO as gpio
from time import sleep

triger=16
img_num=0
camera = picamera.PiCamera()

gpio.setmode(gpio.BOARD)
gpio.setup(triger,  gpio.IN, pull_up_down=gpio.PUD_DOWN)

camera.start_preview()
while True:

    if gpio.input(triger)==True:
        print("%s" % img_num)
        camera.capture('snapshot%s.jpeg' % img_num, resize=(1080,1920))
        img_num+=1
        sleep(0.2)
camera.stop_preview()
    