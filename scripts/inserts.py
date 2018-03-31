import psycopg2
import sys

def insert_into_users(forms):

    #Define our connection parameters
    conn_string = "host='localhost' dbname='postgres' user='postgres' password='password'"
    
    #Connect to database
    conn = psycopg2.connect(conn_string)

    #Initialize cursor
    cur = conn.cursor()

    name = forms[0]
    email = forms[1]
    username = forms[2]
    password = forms[3]


    cur.execute("INSERT INTO users (username, password, email) VALUES(%s, %s, %s);" ,(username, password ,email))

    #Destroy connection
    cur.close()
    conn.commit()
    conn.close()