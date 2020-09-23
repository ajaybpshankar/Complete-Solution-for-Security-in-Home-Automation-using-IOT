from time import sleep 
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
reader = SimpleMFRC522()
servo_pin = 3

print("place your tag")
id, text=reader.read()
if id==1002016711647:

        #print(id)
        print("waiting...")
        GPIO.setup(servo_pin,GPIO.OUT)
        p = GPIO.PWM(servo_pin,50) 
        p.start(2.5)
        try:
         
             p.ChangeDutyCycle(7.5)
             sleep(2)
             print("door is opened")
             p.ChangeDutyCycle(12.5)
             sleep(1)
             print("door is closed")
             
            
        except KeyboardInterrupt:
         pass 
        GPIO.cleanup() 
else:
        print("door is not opened")
        print(id)

