import sqlite3

DB_PATH = "data/nomikai.db"


def get_connection():
    return sqlite3.connect(
        DB_PATH
    )


def init_db():
    conn = get_connection()

    # 参加者
    conn.execute("""
        CREATE TABLE IF NOT EXISTS members(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)

    # イベント
    conn.execute("""
        CREATE TABLE IF NOT EXISTS events(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL
        )
    """)

    # 候補日
    conn.execute("""
        CREATE TABLE IF NOT EXISTS event_data(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_id INTEGER NOT NULL,
            candidate_date TEXT NOT NULL
        )
    """)

    # 投票
    conn.execute("""
        CREATE TABLE IF NOT EXISTS votes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            member_id INTEGER NOT NULL,
            data_id INTEGER NOT NULL,
            status TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()