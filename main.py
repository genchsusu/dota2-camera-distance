import tkinter as tk
from tkinter import messagebox
from modules.distance import DistanceInput  # Ensure the import path matches the actual file location
from utils import config

class Dota2(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dota2")
        self.config_update()

    def config_update(self):
        # Check for config updates at startup
        if config.check_for_updates():
            messagebox.showinfo("Update", "Configuration has been updated. Please restart the application.")

    def init_ui(self):
        self.group = tk.Frame(self)
        self.group.pack(padx=20, pady=10)

        # Initialize DistanceInput without the unnecessary 'update_distance' argument
        self.distance_input = DistanceInput(self.group, "Camera Distance:")
        self.distance_input.pack(padx=5, pady=5)

    def on_focus(self, event):
        # Refresh the input when the window gains focus
        self.distance_input.refresh()

    def run(self):
        self.init_ui()
        self.bind("<FocusIn>", self.on_focus)
        self.mainloop()

if __name__ == "__main__":
    app = Dota2()
    app.run()