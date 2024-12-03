import streamlit as st
import time

text="Downloading the effects"
bar=st.progress(0,text)

for i in range(100):
    time.sleep(0.01)
    bar.progress(i+1,text)

bar.empty()
st.button("Rerun")
st.balloons()