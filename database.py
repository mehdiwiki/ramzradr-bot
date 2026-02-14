import sqlite3
from datetime import datetime

conn = sqlite3.connect("ramzalert.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_id INTEGER UNIQUE,
    username TEXT,
    plan TEXT DEFAULT 'free',
    created_at TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS alerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    asset TEXT,
    target_price REAL,
    is_active INTEGER DEFAULT 1
)
""")

conn.commit()


def add_user(telegram_id, username):
    cursor.execute(
        "INSERT OR IGNORE INTO users (telegram_id, username, created_at) VALUES (?, ?, ?)",
        (telegram_id, username, datetime.now())
    )
    conn.commit()


def get_user(telegram_id):
    cursor.execute("SELECT * FROM users WHERE telegram_id=?", (telegram_id,))
    return cursor.fetchone()
