import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# ------------------------
# Database Setup
# ------------------------
# Connect to SQLite database (or create it)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create the table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        course TEXT NOT NULL
    )
""")
conn.commit()

# ------------------------
# Tkinter Application Setup
# ------------------------
root = tk.Tk()
root.title("Student Management System")
root.geometry("650x500")


# ------------------------
# Functions for CRUD Operations
# ------------------------

def add_student():
    """Insert a new student record into the database."""
    name = entry_name.get()
    age = entry_age.get()
    course = entry_course.get()

    if name and age and course:
        try:
            cursor.execute("INSERT INTO students (name, age, course) VALUES (?, ?, ?)", (name, age, course))
            conn.commit()
            messagebox.showinfo("Success", "Student added successfully")
            clear_fields()
            load_students()
        except Exception as e:
            messagebox.showerror("Database Error", f"Error: {e}")
    else:
        messagebox.showwarning("Input Error", "All fields are required")


def load_students():
    """Fetch all student records and display them in the Treeview."""
    tree.delete(*tree.get_children())
    cursor.execute("SELECT * FROM students")
    for row in cursor.fetchall():
        tree.insert("", tk.END, values=row)


def delete_student():
    """Delete the selected student record from the database."""
    selected_item = tree.selection()
    if selected_item:
        student_id = tree.item(selected_item, "values")[0]
        confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this record?")
        if confirm:
            cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
            conn.commit()
            messagebox.showinfo("Deleted", "Student record deleted successfully")
            load_students()
    else:
        messagebox.showwarning("Selection Error", "Please select a record to delete")


def update_student():
    """Update the selected student record with new data."""
    selected_item = tree.selection()
    if selected_item:
        student_id = tree.item(selected_item, "values")[0]
        name = entry_name.get()
        age = entry_age.get()
        course = entry_course.get()

        if name and age and course:
            cursor.execute("UPDATE students SET name=?, age=?, course=? WHERE id=?", (name, age, course, student_id))
            conn.commit()
            messagebox.showinfo("Success", "Student record updated successfully")
            clear_fields()
            load_students()
        else:
            messagebox.showwarning("Input Error", "All fields are required to update")
    else:
        messagebox.showwarning("Selection Error", "Please select a record to update")


def clear_fields():
    """Clear the entry fields."""
    entry_name.delete(0, tk.END)
    entry_age.delete(0, tk.END)
    entry_course.delete(0, tk.END)


def on_tree_select(event):
    """Populate the entry fields with data from the selected row."""
    selected_item = tree.selection()
    if selected_item:
        student_data = tree.item(selected_item, "values")
        entry_name.delete(0, tk.END)
        entry_age.delete(0, tk.END)
        entry_course.delete(0, tk.END)
        entry_name.insert(0, student_data[1])
        entry_age.insert(0, student_data[2])
        entry_course.insert(0, student_data[3])


# ------------------------
# GUI Components
# ------------------------

# Frame for Input Fields
input_frame = tk.Frame(root)
input_frame.pack(pady=20)

# Name Field
tk.Label(input_frame, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
entry_name = tk.Entry(input_frame)
entry_name.grid(row=0, column=1, padx=10, pady=5)

# Age Field
tk.Label(input_frame, text="Age:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
entry_age = tk.Entry(input_frame)
entry_age.grid(row=1, column=1, padx=10, pady=5)

# Course Field
tk.Label(input_frame, text="Course:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
entry_course = tk.Entry(input_frame)
entry_course.grid(row=2, column=1, padx=10, pady=5)

# Buttons for CRUD operations
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Add Student", width=15, command=add_student).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Update Student", width=15, command=update_student).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Delete Student", width=15, command=delete_student).grid(row=0, column=2, padx=5)
tk.Button(button_frame, text="Clear Fields", width=15, command=clear_fields).grid(row=0, column=3, padx=5)

# Treeview for displaying students
tree_frame = tk.Frame(root)
tree_frame.pack(pady=10, fill="both", expand=True)

columns = ("ID", "Name", "Age", "Course")
tree = ttk.Treeview(tree_frame, columns=columns, show="headings")

# Define headings
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100, anchor="center")

# Add a vertical scrollbar to the Treeview
scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side="right", fill="y")
tree.pack(fill="both", expand=True)

# Bind the Treeview selection event to the on_tree_select function
tree.bind("<<TreeviewSelect>>", on_tree_select)

# Load student records initially
load_students()

# Run the application
root.mainloop()

# ------------------------
# Cleanup: Close database connection on exit.
# ------------------------
conn.close()
