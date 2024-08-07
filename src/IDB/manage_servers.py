import sqlite3

location = r'D:\Projects\PYTHON\GIT\bot\SFAH\src\IDB\IDB.db'
table = 'servers'


def server_registration(identifier):
	with sqlite3.connect(location) as connection:
		cursor = connection.cursor()
		try:
			with connection:
				cursor.execute(f"""
				INSERT INTO {table} VALUES (
				"{identifier}", "nothing");""")
				return 0
		except Exception as e:
			print('DB Err? {}'.format(e))
			return -1


def server_unregistration(identifier):
	with sqlite3.connect(location) as connection:
		cursor = connection.cursor()
		try:
			with connection:
				cursor.execute(f"""
				DELETE FROM {table} WHERE server = "{identifier}";""")
				return 0
		except Exception as e:
			print('DB Err? {}'.format(e))
			return -1


def upd_manage_role(identifier_server, identifier_role):
	with sqlite3.connect(location) as connection:
		cursor = connection.cursor()
		try:
			with connection:
				cursor.execute(f"""
				UPDATE {table} 
				SET manage_morphs_role="{identifier_role}"
				WHERE server = "{identifier_server}";""")
				return 0
		except Exception as e:
			print('DB Err? {}'.format(e))
			return -1


def get_manage_role(identifier):
	with sqlite3.connect(location) as connection:
		cursor = connection.cursor()
		try:
			with connection:
				data = cursor.execute(f"""
				SELECT manage_morphs_role FROM {table} 
				WHERE server = "{identifier}";""").fetchone()

				if data == 'nothing':
					return 0
				return data[0]
		except Exception as e:
			print('DB Err? {}'.format(e))
			return -1