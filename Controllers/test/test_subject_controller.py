import sys
import os

# Add the project root directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from Controllers.subject_controller import SubjectController

# === Test SubjectController ===

# Add Subject
print("\n--- Adding Subject ---")
print(SubjectController.add_subject("Physics"))

# Get All Subjects
print("\n--- All Subjects ---")
subjects = SubjectController.get_all_subjects()
print(subjects)

# Get Subject by ID
if isinstance(subjects, list) and subjects:
    subject_id = subjects[0]["subject_id"]
    print("\n--- Get Subject by ID ---")
    print(SubjectController.get_subject_by_id(subject_id))

    # Update Subject
    print("\n--- Updating Subject ---")
    print(SubjectController.update_subject(subject_id, "Advanced Physics"))

    # Retrieve Updated Subject
    print("\n--- Updated Subject ---")
    print(SubjectController.get_subject_by_id(subject_id))

    # Delete Subject
    print("\n--- Deleting Subject ---")
    print(SubjectController.delete_subject(subject_id))

    # Get Subjects after deletion
    print("\n--- Subjects after deletion ---")
    print(SubjectController.get_all_subjects())
