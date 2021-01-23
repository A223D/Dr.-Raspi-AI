import email
import imaplib
from time import sleep
import tensorflow as tf
from PIL import Image
import numpy as np
from picamera import PiCamera
from gpiozero import Button
button = Button(4)
camera = PiCamera()
import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import Adafruit_CharLCD as LCD

lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 2
lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)


print("Everything imported succesfully")

model=tf.keras.models.load_model("newModel.h5")
print("model loaded")

lesion_type_dict = {
    4: 'Melanocytic nevi',
    'mel': 'Melanoma',
    'bkl': 'Benign keratosis-like lesions ',
     2: 'Basal cell carcinoma',
    0: 'Actinic keratoses',
    6: 'Vascular lesions',
    'df': 'Dermatofibroma'
}

lcd.message("READY!")
sleep(1)
lcd.clear()

while True:
      lcd.message("Checking\nfor email")
      mail = imaplib.IMAP4_SSL('imap.gmail.com')
      (retcode, capabilities) = mail.login('dr.raspi@gmail.com','PASSWORD')
      mail.list()
      mail.select('inbox')

      print("Checking for email")
      n=0
      (retcode, messages) = mail.search(None, '(UNSEEN)')
      if retcode == 'OK':


            for num in messages[0].split() :
                  print ('Processing ')
                  n=n+1
                  typ, data = mail.fetch(num,'(RFC822)')
                  for response_part in data:
                        if isinstance(response_part, tuple):
                              lcd.message("Mail\nreceived")
                              original = email.message_from_bytes(response_part[1])
                              print (original)

                              print (original['From'])
                              print (original['Subject'])
                              recipient = original['Subject']
            #print on screen that we are ready

                              typ, data = mail.store(num,'+FLAGS','\\Seen')

                              f = open("maildata.txt", "w")
                              f.write(original['Subject'])
                              f.close()
                              exec(open("./worker.py").read())

      #exec(open("./worker.py").read())
      sleep(5)
      print (n)
      lcd.clear()
