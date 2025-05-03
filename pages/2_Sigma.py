import streamlit as st
st.set_page_config(
    page_title="Sigma",
    page_icon="👋",
)
st.markdown("# Sigma?")
st.sidebar.header("")
backgroundColor= "#000000"
on = st.toggle("Sigma")
if on:
  st.image("960.webp")
