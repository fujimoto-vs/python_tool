import streamlit as st
from database.db import init_db

init_db()

st.set_page_config(
    page_title = "飲み会出欠管理",
    layoiut = "wide"
)

st.title("飲み会出欠管理")

st.write("左のメニューから選択してください")