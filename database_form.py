import sqlite3

CREATE_BEANS_TABLE = "CREATE TABLE signupinfo(ID INTEGER PRIMARY KEY, name TEXT NOT NULL,username TEXT NOT NULL UNIQUE,email TEXT,password TEXT,subjectname TEXT);"
CREATE_HONEY_TABLE = "CREATE TABLE paymentinfo(ID INTEGER PRIMARY KEY,uid TEXT ,username TEXT NOT NULL,email TEXT,card_number TEXT,amount INTEGER);"
CREATE_CERTY_TABLE = "CREATE TABLE certify(ID INTEGER PRIMARY KEY,uid TEXT, name TEXT NOT NULL,email TEXT);"

CREATE_RAND_TABLE = "CREATE TABLE randomaccess(ID INTEGER PRIMARY KEY,Key INTEGER,username TEXT, password INTEGER NOT NULL);"
INSERT_RAND = "INSERT INTO randomaccess(Key,username,password);"
GET_ALL_RAND ="SELECT * FROM randomaccess WHERE Key = ?;"
GET_RAND_BY_NAME ="SELECT * FROM signupinfo where username = ? AND password=?;"

INSERT_BEANS ="INSERT INTO signupinfo(name,username,email,password,subjectname) VALUES(?,?,?,?,?);"
INSERT_HONEY = "INSERT INTO paymentinfo(uid,username,email,card_number,amount) VALUES(?,?,?,?,?);"
INSERT_CERTY ="INSERT INTO certify(uid,name,email) VALUES (?,?,?)"
GET_ALL_BEANS = "SELECT * FROM signupinfo;"
GET_ALL_HONEY = "SELECT * FROM paymentinfo;"

GET_BEANS_BY_NAME ="SELECT * FROM signupinfo where username = ? AND password=?;"
GET_BEST_PREP_FOR_BEAN = "SELECT * FROM signupinfo where name=? ORDER BY rating DESC LIMIT 1;"
EDIT_TABLE_BEANS ='''UPDATE signupinfo
                    SET name = (?),
                     username = (?),
                     email = (?),
                     password = (?),
                     subjectname = (?)
                    WHERE
                     username = (?);
                    '''
GET_NAME ="SELECT name FROM signupinfo where username =?;"


def connect():
    return sqlite3.connect('formsinfo.db')

def create_table(connection):
    with connection:
        connection.execute(CREATE_BEANS_TABLE)

def create_table_honey(connection):
    with connection:
        connection.execute(CREATE_HONEY_TABLE)

def create_table_certy(connection):
    with connection:
        connection.execute(CREATE_CERTY_TABLE)

def create_table_rand(connection):
    with connection:
        connection.execute(CREATE_RAND_TABLE)

def add_rand(connection,Key,username,password):
    with connection:
        connection.execute(INSERT_RAND,(Key,username,password))

def add_bean(connection,name,username,email,password,subjectname):
    try:
        with connection:
            connection.execute(INSERT_BEANS,(name,username,email,password,subjectname))
    except:
        return "loggin fail"

def add_honey(connection,uid,username,email,card_number,amount):
    try:
        with connection:
            connection.execute(INSERT_HONEY,(uid,username,email,card_number,amount))
    except:
        return "loggin fail"

def add_certy(connection,uid,name,email):
    try:
        with connection:
            connection.execute(INSERT_CERTY,(uid,name,email))
    except:
        return "loggin fail"

def edit_value(connection,nname,nusername,nemail,npassword,nsubjectname,usernameold):
    with connection:
        connection.execute(EDIT_TABLE_BEANS,(nname,nusername,nemail,npassword,nsubjectname,usernameold))

def get_name(connection,username):
    with connection:
        return connection.execute(GET_NAME,(username,)).fetchone()  
              
def get_info(connection,Key):
    with connection:
        return connection.execute(GET_ALL_RAND,(Key,)).fetchall()

def get_rand_info(connection,username,password):
    with connection:
        return connection.execute(GET_RAND_BY_NAME,(username,password,)).fetchall()

def get_all_beans(connection):
    with connection:
        return connection.execute(GET_ALL_BEANS).fetchall()

def get_all_honey(connection):
    with connection:
        return connection.execute(GET_ALL_HONEY).fetchall()

def get_beans_by_name(connection,username,password):
    with connection:
        return connection.execute(GET_BEANS_BY_NAME,(username,password,)).fetchall() 

def get_best_prep_for_bean(connection,Name):
    with connection:
        return connection.execute(GET_BEST_PREP_FOR_BEAN,(Name,)).fetchall()        



      