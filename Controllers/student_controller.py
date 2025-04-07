import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from Models.student import Student

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

    @staticmethod
    def show_all_averages():
        """Retrieves all students with their average marks"""
        try:
            students = Student.get_students_with_avg_marks()
            for student in students:
                print(f"{student['student_id']}: {student['student_name']} - Avg: {student['average_marks']}")
            return students
        except Exception as e:
            return f"Error retrieving averages: {e}"
        
    @staticmethod
    def show_top_students(limit=5):
        top_students = Student.get_top_students(limit)
        print(f"Top {limit} Students:")
        for student in top_students:
            print(f"{student['student_name']} - Avg Marks: {student['average_marks']}")

    @staticmethod
    def show_students_without_marks():
        students = Student.get_students_without_marks()
        print("Students without any marks:")
        for student in students:
            print(student['student_name'])
    