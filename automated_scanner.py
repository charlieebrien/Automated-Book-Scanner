# This program is a proof of concept for an automated book scanner.
# It runs once but it could be put in a for loop to runs many times to flip through an entire book and capture photos



# Import libraries
import RPi.GPIO as GPIO
import time
from picamera import PiCamera
from time import sleep

#creating a camera object
camera = PiCamera()

# set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

#  Set pins 11 & 12 as outputs, and define as PWM servo1 & servo2
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50) # pin 11 for servo1
GPIO.setup(12,GPIO.OUT)
servo2 = GPIO.PWM(12,50) # pin 12 for servo2

# setting variables which will be parameters to change the duty cycle
duty = 2
duty2 = 12
duty3 = 12

print("Start")

#flipping position of camera to get a properly orientated image
camera.vflip = True
camera.hflip = True
camera.resolution = (2592, 1944)
#taking a picture and saving it
camera.capture('/home/pi/Desktop/image.jpg')


# Start PWM running on both servos, value of 0 (pulse off)
servo1.start(0)
servo2.start(0)


# rotate servo1 (wheel) 180 degrees to lift page
while duty3 >= 2:
    servo1.ChangeDutyCycle(duty3)
    time.sleep(0.05)
    duty3 = duty3 - 1




# need to sleep program between consecutive movements of a servo for it to run correctly
time.sleep(2) 

#rotate servo2 (rod) to 0 degrees (starts at 180 deg) to flip page
while duty2 >= 2:
    servo2.ChangeDutyCycle(duty2)
    time.sleep(0.1)
    duty2 = duty2 - 1

time.sleep(2)

#rotate servo2 back to original position
servo2.ChangeDutyCycle(12)

#rotate servo1 back to original position
while duty <= 12:
    servo1.ChangeDutyCycle(duty)
    time.sleep(0.1)
    duty = duty + 1

time.sleep(0.5)


servo2.ChangeDutyCycle(0)
servo1.ChangeDutyCycle(0)




#stopping the servos
servo1.stop()
servo2.stop()
GPIO.cleanup()

print("End")

