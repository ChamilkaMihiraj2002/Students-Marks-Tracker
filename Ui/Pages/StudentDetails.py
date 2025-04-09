from Pages.BasePage import BasePage
import customtkinter as ctk

class StudentDetails(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        
        # Header section
        header = ctk.CTkFrame(self.content, fg_color="transparent", height=100)
        header.pack(fill="x", padx=40, pady=(40, 20))
        
        page_title = ctk.CTkLabel(
            header,
            text="Student Details",
            font=ctk.CTkFont(family="Arial", size=24, weight="bold"),
            text_color="#333333"
        )
        page_title.pack(anchor="w")
        
        # Main content
        main_frame = ctk.CTkFrame(self.content, fg_color="transparent")
        main_frame.pack(fill="both", expand=True, padx=40, pady=20)
        
        # Create student management section
        self.create_student_management_section(main_frame)
    
    def create_student_management_section(self, parent):
        """Create a sample student management section"""
        # Top controls
        controls_frame = ctk.CTkFrame(parent, fg_color="transparent")
        controls_frame.pack(fill="x", pady=(0, 20))
        
        # Search bar
        search_frame = ctk.CTkFrame(controls_frame, fg_color="transparent")
        search_frame.pack(side="left")
        
        search_entry = ctk.CTkEntry(
            search_frame, 
            placeholder_text="Search students...",
            width=300,
            height=40,
            fg_color="white",
            corner_radius=8
        )
        search_entry.pack(side="left", padx=(0, 10))
        
        search_button = ctk.CTkButton(
            search_frame,
            text="Search",
            height=40,
            width=100,
            corner_radius=8
        )
        search_button.pack(side="left")
        
        # Add student button
        add_button = ctk.CTkButton(
            controls_frame,
            text="+ Add Student",
            height=40,
            width=140,
            corner_radius=8,
            fg_color="#4CAF50",
            hover_color="#388E3C"
        )
        add_button.pack(side="right")
        
        # Student list in a table-like format
        table_frame = ctk.CTkFrame(parent, fg_color="#d3d5db", corner_radius=10)
        table_frame.pack(fill="both", expand=True)
        
        # Table header
        header_frame = ctk.CTkFrame(table_frame, fg_color="#f0f0f0", height=50, corner_radius=0)
        header_frame.pack(fill="x", padx=1, pady=1)
        
        # Configure grid for the header
        header_frame.grid_columnconfigure(0, weight=1)  # ID
        header_frame.grid_columnconfigure(1, weight=3)  # Name
        header_frame.grid_columnconfigure(2, weight=2)  # Class
        header_frame.grid_columnconfigure(3, weight=2)  # Actions
        
        # Header labels
        headers = ["Student ID", "Full Name", "Class", "Actions"]
        for i, header_text in enumerate(headers):
            label = ctk.CTkLabel(
                header_frame,
                text=header_text,
                font=ctk.CTkFont(weight="bold"),
                text_color="#333333"
            )
            label.grid(row=0, column=i, padx=15, pady=15, sticky="w")
        
        # Sample data rows
        sample_data = [
            {"id": "S001", "name": "John Smith", "class": "Class 10A"},
            {"id": "S002", "name": "Emily Johnson", "class": "Class 11B"},
            {"id": "S003", "name": "Michael Brown", "class": "Class 9C"},
            {"id": "S004", "name": "Sophia Williams", "class": "Class 12A"},
            {"id": "S005", "name": "Robert Davis", "class": "Class 10B"},
        ]
        
        # Student rows container with scrolling
        rows_container = ctk.CTkScrollableFrame(table_frame, fg_color="transparent")
        rows_container.pack(fill="both", expand=True, padx=1, pady=1)
        
        # Configure grid for the rows container
        rows_container.grid_columnconfigure(0, weight=1)  # ID
        rows_container.grid_columnconfigure(1, weight=3)  # Name
        rows_container.grid_columnconfigure(2, weight=2)  # Class
        rows_container.grid_columnconfigure(3, weight=2)  # Actions
        
        # Add sample data rows
        for i, student in enumerate(sample_data):
            # Row background (alternating for better readability)
            row_bg = "#d3d5db" if i % 2 == 0 else "#d3d5db"
            
            # Student ID
            id_label = ctk.CTkLabel(
                rows_container,
                text=student["id"],
                text_color="#555555",
                fg_color=row_bg
            )
            id_label.grid(row=i, column=0, padx=15, pady=12, sticky="w")
            
            # Student name
            name_label = ctk.CTkLabel(
                rows_container,
                text=student["name"],
                text_color="#333333",
                fg_color=row_bg
            )
            name_label.grid(row=i, column=1, padx=15, pady=12, sticky="w")
            
            # Class
            class_label = ctk.CTkLabel(
                rows_container,
                text=student["class"],
                text_color="#555555",
                fg_color=row_bg
            )
            class_label.grid(row=i, column=2, padx=15, pady=12, sticky="w")
            
            # Actions
            actions_frame = ctk.CTkFrame(rows_container, fg_color=row_bg)
            actions_frame.grid(row=i, column=3, padx=15, pady=8, sticky="w")
            
            edit_button = ctk.CTkButton(
                actions_frame,
                text="Edit",
                fg_color="#2196F3",
                hover_color="#1976D2",
                width=70,
                height=30,
                corner_radius=6
            )
            edit_button.pack(side="left", padx=(0, 10))
            
            delete_button = ctk.CTkButton(
                actions_frame,
                text="Delete",
                fg_color="#F44336",
                hover_color="#D32F2F",
                width=70,
                height=30,
                corner_radius=6
            )
            delete_button.pack(side="left")