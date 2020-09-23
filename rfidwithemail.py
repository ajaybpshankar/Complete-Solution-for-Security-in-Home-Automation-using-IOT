import time
from threading import Thread, Event
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import cv2
import numpy as np
import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import password
password = password.password
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
GPIO.setwarnings(False)
stop_event = Event()
 
 
def do_actions():
 while True: 
    reader = SimpleMFRC522()
    id, text=reader.read()
    print(id)
    print("door is open")
 
        # Here we make the check if the other thread sent a signal to stop execution.
    if stop_event.is_set():
            break
 
 
if __name__ == '__main__':
    # We create another Thread
 action_thread = Thread(target=do_actions)
 
    # Here we start the thread and we wait 5 seconds before the code continues to execute.
 action_thread.start()
 action_thread.join(timeout=5)
 
    # We send a signal that the other thread should stop.
 stop_event.set()
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
 print('Colleting Samples Complete!!!')
 cap.release()
 cv2.destroyAllWindows()

 if count==1:
    print("waiting....")
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

