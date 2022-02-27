import sqlite3

connection = sqlite3.connect('mydatabase.db')
cursor = connection.cursor()
sql = '''
    Create TABLE IF NOT EXISTS Employees(
        id INTEGER,
        name VARCHAR(64),
        department VARCHAR(32)
    ):
'''

cursor.execute(sql)
connection.commit()
connection.close()