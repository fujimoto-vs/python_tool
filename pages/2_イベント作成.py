import streamlit as st

from services.event_service import (
    add_event
)

st.title("イベント作成")

title = st.text_input("イベント名")

date1 = st.date_input(
    "候補日1"
)

date2 = st.date_input(
    "候補日2"
)

date3 = st.date_input(
    "候補日3"
)

date4 = st.date_input(
    "候補日4"
)

date5 = st.date_input(
    "候補日5"
)

date6 = st.date_input(
    "候補日6"
)

date7 = st.date_input(
    "候補日7"
)

date8 = st.date_input(
    "候補日8"
)

date9 = st.date_input(
    "候補日9"
)

date10 = st.date_input(
    "候補日10"
)

if st.button("イベント作成"):

    if add_event(title):
        st.success(f"{title}を作成しました")

    else:
        st.error("イベント名を入力してください")