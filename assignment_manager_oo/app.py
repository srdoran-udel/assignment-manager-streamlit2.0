import streamlit as st

from assignment_manager_oo.data.assignment_store import AssignmentStore
from assignment_manager_oo.services.assignment_manager import AssignmentManager
from assignment_manager_oo.ui.assignment_dashboard import AssignmentDashboard

from pathlib import Path

st.set_page_config("Assignment Manager")

st.title("Assignment Manager")

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = True

if "role" not in st.session_state:
    st.session_state["role"] = "instructor"

if "page" not in st.session_state:
    st.session_state["page"] = "Assignments Dashboard"

if st.session_state["logged_in"]:
    if st.session_state["role"] == "instructor":
        if st.session_state["page"] == "dashboard":
            store = AssignmentStore(Path("assignment_manager_oo/assignments.json"))
            manager = AssignmentManager(store.load())
            dashboard = AssignmentDashboard(manager, store)
            dashboard.main()

    elif st.session_state["role"] == "student":
        pass
else:
    pass
    #design/set up log in page 