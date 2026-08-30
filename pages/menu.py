import tkinter as tk
from utils import add_hover

class MenuFrame(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg="#212121")
        self.app = app
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the menu frame UI."""
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        
        # Main menu label
        menu_label = tk.Label(
            self,
            text="Personal Dashboard",
            font=("Arial", 20, "bold"),
            bg="#171717",
            fg="#ffffff"
        )
        menu_label.grid(row=0, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
        
        # To-Do List button
        todolistbtn = tk.Button(
            self,
            text="To-Do List",
            font=("Arial", 20),
            bg="#303030",
            fg="#ffffff",
            activebackground="#404040",
            activeforeground="#ffffff",
            command=lambda: self.app.show_frame(self.app.todolist_frame)
        )
        todolistbtn.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)
        add_hover(todolistbtn, "#3a3a3a", "#303030")
        
        # Notes button
        notesbtn = tk.Button(
            self,
            text="Notes",
            font=("Arial", 20),
            bg="#303030",
            fg="#ffffff",
            activebackground="#404040",
            activeforeground="#ffffff",
            command=lambda: self.app.show_frame(self.app.notes_frame)
        )
        notesbtn.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)
        add_hover(notesbtn, "#3a3a3a", "#303030")
        
        # Weather button
        weatherbtn = tk.Button(
            self,
            text="Weather",
            font=("Arial", 20),
            bg="#303030",
            fg="#ffffff",
            activebackground="#404040",
            activeforeground="#ffffff",
            command=lambda: self.app.show_frame(self.app.weather_frame)
        )
        weatherbtn.grid(row=2, column=0, sticky="nsew", padx=10, pady=5)
        add_hover(weatherbtn, "#3a3a3a", "#303030")
        
        # Timer button
        timerbtn = tk.Button(
            self,
            text="Timer/Clock",
            font=("Arial", 20),
            bg="#303030",
            fg="#ffffff",
            activebackground="#404040",
            activeforeground="#ffffff",
            command=lambda: self.app.show_frame(self.app.timer_frame)
        )
        timerbtn.grid(row=2, column=1, sticky="nsew", padx=10, pady=5)
        add_hover(timerbtn, "#3a3a3a", "#303030")