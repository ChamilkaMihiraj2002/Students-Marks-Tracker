import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from Database.models import Subject

class SubjectController:
    """Controller to handle subject operations"""

    @staticmethod
    def add_subject(subject_name):
        """Adds a new subject to the database"""
        try:
            Subject.add_subject(subject_name)
            return "Subject added successfully!"
        except Exception as e:
            return f"Error adding subject: {e}"

    @staticmethod
    def get_all_subjects():
        """Retrieves all subjects from the database"""
        try:
            subjects = Subject.get_all_subjects()
            if subjects:
                return subjects
            return "No subjects found."
        except Exception as e:
            return f"Error retrieving subjects: {e}"

    @staticmethod
    def get_subject_by_id(subject_id):
        """Retrieves a specific subject by ID"""
        try:
            subject = Subject.get_subject_by_id(subject_id)
            if subject:
                return subject
            return "Subject not found."
        except Exception as e:
            return f"Error retrieving subject: {e}"

    @staticmethod
    def update_subject(subject_id, subject_name):
        """Updates a subject name"""
        try:
            Subject.update_subject(subject_id, subject_name)
            return "Subject updated successfully!"
        except Exception as e:
            return f"Error updating subject: {e}"

    @staticmethod
    def delete_subject(subject_id):
        """Deletes a subject from the database"""
        try:
            Subject.delete_subject(subject_id)
            return "Subject deleted successfully!"
        except Exception as e:
            return f"Error deleting subject: {e}"
