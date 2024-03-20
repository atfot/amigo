import streamlit as st
from time import sleep

language_selection=st.selectbox(
            'Language(언어)',
            ('한국어','English')
        )
if language_selection=='English': 
    col1,col2,col3=st.columns([4,2,4])
    with col2:
        st.title("Neri")
    st.title('')
    col1,col2=st.columns([5.5,4.5])
    with col2:
        st.write("Please login (username `test`, password `test`).")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    col1, col2 = st.columns([8.5,1.5])
    with col1:
        if st.button("New User", type="secondary"):
            st.session_state.signin = True
            st.success("Welcome to Neri!")
            sleep(0.5)
            st.switch_page("pages/signin.py")
    with col2:
        if st.button("Log in", type="primary"):
            if username == "test" and password == "test":
                st.session_state.logged_in = True
                st.success("Logged in successfully!")
                sleep(0.5)
                st.switch_page("pages/page1.py")
            else:
                st.error("Incorrect username or password")
    if 'logged_in' in st.session_state:
        col, col2, col3 = st.columns([3,4,3])
        with col2:
            st.success("Logged in successfully!")
            sleep(0.5)
            st.switch_page("pages/page1.py")
    if 'logged_in' not in st.session_state:
        pass
    if 'signin' in st.session_state:
        col, col2, col3 = st.columns([3,4,3])
        with col2:
            st.success("Welcome to Neri!")
            sleep(0.5)
            st.switch_page("pages/signin.py")
    if 'signin' not in st.session_state:
        pass

if language_selection=='한국어': 
    col1,col2,col3=st.columns([4,2,4])
    with col2:
        st.title("네리")
    st.title('')
    col1,col2=st.columns([5.5,4.5])
    with col2:
        st.write("로그인해주세요 (유저이름 `test`, 패스워드 `test`).")
    username = st.text_input("유저 이름")
    password = st.text_input("비밀번호", type="password")

    col1, col2 = st.columns([8.7,1.3])
    with col1:
        if st.button("새로 오신 분", type="secondary"):
            st.session_state.signin = True
            st.success("성공적으로 로그인 되었습니다!")
            sleep(0.5)
            st.switch_page("pages/signin.py")
    with col2:
        if st.button("로그인", type="primary"):
            if username == "test" and password == "test":
                st.session_state.logged_in = True
                st.success("성공적으로 로그인 되었습니다!")
                sleep(0.5)
                st.switch_page("pages/page1.py")
            else:
                st.error("유저 이름 또는 패스워드가 맞지 않습니다.")
    if 'logged_in' in st.session_state:
        col, col2, col3 = st.columns([3,4,3])
        with col2:
            st.success("성공적으로 로그인 되었습니다!")
            sleep(0.5)
            st.switch_page("pages/page1.py")
    if 'logged_in' not in st.session_state:
        pass
    if 'signin' in st.session_state:
        col, col2, col3 = st.columns([3,4,3])
        with col2:
            st.success("네리에 오신 것을 환영합니다!")
            sleep(0.5)
            st.switch_page("pages/signin.py")
    if 'signin' not in st.session_state:
        pass