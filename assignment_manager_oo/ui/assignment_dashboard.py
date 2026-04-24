import streamlit as st

from assignment_manager_oo.services.assignment_manager import AssignmentManager




class AssignmentDashboard:
    def __init__(self, manager: AssignmentManager) -> None:
        self.manager = manager
        self.store = self.store

    def main(self):
        if st.session_state["page"] == "dashboard":
            self.show_manage_assignments()
        else:
            self.show_add_new_assignment()
        pass
    def show_manage_assignments(self):
        pass

    def show_add_new_assignment(self):
        pass