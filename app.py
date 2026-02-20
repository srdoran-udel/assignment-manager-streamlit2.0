import streamlit as st

#step 1: header first (text elements), frontend development
st.title("Course Manager")
st.header("Course Assignments Manager")
st.subheader("Course Assignments Manager")

st.divider()
#step2 : define assignments list (data continuity), backend development
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

#step 3: add new assignment section
st.subheader("Add New Assignment")
with st.container(border=True):
    col1,col2 =st.columns([2,1])
    with col1:
        with st.container(border=True):
            st.markdown("### Assignment Details")
            title = st.text_input("Assignment title",placeholder="homework1",help="enter a short name")
            description = st.text_area("Assignment Description", placeholder="ex. details...")
        with col2:
            st.markdown("**Due Date Selection**")
            due_date = st.date_input("Due Date")

#col1,col2 =st.columns(2) this will give you 50% col1 50% col2
#col1,col2 =st.columns([2,1]) this will give you like 70% 30

col1,col2 =st.columns([2,1])

with col1:
    with st.container(border=True):
        st.markdown("### Assignment Details")
        title = st.text_input("Assignment title",placeholder="homework1",help="enter a short name")
        description = st.text_area("Assignment Description", placeholder="ex. details...")

with col2:
    st.markdown("**Due Date Selection**")
    due_date = st.date_input("Due Date")

#st.success("Streamlit works in this environment.")