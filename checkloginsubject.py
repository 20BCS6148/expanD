#!C:\Users\bisht\AppData\Local\Programs\Python\Python39\python.exe
from sqlite3.dbapi2 import connect
import database_form
import sqlite3
import cgi,cgitb
import random
form = cgi.FieldStorage()
print("Content-type: text/html\r\n\r\n")
print('<html>')
print('<head>')

username = form.getvalue('username')
password = form.getvalue('password')
file = open("expanD.txt","w")
file.write(str(username))
file.write("\n")
file.write(str(password))
file.close()

def menu():
    connection = database_form.connect()
    
    #database_form.create_table_rand(connection)
    #database_form.add_rand(connection,Key,username,password)
    beans=database_form.get_beans_by_name(connection,username,password)
    if len(beans)==1:
      for bean in beans:
        name = bean[1] 
        email =bean[3]
        uname = bean[2]
        course = bean[5] 
    return course

subject = menu()    
if subject == "Web Development":
    print("<meta http-equiv='refresh' content=0;url='web-dev.html' />")
elif subject == "Data Structures":
    print("<meta http-equiv='refresh' content=0;url='data-structure.html' />") 
elif subject == "Algorithm":
    print("<meta http-equiv='refresh' content=0;url='algorithm.html' />")
elif subject == "Competitional Coding":
    print("<meta http-equiv='refresh' content=0;url='comp-code.html' />")           
else:
    print('<script>')
    print('''
      
       
       alert("There is some problem in your login!");

          ''')
    print('</script>')
    print("<meta http-equiv='refresh' content=0;url='login-signup.html' />")
print('</head>')
print("</html>")    