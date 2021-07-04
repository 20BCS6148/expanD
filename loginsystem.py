from flask import Flask,request ,render_template,redirect
import os
import sqlite3

currentlocation = os.path.dirname(os.path.abspath(__file__))

myapp =  Flask(__name__)

@myapp.route("/")
def homepage():
    return render_template("index.html")

@myapp.route("/", methods =["POST"])
def checklogin():
    un = request.form["username"]
    p = request.form["password"]

    sqlconnection = sqlite3.Connection(currentlocation + "\Formsinfo.db")
    cursor = sqlconnection.cursor()

    query1 = "SELECT username,password From signupinfo WHERE username={UN} AND password={P})".format(UN=un ,P=p)        
    rows = cursor.execute(query1)
    rows = rows.fetchall()
    if len(rows)==1:
        return render_template("loggedin.html")
    else:
        return redirect("/index.html")

@myapp.route("/index.html", methods =["GET", "POST"])
def registorpage():
    if request.method == "POST":
        dname = request.form('name')
        dusername =request.form('username')
        demail = request.form('email')
        dpassword = request.form('pass')
        dsubjectname = request.form('subjectname')
        sqlconnection = sqlite3.Connection(currentlocation, + "\Formsinfo.db")
        cursor = sqlconnection.cursor()
        INSERT_BEANS ="INSERT INTO signupinfo VALUES('{name}','{username}','{email}','{password}','{subjectname}')".format(name= dname,username = dusername,email = demail,password = dpassword,subjectname=dsubjectname)
        cursor.execute(INSERT_BEANS)
        sqlconnection.commit()
        return redirect("/")
    return render_template("registered.html")




if (__name__)== "__main__":
    myapp.run()