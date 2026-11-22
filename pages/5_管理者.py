import streamlit as st

from services.member_service import get_members

st.title("管理者画面")

members = get_members()

join_count = sum(
    1 for _, _, status in members
    if status == "参加"
)

no_count = sum(
    1 for _, _, status in members
    if status == "不参加"
)

pending_count = sum(
    1 for _, _, status in members
    if status == "未回答"
)

c1, c2, c3 = st.columns(3)

c1.metric("参加", join_count)
c2.metric("不参加", no_count)
c3.metric("未回答", pending_count)