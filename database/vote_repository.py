from database.db import get_connection


def insert_vote(
    member_id,
    date_id,
    status
):

    conn = get_connection()

    conn.execute(
        """
        INSERT INTO votes(
            member_id,
            date_id,
            status
        )
        VALUES(?,?,?)
        """,
        (
            member_id,
            date_id,
            status
        )
    )

    conn.commit()
    conn.close()