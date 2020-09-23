import time, datetime
import RPi.GPIO as GPIO
import telepot
from telepot.loop import MessageLoop

room = 8
kitchen = 10
veranda =11 
puje=12

now = datetime.datetime.now()
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)


#LED Room
GPIO.setup(room, GPIO.OUT)
GPIO.output(room, 1) #Off initially
#LED Yellow
GPIO.setup(kitchen, GPIO.OUT)
GPIO.output(kitchen, 1) #Off initially
#LED Red
GPIO.setup(veranda, GPIO.OUT)
GPIO.output(veranda, 1) #Off initially
#LED green
GPIO.setup(puje,GPIO.OUT)
GPIO.output(puje,0)

def action(msg):
    chat_id = msg['chat']['id']
    command =str(msg['text']).lower()

    print 'Received: %s' % command

    if 'on' in command:
        message = " on "
        if 'room' in command:
            message = message + "room "
            GPIO.output(room,0)

        if 'kitchen' in command:
            message = message + "kitchen "
            GPIO.output(kitchen,0 )
        if 'veranda' in command:
            message = message + "veranda "
            GPIO.output(veranda, 0)
        if 'puje' in command:
            message = message + "puje "
            GPIO.output(puje, 1)
        if 'all' in command:
            message = message + "all "
            GPIO.output(room, 0)
            GPIO.output(kitchen, 0)
            GPIO.output(veranda, 0)
            GPIO.output(puje, 1)
        message = message + "light(s)"
        telegram_bot.sendMessage (chat_id, message)

    if 'off' in command:
        message = "Turned off "
        if 'room' in command:
            message = message + "room "
            GPIO.output(room, 1)
        if 'kitchen' in command:
            message = message + "kitchen "
            GPIO.output(kitchen, 1)
        if 'veranda' in command:
            message = message + "veranda "
            GPIO.output(veranda, 1)
        if 'puje' in command:
             message = message + "puje"
             GPIO.output(green, 0)
        if 'all' in command:
            message = message + "all "
            GPIO.output(room, 1)
            GPIO.output(kitchen, 1)
            GPIO.output(veranda, 1)
            GPIO.output(puje, 0)
        message = message + "light(s)"
        telegram_bot.sendMessage (chat_id, message)

 

telegram_bot = telepot.Bot('932479221:AAECcGQ1GiYw0LY7bJTnicclEGNxpk21S8w')
print (telegram_bot.getMe())
telegram_bot.message_loop(action)
print 'Up and Running....'


while 1:
    time.sleep(10)
