import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
GPIO.setwarnings(False)
reader = SimpleMFRC522()

print("place your tag")
id, text=reader.read()
if id==1002016711647:

	#print(id)
	print("door is opened")
else:
	print("door is not opened")
	print(id)
