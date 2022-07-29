import sqlite3
import threading
from config import fields


class BotDB:

    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.lock = threading.Lock()
        self.id = lambda user_id: f'id_{user_id}'

    def sql_execute(self, sql):
        with self.lock:
            return self.cursor.execute(sql)

    def new_user(self, user_id):
        self.sql_execute(f"CREATE TABLE if not exists {self.id(user_id)} (id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE, "
                         f"task STRING ({fields[0][1]}), deadline STRING ({fields[1][1]}), status INTEGER DEFAULT (0))")
        if not self.sql_execute(f"SELECT id FROM {self.id(user_id)}").fetchall():
            self.sql_execute(
                f"INSERT INTO {self.id(user_id)} (id,task, deadline, status) VALUES (0, 'last command', '', 3)")
        self.conn.commit()

    def get_table(self, user_id):
        result = self.sql_execute(f"SELECT * FROM {self.id(user_id)}").fetchall()
        print(result)
        return result

    def update_command(self, user_id, command):
        self.sql_execute(f"UPDATE {self.id(user_id)} SET deadline = '{command}' WHERE id = 0")
        self.conn.commit()

    def check_command(self, user_id):
        result = self.sql_execute(f"SELECT deadline FROM {self.id(user_id)} WHERE id = 0").fetchone()[0]
        return result

    def add_task(self, user_id, task):
        self.sql_execute(f"INSERT INTO {self.id(user_id)} (task, deadline, status) "
                         f"VALUES ('{task}', '', 0)")
        self.conn.commit()
        result = self.sql_execute(f"SELECT id FROM {self.id(user_id)}").fetchall()[-1][0]
        return result

    def change_task(self, user_id, task, id):
        self.sql_execute(f"UPDATE {self.id(user_id)} SET task = '{task}' WHERE id = {id}")
        self.conn.commit()

    def add_deadline(self, user_id, deadline, id):
        self.sql_execute(f"UPDATE {self.id(user_id)} SET deadline = '{deadline}' WHERE id = {id}")
        self.conn.commit()

    def change_status(self, user_id, id, status):
        self.sql_execute(f"UPDATE {self.id(user_id)} SET status = {status} WHERE id = {id}")
        self.conn.commit()
