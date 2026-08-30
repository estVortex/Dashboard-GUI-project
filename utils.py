"""Utility functions for the dashboard application."""
 
def add_hover(button, hover_color, normal_color):
    button.bind("<Enter>", lambda x: button.config(bg=hover_color))
    button.bind("<Leave>", lambda x: button.config(bg=normal_color))

api_key = None