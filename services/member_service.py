from database.member_repository import(
    insert_member,
    get_all_members,
    update_status
)


def add_member(name):

    if not name:
        return False

    insert_member(name)

    return True


def get_members():
    return get_all_members()


def change_status(member_id, status):
    update_status(member_id, status)