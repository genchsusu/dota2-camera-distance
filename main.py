import json
import tkinter as tk
from tkinter import simpledialog, messagebox
from pymem import Pymem
from pymem.process import module_from_name

# Load process address from config.json
with open('config.json', 'r') as f:
    config = json.load(f)
# Convert hexadecimal string to integer
process = int(config['address'], 16)

# Function to modify memory
def modify_memory(distance):
    try:
        mem = Pymem("dota2.exe")
        game_module = module_from_name(mem.process_handle, "client.dll").lpBaseOfDll
        mem.write_float(game_module + process, float(distance))
        return "Successful"
    except Exception as e:
        return f"Error: {e}"

# GUI creation
def show_input_dialog():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    distance = simpledialog.askfloat("Input", "Distance:", parent=root)
    if distance is not None:
        result = modify_memory(distance)
        messagebox.showinfo("Result", result)
    root.destroy()

if __name__ == "__main__":
    show_input_dialog()
