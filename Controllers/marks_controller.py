import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from Models.mark import Mark

class MarksController:
    """Controller to handle marks operations"""

    @staticmethod
    def add_mark(student_id, subject_id, marks_obtained, exam_date):
        """Adds a new mark entry for a student"""
        try:
            Mark.add_mark(student_id, subject_id, marks_obtained, exam_date)
            return "Marks added successfully!"
        except Exception as e:
            return f"Error adding marks: {e}"

    @staticmethod
    def get_marks_by_student(student_id):
        """Retrieves all marks for a specific student"""
        try:
            marks = Mark.get_marks_by_student(student_id)
            if marks:
                return marks
            return "No marks found for this student."
        except Exception as e:
            return f"Error retrieving marks: {e}"

    @staticmethod
    def get_marks_by_id(mark_id):
        """Retrieves a specific mark entry by ID"""
        try:
            mark = Mark.get_marks_by_id(mark_id)
            if mark:
                return mark
            return "Mark entry not found."
        except Exception as e:
            return f"Error retrieving mark entry: {e}"

    @staticmethod
    def update_marks(mark_id, marks_obtained, exam_date):
        """Updates an existing mark entry"""
        try:
            Mark.update_marks(mark_id, marks_obtained, exam_date)
            return "Marks updated successfully!"
        except Exception as e:
            return f"Error updating marks: {e}"

    @staticmethod
    def delete_marks(mark_id):
        """Deletes a specific mark entry"""
        try:
            Mark.delete_marks(mark_id)
            return "Marks deleted successfully!"
        except Exception as e:
            return f"Error deleting marks: {e}"
