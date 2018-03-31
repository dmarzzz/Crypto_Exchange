import psycopg2
import sys

def main():
    #Define our connection string
    conn_string = "host='localhost' dbname='Ox431_DB' user='postgres' password='Xana42169!!!'"

    # print the connection string we will use to connect
    #print "Connecting to database\n	->%s" % (conn_string)

    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cur = conn.cursor()
    print("Connected!")
    creates = (
    """CREATE TABLE questions (
            question_id SERIAL PRIMARY KEY,
            question_summary VARCHAR(255) NOT NULL,
            question_desc varchar(1000),
            category varchar(30))""",
    """CREATE TABLE comments (
            comment_id SERIAL PRIMARY KEY,
            question_id int,
            foreign key(question_id) references questions,
            comment_text varchar(1000))
    """,
    """INSERT INTO questions values (19823,
        'This is a question summary... Cool shit bruh',
        'This description is dank',
        'Memes')
    """,
    """INSERT INTO comments values (01023,
        19823,
        'This comment is for the dank question'),
        (39033,
            19823,
            'This comment is another for the dank question'),
        (09182,
            19823,
            'This comment  yet another for the dank question'),
        (03928,
            19823,
            'This comment is the fourth for the dank question'),
        (55555,
            19823,
            'This comment is the final for the dank question')
    """)

    selects = (
    """
        SELECT * FROM questions

    """,
    """
        SELECT * FROM comments

    """
    )

    for create in creates:
        cur.execute(create)
    for select in selects:
        cur.execute(select)
        print(cur.fetchall())

    #destroy/close connections


    cur.close()
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
