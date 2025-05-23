import streamlit as st
import pandas as pd
from datetime import datetime
from tasks import load_tasks, save_tasks, filter_tasks_by_priority, filter_tasks_by_category
import subprocess

def main():
    st.title("To-Do Application")
    
    # Load existing tasks
    tasks = load_tasks()
    
    # Sidebar for adding new tasks
    st.sidebar.header("Add New Task")
    
    # Task creation form
    with st.sidebar.form("new_task_form"):
        task_title = st.text_input("Task Title")
        task_description = st.text_area("Description")
        task_priority = st.selectbox("Priority", ["Low", "Medium", "High"])
        task_category = st.selectbox("Category", ["Work", "Personal", "School", "Other"])
        task_due_date = st.date_input("Due Date")
        submit_button = st.form_submit_button("Add Task")
        
        if submit_button and task_title:
            new_task = {
                "id": len(tasks) + 1,
                "title": task_title,
                "description": task_description,
                "priority": task_priority,
                "category": task_category,
                "due_date": task_due_date.strftime("%Y-%m-%d"),
                "completed": False,
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            tasks.append(new_task)
            save_tasks(tasks)
            st.sidebar.success("Task added successfully!")
    
    # Main area to display tasks
    st.header("Your Tasks")
    
    # Filter options
    col1, col2 = st.columns(2)
    with col1:
        filter_category = st.selectbox("Filter by Category", ["All"] + list(set([task["category"] for task in tasks])))
    with col2:
        filter_priority = st.selectbox("Filter by Priority", ["All", "High", "Medium", "Low"])
    
    show_completed = st.checkbox("Show Completed Tasks")
    
    # Apply filters
    filtered_tasks = tasks.copy()
    if filter_category != "All":
        filtered_tasks = filter_tasks_by_category(filtered_tasks, filter_category)
    if filter_priority != "All":
        filtered_tasks = filter_tasks_by_priority(filtered_tasks, filter_priority)
    if not show_completed:
        filtered_tasks = [task for task in filtered_tasks if not task["completed"]]
    
    # Display tasks
    for task in filtered_tasks:
        col1, col2 = st.columns([4, 1])
        with col1:
            if task["completed"]:
                st.markdown(f"~~**{task['title']}**~~")
            else:
                st.markdown(f"**{task['title']}**")
            st.write(task["description"])
            st.caption(f"Due: {task['due_date']} | Priority: {task['priority']} | Category: {task['category']}")
        with col2:
            if st.button("Complete" if not task["completed"] else "Undo", key=f"complete_{task['id']}"):
                for t in tasks:
                    if t["id"] == task["id"]:
                        t["completed"] = not t["completed"]
                        save_tasks(tasks)
                        st.rerun()
            if st.button("Delete", key=f"delete_{task['id']}"):
                tasks = [t for t in tasks if t["id"] != task["id"]]
                save_tasks(tasks)
                st.rerun()

    st.title("Run Unit Tests")

    if st.button("Run Unit Tests"):
        st.write("Running unit tests...")
        result = subprocess.run(["pytest", "tests/test_basic.py"], capture_output=True, text=True)

        st.text(result.stdout)

    # Title for the Streamlit app
    st.title("Pytest Features with Streamlit")

    # Run Tests with Code Coverage
    if st.button("Run Tests with Code Coverage"):
        st.write("Running tests with code coverage...")
        result = subprocess.run(["pytest", "--cov=src", "--cov-report=html", "tests"], capture_output=True, text=True)
        st.text(result.stdout)
        if result.returncode == 0:
            st.success("Tests passed with coverage.")
        else:
            st.error("Tests failed. Check output for details.")

    # Run Parameterized Tests
    if st.button("Run Parameterized Tests"):
        st.write("Running parameterized tests...")
        result = subprocess.run(["pytest", "tests/test_advanced.py"], capture_output=True, text=True)
        st.text(result.stdout)

    # Run Tests with Mocking
    if st.button("Run Mocking Tests"):
        st.write("Running tests with mocking...")
        result = subprocess.run(["pytest", "tests/test_advanced.py"], capture_output=True, text=True)
        st.text(result.stdout)

    # Run Tests and Generate HTML Report
    if st.button("Run Tests and Generate HTML Report"):
        st.write("Running tests and generating HTML report...")
        result = subprocess.run(["pytest", "--html=report.html", "tests"], capture_output=True, text=True)
        st.text(result.stdout)
        if result.returncode == 0:
            st.success("Tests passed. Check the HTML report.")
        else:
            st.error("Tests failed. Check output for details.")

    st.title("Behavior-Driven Development (BDD) Tests")

    # BDD tests
    if st.button("Run BDD Tests"):
        st.write("Running BDD tests...")
        result = subprocess.run(["pytest", "tests/test_bdd.py"], capture_output=True, text=True)
        st.text(result.stdout)
        if result.returncode == 0:
            st.success("BDD tests passed.")
        else:
            st.error("BDD tests failed. Check output for details.")

    # Hypothesis
    st.title("Hypothesis Tests Runner")

    if st.button("Run Hypothesis Tests"):
        result = subprocess.run(["pytest", "tests/test_property.py", "--maxfail=1", "--disable-warnings", "-q"], capture_output=True, text=True)
        st.text(result.stdout)
        st.text(result.stderr)   
                     
if __name__ == "__main__":
    main()