import tkinter as tk
from tkinter import ttk

def main_styles(window):
    style = ttk.Style(window)
    style.configure("title.Label", font=("Arial", 24))