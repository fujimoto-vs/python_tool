import streamlit as st
from services.member_service import get_members

st.title("参加者一覧")

members = get_members()

if not members:
    st.info("参加者が登録されていません")

else:
    for member in members:
        id, name, status = member

        st.write(
            f"名前:{name} 状態:{status}"
        )