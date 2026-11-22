from database.member_repository import(
    insert_member,
    get_all_members
)


def add_member(name):

    if not name:
        return False

    insert_member(name)

    return True


def get_members():
    return get_all_members()