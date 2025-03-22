import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from Controllers.marks_controller import MarksController
from Controllers.student_controller import StudentController
from Controllers.subject_controller import SubjectController

# === Test MarksController ===

# Step 1: Add a test student and subject
print("\n--- Adding test student and subject ---")
student_response = StudentController.add_student("Emily", "White","10-A" ,"2003-07-22", "emily.white@example.com", "5559876543")
print(student_response)

students = StudentController.get_all_students()
student_id = students[-1]["student_id"] if students else None

subject_response = SubjectController.add_subject("Mathematics")
print(subject_response)

subjects = SubjectController.get_all_subjects()
subject_id = subjects[-1]["subject_id"] if subjects else None

# Step 2: Add Marks
if student_id and subject_id:
    print("\n--- Adding marks for student ---")
    print(MarksController.add_mark(student_id, subject_id, 78, "2025-05-12"))

    # Step 3: Retrieve Marks
    marks = MarksController.get_marks_by_student(student_id)
    print("\n--- Retrieved Marks ---")
    print(marks)

    if isinstance(marks, list) and marks:
        mark_id = marks[0]["mark_id"]

        # Step 4: Update Marks
        print("\n--- Updating Marks ---")
        print(MarksController.update_marks(mark_id, 85, "2025-06-01"))

        # Retrieve Updated Marks
        print("\n--- Updated Marks ---")
        print(MarksController.get_marks_by_id(mark_id))

        # Step 5: Delete Marks
        print("\n--- Deleting Marks ---")
        print(MarksController.delete_marks(mark_id))

        # Check Marks After Deletion
        print("\n--- Marks after deletion ---")
        print(MarksController.get_marks_by_student(student_id))
else:
    print("Failed to add student or subject. Cannot proceed with marks testing.")
