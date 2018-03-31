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
        """CREATE TABLE users (
            user_id SERIAL PRIMARY KEY,
            username VARCHAR(20) UNIQUE,
            password VARCHAR(30),
            email VARCHAR(50) UNIQUE)""",

        """CREATE TABLE questions (
                question_id SERIAL PRIMARY KEY,
                user_id INT REFERENCES users(user_id),
                question_summary VARCHAR(255) NOT NULL,
                question_desc VARCHAR(1000),
                category VARCHAR(30))""",

        """CREATE TABLE comments (
                comment_id SERIAL PRIMARY KEY,
                user_id INT REFERENCES users(user_id),
                question_id INT REFERENCES questions(question_id),
                comment_text VARCHAR(1000) NOT NULL)""",

        """INSERT INTO users (username, password, email) VALUES
            ('alex1996', 'password1', 'asdf1@gmail.com'),
            ('alex1995', 'password2', 'asdf2@gmail.com'),
            ('alex1994', 'password3', 'asdf3@gmail.com'),
            ('alex1993', 'password4', 'asdf4@gmail.com')""",

        """INSERT INTO questions (user_id, question_summary, question_desc, category) VALUES
            (3, 'This is a question summary... Cool shit bruh', 'This description is dank', 'Memes'),
            (3, 'This question summary is cool shit bruh', 'This is a dank description', 'Memes'),
            (2, 'Question: is this summary cool shit bruh?', 'More like a dank prescription', 'Memes'),
            (1, 'This cool question summary is shit bruh', 'You can take this description to the bank', 'Memes')
            """,

        """INSERT INTO comments (user_id, question_id, comment_text) VALUES 
            (4, 1, 'This comment is for the dank question'),
            (2, 1, 'This comment is another for the dank question'),
            (1, 1, 'This comment  yet another for the dank question'),
            (3, 1, 'This comment is the fourth for the dank question'),
            (3, 1, 'This comment is the final for the dank question')
        """)


    selects = (
        "SELECT * FROM users",
        "SELECT * FROM questions",
        "SELECT * FROM comments"
    )

    for create in creates:
        cur.execute(create)

    for select in selects:
        cur.execute(select)
        rows = cur.fetchall()
        for row in rows:
            print(row)


    #Destroy connection
    cur.close()
    conn.commit()
    conn.close()

create_and_populate_tables()