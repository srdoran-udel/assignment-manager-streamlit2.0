import streamlit as st
import time 
import json 
import uuid
from pathlib import Path

#1. Project Setup 
#step 1
#always do this at the beginning of the code, to set up the page configuration
st.set_page_config(page_title="Course Manager",
                   page_icon="",
                   layout="centered",
                   initial_sidebar_state="collapsed")

#load data 
users = {"id": "1",
         "email": "admin@school.edu",
         "full_name": "System Admin",
         "password": "123ssag@43AE",
         "role": "Admin",
         "registered_at": "..."}

#step 2 Initialize a variable json_file pointing to "users.json"
json_path = Path("users.json")


#if the file exists load its content into a list variable called users
#  from a json file 
if json_path.exists():
    with json_path.open("r",encoding="utf-8") as f:
        users = json.load(f)

tab1, tab2= st.tabs(["Register","Login"])

#2. Navigation and Page Structure 
#streamlit toolbox 
with tab1:
    st.markdown("## Create an Account")
    username = st.text_input("Email", key="reg_username")
    full_name = st.text_input("Full Name", key="reg_full_name")
    password = st.text_input("Password", type="password", key="reg_password")
    role = st.selectbox("Role", ["Admin","Instructor","Student"])
    
    btn_register = st.button("Register", use_container_width=True)

    if btn_register:
        with st.spinner("Creating your account..."):
            time.sleep(5)
            new_user_id = str(uuid.uuid4())
            users.append({"id":new_user_id,
                          "email":username,
                          "full_name":full_name,
                          "password":password,
                          "role":role,
                          "registered_at":"..."})

            with json_path.open("w", encoding="utf-8") as f:
                json.dump(users,f,indent=4)

            st.success("Your account is created!")
            time.sleep(5)
            st.rerun()
with tab2:
    st.markdown("## Login to Your Account")
    username_login = st.text_input("Username", key="username_login")
    password_login = st.text_input("Password", type="password", key="password_login")

    btn_login = st.button("Login", use_container_width=True)

    if btn_login:
        with st.spinner("Logging you in..."):
            time.sleep(5)
            user_found = False
            for user in users:
                if user["email"] == username_login and user["password"] == password_login:
                    user_found = True
                    st.success(f"Welcome back, {user['full_name']}!")
                    break
            if not user_found:
                st.error("Invalid username or password. Please try again.")
