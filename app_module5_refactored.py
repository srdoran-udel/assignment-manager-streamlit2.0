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

def add_new_assignment(assignments, title, description, points, type):
     assignments.append({"id": str(uuid.uuid4()),
                                "title": title,
                                "description": description,
                                "points": points,
                                "type": type})
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

    # Form Inputs
    st.session_state['draft']['title'] = st.text_input("Title")
    st.session_state['draft']['description'] = st.text_area("Description", placeholder="normalization is covered here",
                            help="Here you are entering the assignment details")
    st.session_state["draft"]['points'] = st.number_input("Points")

    st.session_state['draft']['assignment_type'] = st.selectbox("Type", ["Select an option", "Homework", "Lab", "other"])
    if st.session_state["draft"]['assignment_type'] == "other":
        st.session_state["draft"]['assignment_type'] = st.text_input("Type", placeholder="Enter the assignment Type")

    # Live Preview
    with st.container(border=True):
        with st.expander("Assignment Details", expanded=True):
            # Using .get() for safe dictionary access on initial load
            st.markdown(f"### Title: {st.session_state['draft'].get('title', '')}")
            st.markdown(f"**Description**: {st.session_state['draft'].get('description', '')}")
            st.markdown(f"Type: **{st.session_state['draft'].get('assignment_type', '')}**")
    
    # Save Action
    btn_save = st.button("Save", use_container_width=True, key="save_btn", type="primary")

    if btn_save:
        if not st.session_state['draft'].get('title'):
            st.warning("Title needs to be provided!")
        else:
            with st.spinner("Assignment is being recorded...."):
                time.sleep(2)
                
                # Append to list
                assignments.append(
                    {
                        "id": str(uuid.uuid4()),
                        "title": st.session_state['draft']['title'],
                        "description": st.session_state['draft']['description'],
                        "points": st.session_state['draft']['points'],
                        "type": st.session_state['draft']['assignment_type']
                    }
                )

                # Record directly into JSON file 
                with open(json_path, "w", encoding="utf-8") as f:
                    json.dump(assignments, f, indent=4)

                st.success("New Assignment is recorded!")
                st.info("This is a new assignment")
                
                time.sleep(2)
                st.session_state["page"] = "Assignments Dashboard"
                st.session_state["draft"] = {}
                st.rerun()
def render_add_new_assignment(assignments, json_path):
    pass

def main():
    st.set_page_config(page_title="Assignment Management", page_icon=":mortar_board:", layout="collapsed")
    st.title("Assignment Management Application")
    #loading the daav 
    assignments = []

    json_path = Path("assignments.json")
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
        st.rerun()
        pass

    if __name__ == "__main__":
        main()