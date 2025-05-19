import streamlit as st

st.write("# Галерея опенингов")


left, right = st.columns(2)
left.video("3op.mp4")
right.video("4op.mp4")