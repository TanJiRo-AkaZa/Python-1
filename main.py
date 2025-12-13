import tkinter as tk
window = tk.Tk()
window.title("")
window.geometry("400x300")
def handle_keypress(event):
    """print the character of the key pressed"""
    print(event.char)
window.bind("<KeyPress>", handle_keypress)
def handle_click(event):
    """print the coordinates of the mouse click"""
    print("\nThe button was clicked")
button = tk.Button(window, text="Click Me")
button.pack()
button.bind("<Button-1>", handle_click)
window.mainloop()