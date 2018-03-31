import psycopg2
import sys
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def main():
    #Define our connection string
    conn_string = "host='localhost' dbname='postgres' user='postgres' password='Xana42169!!!'"

    # print the connection string we will use to connect
    #print "Connecting to database\n	->%s" % (conn_string)

    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cur = conn.cursor()
    print("Disconnected!")
    createdb = ("""DROP DATABASE Ox431_DB""")

    cur.execute(createdb)


if __name__ == "__main__":
    main()
