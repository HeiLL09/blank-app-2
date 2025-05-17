import streamlit as st
st.sidebar.header("Smurfik kombat")
st.write("# Smurfik Kombat")
left, middle, right = st.columns(3)
backgroundColor= "#000000"

if left.button("Кликнуть", type = "primary"):
   left.markdown("Ты же не думал, что я что то сделал?")