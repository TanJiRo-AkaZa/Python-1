import tkinter as tk
def convert():
    """Convert inches to centimeters and display the result"""
    inch = float(entry.get())
    cm = inch * 2.48
    result_label.config(text=f"{inch} inches is {cm} centimeters")
window = tk.Tk()
window.title("Inch to Centimeter Converter")
window.geometry("400x300")
label = tk.Label(window, text="Enter length in inches:")
label.pack(pady=10)
result_label = tk.Label(window, text="")
result_label.pack(pady=10)
entry = tk.Entry(window)
entry.pack(pady=10)
button = tk.Button(window, text="Convert", command=convert)
button.pack(pady=10)
window.mainloop()
