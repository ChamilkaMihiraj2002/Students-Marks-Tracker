import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from Database.db_connection import get_db_connection

class Subject:
    """Class to manage subjects"""
    
    @staticmethod
    def add_subject(subject_name):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO subjects (subject_name) VALUES (%s)"
        cursor.execute(query, (subject_name,))
        conn.commit()
        cursor.close()
        conn.close()
        print("Subject added successfully!")

    @staticmethod
    def get_all_subjects():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = """SELECT * FROM subjects"""
        cursor.execute(query)
        subjects = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return subjects
    
    @staticmethod
    def get_subject_by_id(subject_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = """SELECT * FROM subjects WHERE subject_id = %s"""
        cursor.execute(query, (subject_id,))
        subject = cursor.fetchone()
        cursor.close()
        conn.close()
        
        return subject

    @staticmethod
    def update_subject(subject_id, subject_name):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """UPDATE subjects SET subject_name = %s WHERE subject_id = %s"""
        cursor.execute(query, (subject_name, subject_id))
        conn.commit()
        cursor.close()
        conn.close()
        print("Subject updated successfully!")
    
    @staticmethod
    def delete_subject(subject_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """DELETE FROM subjects WHERE subject_id = %s"""
        cursor.execute(query, (subject_id,))
        conn.commit()
        cursor.close()
        conn.close()
        print("Subject deleted successfully!")