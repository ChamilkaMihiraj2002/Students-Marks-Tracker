import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Configure window
        self.title("Student Mark Management System")
        self.geometry("1200x700")
        self.minsize(1000, 600)  # Set minimum size
        
        # Initial setup
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        # Configure grid layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Keep track of active navigation item
        self.active_nav_item = "HomePage"
        
        # Create container frame
        self.container = ctk.CTkFrame(self, fg_color="transparent", corner_radius=0)
        self.container.grid(row=0, column=0, sticky="nsew")
        
        # Configure container layout
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        
        # Initialize frame dictionary
        self.frames = {}
        
        # Import frames
        from Pages.HomePage import HomePage
        from Pages.StudentDetails import StudentDetails
        from Pages.Subjects import Subjects
        from Pages.Marks import Marks
        from Pages.Analysis import Analysis
        
        for F in (HomePage, StudentDetails, Subjects, Marks, Analysis):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        # Show initial frame
        self.show_frame("HomePage")
    
    def show_frame(self, page_name):
        """Show the specified frame and update active nav state"""
        # Update active navigation item
        self.active_nav_item = page_name
        
        # Show the requested frame
        frame = self.frames[page_name]
        frame.tkraise()
        
        # Update navigation state in all frames
        for frame_name, frame_obj in self.frames.items():
            if hasattr(frame_obj, 'update_nav_state'):
                frame_obj.update_nav_state(page_name)
    
    def on_closing(self):
        """Handle window close event"""
        self.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()