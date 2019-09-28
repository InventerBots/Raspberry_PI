import picamera
import RPi.GPIO as gpio
from time import sleep

triger=16
kill=18
img_num=0
camera = picamera.PiCamera()

gpio.setmode(gpio.BOARD)
gpio.setup(triger,  gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.setup(kill, gpio.IN, pull_up_down=gpio.PUD_DOWN)

camera.resolution = (150, 100)
camera.start_preview()
while True:
##	if gpio.input(kill)==True:
##		break
    if gpio.input(triger)==True:
        print("True, %s" % img_num)
        camera.capture('snapshot%s.jpeg' % img_num, resize=(720,480))
        img_num+=1
        sleep(0.5)
camera.stop_preview()
    