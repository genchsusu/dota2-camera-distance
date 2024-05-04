import json
import requests
import os
import tkinter as tk
from tkinter import messagebox

CONFIG_URL = "https://raw.githubusercontent.com/genchsusu/dota2-camera-distance/master/config.json"
CONFIG_LOCAL = "config.json"

def download_config():
    response = requests.get(CONFIG_URL)
    response.raise_for_status()  # Raise an error for bad status codes
    with open(CONFIG_LOCAL, 'w') as f:
        f.write(response.text)

def check_for_updates():
    if not os.path.exists(CONFIG_LOCAL):
        download_config()
        return
    response = requests.get(CONFIG_URL)
    response.raise_for_status()
    local_config = json.load(open(CONFIG_LOCAL, 'r'))
    remote_config = response.json()
    if local_config != remote_config:
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        if messagebox.askyesno("Update Available", "Do you want to update now?"):
            download_config()
        root.destroy()
    return

def load_config():
    with open(CONFIG_LOCAL, 'r') as f:
        return json.load(f)
