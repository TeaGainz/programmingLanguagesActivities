import tkinter as tk
from tkinter import messagebox

def calculate_area():
    try:
        base1 = float(base1_entry.get())
        base2 = float(base2_entry.get())
        height = float(height_entry.get())
        area = ((base1 + base2) / 2) * height
        result_label.config(text=f"Area: {area}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for bases and height")

# Create the main window
root = tk.Tk()
root.title("Trapezoid Area Calculator")
root.geometry("225x200")

# Function to clear the default text when the entry is focused
def clear_entry(event, entry):
    if entry.get() == "Enter value":
        entry.delete(0, tk.END)
        entry.config(fg='black')

# Create and place the widgets
tk.Label(root, text="Base a:").grid(row=0, column=0, padx=10, pady=10)
base1_entry = tk.Entry(root, fg='grey')
base1_entry.insert(0, "Enter value")
base1_entry.bind("<FocusIn>", lambda event: clear_entry(event, base1_entry))
base1_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Base b:").grid(row=1, column=0, padx=10, pady=10)
base2_entry = tk.Entry(root, fg='grey')
base2_entry.insert(0, "Enter value")
base2_entry.bind("<FocusIn>", lambda event: clear_entry(event, base2_entry))
base2_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Height:").grid(row=2, column=0, padx=10, pady=10)
height_entry = tk.Entry(root, fg='grey')
height_entry.insert(0, "Enter value")
height_entry.bind("<FocusIn>", lambda event: clear_entry(event, height_entry))
height_entry.grid(row=2, column=1, padx=10, pady=10)



calculate_button = tk.Button(root, text="Calculate Area", command=calculate_area)
calculate_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="Area: ")
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()