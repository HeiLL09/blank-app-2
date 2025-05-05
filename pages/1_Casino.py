import streamlit as st
import random
import time
st.set_page_config(page_title="Casino", page_icon="🎰")
st.markdown("# Casino")
st.sidebar.header("Smurfik casino")
backgroundColor= "#000000"
left, middle, right = st.columns(3, gap="small")
 
if st.button("Крутить"):
  x = random.randint(1,3)
  if x ==1:
    left.image("72.png")
  if x ==2:
    left.image("lemon.png")
  if x ==3:
    left.image("vishna1.png") 
  y = random.randint(1,3)
  if y ==1:
    middle.image("72.png")
  if y ==2:
    middle.image("lemon.png")
  if y ==3:
    middle.image("vishna1.png") 
 
  z = random.randint(1,3)
  if z ==1:
    right.image("72.png")
  if z ==2:
    right.image("lemon.png")
  if z ==3:
    right.image("vishna1.png") 
  if x== y and x == z and z == y:
    st.balloons()
    st.write("# ВЫ ВЫИГРАЛИ")
    st.video("document_5436337962805651912.mp4")
    time.sleep(3)
  else:
    st.write("# ВЫ ПРОИГРАЛИ")
  
