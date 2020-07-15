import sqlite3

with sqlite3.connect("sample.db") as connection:
    c = connection.cursor()
    c.execute("CREATE TABLE posts(title TEXT, description TEXT )")
    c.execute('INSERT INTO posts VALUES("Good", "I am good")')
    c.execute('INSERT INTO posts VALUES("Hey", "How are you")')
    c.execute('INSERT INTO posts VALUES("Lets", "Have cup of tea")')




