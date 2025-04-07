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
    
    @staticmethod
    def get_students_with_avg_marks():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT 
                s.student_id,
                CONCAT(s.first_name, ' ', s.last_name) AS student_name,
                ROUND(AVG(m.marks_obtained), 2) AS average_marks
            FROM students s
            JOIN marks m ON s.student_id = m.student_id
            GROUP BY s.student_id
        """
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return data
    
    @staticmethod
    def get_top_students(limit=5):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT 
                s.student_id,
                CONCAT(s.first_name, ' ', s.last_name) AS student_name,
                ROUND(AVG(m.marks_obtained), 2) AS average_marks
            FROM students s
            JOIN marks m ON s.student_id = m.student_id
            GROUP BY s.student_id
            ORDER BY average_marks DESC
            LIMIT %s
        """
        cursor.execute(query, (limit,))
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return data
    
    @staticmethod
    def get_students_without_marks():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT 
                s.student_id,
                CONCAT(s.first_name, ' ', s.last_name) AS student_name
            FROM students s
            LEFT JOIN marks m ON s.student_id = m.student_id
            WHERE m.marks_obtained IS NULL
        """
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return data

    @staticmethod
    def get_students_total_marks():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        query = """
            SELECT 
                s.student_id,
                CONCAT(s.first_name, ' ', s.last_name) AS student_name,
                SUM(m.marks_obtained) AS total_marks
            FROM students s
            JOIN marks m ON s.student_id = m.student_id
            GROUP BY s.student_id
        """
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        
        return data