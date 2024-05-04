from utils import config
from utils import memory
from tkinter import messagebox
from .base import BaseInput

class DistanceInput(BaseInput):
    def __init__(self, parent, label_text, **kwargs):
        super().__init__(parent, label_text, **kwargs)
    
    def update_action(self):
        distance_address = config.load_config()['distance']
        distance = self.entry.get()

        if distance.isdigit():
            result = memory.update_client(distance_address, int(distance))
            messagebox.showinfo("Result", "Distance updated successfully")
        else:
            messagebox.showinfo("Result", "Invalid input. Please enter a number.")
    
    def refresh(self):
        distance_address = config.load_config()['distance']
        current_distance = memory.read_client(distance_address)
        self.var.set(current_distance)