import streamlit as st

from services.event_service import add_event

st.title("イベント作成")

title = st.text_input("イベント名")

if st.button("イベント作成"):

    if add_event(title):
        st.success(f"{title}を作成しました")

    else:
        st.error("イベント名を入力してください")