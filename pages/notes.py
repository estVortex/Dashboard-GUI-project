import tkinter as tk
from utils import add_hover
from tkinter import ttk
from tkinter import messagebox
import os

NOTES_DIR = "notes"

if not os.path.exists(NOTES_DIR):
    os.makedirs(NOTES_DIR)

class Notes(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#212121")
        self.tabs = {}
        self.current_text = None
        self.current_name = None

        container = tk.Frame(self, bg="#171717")
        container.pack(fill="both", expand=True)

        self.tab_bar = tk.Frame(container, height=60, bg="#171717")
        self.tab_bar.pack(fill="x", side="top")

        self.editor_frame = tk.Frame(container, bg="#212121")
        self.editor_frame.pack(fill="both", expand=True)
        self.load_notes()

    def name_note(self):
        popup = tk.Toplevel(self)
        popup.geometry("300x150")
        popup.configure(bg="#212121")
        popup.grab_set()

        entry = tk.Entry(
            popup,
            font=("Arial", 14),
            bg="#171717",
            fg="#ffffff",
            insertbackground="#ffffff"
        )
        entry.pack(fill="x", padx=20, pady=(20, 10))

        def create():
            name = entry.get().strip()

            if not name:
                return

            if name in self.tabs:
                messagebox.showerror("Error", "Note already exists")
                return

            self.add_note(name)
            popup.destroy()

        create_btn = tk.Button(
            popup,
            text="Create",
            font=("Arial", 14),
            bg="#303030",
            fg="#ffffff",
            command=create
        )
        create_btn.pack(side="bottom", pady=20)

        popup.bind("<Return>", lambda e: create())

    def add_note(self, name):
        text = tk.Text(
            self.editor_frame,
            bg="#171717",
            fg="#ffffff",
            font=("Arial", 15)
        )

        btn = tk.Button(
            self.tab_bar,
            text=name,
            font=("Arial", 20),
            bg="#303030",
            fg="#ffffff",
            command=lambda: self.switch_note(name)
        )
        btn.pack(side="left")
        add_hover(btn, "#3a3a3a", "#303030")

        self.tabs[name] = {
            "text": text,
            "button": btn
        }

        self.switch_note(name)
        file_path = os.path.join(NOTES_DIR, f"{name}.txt")
        if not os.path.exists(file_path):
            with open(file_path, "w", encoding="utf-8") as f:
                f.write("")

    def switch_note(self, name):
        if self.current_text:
            self.current_text.pack_forget()

        self.current_name = name
        self.current_text = self.tabs[name]["text"]

        self.current_text.pack(fill="both", expand=True)
    
    def delete_note(self, name):
        if name not in self.tabs:
            return
    
        note = self.tabs[name]
        note["text"].destroy()
        note["button"].destroy()
    
        del self.tabs[name]
    
        file_path = os.path.join(NOTES_DIR, f"{name}.txt")
        if os.path.exists(file_path):
            os.remove(file_path)

        if self.tabs:
            self.switch_note(next(iter(self.tabs)))
        else:
            self.current_text = None
            self.current_name = None

    def load_notes(self):
        for file in os.listdir(NOTES_DIR):
            if file.endswith(".txt"):
                name = file[:-4]

                if name in self.tabs:
                    continue

                file_path = os.path.join(NOTES_DIR, file)

                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()

                self._create_loaded_note(name, content)

    def _create_loaded_note(self, name, content):
        text = tk.Text(
            self.editor_frame,
            bg="#171717",
            fg="#ffffff",
            font=("Arial", 15)
        )

        text.insert("1.0", content)

        btn = tk.Button(
            self.tab_bar,
            text=name,
            font=("Arial", 20),
            bg="#303030",
            fg="#ffffff",
            command=lambda: self.switch_note(name)
        )
        btn.pack(side="left")

        self.tabs[name] = {
            "text": text,
            "button": btn
        }

        self.switch_note(name)

    def save_current_note(self):
        if not self.current_name or not self.current_text:
            return

        content = self.current_text.get("1.0", "end-1c")

        file_path = os.path.join(NOTES_DIR, f"{self.current_name}.txt")

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

class NotesFrame(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg="#212121")
        self.app = app
        self.note_count = 1
        self.setup_ui()

    def setup_ui(self):
        for i in range(8):
            self.columnconfigure(i, weight=1)
        for i in range(6):
            self.rowconfigure(i, weight=1)

        noteslabel = tk.Label(
            self,
            text="Notes",
            font=("Arial", 20),
            bg="#171717",
            fg="#ffffff"
        )
        noteslabel.grid(
            row=0,
            column=1,
            sticky="new",
            columnspan=7,
            padx=10,
            pady=10
        )

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

        save_button = tk.Button(
            self,
            text="Save",
            font=("Arial", 20),
            bg="#303030",
            fg="#ffffff",
            activebackground="#404040",
            activeforeground="#ffffff",
            command=self.save_current_note
        )

        save_button.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=10,
            pady=10
        )
        add_hover(save_button, "#3a3a3a", "#303030")

        new_button = tk.Button(
            self,
            text="New note",
            font=("Arial", 20),
            bg="#303030",
            fg="#ffffff",
            activebackground="#404040",
            activeforeground="#ffffff",
            command=self.new_note
        )

        new_button.grid(
            row=3,
            column=0,
            sticky="nsew",
            padx=10,
            pady=10
        )
        add_hover(new_button, "#3a3a3a", "#303030")

        self.noteswindow = Notes(self)
        self.noteswindow.grid(
            row=1,
            column=1,
            columnspan=7,
            rowspan=5,
            sticky="nsew",
            padx=10,
            pady=10
        )

        delete_button = tk.Button(
            self,
            text="Delete",
            font=("Arial", 20),
            bg="#303030",
            fg="#ffffff",
            activebackground="#404040",
            activeforeground="#ffffff",
            command=self.delete_current_note
        )

        delete_button.grid(
            row=5,
            column=0,
            sticky="nsew",
            padx=10,
            pady=10
        )
        add_hover(delete_button, "#3a3a3a", "#303030")

    def new_note(self):
        self.noteswindow.name_note()

    def delete_current_note(self):
        if not self.noteswindow.current_name:
            return

        name = self.noteswindow.current_name
        self.noteswindow.delete_note(name)
    
    def save_current_note(self):
        self.noteswindow.save_current_note()