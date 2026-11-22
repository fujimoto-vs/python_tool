from database.db import get_connection


def insert_event(title):

    conn = get_connection()

    conn.execute(
        """
        INSERT INTO events(title)
        VALUES(?)
        """,
        (title,)
    )

    conn.commit()
    conn.close()