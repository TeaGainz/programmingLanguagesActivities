import tkinter as tk
from tkinter import messagebox
import math

def calculate_roots():
    try:
        a = float(a_entry.get())
        b = float(b_entry.get())
        c = float(c_entry.get())

        discriminant = b**2 - 4*a*c

        if discriminant > 0:
            root1 = (-b + math.sqrt(discriminant)) / (2*a)
            root2 = (-b - math.sqrt(discriminant)) / (2*a)
            result_label.config(text=f"x= {root1:.2f} and {root2:.2f}")
        elif discriminant == 0:
            root = -b / (2*a)
            result_label.config(text=f"x= {root:.2f}")
        else:
            result_label.config(text="No real roots")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Quadratic Equation Solver")
root.geometry("350x300")

# Create and place the input labels and entries
a_label = tk.Label(root, text="Enter coefficient a:")
a_label.pack(pady=5)

a_entry = tk.Entry(root)
a_entry.pack(pady=5)

b_label = tk.Label(root, text="Enter coefficient b:")
b_label.pack(pady=5)

b_entry = tk.Entry(root)
b_entry.pack(pady=5)

c_label = tk.Label(root, text="Enter coefficient c:")
c_label.pack(pady=5)

c_entry = tk.Entry(root)
c_entry.pack(pady=5)

# Create and place the calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_roots)
calculate_button.pack(pady=10)

# Create and place the result label
result_label = tk.Label(root, text="x= ")
result_label.pack(pady=5)

# Start the main event loop
root.mainloop()