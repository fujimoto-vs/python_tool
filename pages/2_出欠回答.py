import streamlit as st

from services.member_service import (
    get_members,
    change_status
)

st.title("出欠回答")

members = get_members()

if not members:
    st.warning("参加者がいません")

else:
    member_dict = {
        f"{name} (ID:{id})": id
        for id, name, status in members
    }

    selected = st.selectbox(
        "名前を選択",
        member_dict.keys()
    )

    status = st.radio(
        "出欠",
        ["参加", "不参加"]
    )

    if st.button("更新"):

        member_id = member_dict[selected]

        change_status(
            member_id,
            status
        )

        st.success("更新しました")