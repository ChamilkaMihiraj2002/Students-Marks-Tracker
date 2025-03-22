import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from Database.models import Student

class StudentController:
    """Controller to handle student operations"""

    @staticmethod
    def add_student(first_name, last_name, class_id, dob, email, phone):
        """Adds a student to the database"""
        try:
            Student.add_student(first_name, last_name, class_id, dob, email, phone)
            return "Student added successfully!"
        except Exception as e:
            return f"Error adding student: {e}"

    @staticmethod
    def get_all_students():
        """Retrieves all students from the database"""
        try:
            return Student.get_all_students()
        except Exception as e:
            return f"Error retrieving students: {e}"

    @staticmethod
    def get_student_by_id(student_id):
        """Retrieves a student by ID"""
        try:
            student = Student.get_student_by_id(student_id)
            if student:
                return student
            return "Student not found."
        except Exception as e:
            return f"Error retrieving student: {e}"

    @staticmethod
    def update_student(student_id, first_name, last_name, class_id, dob, email, phone):
        """Updates a student record"""
        try:
            Student.update_student(student_id, first_name, last_name, class_id, dob, email, phone)
            return "Student updated successfully!"
        except Exception as e:
            return f"Error updating student: {e}"

    @staticmethod
    def delete_student(student_id):
        """Deletes a student record"""
        try:
            Student.delete_student(student_id)
            return "Student deleted successfully!"
        except Exception as e:
            return f"Error deleting student: {e}"
