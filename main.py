import tkinter as tk
from pages.menu import MenuFrame
from pages.weather import WeatherFrame
from pages.notes import NotesFrame
from pages.timer import TimerFrame
from pages.todo import TodoListFrame

class DashboardApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.configure()
        self.root.title("Personal dashboard")
        self.root.minsize(600, 400)
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)
        self.root.rowconfigure(2, weight=1)
        
        # Initialize frames
        self.menu_frame = MenuFrame(self.root, self)
        self.timer_frame = TimerFrame(self.root, self)
        self.weather_frame = WeatherFrame(self.root, self)
        self.notes_frame = NotesFrame(self.root, self)
        self.todolist_frame = TodoListFrame(self.root, self)
        
        self.frames = [
            self.menu_frame,
            self.timer_frame,
            self.notes_frame,
            self.todolist_frame,
            self.weather_frame
        ]
        
        # Show menu on startup
        self.show_frame(self.menu_frame)
    
    def show_frame(self, frame):
        for f in self.frames:
            f.grid_forget()
        frame.grid(row=0, column=0, sticky="nsew", rowspan=3, columnspan=4)
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = DashboardApp()
    app.run()