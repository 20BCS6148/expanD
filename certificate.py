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
username = mail.getvalue('username')
Name = mail.getvalue('name')
email = mail.getvalue('email')
uid = str(username) + str(len(username)*100)
def menu():
    connection = database_form.connect()
    #database_form.create_table_certy(connection)
    database_form.add_certy(connection,uid,Name,email)

menu()
Sender_Email = "sushantbisht1649@gmail.com"
Reciever_Email = email
#Password = 'Dell@1649'
newMessage = EmailMessage()                         
newMessage['Subject'] = "Subscription" 
newMessage['From'] = Sender_Email                   
newMessage['To'] = Reciever_Email                   
newMessage.set_content('from Team expanD !') 

font = ImageFont.truetype('arial.ttf',60)

img = Image.open('receipt.jpg')
draw = ImageDraw.Draw(img)
draw.text(xy=(550,660),text='{}'.format(Name),fill=(0,0,0),font=font)

img.save('pictures/{}.jpg'.format(Name))
with open('pictures/{}.jpg'.format(Name),'rb') as m:
    file_data = m.read()
    file_type = imghdr.what(m.name)
    file_name = m.name
newMessage.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    
    smtp.login('sushantbisht1649@gmail.com', 'isutovgafibgssua')              
    smtp.send_message(newMessage)   

  


print("Message sent plz check  your mail !")

print("<meta http-equiv='refresh' content=0;url='index.html' />")
print("</body>")
print("</html>")


