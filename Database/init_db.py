from db_connection import get_db_connection

def create_tables():
    queries = [
        """CREATE TABLE IF NOT EXISTS students (
            student_id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(100) NOT NULL,
            last_name VARCHAR(100) NOT NULL,
            class_id VARCHAR(10) NOT NULL,
            dob DATE NOT NULL,
            email VARCHAR(255) UNIQUE,
            phone VARCHAR(15),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )""",
        """CREATE TABLE IF NOT EXISTS subjects (
            subject_id INT AUTO_INCREMENT PRIMARY KEY,
            subject_name VARCHAR(100) NOT NULL UNIQUE
        )""",
        """CREATE TABLE IF NOT EXISTS marks (
            mark_id INT AUTO_INCREMENT PRIMARY KEY,
            student_id INT,
            subject_id INT,
            marks_obtained DECIMAL(5,2) NOT NULL,
            exam_date DATE NOT NULL,
            FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
            FOREIGN KEY (subject_id) REFERENCES subjects(subject_id) ON DELETE CASCADE
        )"""
    ]
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    for query in queries:
        cursor.execute(query)
    
    conn.commit()
    cursor.close()
    conn.close()
    print("Database tables created successfully!")

    conn = get_db_connection()
    cursor = conn.cursor()
    
    for query in queries:
        cursor.execute(query)
    
    conn.commit()
    cursor.close()
    conn.close()
    print("Sample data inserted successfully!")

if __name__ == "__main__":
    create_tables()