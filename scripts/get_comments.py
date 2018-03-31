import psycopg2
import sys

def getcomments():
    #Define our connection string
    conn_string = "host='localhost' dbname='Ox431_DB' user='postgres' password='Xana42169!!!'"
    conn = psycopg2.connect(conn_string)

    curr = conn.cursor()

    selectcomments = (
    """
    SELECT * FROM comments
    """
    )

    curr.execute(selectcomments)
    print(curr.fetchall())
    print("\n")

    curr.close()
    conn.commit()
    conn.close()


if __name__ == "__main__":
    getcomments()
