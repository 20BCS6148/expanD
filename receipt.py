#!C:\Users\bisht\AppData\Local\Programs\Python\Python39\python.exe
#!C:\Users\bisht\AppData\Local\Programs\Python\Python39\python.exe

import smtplib

import database_form
import cgi,cgitb
import imghdr
from email.message import EmailMessage
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
from email.mime.text import MIMEText
cgitb.enable()


mail = cgi.FieldStorage()
print("Content-type: text/html\r\n\r\n")
print('<html>')
print('<head>')
print('<style>')
print(".body{ background:url(https://tenor.com/view/pretty-colour-pop-gif-18875088);}")
print('</style>')
email = mail.getvalue('email')
username = mail.getvalue('username')
card_number = mail.getvalue('card_number')
amount = mail.getvalue('amount')
uid = str(username) + str(len(username)*100)

def menu():
    connection = database_form.connect()
    #database_form.create_table_honey(connection)
    database_form.add_honey(connection,uid,username,email,card_number,amount)
    print("Record entred successfully !!!!")

menu()

Sender_Email = "sushantbisht1649@gmail.com"
Reciever_Email = email
#Password = 'Dell@1649'
newMessage = EmailMessage()                         
newMessage['Subject'] = "Subscription" 
newMessage['From'] = Sender_Email                   
newMessage['To'] = Reciever_Email                   
newMessage.set_content('we heartly welcome you in expanD !') 

with open('subscription.jpg', 'rb') as f:
    image_data = f.read()
    image_type = imghdr.what(f.name)
    image_name = f.name
newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    
    smtp.login('sushantbisht1649@gmail.com', 'isutovgafibgssua')              
    smtp.send_message(newMessage)   

  


print("Message sent plz check  your mail !")

print("<meta http-equiv='refresh' content=5;url='index.html' />")
print("</body>")
print("</html>")


