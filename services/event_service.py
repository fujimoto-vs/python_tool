from database.event_repository import (
    insert_event,
    insert_event_date,
    get_all_events,
    get_event_dates
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


def get_events():
    return get_all_events()


def get_dates(event_id):
    return get_event_dates(event_id)