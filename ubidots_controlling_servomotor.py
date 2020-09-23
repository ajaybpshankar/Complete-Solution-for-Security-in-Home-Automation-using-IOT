import RPi.GPIO as GPIO
import serial
from ubidots import ApiClient
from time import sleep      # Importing sleep from time library to add delay in code
servo_pin = 3
#ser=serial.Serial('/dev/ttyS0',9600,timeout=1)
GPIO.setwarnings(False)      # Initializing the GPIO 21 for servo motor
GPIO.setmode(GPIO.BOARD)
api=ApiClient(token="BBFF-z4uoYPhjFEfT7MnRapKthXwTVs4XJ1")
variable=api.get_variable("5f33cf8b1d847271090a8e78")

a=variable.get_values(1)
if a[0]['value']:
    GPIO.setup(servo_pin, GPIO.OUT)     # Declaring GPIO 21 as output pin
    p = GPIO.PWM(servo_pin, 50)     # Created PWM channel at 50Hz frequency
    p.start(2.5)
    sleep(10)
    try: 
        p.ChangeDutyCycle(7.5)  # Move servo to 90 degrees
        sleep(1)
        print("door is opened")
        p.ChangeDutyCycle(12.5) # Move servo to 180 degrees
        sleep(1)
        print("door is closed")
    except KeyboardInterrupt:
        pass   # Go to next line
    GPIO.cleanup()
else:
	print("door is closed :) ")




