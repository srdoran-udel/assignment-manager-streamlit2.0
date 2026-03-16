import streamlit as st
import json
from pathlib import Path
from datetime import datetime
import uuid
import time

st.set_page_config(page_title="Course Manager", layout="centered")
st.title("Course Manager App")


#storing initial values in session state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

#where user info is stored when a user is logged in
if "user" not in st.session_state:
    st.session_state["user"] = None

if "role" not in st.session_state:
    st.session_state["role"] = None

if "page" not in st.session_state:
    st.session_state["page"] = "login"





#load data 
users = {"id": "1",
         "email": "admin@school.edu",
         "full_name": "System Admin",
         "password": "123ssag@43AE",
         "role": "Admin",
         "registered_at": "..."}



josn_path = Path("users.json")
if josn_path.exists():
    with open(josn_path, "r") as f:
        users = json.load(f)

#load data
assignments = [{"id":"HW1",
                "title":"Intro to Database",
                "description":"basics of database design",
                "points":100,
                "type":"homework"}
                ,
                {"id":"HW2",
                "title":"Normalization",
                "description":"normalizing",
                "points":100,
                "type":"homework"}]

json_path_assignments = Path("assignments.json")




if st.session_state["role"] == "Instructor":
    if st.session_state["page"] == "home":
            st.markdown("Welcome, Instructor! This is the Instructor Dashboard.")
            if st.button("Go to Dashboard", key= "dashboard__view_btn", type = "primary", use_container_width=True):
                st.session_state["page"] = "dashboard"
                st.rerun()
            elif st.session_state["page"] == "dashboard":
                st.markdown("Dashboard")

            tab1, tab2, tab3 = st.tabs(["View Assignments","Add New Assignment","Update An Assignment"])

            with tab1:
                tab_option = st.radio("View/Search",["View","Search"], horizontal=True)
                if tab_option == "View":
                    st.dataframe(assignments)
                else:
                    titles = []
                    for assignment in assignments:
                        titles.append(assignment["title"])

                    selected_title = st.selectbox("Select a title",titles,key="selected_title")

                    selected_assignment = {}

                    for assignment in assignments:
                        if assignment["title"] == selected_title:
                            selected_assignment = assignment
                            break


                    st.divider()
                    selected_assignment = st.selectbox("Select Title",
                                                    options=assignments,
                                                    format_func=lambda x: f"{x['title']} - {x['type']}")


                    if selected_assignment:
                        with st.expander("Assignment Details",expanded=True):
                            st.markdown(f"### Title: {selected_assignment['title']}")
                            st.markdown(f"Description: {selected_assignment['description']}")
                            st.markdown(f"Type: **{selected_assignment['type']}**")
                            



            with tab2:
                st.markdown("## Add New Assignment")
                #st.markdown("### Add New Assignment")

                title = st.text_input("Title")
                description = st.text_area("Description",placeholder="Normalization is covered here",help="Here you are entering the assignment details")
                points = st.number_input("Points")

                #assignment_type = st.text_input("Assignment Type")
                assignment_type = st.radio("Type", ["Homework","Lab"],horizontal=True)
                st.caption ("Homework Type")
                assignment_type2 = st.selectbox("Type", ["Select an option","Homeork","Lab","Other"])

                if assignment_type2 == "other":
                    assignment_type2 = st.text_input("Type", placeholder="Enter the assignment type")

                due_date = st.date_input("Due_Date")

                #button when changing between pages, next page action 
                btn_save = st.button("Save", width="stretch",disabled=False)


                #validation check, if title is empty, show warning, else save the data
                if btn_save:
                    if not title:
                        st.warning("Title needs to be provided!")
                    else:
                        with st.spinner("Assignment is being recorded..."):
                            time.sleep(5)

                            #next_assignment_id = "HW" + str(next_assignment_id_number)
                            #next_assignment_id_number += 1

                            assignments.append({"id":next_assignment_id,
                                    "title":title,
                                    "description":description,
                                    "points":points,
                                    "type":assignment_type})

                #record data into json file
                            with json_path_assignments.open("w",encoding="utf-8") as f:
                                json.dump(assignments,f,indent=4)

                            st.success("New Assignment is recorded!")
                            st.info("This is a new assignment")
                            time.sleep(4)
                            #st.dataframe(assignments)
                            st.rerun()
                            



            with tab3:
                st.markdown("## Update An Assignment")
                titles = []
                for assignment in assignments:
                    titles.append(assignment["title"])

                selected_title = st.selectbox("Select a title", titles, key="selected_title_edit1")

                assignment_edit = {}
                for assignment in assignments:
                    if assignment["title"]== selected_title:
                        assignment_edit = assignment
                        break

            #static key example: st.text_input("Title", key="edit_title", value=assignment_edit["title"])
                if assignment_edit:
                    edit_title = st.text_input("Title", key=f"edit_title_{assignment_edit['id']}", value=assignment_edit['title'])
                    edit_description = st.text_area("Description", key=f"edit_description_{assignment_edit['id']}", value=assignment_edit['description'])

                    type_options = ["Homework","Lab"]
                    selected_index = type_options.index(assignment_edit["type"].capitalize()) if assignment_edit["type"].capitalize() in type_options else 0

                    edit_type = st.radio("Type", type_options, 
                                        key=f"edit_type_{assignment_edit['id']}",
                                        index = selected_index)

                btn_update = st.button("Update", key=f"update_button_{assignment_edit['id']}", type="secondary",use_container_width=True)
                if btn_update:
                    with st.spinner("Updating..."):
                        time.sleep(5)
                        assignment_edit["title"] = edit_title
                        assignment_edit["description"] = edit_description
                
                        with json_path.open("w", encoding="utf-8") as f:
                            json.dump(assignments,f)

                        st.success("Assignment is updated!")
                        time.sleep(5)
                        st.rerun()



elif st.session_state["role"] == "Admin":
    st.markdown("Welcome, Admin! This is the Admin Dashboard.")
    if st.button("Log Out", type="primary", use_container_width=True):
        with st.spinner("Logging out..."):
            st.session_state["logged_in"] = False
            st.session_state["user"] = None
            st.session_state["role"] = None
            st.session_state["page"] = "login"

            time.sleep(2)
            st.rerun()

else:
    # --- LOGIN ---
    st.subheader("Log In")
    with st.container(border=True):
        email_input = st.text_input("Email", key="login_email")
        password_input = st.text_input("Password", type="password", key="login_password")
        
        if st.button("Log In",type ="primary", use_container_width=True):
            with st.spinner("Logging in..."):
                time.sleep(2) # Fake backend delay
                
                # Find user
                found_user = None
                for user in users:
                    if user["email"].strip().lower() == email_input.strip().lower() and user["password"] == password_input:
                        found_user = user
                        break
                
                if found_user:
                    st.success(f"Welcome back, {found_user['email']}!")
                    st.session_state["logged_in"] = True
                    st.session_state["user"] = found_user
                    st.session_state["role"] = found_user["role"]
                    st.session_state["page"] = "home"

                    time.sleep(2)
                    st.rerun()
                else:
                    st.error("Invalid credentials")

    # --- REGISTRATION ---
    st.subheader("New Instructor Account")
    with st.container(border=True):
        new_email = st.text_input("Email", key="reg_email")
        new_password = st.text_input("Password", type="password", key="reg_password")
        
        if st.button("Create Account", key="register_btn"):
            with st.spinner("Creating account..."):
                time.sleep(2) # Fake backend delay
                # ... (Assume validation logic here) ...
                users.append({
                    "id": str(uuid.uuid4()),
                    "email": new_email,
                    "password": new_password,
                    "role": "Instructor"
                })

                with open(josn_path, "w") as f:
                    json.dump(users, f)
            
                st.success("Account created!")
                st.rerun()

    st.write("---")
    st.dataframe(users)

with st.sidebar:
    st.markdown("Course Manager Sidebar")
    if st.session_state["logged_in"] == True:
        user = st.session_state["user"]
        st.markdown(f"**Logged User Email:** {user['email']}")



