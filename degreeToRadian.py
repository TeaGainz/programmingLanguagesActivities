import math
import tkinter as tk
from tkinter import messagebox

def convert_to_radian():
    try:
        degrees = float(degree_entry.get())
        radians = degrees * (math.pi / 180)
        result_label.config(text=f"Radian: {radians:.4f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number")

# Create the main window
root = tk.Tk()
root.title("Degree to Radian Converter")
root.geometry("325x150")

# Create and place the input label and entry
degree_label = tk.Label(root, text="Enter degrees:")
degree_label.pack(pady=5)

degree_entry = tk.Entry(root)
degree_entry.pack(pady=5)

# Create and place the convert button
convert_button = tk.Button(root, text="Convert", command=convert_to_radian)
convert_button.pack(pady=10)

# Create and place the result label
result_label = tk.Label(root, text="Radian: ")
result_label.pack(pady=5)

# Start the main event loop
root.mainloop()