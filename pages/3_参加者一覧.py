import streamlit as st
from services.member_service import get_members

st.title("参加者一覧")

members = get_members()

if not members:
    st.info("参加者がいません")

else:
    for id, name, status in members:
        st.write(
            f"{name} : {status}"
        )