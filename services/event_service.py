from database.event_repository import (
    insert_event,
    insert_event_date
)


def add_event(
        title,
        dates
):

    title = title.strip()

    if not title:
        return False
    
    event_id = insert_event(title)

    for date in dates:
        insert_event_date(
            event_id,
            str(date)
        )

    return True