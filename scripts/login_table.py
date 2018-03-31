import psycopg2
import sys

def insert_into_db(forms):
    #Define our connection string
    conn_string = "host='localhost' dbname='projectoutline' user='postgres' password='Xana42169!!!'"

    # print the connection string we will use to connect
    #print "Connecting to database\n	->%s" % (conn_string)

    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)
    createusertable = ("""CREATE TABLE login_credentials (
    username VArCHAR(30) NOT NULL,
    PRIMARY KEY(username),
    name VARCHAR(60) NOT NULL,
    email VARCHAR(60) NOT NULL,
    login_password VARCHAR(60) NOT NULL
    )""")
    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cur = conn.cursor()
    print("Connected!")
    cur.execute("""SELECT * FROM forum""")
    rows = cur.fetchall()
    print(rows)
