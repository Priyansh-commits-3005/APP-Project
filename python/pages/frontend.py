import mysql.connector as mysql
import backend as bck
import streamlit as st
import subprocess
import pandas as pd
#--------- runnning backend file first
#--- for the stage part we can either have selectbox or two buttons which increment and decrement and the stage is showed on a slider
# subprocess.run(["python", "backend.py"])
st.title("this is a test page")
# to print the table
val = bck.printML()
df = pd.DataFrame(val)
st.table(df)
# button to incrememnt values
st.button("test")
st.button("+",on_click=bck.increase_ml_stage("RA2211051010014"))
# tasks checkbox
st.checkbox("test",value=False)
#sidebar? might be usable to navigate through pages
# add_selectbox = st.sidebar.selectbox(
#     'How would you like to be contacted?',
#     ('Email', 'Home phone', 'Mobile phone')
# )

# # Add a slider to the sidebar:
# add_slider = st.sidebar.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0)
# )
#themes are in the streamlit hamburger 
st.markdown("Main page")


