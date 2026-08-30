import tkinter as tk
from utils import add_hover


class ScrollableChecklist(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent, bg="#212121")
    
        canvas = tk.Canvas(
            self,
            bg="#303030",
            highlightthickness=0
        )
    
        scrollbar = tk.Scrollbar(
            self,
            orient="vertical",
            command=canvas.yview
        )
    
        self.scrollable_frame = tk.Frame(
            canvas,
            bg="#303030"
        )
    
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
    
        canvas.bind_all(
            "<MouseWheel>",
            lambda e: canvas.yview_scroll(int(-1 * (e.delta / 120)), "units")
        )
    
        canvas.create_window(
            (0, 0),
            window=self.scrollable_frame,
            anchor="nw"
        )
    
        canvas.configure(yscrollcommand=scrollbar.set)
    
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
    
        self.todos = []
    
    def add_todo(self, text_input):
        var = tk.BooleanVar()

        cb = tk.Checkbutton(
            self.scrollable_frame,
            text=text_input,
            font=("Arial", 20),
            variable=var,
            bg="#303030",
            fg="white",
            activebackground="#808080",
            activeforeground="white",
            selectcolor="#303030"
        )

        item = TodoItem(text_input, var, cb)
        self.todos.append(item)

        def toggle():
            if var.get():
                cb.config(font=("Arial", 20, "overstrike"))
            else:
                cb.config(font=("Arial", 20))

        var.trace_add("write", lambda *args: toggle())

        cb.pack(anchor="w", padx=20, pady=5)

    def del_checked(self):
        for item in self.todos[:]:
            if item.var.get():
                item.widget.destroy()
                self.todos.remove(item)

    def del_all(self):
        for item in self.todos[:]:
                item.widget.destroy()
                self.todos.remove(item)

class TodoItem:
    def __init__(self, text, var, widget):
        self.text = text
        self.var = var
        self.widget = widget


class TodoListFrame(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent, bg="#212121")
        self.app = app
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the to-do list frame UI."""
        for i in range(7):
            self.columnconfigure(i, weight=1)
            self.rowconfigure(i, weight=1)
        
        # To-do list label
        noteslabel = tk.Label(
            self,
            text="To-Do list",
            font=("Arial", 20),
            bg="#171717",
            fg="#ffffff"
        )
        noteslabel.grid(row=0, column=1, sticky="ewn", columnspan=5, rowspan=1, padx=10, pady=10)
        
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

        # Scrollable list
        self.checklist = ScrollableChecklist(self)
        self.checklist.grid(row=2, column=1, columnspan=7, sticky="nsew", padx=10, pady=10, rowspan=4)

        # Entry field and submiting
        todo_entry = tk.Entry(
            self,
            text="Menu",
            font=("Arial", 20),
            bg="#303030",
            fg="#ffffff",
        )
        todo_entry.grid(row=1, column=1, columnspan=1, sticky="nwes", padx=10, pady=10)

        def add_todo(event=None):
            text_input = todo_entry.get().strip()
            if not text_input:
                return

            self.checklist.add_todo(text_input)
            todo_entry.delete(0, tk.END)

        todo_entry.bind("<Return>", add_todo)

        # Delete all checked
        del_checked_button = tk.Button(
            self,
            text="Delete Checked",
            font=("Arial", 20),
            bg="#303030",
            fg="#ffffff",
            activebackground="#404040",
            activeforeground="#ffffff",
            command=self.checklist.del_checked
        )
        del_checked_button.grid(row=5, column=0, sticky="ew", padx=10, pady=10)
        add_hover(del_checked_button, "#3a3a3a", "#303030")

        # Delete all
        del_all_button = tk.Button(
            self,
            text="Delete All",
            font=("Arial", 20),
            bg="#303030",
            fg="#ffffff",
            activebackground="#404040",
            activeforeground="#ffffff",
            command=self.checklist.del_all
        )
        del_all_button.grid(row=3, column=0, sticky="ew", padx=10, pady=10)
        add_hover(del_all_button, "#3a3a3a", "#303030")

        # Add item
        del_selected_button = tk.Button(
            self,
            text="Add To List",
            font=("Arial", 20),
            bg="#303030",
            fg="#ffffff",
            activebackground="#404040",
            activeforeground="#ffffff",
            command=add_todo
        )
        del_selected_button.grid(row=1, column=0, sticky="ew", padx=10, pady=10)
        add_hover(del_selected_button, "#3a3a3a", "#303030")