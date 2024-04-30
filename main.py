import json
import tkinter as tk
from tkinter import simpledialog, messagebox
from pymem import Pymem
from pymem.process import module_from_name
import os
import requests

CONFIG_URL = "https://raw.githubusercontent.com/genchsusu/dota2-camera-distance/master/config.json"
CONFIG_LOCAL = "config.json"

def download_config():
    response = requests.get(CONFIG_URL)
    response.raise_for_status()  # Raise an error for bad status codes
    with open(CONFIG_LOCAL, 'w') as f:
        f.write(response.text)

def check_for_updates():
    response = requests.get(CONFIG_URL)
    response.raise_for_status()
    local_config = json.load(open(CONFIG_LOCAL, 'r'))
    remote_config = response.json()
    return local_config != remote_config

# Ensure config file exists and check for updates
if not os.path.exists(CONFIG_LOCAL):
    download_config()
elif check_for_updates():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    if messagebox.askyesno("Update Available", "Do you want to update now?"):
        download_config()
    root.destroy()

# Load process address from config.json
with open(CONFIG_LOCAL, 'r') as f:
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
