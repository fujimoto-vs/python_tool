from database.db import get_connection


def insert_event(title):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO events(title)
        VALUES(?)
        """,
        (title,)
    )

    event_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return event_id


def insert_event_date(
        event_id,
        candidate_date
):

    conn = get_connection()

    conn.execute(
        """
        INSERT INTO event_dates(
            event_id,
            candidate_date
        )
        VALUES (?, ?)
        """,
        (
            event_id,
            candidate_date
        )
    )

    conn.commit()
    conn.close()


def get_all_events():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, title
        FROM events
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows