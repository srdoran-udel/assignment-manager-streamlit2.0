import streamlit as st
import json
import time
import uuid 
from pathlib import Path

#data layer 
def load_data(json_path):
    if json_path.exists():
        with json_path.open("r") as f:
            assignments = json.load(f)
    else:
        assignments = []

    return assignments
def save_data(assignments, json_path):
    with json_path.open("w") as f:
        json.dump(assignments, f)


#service layer

def add_new_assignment(assignments):
     assignments.append({"id": str(uuid.uuid4()),
                                "title": st.session_state['draft']['title'],
                                "description": st.session_state['draft']['description'],
                                "points": st.session_state['draft']['points'],
                                "type": st.session_state['draft']['assignment_type']})
     return assignments

def edit_assignment(assignments: list) -> list:
    for assignment in assignments:
        if assignment["id"] == st.session_state["draft"]["id"]:
            assignments['title'] = st.session_state["draft"]['title']
            assignments['description'] = st.session_state["draft"]['description']
            assignments['points'] = st.session_state["draft"]['points']
            assignments['type'] = st.session_state["draft"]['assignment_type']
            break
    return assignments

# UI layer 

def render_dashboard(assignments, json_path):
    col1, col2 = st.columns([3, 1])
    with col1:
        st.markdown("## Add New Assignment")
    with col2:
        if st.button("Back", key="back_btn", use_container_width=False):
            st.session_state["page"] = "Assignments Dashboard" 
            st.rerun()
    with st.container(border=True):
        for assignment in assignments:
            with st.container(border = True):
                st.markdown(f"**Title:** {assignment['title']}")
                st.markdown(f"**Description:** {assignment['description']}")
                if st.button("Edit", key=f"edit_btn_{assignment['id']}", type="primary",use_container_width=True):
                    st.session_state["page"] = "Edit Assignment"
                    st.session_state["draft"] = assignment

                    st.rerun()

def render_add_new_assignment(assignments, json_path):
    col1, col2 = st.columns([3, 1])
    with col1:
        if st.session_state["page"] == "Add New Assignment":
            st.subheader("Add New Assignment")
        elif st.session_state["page"] == "Edit Assignment":
            st.subheader("Edit Assignment")
    with col2:
        if st.button("Back", key="back_btn", type="secondary"):
            st.session_state["page"] = "Assignments Dashboard" 
            st.rerun()
    # Form Inputs
        st.session_state['draft']['title'] = st.text_input("Title", key="title_txt_input", value=st.session_state['draft']['title'])
        st.session_state['draft']['description'] = st.text_area("Description", key="description_txt_area", value=st.session_state['draft']['description'], placeholder="normalization is covered here",
                                help="Here you are entering the assignment details")
        st.session_state['draft']['points'] = st.number_input("Points", key="points_num_input", value=st.session_state["draft"]['points'])

        st.session_state['draft']['assignment_type'] = st.selectbox("Type", ["Select an option", "Homework", "Lab", "other"])
        if st.session_state['draft']['assignment_type'] == "other":
            st.session_state['draft']['assignment_type'] = st.text_input("Type", placeholder="Enter the assignment Type")

    
    # Save Action
    if st.button("Save", use_container_width=True, key="save_btn", type="primary"):
        with st.spinner("Assignment is being recorded..."):
            time.sleep(3)

        #add new assigbment 
        if st.session_state["page"] == "Add New Assignment":
            assignments = add_new_assignment(assignments)

        elif st.session_state["page"] == "Edit Assignment":
            assignments = edit_assignment(assignments)

        #record data into json file
        save_data(assignments, json_path)
        st.success("New Assignment is recorded!")
        time.sleep(3)
        st.session_state["draft"] = {}
        st.session_state["page"] = "Assignments Dashboard"
        st.rerun()  
        

def main():
    st.set_page_config(page_title="Assignment Management", page_icon=":mortar_board:", layout="collapsed", initial_sidebar_state="collapsed")
    st.title("Assignment Management Application")
    #loading the daav 
    assignments = []
    json_path = Path("assignments.json")
    assignments = load_data(json_path)

    #3 session srate initialization 
    if "page" not in st.session_state:
        st.session_state["page"] = "Assignments Dashboard"

    if "draft" not in st.session_state:
        st.session_state["draft"] = {}
    
    if st.session_state["page"] == "Assignments Dashboard":
        render_dashboard(assignments=assignments)
    elif st.session_state["page"] == "Add New Assignment":
        render_add_new_assignment(assignments=assignments, json_path=json_path)
    elif st.session_state["page"] == "Edit Assignment":
        render_add_new_assignment(assignments=assignments, json_path=json_path)
        st.rerun()
        pass

    if __name__ == "__main__":
        main()