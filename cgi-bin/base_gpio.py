import RPi.GPIO as gpio


class BaseGPIO:
    def __init__():
    self.gpio = gpio
    self.gpio.setmode(self.gpio.BOARD)
    
    def setup_pin_out(pin_number):
        return self.gpio.setup(pin_number, self.gpio.OUT)

    def set_pin_true(pin_number):