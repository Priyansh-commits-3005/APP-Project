import streamlit as st
import pandas as pd
import backend as bck


# Page title
st.title("To-Do List App")

# Create a list to store tasks
tasks = []

# Text input for adding tasks
task_input = st.text_input("Add a new task:")
add_button = st.button("Add Task")

# Check if the "Add Task" button is clicked
if add_button and task_input:
    bck.add_task(task_input)
    task_input = ""  # Clear the input field after adding the task
    val = bck.PrintTasks()
    st.table(val)  
# Display the tasks


# Checkbox for completing tasks
completed_tasks = st.checkbox("Show completed tasks")
if completed_tasks:
    completed = st.checkbox("Mark as completed", value=False)
    st.write("## Completed Tasks:")
    for i, task in enumerate(tasks, start=1):
        if completed:
            st.write(f"{i}. [x] {task}")
        else:
            st.write(f"{i}. [ ] {task}")

# Clear all tasks button
clear_button = st.button("Clear All Tasks")
if clear_button:
    tasks = []  # Clear the tasks list

# Save tasks to a file
with open("tasks.txt", "w") as file:
    for task in tasks:
        file.write(f"{task}\n")
