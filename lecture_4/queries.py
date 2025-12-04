import sqlite3

conn = sqlite3.connect("school.db")
cur = conn.cursor()

with open("queries.sql", "r") as f:
    queries = f.read()

# Split queries by semicolons
for query in queries.split(";"):
    q = query.strip()
    if q:
        print("\nQuery:")
        print(q)
        try:
            rows = cur.execute(q).fetchall()
            for row in rows:
                print(row)
        except Exception as e:
            print("Error:", e)

conn.close()
