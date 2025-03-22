import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from Database.db_connection import get_db_connection

class Student:
    """ Class to manage student records """
    
    @staticmethod
    def add_student( first_name, Last_name, Class_id, dob, email, phone ):
        conn = get_db_connection()
        cursor = conn.cursor()
        
        query = """INSERT INTO students (first_name, Last_name, Class_id, dob, email, phone) VALUES (%s, %s, %s, %s, %s, %s)"""
        
        cursor.execute(query, (first_name, Last_name, Class_id, dob, email, phone))
        conn.commit()
        
        cursor.close()
        conn.close()
        print("Student added successfully")
    
    @staticmethod
    def get_all_students():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = """SELECT * FROM students"""
        cursor.execute(query)
        students = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return students
    
    @staticmethod
    def get_student_by_id(student_id):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = """SELECT * FROM students WHERE student_id = %s"""
        cursor.execute(query, (student_id,))
        student = cursor.fetchone()
        cursor.close()
        conn.close()
        
        return student
    
    @staticmethod
    def update_student(student_id, first_name, Last_name, Class_id, dob, email, phone):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """UPDATE students SET first_name = %s, Last_name = %s, Class_id = %s, dob = %s, email = %s, phone = %s WHERE student_id = %s"""
        cursor.execute(query, (first_name, Last_name, Class_id, dob, email, phone, student_id))
        conn.commit()
        cursor.close()
        conn.close()
        print("Student updated successfully!")
        
    @staticmethod
    def delete_student(student_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """DELETE FROM students WHERE student_id = %s"""
        cursor.execute(query, (student_id,))
        conn.commit()
        cursor.close()
        conn.close()
        print("Student deleted successfully!")
    
    
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