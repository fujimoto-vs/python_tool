import streamlit as st
from services.member_service import get_members

st.title("参加者一覧")

members = get_members()

for member in members:

    st.write(
        f"{member[1]} : {member[2]}"
    )