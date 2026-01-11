import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE users (
    username TEXT,
    password TEXT
)
""")

cursor.execute("INSERT INTO users VALUES ('admin','admin123')")

conn.commit()
conn.close()

print("Database created successfully")
