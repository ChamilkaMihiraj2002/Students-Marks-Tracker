import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import streamlit as st
from Controllers.student_controller import StudentController
from Controllers.subject_controller import SubjectController
from Controllers.marks_controller import MarksController

# Configure page settings
st.set_page_config(
    page_title="Students Marks Tracker",
    layout="wide"
)

# Navigation using tabs
nav_selection = st.tabs(["Dashboard", "Students", "Subjects", "Marks", "Analysis"])

# Main content based on navigation
with nav_selection[0]:  # Dashboard
    st.title("Dashboard")
    st.write("Welcome to Students Marks Tracker")
    
with nav_selection[1]:  # Students
    st.title("Students Management")
    
    # Create tabs for different student operations
    student_tabs = st.tabs(["Add Student", "View Students", "Update Student", "Delete Student", "Statistics"])
    
    # First, modify the grade level options
    GRADE_LEVELS = [
        "9-A", "9-B", "10-A", "10-B", "11-A", "11-B", "12-A", "12-B"
    ]
    
    with student_tabs[0]:  # Add Student
        st.subheader("Add New Student")
        col1, col2 = st.columns(2)
        with col1:
            first_name = st.text_input("First Name", key="add_fname")
            class_id = st.selectbox("Grade Level", GRADE_LEVELS, key="add_class")
            email = st.text_input("Email", key="add_email")
        with col2:
            last_name = st.text_input("Last Name", key="add_lname")
            dob = st.date_input("Date of Birth", key="add_dob")
            phone = st.text_input("Phone", key="add_phone")
        
        if st.button("Add Student"):
            result = StudentController.add_student(first_name, last_name, class_id, dob, email, phone)
            st.write(result)
    
    with student_tabs[1]:  # View Students
        st.subheader("All Students")
        # Get students list automatically
        students = StudentController.get_all_students()
        if students:
            # Add a search/filter box
            search_term = st.text_input("Search by Name", key="student_search")
            
            # Filter students if search term is provided
            if search_term:
                filtered_students = [
                    student for student in students 
                    if search_term.lower() in student['first_name'].lower() 
                    or search_term.lower() in student['last_name'].lower()
                ]
                st.table(filtered_students)
            else:
                st.table(students)
            
            # Add a refresh button for manual reload
            if st.button("Refresh", key="refresh_students"):
                st.experimental_rerun()
        else:
            st.warning("No students found in the database.")
    
    with student_tabs[2]:  # Update Student
        st.subheader("Update Student")
        student_id = st.number_input("Enter Student ID", min_value=1, key="update_student_id")
        if st.button("Search", key="search_student_btn"):
            student = StudentController.get_student_by_id(student_id)
            if isinstance(student, dict):
                with st.form("update_form"):
                    col1, col2 = st.columns(2)
                    with col1:
                        u_first_name = st.text_input("First Name", value=student.get('first_name', ''), key="update_fname")
                        current_class = student.get('class_id', '9-A')
                        u_class_id = st.selectbox("Grade Level", 
                                                GRADE_LEVELS,
                                                index=GRADE_LEVELS.index(current_class) if current_class in GRADE_LEVELS else 0,
                                                key="update_class")
                        u_email = st.text_input("Email", value=student.get('email', ''), key="update_email")
                    with col2:
                        u_last_name = st.text_input("Last Name", value=student.get('last_name', ''), key="update_lname")
                        u_dob = st.date_input("Date of Birth", value=student.get('dob'), key="update_dob")
                        u_phone = st.text_input("Phone", value=student.get('phone', ''), key="update_phone")
                    
                    if st.form_submit_button("Update Student"):
                        result = StudentController.update_student(student_id, u_first_name, u_last_name, 
                                                            u_class_id, u_dob, u_email, u_phone)
                        st.write(result)
    
    with student_tabs[3]:  # Delete Student
        st.subheader("Delete Student")
        del_student_id = st.number_input("Enter Student ID to Delete", min_value=1)
        if st.button("Delete"):
            if st.warning("Are you sure you want to delete this student?"):
                result = StudentController.delete_student(del_student_id)
                st.write(result)
    
    with student_tabs[4]:  # Statistics
        st.subheader("Student Statistics")
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("Show Top 5 Students"):
                top_students = StudentController.show_top_students(5)
                st.table(top_students)
        
        with col2:
            if st.button("Show Students Without Marks"):
                no_marks = StudentController.show_students_without_marks()
                st.table(no_marks)
                
        if st.button("Show All Averages"):
            averages = StudentController.show_all_averages()
            st.table(averages)

with nav_selection[2]:  # Subjects
    st.title("Subjects Management")
    
    # Create tabs for different subject operations
    subject_tabs = st.tabs(["Add Subject", "View Subjects", "Update Subject", "Delete Subject"])
    
    with subject_tabs[0]:  # Add Subject
        st.subheader("Add New Subject")
        subject_name = st.text_input("Subject Name")
        if st.button("Add Subject"):
            result = SubjectController.add_subject(subject_name)
            st.write(result)
    
    with subject_tabs[1]:  # View Subjects
        st.subheader("All Subjects")
        if st.button("Refresh Subject List"):
            subjects = SubjectController.get_all_subjects()
            st.table(subjects)
    
    with subject_tabs[2]:  # Update Subject
        st.subheader("Update Subject")
        subject_id = st.number_input("Enter Subject ID", min_value=1)
        if st.button("Search Subject"):
            subject = SubjectController.get_subject_by_id(subject_id)
            if isinstance(subject, dict):
                with st.form("update_subject_form"):
                    u_subject_name = st.text_input("Subject Name", value=subject.get('subject_name', ''))
                    if st.form_submit_button("Update Subject"):
                        result = SubjectController.update_subject(subject_id, u_subject_name)
                        st.write(result)
    
    with subject_tabs[3]:  # Delete Subject
        st.subheader("Delete Subject")
        del_subject_id = st.number_input("Enter Subject ID to Delete", min_value=1)
        if st.button("Delete Subject"):
            if st.warning("Are you sure you want to delete this subject?"):
                result = SubjectController.delete_subject(del_subject_id)
                st.write(result)

with nav_selection[3]:  # Marks
    st.title("Marks Entry")
    
    marks_tabs = st.tabs(["Add Marks", "View Marks", "Update Marks", "Delete Marks"])
    
    with marks_tabs[0]:  # Add Marks
        st.subheader("Add New Marks")
        students = StudentController.get_all_students()
        subjects = SubjectController.get_all_subjects()
        
        if isinstance(students, list) and isinstance(subjects, list):
            student_dict = {f"{s['first_name']} {s['last_name']}": s['student_id'] for s in students}
            subject_dict = {s['subject_name']: s['subject_id'] for s in subjects}
            
            col1, col2 = st.columns(2)
            with col1:
                selected_student = st.selectbox("Select Student", options=list(student_dict.keys()), key="add_marks_student")
                marks = st.number_input("Enter Marks", min_value=0, max_value=100, value=0, key="add_marks_value")
            with col2:
                selected_subject = st.selectbox("Select Subject", options=list(subject_dict.keys()), key="add_marks_subject")
                exam_date = st.date_input("Exam Date", key="add_marks_date")
            
            if st.button("Submit Marks", key="submit_marks_btn"):
                student_id = student_dict[selected_student]
                subject_id = subject_dict[selected_subject]
                result = MarksController.add_mark(student_id, subject_id, marks, exam_date)
                st.write(result)
    
    with marks_tabs[1]:  # View Marks
        st.subheader("View Student Marks")
        view_student_id = st.number_input("Enter Student ID", 
                                        min_value=1,
                                        key="view_marks_student_id")
        if st.button("View Marks", key="view_marks_btn"):
            marks = MarksController.get_marks_by_student(view_student_id)
            st.table(marks)
    
    with marks_tabs[2]:  # Update Marks
        st.subheader("Update Marks")
        update_student_id = st.number_input("Enter Student ID", 
                                          min_value=1,
                                          key="update_marks_student_id")
        update_subject_id = st.number_input("Enter Subject ID", 
                                          min_value=1,
                                          key="update_marks_subject_id")
        if st.button("Search Marks", key="search_marks_btn"):
            mark = MarksController.get_mark(update_student_id, update_subject_id)
            if isinstance(mark, dict):
                with st.form("update_marks_form"):
                    new_marks = st.number_input("New Marks", 
                                              min_value=0, 
                                              max_value=100, 
                                              value=mark.get('marks', 0),
                                              key="update_marks_value")
                    new_date = st.date_input("New Exam Date", 
                                           value=mark.get('exam_date'),
                                           key="update_marks_date")
                    if st.form_submit_button("Update Marks"):
                        result = MarksController.update_mark(update_student_id, 
                                                          update_subject_id, 
                                                          new_marks, 
                                                          new_date)
                        st.write(result)
    
    with marks_tabs[3]:  # Delete Marks
        st.subheader("Delete Marks")
        del_student_id = st.number_input("Enter Student ID", 
                                       min_value=1,
                                       key="delete_marks_student_id")
        del_subject_id = st.number_input("Enter Subject ID", 
                                       min_value=1,
                                       key="delete_marks_subject_id")
        if st.button("Delete Marks", key="delete_marks_btn"):
            if st.warning("Are you sure you want to delete these marks?"):
                result = MarksController.delete_mark(del_student_id, del_subject_id)
                st.write(result)

with nav_selection[4]:  # Analysis
    st.title("Analysis")
    st.write("View analytics and reports here")