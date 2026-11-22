import sqlite3

DB_PATH = "data/nomikai.db"


def get_connection():
    return sqlite3.connect(
        DB_PATH
    )


def init_db():
    conn = get_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS members(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()