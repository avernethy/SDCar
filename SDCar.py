import cv2
import numpy as np
import logging
import math
import datetime
import sys

import car_dir as steer_motor
import motor as drive_motor

class SDCar(object):
    busnum = 1
    def __init__(self):
        logging.info('Creating an SDC object')
        steer_motor.setup(busnum=busnum)
        drive_motor.setup(busnum=busnum)
        self.spd_cmd = 0
        self.spd_cur = self.spd_cmd
        self.str_cmd = 450
        self.str_cur = self.str_cmd
        steer_motor.home()
        drive_motor.stop()

    def steer(self, str_cmd):
        MAX_STEER_DIFF = 1
        steer_motor.turn(self.str_cmd)

    def accel(self, spd_cmd):
        drive_motor.setSpeed(self.spd_cmd)

    def stop_all(self):
        steer_motor.home()
        drive_motor.stop()


