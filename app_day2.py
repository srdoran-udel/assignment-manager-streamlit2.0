import streamlit as st

st.title("Course Management App")
st.header("Assignment Management")
st.markdown("-------------")
st.subheader("Dashboard")

st.divider()
st.markdown("")

#load data
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

#input 
#st.markdown("# Add New Assignment")
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
btn_save = st.button("Save", width="stretch")
if btn_save:
    st.warning("Working on it...")



