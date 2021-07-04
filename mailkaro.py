#!C:\Users\bisht\AppData\Local\Programs\Python\Python39\python.exe
import smtplib
import cgi,cgitb
import database_form
import imghdr
from email.message import EmailMessage
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
cgitb.enable()
msg = EmailMessage()
mail = cgi.FieldStorage()
print("Content-type: text/html\r\n\r\n")
print('<html>')
print('<head>')



email = mail.getvalue('email')
username = mail.getvalue('username') 
def menu():
    connection = database_form.connect()
    #database_form.create_table_honey(connection)
    nme = database_form.get_name(connection,username)
    return nme[0]
nmme =menu() 
print(nmme)   

message = str(username) + str(len(username)*100) + "  -  This is your UID"
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()

server.login('sushantbisht1649@gmail.com','isutovgafibgssua')


font = ImageFont.truetype('arial.ttf',60)

img = Image.open('receipt.jpg')
draw = ImageDraw.Draw(img)
draw.text(xy=(550,660),text='{}'.format(nmme),fill=(0,0,0),font=font)

img.save('pictures/{}.jpg'.format(nmme))
with open('pictures/{}.jpg'.format(nmme),'rb') as m:
    file_data = m.read()
    file_type = imghdr.what(m.name)
    file_name = m.name

  
server.sendmail('sushantbisht1649@gmail.com',email,message)

print("Message sent plz check your mail!")
def get_email(email):
    return email
def get_username(username):
    return username  
server.quit()
print("<meta http-equiv='refresh' content=0;url='payment3.html' />")
print("</body>")
print("</html>")

  