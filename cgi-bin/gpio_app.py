#!/usr/bin/python

import RPi.GPIO as gpio
import time


gpio.setmode(gpio.BOARD)

gpio.setup(8, gpio.OUT)
gpio.setup(40, gpio.OUT)

pwm = gpio.PWM(8, 01)
pwm2 = gpio.PWM(40, 10)

pwm.start(4)
pwm2.start(4)
time.sleep(10)

pwm.stop()
pwm2.stop()

def blink(pwm, timeout):
    counter = 0
    pwm.start(1)
    while True:
        counter += 1
        if counter == timeout:
            pwm.stop()
            break

#blink(pwm2, 40)
