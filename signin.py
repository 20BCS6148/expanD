#!C:\Users\bisht\AppData\Local\Programs\Python\Python39\python.exe
import database_form
import cgi,cgitb
import sqlite3
form = cgi.FieldStorage()
print("Content-type: text/html\r\n\r\n")
print('<html>')
print('<head>')
print("<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css' integrity='sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm' crossorigin='anonymous'>")


#name = form.getvalue('name')
username = form.getvalue('username')
#email = form.getvalue('email')
password = form.getvalue('password')
#subjectname = form.getvalue('subjectname')
beans =[]
def menu():
    connection = database_form.connect()
    #database_form.create_table(connection)
    #database_form.add_bean(connection,name,username,email,password,subjectname)
    beans=database_form.get_beans_by_name(connection,username,password)
    if len(beans)==1:
      for bean in beans:
        print(bean)
        print("welcome again!")
    else:
        print('''<div class="alert1">
                 <span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span>
                    Invalid username and password!!
                 </div>''')  
        print('''<div class="alert2">
                 <span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span>
                    Redirecting back to Signin Form !
                 </div>''')  
        print("<button type='button' class='btn btn-outline-info'><a href='index.html'>HOME</a></button>")                 

menu()



print('</head>')
print('<style>')
print('''/* The alert message box */
.alert1 {
  padding: 20px;
  background-color: #f44336; /* Red */
  color: white;
  margin-bottom: 15px;
}
.alert2 {
  padding: 20px;
  background-color: #D1D100; /* Yellow*/
  color: white;
  margin-bottom: 15px;
}
body{
    background:url(https://tenor.com/view/pretty-colour-pop-gif-18875088) ;
    background-position: center;
    
}
button{
    text-align: center;
    margin: 0;
    position: absolute;
    top: 30%;
    left: 50%;
    -ms-transform: translate(-50%, -50%);
    transform: translate(-50%, -50%);
}

/* The close button */
.closebtn {
  margin-left: 15px;
  color: white;
  font-weight: bold;
  float: right;
  font-size: 22px;
  line-height: 20px;
  cursor: pointer;
  transition: 0.3s;
}

/* When moving the mouse over the close button */
.closebtn:hover {
  color: black;
}''')
print('</style>')
print('<body>')
print("<h2>Hello %s %s </h2>" % (username))
print('<script>')
print('''// Get all elements with class="closebtn"
var close = document.getElementsByClassName("closebtn");
var i;

// Loop through all close buttons
for (i = 0; i < close.length; i++) {
  // When someone clicks on a close button
  close[i].onclick = function(){

    // Get the parent of <span class="closebtn"> (<div class="alert">)
    var div = this.parentElement;

    // Set the opacity of div to 0 (transparent)
    div.style.opacity = "0";

    // Hide the div after 600ms (the same amount of milliseconds it takes to fade out)
    setTimeout(function(){ div.style.display = "none"; }, 600);
  }
}''')
print('</script>')
print("<meta http-equiv='refresh' content=5;url='index.html' />")
print("</body>")
print("</html>")