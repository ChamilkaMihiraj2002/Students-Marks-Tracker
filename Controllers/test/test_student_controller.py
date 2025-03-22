import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from Controllers.student_controller import StudentController

# === Test StudentController ===

# Add Student
print(StudentController.add_student("John", "Doe","11-C", "2001-06-15", "john.doe@example.com", "5551234567"))

# Get All Students
students = StudentController.get_all_students()
print("All Students:", students)

# Get Student by ID
if isinstance(students, list) and students:
    student_id = students[0]["student_id"]
    print("Student by ID:", StudentController.get_student_by_id(student_id))

    # Update Student
    print(StudentController.update_student(student_id, "John", "Smith", "11-C", "2001-06-15", "john.smith@example.com", "5559998888"))
    
    # Get Updated Student
    print("Updated Student:", StudentController.get_student_by_id(student_id))
    
    # Delete Student
    print(StudentController.delete_student(student_id))

    # Get Students after deletion
    print("Students after deletion:", StudentController.get_all_students())
