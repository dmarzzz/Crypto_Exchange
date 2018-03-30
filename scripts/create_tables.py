import psycopg2
import sys

def create_and_populate_tables():

    #Define our connection parameters
    conn_string = "host='localhost' dbname='postgres' user='postgres' password='password'"
    
    #Connect to database
    conn = psycopg2.connect(conn_string)

    #Initialize cursor
    cur = conn.cursor()

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
    """INSERT INTO comments values 
        (01023, 19823, 'This comment is for the dank question'),
        (39033, 19823, 'This comment is another for the dank question'),
        (09182, 19823, 'This comment  yet another for the dank question'),
        (03928, 19823, 'This comment is the fourth for the dank question'),
        (55555, 19823, 'This comment is the final for the dank question')
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


    #Destroy connection
    cur.close()
    conn.commit()
    conn.close()

create_and_populate_tables()