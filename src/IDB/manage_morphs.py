import sqlite3

location = r'D:\Projects\PYTHON\GIT\bot\SFAH\src\IDB\IDB.db'
table = 'SFAH'


def add_morph(data):
	with sqlite3.connect(location) as connection:
		cursor = connection.cursor()
		try:
			with connection:
				cursor.execute(f"""
				INSERT INTO {table} VALUES (
				"{str(data['id'])}",
				"{data['morph']}",
				"{data['inspector']}",
				"{data['bound']}",
				"{data['photo']}",
				"{data['structure']}")""")
				return 0
		except Exception as e:
			print('DB Err? {}'.format(e))
			return -1


def del_morph(identifier):
	with sqlite3.connect(location) as connection:
		cursor = connection.cursor()
		try:
			with connection:
				cursor.execute(f"""
				DELETE FROM {table} WHERE id = "{identifier}";""")
				return 0
		except Exception as e:
			print('DB Err? {}'.format(e))
			return -1


def find_morph(identifier):
	with sqlite3.connect(location) as connection:
		cursor = connection.cursor()
		try:
			with connection:
				data = cursor.execute(f"""
				SELECT * FROM {table} WHERE id = "{identifier}";""")
				return data.fetchone()
		except Exception as e:
			print('DB Err? {}'.format(e))
			return -1
