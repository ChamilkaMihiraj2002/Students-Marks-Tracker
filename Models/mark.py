import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from Database.db_connection import get_db_connection

class Mark:
    """Class to manage student marks"""
    
    @staticmethod
    def add_mark(student_id, subject_id, marks_obtained, exam_date):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """INSERT INTO marks (student_id, subject_id, marks_obtained, exam_date) 
                   VALUES (%s, %s, %s, %s)"""
        cursor.execute(query, (student_id, subject_id, marks_obtained, exam_date))
        conn.commit()
        cursor.close()
        conn.close()
        print("Marks added successfully!")

    @staticmethod
    def get_marks_by_student(student_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
                    SELECT marks.mark_id, students.first_name, students.last_name, 
                    subjects.subject_name, marks.marks_obtained, marks.exam_date 
                    FROM marks
                    JOIN students ON marks.student_id = students.student_id
                    JOIN subjects ON marks.subject_id = subjects.subject_id
                    WHERE marks.student_id = %s
                """
        cursor.execute(query, (student_id,))
        marks = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return marks

    @staticmethod
    def get_marks_by_subject(subject_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = """SELECT students.first_name, students.last_name, subjects.subject_name, marks.marks_obtained, marks.exam_date 
                   FROM marks
                   JOIN students ON marks.student_id = students.student_id
                   JOIN subjects ON marks.subject_id = subjects.subject_id
                   WHERE marks.subject_id = %s"""
        cursor.execute(query, (subject_id,))
        marks = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return marks
    
    @staticmethod
    def update_marks(mark_id, marks_obtained, exam_date):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """UPDATE marks SET marks_obtained = %s, exam_date = %s WHERE mark_id = %s"""
        cursor.execute(query, (marks_obtained, exam_date, mark_id))
        conn.commit()
        cursor.close()
        conn.close()
        print("Marks updated successfully!")
    
    @staticmethod
    def delete_marks(mark_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """DELETE FROM marks WHERE mark_id = %s"""
        cursor.execute(query, (mark_id,))
        conn.commit()
        cursor.close()
        conn.close()
        print("Marks deleted successfully!")