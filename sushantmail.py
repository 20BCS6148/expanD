#!C:\Users\bisht\AppData\Local\Programs\Python\Python39\python.exe
import smtplib
import cgi,cgitb
from email.message import EmailMessage
from os import name
cgitb.enable()
msg = EmailMessage()
mail = cgi.FieldStorage()
print("Content-type: text/html\r\n\r\n")
print('<html>')
print('<head>')
name = mail.getvalue('name')
phonenumber = mail.getvalue('phonenumber')
email = mail.getvalue('email')
message = str(name) +"  "+ str(phonenumber) +"  "+ str(email)
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('sushantbisht1649@gmail.com','isutovgafibgssua')
server.sendmail(email,'sushantbisht1649@gmail.com',message)

print("Message sent plz check your mail!")
server.quit()
print("<meta http-equiv='refresh' content=0;url='sushantindex.html' />")
print("</body>")
print("</html>")