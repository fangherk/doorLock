
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
MOTORS = [33, 35, 37]

for j in range(4):
    GPIO.setup(COL[j], GPIO.OUT)
    GPIO.output(COL[j], 1)

for i in range(4):
    GPIO.setup(ROW[i], GPIO.IN, pull_up_down = GPIO.PUD_UP)


for k in range(3):
    GPIO.setup(MOTORS[k], GPIO.OUT)
    
state = 0
storage = ""
#old = time.time()

GPIO.output(MOTORS[2], GPIO.LOW)
    
def unlock():
    print(" OPEN MOTORS HIGH ")
    GPIO.output(MOTORS[0], GPIO.HIGH)
    GPIO.output(MOTORS[1], GPIO.LOW)
    GPIO.output(MOTORS[2], GPIO.HIGH)
    time.sleep(2)
    GPIO.output(MOTORS[2], GPIO.LOW)
        


def wrong():
    print("wrong")
    GPIO.setup(40, GPIO.OUT)
    GPIO.output(40, GPIO.HIGH)
    time.sleep(0.05)
    GPIO.output(40, GPIO.LOW)
    time.sleep(0.05)
    GPIO.output(40, GPIO.HIGH)
    time.sleep(0.05)
    GPIO.output(40, GPIO.LOW)
    time.sleep(0.05)
    GPIO.output(40, GPIO.HIGH)
    time.sleep(0.05)
    GPIO.output(40, GPIO.LOW)

try:
    while(True):
        
        for j in range(4):
            GPIO.output(COL[j], 0)
            for i in range(4):
                if GPIO.input(ROW[i]) == 0:
                    storage += str(MATRIX[i][j])
                    print("code: {} state: {}".format(MATRIX[i][j], state))
                    print(storage)

                    if state == 3:
                        if storage == "1234":
                            unlock()
                        else:
                            wrong()
                    state += 1
                    if state >= 4:
                        storage = ""   
                        state = 0
                    #now = time.time()
                    # if now- old > 10 and state = 0:
                      #  state = 0
                      #  old = now
                    
                    while(GPIO.input(ROW[i])== 0):
                        pass

            time.sleep(0.02)
            GPIO.output(COL[j], 1)
except KeyboardInterrupt:
    GPIO.cleanup()









