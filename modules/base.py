import tkinter as tk

class BaseInput(tk.Frame):
    def __init__(self, parent, label_text, **kwargs):
        super().__init__(parent, **kwargs)
        self.create_input_section(label_text)
    
    def create_input_section(self, label_text):
        label = tk.Label(self, text=label_text)
        label.pack(side=tk.LEFT, pady=5)

        self.var = tk.IntVar()
        self.var.set('') 

        self.entry = tk.Entry(self, textvariable=self.var, width=10, justify=tk.CENTER)
        self.entry.pack(side=tk.LEFT, pady=4)

        button = tk.Button(self, text="Update", command=self.update_action)
        button.pack(side=tk.RIGHT, pady=5)

    def update_action(self):
        raise NotImplementedError("Subclasses must implement this method")

    def refresh(self):
        raise NotImplementedError("Subclasses must implement this method")