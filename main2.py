import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.geometry("400x300")
def msg():
    messagebox.showwarning("alert", "stop virus is visible")
button = tk.Button(root, text="Click Me", command=msg)
button.place(x=40,y=80)
root.mainloop()