import customtkinter as ctk

class BasePage(ctk.CTkFrame):
    """Base class for all pages with consistent navigation"""
    
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="#f5f5f5")
        self.controller = controller
        
        # Configure grid to fill space
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_columnconfigure(0, weight=1)
        
        # Create a two-column layout
        self.grid_columnconfigure(1, weight=1)  # Content area takes up more space
        self.grid_columnconfigure(0, weight=0)  # Sidebar fixed width
        self.grid_rowconfigure(0, weight=1)
        
        # === SIDEBAR ===
        sidebar_width = 250
        self.sidebar = ctk.CTkFrame(self, fg_color="#e0e0e0", width=sidebar_width, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_propagate(False)  # Fix the width
        
        # App title
        title_frame = ctk.CTkFrame(self.sidebar, fg_color="transparent", height=150)
        title_frame.pack(fill="x", padx=20, pady=(40, 20))
        
        # App logo or title
        app_title = ctk.CTkLabel(
            title_frame, 
            text="Student Marks",
            font=ctk.CTkFont(family="Arial", size=22, weight="bold"),
            text_color="#333333"
        )
        app_title.pack(anchor="w")
        
        subtitle = ctk.CTkLabel(
            title_frame, 
            text="Management System",
            font=ctk.CTkFont(family="Arial", size=14),
            text_color="#666666"
        )
        subtitle.pack(anchor="w", pady=(0, 20))
        
        # Navigation menu
        self.nav_buttons = []
        self.create_navigation()
        
        # === MAIN CONTENT AREA ===
        self.content = ctk.CTkFrame(self, fg_color="white", corner_radius=0)
        self.content.grid(row=0, column=1, sticky="nsew", padx=(0, 0))
    
    def create_navigation(self):
        """Create consistent navigation across all pages"""
        # Navigation menu container
        nav_container = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        nav_container.pack(fill="x", pady=10)
        
        # Navigation items
        nav_items = [
            {"name": "Home", "page": "HomePage"},
            {"name": "Students", "page": "StudentDetails"},
            {"name": "Subjects", "page": "Subjects"},
            {"name": "Marks", "page": "Marks"},
            {"name": "Analysis", "page": "Analysis"}
        ]
        
        # Create navigation buttons
        for item in nav_items:
            button_frame = ctk.CTkFrame(nav_container, fg_color="transparent", height=50)
            button_frame.pack(fill="x", pady=2)
            
            # Active indicator bar
            indicator = ctk.CTkFrame(button_frame, width=4, corner_radius=2)
            indicator.place(relheight=0.8, rely=0.1, x=0)
            
            # Make indicator invisible by default
            indicator.configure(fg_color="transparent")
            
            # Button with special hover effect
            button = ctk.CTkButton(
                button_frame,
                text=item["name"],
                font=ctk.CTkFont(size=14, weight="normal"),
                height=40,
                anchor="w",
                fg_color="transparent",
                hover_color="#d0d0d0",
                text_color="#333333",
                corner_radius=6
            )
            button.pack(fill="x", padx=(15, 10), pady=2)
            
            # Store data for active state management
            button_data = {
                "button": button,
                "indicator": indicator,
                "page": item["page"]
            }
            
            # Set button command
            page_name = item["page"]
            button.configure(command=lambda p=page_name: self.controller.show_frame(p))
            
            # Store button data
            self.nav_buttons.append(button_data)
        
        # Initialize active state based on current page (if controller knows it)
        if hasattr(self.controller, 'active_nav_item'):
            self.update_nav_state(self.controller.active_nav_item)
    
    def update_nav_state(self, active_page):
        """Update the active navigation button based on the current page"""
        # Reset all buttons
        for item in self.nav_buttons:
            item["button"].configure(fg_color="transparent", text_color="#333333")
            item["indicator"].configure(fg_color="transparent")
        
        # Find and activate the button for the current page
        for item in self.nav_buttons:
            if item["page"] == active_page:
                item["button"].configure(fg_color="#d0d0d0", text_color="#1565C0")
                item["indicator"].configure(fg_color="#1565C0")
                break