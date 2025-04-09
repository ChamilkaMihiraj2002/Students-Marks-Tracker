from Pages.BasePage import BasePage
import customtkinter as ctk

class HomePage(BasePage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        
        # Header section
        header = ctk.CTkFrame(self.content, fg_color="transparent", height=100)
        header.pack(fill="x", padx=40, pady=(40, 20))
        
        welcome_label = ctk.CTkLabel(
            header,
            text="Welcome to Student Marks Tracker",
            font=ctk.CTkFont(family="Arial", size=24, weight="bold"),
            text_color="#333333"
        )
        welcome_label.pack(anchor="w")
        
        # Dashboard cards
        cards_container = ctk.CTkFrame(self.content, fg_color="transparent")
        cards_container.pack(fill="both", expand=True, padx=40, pady=20)
        
        # Grid layout for cards
        cards_container.grid_columnconfigure((0, 1, 2), weight=1, uniform="cards")
        cards_container.grid_rowconfigure(0, weight=2)
        
        # Create dashboard cards
        self.create_dashboard_card(
            cards_container, 
            "Total Students", 
            "0", 
            "#4CAF50", 
            0, 0
        )
        
        self.create_dashboard_card(
            cards_container, 
            "Total Subjects", 
            "0", 
            "#2196F3", 
            0, 1
        )
        
        self.create_dashboard_card(
            cards_container, 
            "Average Marks", 
            "0", 
            "#FF9800", 
            0, 2
        )
                
    def create_dashboard_card(self, parent, title, value, accent_color, row, col):
        """Create a modern dashboard card with shadow effect"""
        # Create card with shadow effect
        card = ctk.CTkFrame(
            parent,
            corner_radius=8,  # Reduced corner radius
            fg_color="white", 
            border_width=0
        )
        card.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")  # Reduced padding
        
        # Title
        title_label = ctk.CTkLabel(
            card,
            text=title,
            font=ctk.CTkFont(size=12),  # Reduced font size
            text_color="#666666"
        )
        title_label.pack(anchor="w", padx=15, pady=(15, 5))  # Reduced padding
        
        # Value
        value_label = ctk.CTkLabel(
            card,
            text=value,
            font=ctk.CTkFont(size=30, weight="bold"),  # Reduced font size
            text_color="#333333"
        )
        value_label.pack(anchor="w", padx=15, pady=(0, 15))  # Reduced padding
        
        # Accent line at bottom
        accent = ctk.CTkFrame(card, height=4, fg_color=accent_color, corner_radius=2)  # Reduced height
        accent.pack(fill="x", padx=15, pady=(5, 15))  # Reduced padding