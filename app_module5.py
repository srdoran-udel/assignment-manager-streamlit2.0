import streamlit as st
import json
import time
import uuid 
from pathlib import Path

st.set_page_config(page_title="Course Management", layout="centered", initial_sidebar_state="collapsed")

st.title("Course Management")
st.divider()

assignments = [{"id":"HW1",
                "title":"Intro to Database",
                "description":"basics of database design",
                "points":100,
                "type":"homework"}
                ,
                {"ID":"HW2",
                "title":"Normalization",
                "description":"normalizing",
                "points":100,
                "type":"homework"}]


json_path = Path("assignments.json")

if json_path.exists():
    with json_path.open("r") as f:
        assignments = json.load(f)
        

#session state intialization 
if "page" not in st.session_state:
    st.session_state["page"] = "Assignment Dashboard"

if "draft" not in st.session_state:
    st.session_state["draft"] = {}

if st.session_state["page"] == "Assignment Dashboard":
    col1, col2 = st.columns([3,1])
    with col1:
        st.subheader("Assignments")
    with col2: 
        if st.button("Add New Assignment", key = "add_new_assignment_btn", type="primary", use_container_width=True):
            st.session_state["page"] = "Add New Assignment"
            st.rerun()

    with st.container(border = True):
        st.dataframe(assignments)


elif st.session_state["page"] == "Add New Assignment":
    col1, col2 = st.columns([3,1])
    with col1:
        st.subheader("Add New Assignment")
    with col2:
        if st.button("Back", key = "back_btn", type = "secondary", use_container_width=True):
            st.session_state["page"] = "Assignment Dashboard"
            st.rerun()

    st.session_state['draft']['title'] = st.text_input("Title")
    st.session_state['draft']['description'] = st.text_area("Description", placeholder="normalization is covered here",
                            help="Here you are entering the assignment details")
    st.session_state["draft"]['points'] = st.number_input("Points", key = "points_input")
    st.session_state["draft"]['assignment_type'] = st.selectbox("Type", ["Select an Option", "Homework", "Lab", "Other"], key = "type_selector")
    if st.button("Save", key = "save_btn", type = "primary", use_container_width=True):
        with st.spinner("In progress..."):
            time.sleep(3)
            assignments.append({"id": str(uuid.uuid4()),
                                "title": st.session_state['draft']['title'],
                                "description": st.session_state['draft']['description'],
                                "points": st.session_state['draft']['points'],
                                "type": st.session_state['draft']['assignment_type']})
            with json_path.open("w", encoding="utf-8") as f:
                json.dump(assignments, f)
            st.success("Assignment is recorded!")
            time.sleep(3)

            st.session_state["page"] = "Assignment Dashboard"
            st.rerun()

elif st.session_state["page"] == "Edit Assignment":
    pass
