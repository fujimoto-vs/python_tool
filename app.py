import streamlit as st

st.title("飲み会出欠管理")

name = st.text_input("名前")

if st.button("登録"):
    st.success(f"{name}さんを登録しました")
