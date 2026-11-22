import streamlit as st
from services.member_service import add_member

st.title("参加登録")

name = st.text_input("名前")

if st.button("登録"):
    add_member(name)