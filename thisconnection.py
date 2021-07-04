import mysql.connector

conn = mysql.connector.connect(host = "localhost",user = "root", password="",database="formsinfo")
cursor = conn.cursor()

CREATE_BEANS_TABLE = "CREATE TABLE signupinfo(ID INTEGER PRIMARY KEY, name TEXT,username TEXT,email TEXT,password TEXT,subjectname TEXT);"
INSERT_BEANS ="INSERT INTO signupinfo(name,username,email,password,subjectname) VALUES(?,?,?,?,?);"

cursor.execute(CREATE_BEANS_TABLE)
