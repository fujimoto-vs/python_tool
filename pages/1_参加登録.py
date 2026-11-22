import streamlit as st
from services.member_service import add_member

st.title("参加登録")

name = st.text_input("名前")

if st.button("登録"):

    if add_member(name):
        st.success(
            f"{name}さんを登録しました"
        )
    else:
        st.error("名前を入力してください")