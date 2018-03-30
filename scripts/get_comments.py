import psycopg2
import sys

def getcomments():
    
    #Define our connection parameters
    conn_string = "host='localhost' dbname='postgres' user='postgres' password='password'"
    
    #Connect to database
    conn = psycopg2.connect(conn_string)

    #Initialize cursor
    cur = conn.cursor()

    sql = ("SELECT * FROM comments")

    curr.execute(sql)
    print(curr.fetchall())

    #Destroy connection
    curr.close()
    conn.commit()
    conn.close()



getcomments()