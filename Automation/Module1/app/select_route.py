import tkinter as tk
from tkinter import ttk, filedialog

def choose_route():
    route=filedialog.askdirectory(title="Choose a Route")
    return route

