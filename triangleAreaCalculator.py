import tkinter as tk
from tkinter import messagebox

def calculate_area():
    try:
        base = float(base_entry.get())
        height = float(height_entry.get())
        area = (base * height) / 2
        result_label.config(text=f"Area: {area}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers for base and height")

# Create the main window
root = tk.Tk()
root.title("Triangle Area Calculator")
root.geometry("225x170")

# Create and place the widgets
tk.Label(root, text="Base:").grid(row=0, column=0, padx=10, pady=10)
base_entry = tk.Entry(root)
base_entry.insert(0, "Enter value")
base_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Height:").grid(row=1, column=0, padx=10, pady=10)
height_entry = tk.Entry(root)
height_entry.insert(0, "Enter value")
def on_entry_click(event, entry):
    if entry.get() == "Enter value":
        entry.delete(0, "end")
        entry.insert(0, "")
        entry.config(fg='black')

def on_focusout(event, entry):
    if entry.get() == "":
        entry.insert(0, "Enter value")
        entry.config(fg='grey')

base_entry.bind('<FocusIn>', lambda event: on_entry_click(event, base_entry))
base_entry.bind('<FocusOut>', lambda event: on_focusout(event, base_entry))
base_entry.config(fg='grey')

height_entry.bind('<FocusIn>', lambda event: on_entry_click(event, height_entry))
height_entry.bind('<FocusOut>', lambda event: on_focusout(event, height_entry))
height_entry.config(fg='grey')
height_entry.grid(row=1, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate Area", command=calculate_area)
calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="Area: ")
result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Run the application
root.mainloop()