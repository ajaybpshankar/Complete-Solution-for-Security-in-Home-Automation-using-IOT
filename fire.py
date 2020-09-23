import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
d0=13
led=15
GPIO.setup(d0,GPIO.IN)
GPIO.setup(led,GPIO.OUT)
while True:
    a=GPIO.input(d0)
    if a==1:
        print("fire is not detected")
        GPIO.output(led,0)
    else:
        print("fire is detected")
        GPIO.output(led,1)
        print("sprinkler is on")


