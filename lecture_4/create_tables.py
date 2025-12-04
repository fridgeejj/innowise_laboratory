import sqlite3

conn = sqlite3.connect("school.db")

with open("create_tables.sql", "r") as f:
    conn.executescript(f.read())

conn.commit()
conn.close()

print("Tables created.")
