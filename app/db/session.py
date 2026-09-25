import sqlite3

connect = sqlite3.connect("test.db")

cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE A (
        id INTEGER, 
        name VARCHAR(50)
    );
""")

connect.commit()

connect.close()