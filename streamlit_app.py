import streamlit as st
from time import sleep

col1,col2,col3=st.columns([4,2,4])
with col2:
    st.title("Neri")
st.write("Please login (username `test`, password `test`).")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

col1, col2, col3 = st.columns([2,6.5,1.5])
with col1:
    if st.button("Log in", type="primary"):
        if username == "test" and password == "test":
            st.session_state.logged_in = True
            st.success("Logged in successfully!")
            sleep(0.5)
            st.switch_page("pages/page1.py")
        else:
            st.error("Incorrect username or password")
with col3:
    if st.button("New User", type="secondary"):
        st.session_state.logged_in = True
        st.success("Welcome to Amigo!")
        sleep(0.5)
        st.switch_page("pages/signin.py")
        