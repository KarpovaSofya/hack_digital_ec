import sqlite3

def create_db():
		conn = sqlite3.connect("users.db")
		cursor = conn.cursor()
		cursor.execute("""CREATE TABLE users (id text, name text, s_group text, admin_acces integer)""")

create_db()