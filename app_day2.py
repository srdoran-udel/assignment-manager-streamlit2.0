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

