import sqlite3

conn = sqlite3.connect("school.db")
conn.execute("PRAGMA foreign_keys = ON;")
conn.close()

print("Database created.")
