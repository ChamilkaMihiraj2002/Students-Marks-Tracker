import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from Controllers.student_controller import StudentController

if __name__ == "__main__":
    StudentController.show_all_averages()
    print()
    StudentController.show_top_students(limit=3)
    print()
    StudentController.show_students_without_marks()
