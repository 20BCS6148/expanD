#!C:\Users\bisht\AppData\Local\Programs\Python\Python39\python.exe
from email import message
import smtplib
import cgi,cgitb
from email.message import EmailMessage
cgitb.enable()
msg = EmailMessage()
mail = cgi.FieldStorage()
print("Content-type: text/html\r\n\r\n")
print('<html>')
print('<head>')



name = mail.getvalue('name')
email = mail.getvalue('email') 
subject = mail.getvalue('subject')
number = mail.getvalue('phonenumber')
mes = mail.getvalue('message')

newMessage = EmailMessage()                         
newMessage['Subject'] = "Contact form" 
newMessage['From'] = email                  
newMessage['To'] = 'sushantbisht1649@gmail.com'    
messag = str(email)+str("   ")+str(mes)+str("   ") +str(number)                
newMessage.set_content(messag) 


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    
    smtp.login('sushantbisht1649@gmail.com', 'isutovgafibgssua')              
    smtp.send_message(newMessage)   

print("Message sent plz check your mail!")  
def get_email(email):
    return email
def get_username(username):
    return username  

print("<meta http-equiv='refresh' content=0;url='contactform.html' />")
print("</body>")
print("</html>")

  