import sqlite3

conn = sqlite3.connect("school.db")

with open("insert_data.sql", "r") as f:
    conn.executescript(f.read())

conn.commit()
conn.close()

print("Data inserted.")
