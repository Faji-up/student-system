import tkinter as tk
from tkinter import ttk

class StudentViewer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Student Viewer")

        # Create TreeView widget
        self.tree = ttk.Treeview(self, columns=("ID", "Name", "Gender", "Year Level", "Course Code"), show="headings")
        self.tree.heading("ID", text="Student ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Gender", text="Gender")
        self.tree.heading("Year Level", text="Year Level")
        self.tree.heading("Course Code", text="Course Code")
        self.tree.pack(fill="both", expand=True)

        # Add some sample data
        self.add_student("S001", "John Doe", "Male", "Senior", "CS101")
        self.add_student("S002", "Jane Smith", "Female", "Junior", "ENG201")

    def add_student(self, student_id, name, gender, year_level, course_code):
        self.tree.insert("", "end", values=(student_id, name, gender, year_level, course_code))




def show_selection():
    selection = gender.get()
    if selection == 1:
        print("Male")
    elif selection == 2:
        print("Female")

# Create the main window
root = tk.Tk()
root.title("Gender Selection")

# Create a Tkinter variable to store the selected gender
gender = tk.IntVar()

# Create Radiobuttons for Male and Female
male_radio = tk.Radiobutton(root, text="Male", variable=gender, value=1, command=show_selection)
female_radio = tk.Radiobutton(root, text="Female", variable=gender, value=2, command=show_selection)

# Pack the Radiobuttons
male_radio.pack(anchor=tk.W)
female_radio.pack(anchor=tk.W)

# Start the Tkinter event loop
root.mainloop()

if __name__ == "__main__":
    app = StudentViewer()
    app.mainloop()
