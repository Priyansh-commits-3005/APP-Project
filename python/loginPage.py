import streamlit as st
import pandas as pd
import backend as bck
import subprocess

subprocess.run(["python", "backend.py"])

st.set_page_config(
     page_title="Login Page",
     initial_sidebar_state="collapsed",
     layout="centered"
)

if 'login_state' not in st.session_state:
   st.session_state.login_state = False

    # If user is not logged in, show login page
if not st.session_state.login_state:
        st.header(":red[Faculty] Advisor Assistant")


        # User input for login
        username = st.text_input("Username:")
        password = st.text_input("Password:", type="password")

        # Login button
        if st.button("Login"):
            result = bck.checkUser(username, password)
            if result:
                st.session_state.login_state = True
                st.success("Login successful! Use the SIDEBAR to navigate to the required pages" )
            else:
                st.error("Invalid username or password")

        # Registration section
        st.subheader("Register")
        new_username = st.text_input("New Username:")
        new_password = st.text_input("New Password:", type="password")

        # Register button
        if st.button("Register"):
            bck.insertUser(new_username, new_password)
            st.success("Registration successful!")
else:
        # User is logged in, show other pages
        st.subheader("Welcome to the ")
        st.header(":red[Faculty] Advisor Assistant")
        st.subheader("Manage :red[ODs], :red[MLs] or your :red[personal tasks] ")
        st.subheader("USE THE SIDEBAR TO NAVIGATE")
        st.sidebar.success("Choose between the given options")
