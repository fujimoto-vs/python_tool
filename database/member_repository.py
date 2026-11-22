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


def update_status(member_id, status):

    conn = get_connection()

    conn.execute(
        """
        UPDATE members
        SET status = ?
        WHERE id = ?
        """,
        (status, member_id)
    )

    conn.commit()
    conn.close()