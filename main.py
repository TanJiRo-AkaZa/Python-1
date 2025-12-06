import tkinter as tk
from datetime import date
root = tk.Tk()
root.title("Getting started with widgets")
root.geometry("400x300")
lbl = tk.Label(root,text="Hey there!",fg = "blue",bg = "yellow",
               height=1,width=300)
name_lbl = tk.Label(root,text="Name:FULLNAME", bg ="blue" ,fg ="white")
name_entry = tk.Entry(root)
text_box = tk.Text(root,height=3)
def display():
    name = name_entry.get()
    message = f"Hello, {name}!\nToday is {date.today()}."
    text_box.delete(1.0, tk.END)
    text_box.insert(tk.END, message)
btn = tk.Button(root,text="begin",command=display,height=1,bg ="black",
                fg = "white")
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()