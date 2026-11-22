import streamlit as st
from services.member_service import get_members

st.title("出欠回答")

members = get_members()

if not members:
    st.warning("参加者がいません")
else:
    names = {
        member[1]: member[0]
        for member in members
    }

    selected_name = st.selectbox(
        "名前を選択",
        names.keys()
    )

    status = st.radio(
        "出欠",
        ["参加", "不参加"]
    )