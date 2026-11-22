from database.member_repository import(
    insert_member
)


def add_member(name):

    if not name:
        return False

    insert_member(name)

    return True