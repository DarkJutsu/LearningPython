import tkinter as tk
from tkinter import ttk
import styles

window=tk.Tk()
window.geometry("500x700") # width x height
window.resizable(False, False) # Prevents the window from being resized
styles.main_styles(window) # Styles
window.title("App Make Folders & Move Files")

labelTitle=ttk.Label(window, text="App Make Folders & Move Files", style="title.Label")
labelTitle.pack(pady=10)

window.mainloop()