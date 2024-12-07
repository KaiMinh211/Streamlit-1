import streamlit as st
#Module --> python -m streamlit run lesson5.py  

if "likes" not in st.session_state:
    st.session_state["likes"]=0
if "comments" not in st.session_state:
    st.session_state["comments"]=[]



st.title("My blog")
st.write("By Khanh Minh")

st.write("I wake up everyday and sleep everyday")

col1,col2=st.columns(2)
with col1:
    st.image("media/me.jpg",caption="Minh in  his handsome school uniform",width=100)
with col2:
    st.image("media/food.jpg",caption="Minh's first atempt for his fried rice",width=100,)



col1,col2=st.columns(2)
with col2:
    bt1=st.button("Like blog")
    if bt1:
        st.session_state["likes"]+=1
        bt1=False
with col1:
    st.write("Likes: ",str(st.session_state["likes"]))



col1,col2=st.columns(2)

with col1:
    comment=st.text_area("Please leave a smart comment",placeholder="You are so handsome <3")
with col2:
    bt2=st.button("Comment")
    if bt2:
        st.session_state["comments"].append(comment)

for i in range(len(st.session_state["comments"])):
    st.write(f"someUser{i+1}: {st.session_state['comments'][i]}")




