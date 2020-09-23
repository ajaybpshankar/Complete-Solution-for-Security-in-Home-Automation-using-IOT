import RPi.GPIO as GPIO
import time

sensor=5
buzzer=3

GPIO.setwarnings(False)
                                #clean up at the end of your script
GPIO.setmode(GPIO.BOARD)                #to specify whilch pin numbering system
    
GPIO.setup(sensor, GPIO.IN)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.output(buzzer,False)
print("water ready")
try:	

	while True:
           i=GPIO.input(sensor)
           if i==0:
      			GPIO.output(buzzer,False)
                	print("hihghlevel",i)
                	#while GPIO.input(sensor):
	                time.sleep(0.2)
           else:
                	GPIO.output(buzzer,True)
                	print("water low",i)
except KeyboardInterrupt:
	GPIO.cleanup()
