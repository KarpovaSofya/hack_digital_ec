import sqlite3

def find_user_id(db, u_id):
	base = db+'.db'
	sql = 'SELECT * FROM ' + db + ' WHERE id=?'
	conn = sqlite3.connect(base)
	cursor = conn.cursor()
	cursor.execute(sql, [(u_id)])
	return cursor.fetchall()

def find_user_name(db, name):
	base = db+'.db'
	sql = 'SELECT * FROM ' + db + ' WHERE name=?'
	conn = sqlite3.connect(base)
	cursor = conn.cursor()
	cursor.execute(sql, [(name)])
	return cursor.fetchall()

def delete_user(db, id):
	base = db+'.db'
	conn = sqlite3.connect(base)
	cursor = conn.cursor()
	sql = 'DELETE FROM ' + db + ' WHERE id = \'' + id + '\''
	cursor.execute(sql)
	conn.commit()

def show_db(db):
	base = db+'.db'
	sql = 'SELECT rowid, * FROM ' + db + ' ORDER BY id'
	conn = sqlite3.connect(base)
	cursor = conn.cursor()
	print("Here's a listing of all the records in the table:")
	for row in cursor.execute(sql):
		print(row)

def user_in_base(db,u_id):
	if len(find_user_id(db,u_id)) > 0:
		return True
	else:
		return False

def add_new_user(db, u_id, name, gr, adm_acc):
	base = db+'.db'
	if user_in_base(db,u_id):
		print('You are already in base')
	else:
		sql = 'INSERT INTO ' + db + ' VALUES (\'' + u_id +'\', \'' + name +'\', \'' + gr +'\', \'' + adm_acc + '\')'
		conn = sqlite3.connect(base)
		cursor = conn.cursor()
		cursor.execute(sql)
		conn.commit()

db = 'users'
i = '2'
n = 'Safonov'
group = 'ПМ-1701'
adm_acc = '1'

#print(user_in_base(db,i))
#add_new_user(db,i,n,group,adm_acc)
#show_db(db)
#delete_user(db,'1')
#find_user_id(db,'1')
#print(find_user_name(db,'5'))
#conn = sqlite3.connect("users.db")
#cursor = conn.cursor()
#print("Here's a listing of all the records in the table:")
#for row in cursor.execute("SELECT rowid, * FROM users ORDER BY id"):
#	print(row)