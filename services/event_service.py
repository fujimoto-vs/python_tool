from database.event_repository import insert_event


def add_event(title):

    title = title.strip()

    if not title:
        return False
    
    insert_event(title)

    return True