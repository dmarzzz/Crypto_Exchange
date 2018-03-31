import psycopg2
import sys

def insert_into_login_credentials(forms):
    print("Connected!")
    #Define our connection string
    conn_string = "host='localhost' dbname='projectoutline' user='postgres' password='Xana42169!!!'"

    name = forms[0]
    email = forms[1]
    username = forms[2]
    password = forms[3]
    # print the connection string we will use to connect
    #print "Connecting to database\n	->%s" % (conn_string)

    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)
    cur = conn.cursor()
    cur.execute("""INSERT INTO login_credentials(username, name, email, login_password) VALUES(%s, %s, %s, %s);""" ,( name, email ,username, password))
    # conn.cursor will return a cursor object, you can use this cursor to perform queries

    print("Connected!")



    conn.commit()
    cur.close()
    conn.close()
