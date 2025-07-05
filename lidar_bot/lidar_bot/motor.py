import lgpio
import time
from lidar_bot.constants import Constants

class Motor:
    def __init__(self, pwm_pin, in1, in2, gpio_handle):
        self.pwm_pin = pwm_pin
        self.in1 = in1
        self.in2 = in2
        self.h = gpio_handle
        self.setup()

    def setup(self):
        for pin in [self.pwm_pin, self.in1, self.in2]:
            lgpio.gpio_claim_output(self.h, pin)

    def forward(self):
        lgpio.gpio_write(self.h, self.in1, 1)
        lgpio.gpio_write(self.h, self.in2, 0)
        lgpio.tx_pwm(self.h, self.pwm_pin, Constants.PWM_FREQ, Constants.PWM_DUTY)

    def backward(self):
        lgpio.gpio_write(self.h, self.in1, 0)
        lgpio.gpio_write(self.h, self.in2, 1)
        lgpio.tx_pwm(self.h, self.pwm_pin, Constants.PWM_FREQ, Constants.PWM_DUTY)

    def stop(self):
        lgpio.tx_pwm(self.h, self.pwm_pin, Constants.PWM_FREQ, 0)
        
    def move(self, speed_a, speed_b):
            lgpio.gpio_write(self.h, self.in1, speed_a)
            lgpio.gpio_write(self.h, self.in2, speed_b)
            lgpio.tx_pwm(self.h, self.pwm_pin, Constants.PWM_FREQ, Constants.PWM_DUTY)
