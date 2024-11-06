import sqlite3
from typing import List, Dict

def create_connection():
    return sqlite3.connect(":memory:")

def create_table(connection):
    with connection:
        connection.execute('''CREATE TABLE users (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL,
                                age INTEGER NOT NULL)''')

def add_user(connection, name: str, age: int):
    with connection:
        connection.execute('INSERT INTO users (name, age) VALUES (?, ?)', (name, age))

def get_all_users(connection) -> List[Dict]:
    cursor = connection.cursor()
    cursor.execute('SELECT id, name, age FROM users')
    rows = cursor.fetchall()
    return [{"id": row[0], "name": row[1], "age": row[2]} for row in rows]

def update_user_age(connection, user_id: int, new_age: int):
    with connection:
        connection.execute('UPDATE users SET age = ? WHERE id = ?', (new_age, user_id))

def delete_user(connection, user_id: int):
    with connection:
        connection.execute('DELETE FROM users WHERE id = ?', (user_id,))
