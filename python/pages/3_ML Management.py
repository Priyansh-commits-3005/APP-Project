import streamlit as st
import pandas as pd
import backend as bck

choice = st.sidebar.selectbox("select the option",["Add Student","Manage Student"])


if choice  == "Add Student":
    st.header(":red[Faculty] Advisor Assistant")
    with st.form("add student info"):
        student_id = st.text_input("enter the student roll number")
        student_name = st.text_input('Enter the name of the new student')
        od = st.text_input("enter the ml type/name")
        submitted = st.form_submit_button("complete submission")
    if submitted:
        bck.add_ml(student_id,student_name,od)
        val = bck.printML()
        st.table(val)
if choice  == "Manage Student":
    st.header(":red[Faculty] Advisor Assistant")
    val = bck.printML()
    st.table(val)
    id = st.text_input("input the register number whose stage is needed to be incremented")
    st.button("increment od stage",on_click=bck.increase_ml_stage(id))

    

    
    

        
           
           
    
        

    