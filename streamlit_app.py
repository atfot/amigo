import streamlit as st
from time import sleep

col1,col2,col3=st.columns([4,2,4])
with col2:
    st.title("Neri")
st.title('')
col1,col2=st.columns([6,4])
with col1:
    st.write("Please login (username `test`, password `test`).")
with col2:
    language_selection=st.selectbox(
        'Language(언어)',
        ('Korean','English')
    )
if language_selection=='English': 
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    col1, col2 = st.columns([8.5,1.5])
    with col1:
        if st.button("Log in", type="primary"):
            if username == "test" and password == "test":
                st.session_state.logged_in = True
                st.success("Logged in successfully!")
                sleep(0.5)
                st.switch_page("pages/page1.py")
            else:
                st.error("Incorrect username or password")
    with col2:
        if st.button("New User", type="secondary"):
            st.session_state.logged_in = True
            st.success("Welcome to Neri!")
            sleep(0.5)
            st.switch_page("pages/signin.py")

if language_selection=='Korean': 
    username = st.text_input("유저 이름")
    password = st.text_input("비밀번호", type="password")

    col1, col2 = st.columns([8.45,1.55])
    with col1:
        if st.button("로그인", type="primary"):
            if username == "test" and password == "test":
                st.session_state.logged_in = True
                st.success("성공적으로 로그인 되었습니다!")
                sleep(0.5)
                st.switch_page("pages/page1.py")
            else:
                st.error("유저 이름 또는 패스워드가 맞지 않습니다.")
    with col2:
        if st.button("새로 오신 분", type="secondary"):
            st.session_state.logged_in = True
            st.success("네리에 오신 것을 환영합니다!")
            sleep(0.5)
            st.switch_page("pages/signin.py")
            