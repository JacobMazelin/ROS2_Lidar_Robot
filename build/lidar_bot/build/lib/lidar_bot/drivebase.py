import lgpio
from lidar_bot.constants import Constants
from lidar_bot.motor import Motor
import time

class DriveBase:
    def __init__(self):
        self.h = lgpio.gpiochip_open(0)
        lgpio.gpio_claim_output(self.h, Constants.STBY)
        self.left_motor = Motor(Constants.PWMA, Constants.AI1, Constants.AI2, self.h)
        self.right_motor = Motor(Constants.PWMB, Constants.BI1, Constants.BI2, self.h)

    def standby(self, state):
        lgpio.gpio_write(self.h, Constants.STBY, state)

    def forward(self):
        self.standby(1)
        self.left_motor.forward()
        self.right_motor.forward()

    def backward(self):
        self.standby(1)
        self.left_motor.backward()
        self.right_motor.backward()

    def left(self):
        self.standby(1)
        self.left_motor.backward()
        self.right_motor.forward()

    def right(self):
        self.standby(1)
        self.left_motor.forward()
        self.right_motor.backward()

    def stop(self):
        self.standby(0)
        self.left_motor.stop()
        self.right_motor.stop()
        
    def move(self, speed_a, speed_b):
        self.standby(1)
        self.left_motor.move(speed_a, speed_b)
        self.right_motor.move(speed_a, speed_b)

    def drive_square(self, duration=1):
        for _ in range(4):
            self.forward()
            time.sleep(duration)
            self.right()
            time.sleep(0.5)
        self.stop()
