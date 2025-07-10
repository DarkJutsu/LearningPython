import tkinter as tk
from tkinter import ttk

def main_styles(window):
    style = ttk.Style(window) # Set the context of style in window

    style.configure("title.Label", font=("Arial", 24), background="#1ABFED", foreground="#29200E") # Set styles for the title
    style.configure("choose_route.Label", font=("Arial", 14), background="#1ABFED", foreground="#FFF")  # Set styles for the title
    style.configure("choose_route.TButton", font=("Arial", 18), background="#2D2E4B", foreground="#2D2E4B")  # Set styles for the title