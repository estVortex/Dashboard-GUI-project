import tkinter as tk
import time
from utils import add_hover

class TimerFrame(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg="#212121")
        self.app = app
        
        # Timer state
        self.running = False
        self.start_time = None
        self.elapsed_time = 0.00
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the timer frame UI."""
        for i in range(7):
            self.columnconfigure(i, weight=1)
            self.rowconfigure(i, weight=1)
        
        # Timer/Clock label
        timerlabel = tk.Label(
            self,
            text="Timer/Clock",
            font=("Arial", 20),
            bg="#171717",
            fg="#ffffff"
        )
        timerlabel.grid(row=0, column=1, sticky="ewn", columnspan=5, padx=10, pady=10)
        
        # Menu button
        menu_button = tk.Button(
            self,
            text="Menu",
            font=("Arial", 20),
            bg="#303030",
            fg="#ffffff",
            activebackground="#404040",
            activeforeground="#ffffff",
            command=lambda: self.app.show_frame(self.app.menu_frame)
        )
        menu_button.grid(row=0, column=0, sticky="nw")
        add_hover(menu_button, "#3a3a3a", "#303030")
        
        # Clock
        self.clock = tk.Label(
            self,
            text="",
            font=("Arial", 50),
            bg="#303030",
            fg="#ffffff"
        )
        self.clock.grid(row=2, column=1, pady=20, padx=10, sticky="nsew", columnspan=5)
        self.update_clock()
        
        # Timer
        self.timer = tk.Label(
            self,
            text="0.00",
            font=("Arial", 50),
            bg="#303030",
            fg="#ffffff"
        )
        self.timer.grid(row=3, column=1, columnspan=3, pady=10, padx=10, sticky="nsew")
        
        # Start/Stop button
        self.startbtn = tk.Button(
            self,
            text="Start",
            font=("Arial", 20),
            bg="#303030",
            fg="#ffffff",
            activebackground="#404040",
            activeforeground="#ffffff",
            command=self.toggle_timer
        )
        self.startbtn.grid(row=3, column=4, sticky="nsew", padx=10)
        
        # Reset button
        resetbtn = tk.Button(
            self,
            text="Reset",
            font=("Arial", 20),
            bg="#303030",
            fg="#ffffff",
            activebackground="#404040",
            activeforeground="#ffffff",
            command=self.reset_timer
        )
        resetbtn.grid(row=3, column=5, sticky="nsew", padx=10)
    
    def update_clock(self):
        """Update the clock display."""
        current_time = time.strftime("%H:%M:%S")
        self.clock.config(text=current_time)
        self.after(1000, self.update_clock)
    
    def toggle_timer(self):
        """Toggle the timer between start and stop."""
        if not self.running:
            self.start_time = time.perf_counter() - self.elapsed_time
            self.running = True
            self.startbtn.config(text="Stop")
            self.update_timer()
        else:
            self.elapsed_time = time.perf_counter() - self.start_time
            self.running = False
            self.startbtn.config(text="Start")
            if self.elapsed_time == 10.0:
                self.startbtn.config(text="WOW SO PRECISE!!!!!!")
    
    def update_timer(self):
        """Update the timer display."""
        if self.running:
            elapsed = time.perf_counter() - self.start_time
            if elapsed >= 60:
                self.timer.config(text=f"{int(elapsed // 60)}:{elapsed % 60:05.2f}")
                self.after(20, self.update_timer)
            else:
                self.timer.config(text=f"{elapsed:.2f}")
                self.after(20, self.update_timer)
    
    def reset_timer(self):
        """Reset the timer to zero."""
        self.running = False
        self.start_time = None
        self.elapsed_time = 0.00
        self.timer.config(text="0.00")
        self.startbtn.config(text="Start")