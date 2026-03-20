
import streamlit as st
import json
from pathlib import Path
from datetime import datetime
import os

st.set_page_config(page_title="Excused Absence App", layout="wide")

# Initialize Session State for Routing
if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

DATA_FILE = "data.json"

# --- HELPER FUNCTIONS ---
def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# Sidebar Navigation
st.sidebar.title("Navigation")
if st.sidebar.button("Dashboard", key="nav_dash"):
    st.session_state.page = "Dashboard"
    st.rerun()

if st.sidebar.button("Submit Request", key="nav_req"):
    st.session_state.page = "Request"
    st.rerun()

#  PAGE 1: Absence Dashboard
col1, col2 = st.columns([4,2])
with col1:
    if st.session_state.page == "Dashboard":
        st.title("Excuse Absence Dashboard")
        my_list_of_requests = load_data()

        if not my_list_of_requests:
            st.info("No requests found.")
        else:
            # Part 3 Snippet: Displaying and capturing selection
            event = st.dataframe(
                my_list_of_requests,
                on_select="rerun",
                selection_mode="single-row",
                key="dashboard_table"
            )

            if event.selection.rows:
                selected_index = event.selection.rows[0]
                selected_request = my_list_of_requests[selected_index]
                
                st.markdown("---")
                st.subheader("Selected Request Details")
                st.write(f"**Student:** {selected_request['student_email']}")
                st.write(f"**Date of Absence:** {selected_request['absence_date']}")
                st.write(f"**Reason:** {selected_request['explanation']}")
                st.write(f"**Status:** {selected_request['status']}")
#with col2:
    #count of requests by status, this isnt working didnt have time to fix it so just pounding it out 
   # if st.session_state.page == "Dashboard":
       # st.divider()
      #  st.metric("Total Requests", f"{len(my_list_of_requests)}")
      #  st.metric("Pending Requests", f"{len([r for r in my_list_of_requests if r['status'] == 'Pending'])}")
        #st.metric("Approved Requests", f"{len([r for r in my_list_of_requests if r['status'] == 'Approved'])}")
      #  st.metric("Denied Requests", f"{len([r for r in my_list_of_requests if r['status'] == 'Denied'])}") 

#  PAGE 2: Absence Request Form 
if st.session_state.page == "Request":
    st.title("Excuse Absence Request Form")
    st.info("This page is currently being developed.") # Assignment requirement

    # Using st.form to manage inputs efficiently
    with st.form("absence_form"):
        # Schema inputs
        email = st.text_input("Student Email", key="req_email")
        
        #date code snippet
        absence_date = st.date_input("Select Absence Date", key="req_date")
        
        excuse_type = st.selectbox(
            "Excuse Type", 
            ["Appointment", "Illness", "Sports","Other"], 
            key="req_type"
        )
        reason = st.text_area("Student Explanation / Reason", key="req_reason")
        
        submit = st.form_submit_button("Submit Request")

        if submit:
            if not email or not reason:
                st.error("Please fill in all fields.")
            else:
                # formatting date to string for JSON 
                date_str = absence_date.strftime("%Y-%m-%d")
                
                # Build the record based on Part 1 Schema
                new_entry = {
                    "status": "Pending",
                    "course_id": "011101",
                    "student_email": email,
                    "absence_date": date_str,
                    "submitted_timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "excuse_type": excuse_type,
                    "explanation": reason,
                    "instructor_note": ""
                }
                
                # Save data
                current_data = load_data()
                current_data.append(new_entry)
                save_data(current_data)
                
                st.success("Request submitted successfully!")
                # Refresh state
                st.session_state.page = "Dashboard"
                st.rerun()