import tkinter as tk
from tkinter import ttk
import styles, select_route
from model.MyRoute import MyRoute

window=tk.Tk()
window.geometry("500x700") # width x height
window.resizable(False, False) # Prevents the window from being resized
window.configure(background="#1ABFED")
styles.main_styles(window) # Styles
window.title("App Make Folders & Move Files")

def handle_route():
    route=select_route.choose_route()
    MyRoute().set_route(route)
    label_select_route.config(text=route)

label_title=ttk.Label(window, text="App Make Folders & Move Files", style="title.Label")
label_title.pack(pady=10)

btn_choose_route=ttk.Button(window, text="Choose Route", command=handle_route, style="choose_route.TButton")
btn_choose_route.pack(pady=10)

label_select_route = ttk.Label(window, text="...", style="choose_route.Label")
label_select_route.pack(pady=10)


window.mainloop()