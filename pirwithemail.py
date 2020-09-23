import time
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import cv2
import numpy as np
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import password
from ubidots import ApiClient
from time import sleep
servo_pin = 3

password = password.password
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(40,GPIO.IN)
GPIO.setup(3,GPIO.OUT)
i=GPIO.input(40)
if i==1:
    print("no intruder")
    GPIO.output(38,1)
    time.sleep(0.1)
elif i==0:
    print("intruder detected")
    GPIO.output(3,0)
    time.sleep(0.1)
    def face_extractor(frame):
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray,1.3,5)
        if faces is():
            return None

        for(x,y,w,h) in faces:
            cropped_face = frame[y:y+h, x:x+w]

        return cropped_face


    cap = cv2.VideoCapture(0)
    count = 0

    while True:
        ret, frame = cap.read()
        if face_extractor(frame) is not None:
            count+=1
            face = cv2.resize(face_extractor(frame),(200,200))
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

            file_name_path = 'faces/user'+str(count)+'.jpg'
            cv2.imwrite(file_name_path,face)

            cv2.putText(face,str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
            cv2.imshow('Face Cropper',face)
        else:
            print("Face not Found")
            pass

        if cv2.waitKey(1)==13 or count==1:
            break
    print('Some one might have waiting here...Colleting Samples.. Completed!!!')
    cap.release()
    cv2.destroyAllWindows()

    if count==1:
	
        reciever = 'ajayshankar1998.bp@gmail.com'
        sender = 'ajayshankar17.bp@gmail.com'
        msg = MIMEMultipart()
        msg['To'] = reciever
        msg['From'] = 'realmeX' + '<' + sender + '>'
        msg['Subject']= 'intruder detected!!'
        msg_ready = MIMEText('Found some one near your house!!.','plain')
   
        image_open = open('faces/user1.jpg','rb').read()
        image_ready = MIMEImage(image_open,'jpg',name='intruder.jpg')
               
        msg.attach(msg_ready)
        msg.attach(image_ready)
               
        server =  smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(sender, password)
        print("logged in")
        server.sendmail(sender, reciever, msg.as_string())
        print("successfully sent mail!!")
        server.quit()
print(" Currently door is closed..wait untill owner respond to you")
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
        print("door is opened..Please step in..")
        p.ChangeDutyCycle(12.5) # Move servo to 180 degrees
        sleep(5)
        print("door is closed :( ")
    except KeyboardInterrupt:
        pass   # Go to next line
    GPIO.cleanup()
else:
	print("door is closed.. ")