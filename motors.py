#!/usr/bin/env python
# Simply sets motors on and off in both directions
# Motor A Pins 21 and 26
# Motor B Pins 19 and 24

import time, RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

# wait after setup to check nothing happens!
time.sleep(3)

# switch MotorA on forwards
GPIO.output (21, 0)
GPIO.output (26, 1)

# wait another 3 seconds
time.sleep(3)

# switch MotorA on backwards
GPIO.output (21, 1)
GPIO.output (26, 0)

# wait another 3 seconds
time.sleep(3)

# switch MotorA off
GPIO.output (21, 0)
GPIO.output (26, 0)

# wait another 3 seconds
time.sleep(3)

# switch MotorB on Forwards
GPIO.output (19, 0)
GPIO.output (24, 1)

# wait another 3 seconds
time.sleep(3)

# switch MotorB on Backwards
GPIO.output (19, 1)
GPIO.output (24, 0)

# wait another 3 seconds
time.sleep(3)

# switch MotorB off
GPIO.output (19, 0)
GPIO.output (24, 0)

GPIO.cleanup()
