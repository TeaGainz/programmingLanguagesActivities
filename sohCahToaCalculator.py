import tkinter as tk
from tkinter import messagebox

def calculate_trig():
    try:
        a = float(a_entry.get())
        b = float(b_entry.get())
        c = float(c_entry.get())

        # Calculate sine, cosine, and tangent of angle A
        sin_A = b / c
        cos_A = a / c
        tan_A = b / a

        result_label.config(text=f"Sine of ∠A: {sin_A:.4f}\nCosine of ∠A: {cos_A:.4f}\nTangent of ∠A: {tan_A:.4f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")
    except ZeroDivisionError:
        messagebox.showerror("Input Error", "Division by zero is not allowed")

# Create the main window
root = tk.Tk()
root.title("Trigonometric Calculator")
root.geometry("350x300")

# Create and place the input labels and entries
a_label = tk.Label(root, text="Enter adjacent side (a):")
a_label.pack(pady=5)

a_entry = tk.Entry(root)
a_entry.pack(pady=5)

b_label = tk.Label(root, text="Enter opposite side (b):")
b_label.pack(pady=5)

b_entry = tk.Entry(root)
b_entry.pack(pady=5)

c_label = tk.Label(root, text="Enter hypotenuse (c):")
c_label.pack(pady=5)

c_entry = tk.Entry(root)
c_entry.pack(pady=5)

calculate_button = tk.Button(root, text="Calculate SOH-CAH-TOA", command=calculate_trig)
calculate_button.pack(pady=10)

result_label = tk.Label(root, text="Sine of ∠A: \nCosine of ∠A: \nTangent of ∠A: ")
result_label.pack(pady=10)

# Run the application
root.mainloop()