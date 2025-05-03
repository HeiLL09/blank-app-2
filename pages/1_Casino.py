import streamlit as st
import random
import time
st.set_page_config(page_title="Casino", page_icon="🎰")
st.markdown("# Casino")
st.sidebar.header("Smurfik casino")
backgroundColor= "#000000"
left, middle, right = st.columns(3)
 
if st.button("Крутить"):
  time.sleep(1)
  x = random.randint(1,3)
  left.write(x)
  y = random.randint(1,3)
  middle.write(y)
  z = random.randint(1,3)
  right.write(z)
  if x== y and x == z and z == y:
    # st.balloons()
    st.write("# ВЫ ВЫИГРАЛИ")
    st.video("document_5436337962805651912.mp4")
    time.sleep(3)
  else:
    st.write("# ВЫ ПРОИГРАЛИ")
  
