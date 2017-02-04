
# GPIO libraries
import numpy as np
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# based off of BCM numbering

MATRIX = [ [1, 2, 3, 'A'],
           [4, 5, 6, 'B'],
           [7, 8, 9, 'C'],
           ['*', 0, '#', 'D']]

ROW = [7 ,11 ,13 ,15]
COL = [12, 16, 18, 22]

for j in range(4):
    GPIO.setup(COL[j], GPIO.OUT)
    GPIO.output(COL[j], 1)

for i in range(4):
    GPIO.setup(ROW[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)

try:
    while(True):
        ## CODE ##
        for j in range(4):
            GPIO.output(COl[j], 0)
            for i in range(4):
                if GPIO.input(ROW[i]) == 0:
                    print MATRIX[i][j]
                    while(GPIO.input(ROW[i])== 0):
                        pass

            GPIO.output(COL[j], 1)
except KeyboardInterrupt:
    GPIO.cleanup()









