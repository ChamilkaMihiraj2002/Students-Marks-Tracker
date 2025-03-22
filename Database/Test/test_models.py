import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from Database.models import Student, Subject, Mark

# ==== Testing Student Model ====
print("\n--- Testing Student Model ---")

# Add Student
Student.add_student("Alice", "Brown", "10-C", "2002-09-05", "alic.brown@example.com", "1231231234")
students = Student.get_all_students()
print("All Students:", students)

# Get Student by ID
student_id = students[0]["student_id"]
print("Student by ID:", Student.get_student_by_id(student_id))

# Update Student
Student.update_student(student_id, "Alice", "Green",  "10-C", "2002-09-05", "ale.green@example.com", "9876543210")
print("Updated Student:", Student.get_student_by_id(student_id))

# Delete Student
Student.delete_student(student_id)
print("Students after deletion:", Student.get_all_students())


# ==== Testing Subject Model ====
print("\n--- Testing Subject Model ---")

# Add Subject
Subject.add_subject("Biology")
subjects = Subject.get_all_subjects()
print("All Subjects:", subjects)

# Get Subject by ID
subject_id = subjects[0]["subject_id"]
print("Subject by ID:", Subject.get_subject_by_id(subject_id))

# Update Subject
Subject.update_subject(subject_id, "Advanced Biology")
print("Updated Subject:", Subject.get_subject_by_id(subject_id))

# Delete Subject
Subject.delete_subject(subject_id)
print("Subjects after deletion:", Subject.get_all_subjects())


# ==== Testing Marks Model ====
print("\n--- Testing Marks Model ---")

# Add Marks
Student.add_student("Bob", "Smith", "10-B", "2003-10-15", "bob.smith@example.com", "1122334455")
students = Student.get_all_students()
subject_id = Subject.add_subject("Physics")
subjects = Subject.get_all_subjects()
Mark.add_mark(students[0]["student_id"], subjects[0]["subject_id"], 85, "2025-04-20")

# Get Marks by ID
marks = Mark.get_marks_by_student(students[0]["student_id"])
mark_id = marks[0]["mark_id"]
print("Marks by ID:", Mark.get_marks_by_student(students[0]["student_id"]))

# Update Marks
Mark.update_marks(mark_id, 90, "2025-05-10")
print("Updated Marks:", Mark.get_marks_by_student(students[0]["student_id"]))

# Delete Marks
Mark.delete_marks(mark_id)
print("Marks after deletion:", Mark.get_marks_by_student(students[0]["student_id"]))