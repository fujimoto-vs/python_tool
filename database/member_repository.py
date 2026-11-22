from database.db import get_connection


def insert_member(name):

    conn = get_connection()

    conn.execute(
        """
        INSERT INTO members
        (name, status)
        VALUES (?, ?)
        """,
        (name, "未回答")
    )

    conn.commit()
    conn.close()


def get_all_members():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name, status
        FROM members
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows