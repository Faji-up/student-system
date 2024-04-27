from MySQLdb import *
from tkinter import *
from tkinter import ttk, messagebox
from tkinter import ttk, Scrollbar

L_FONT = ("Arial", 10, "bold")
mydb = connect(
    host="localhost",
    user="root",
    passwd="",
    db="students"
)

BG_COLOR = "#eee"
mycursor = mydb.cursor()


class StudentsInformation:
    def __init__(self, root):
        self.root = root
        self.active_window = None
        self.header()
        self.sideBar()

    def frame(self):
        self.active_window = Canvas(self.root, width=1000,background=BG_COLOR)
        self.active_window.pack(fill=Y, expand=True, side=RIGHT)

    def reset_frame(self):
        if self.active_window:
            self.active_window.destroy()

    def header(self):

        head = Label(self.root, text="Student Information System (SSIS)", font=("Segoe UI Black", 15, "bold"), pady=8,
                     bg="#eee", width=78)
        head.pack(fill=X)

    def sideBar(self):

        sidebar = LabelFrame(self.root, bg="#fff", width=200)
        self.view = Button(sidebar, text="Student List", padx=80, command=self.view_students_window,
                           font=("Arial", 10, "bold"), bg="#fff", pady=6,
                           relief="ridge", activebackground="black", activeforeground="white")
        self.view.pack(fill=X)

        self.add = Button(sidebar,
                          text="Add",
                          padx=80,
                          command=self.add_student_window,
                          font=("Arial", 10, "bold"),
                          bg="#fff",
                          pady=6,
                          relief="ridge", activebackground="black", activeforeground="white")

        self.add.pack(fill=X)

        self.delete = Button(sidebar, text="Delete", activebackground="black", activeforeground="white", padx=80,
                             command=self.delete_student_window, font=("Arial", 10, "bold"),
                             bg="#fff", pady=6,
                             relief="ridge")
        self.delete.pack(fill=X)

        self.update = Button(sidebar, text="Update", activebackground="black", activeforeground="white", padx=80,
                             command=self.update_student_window, font=("Arial", 10, "bold"),
                             bg="#fff", pady=6,
                             relief="ridge")
        self.update.pack(fill=X)

        self.courses = Button(sidebar, text="Courses", activebackground="black", activeforeground="white", padx=80,
                              command=self.displayCourses, font=("Arial", 10, "bold"),
                              bg="#fff", pady=6,
                              relief="ridge")
        self.courses.pack(fill=X)

        sidebar.pack(fill=Y, side=LEFT)

    def activeBtn(self, btn):
        if (btn == 1):
            self.view.config(bg="gray", fg="white")
            self.add.config(bg="#fff", fg="black")
            self.update.config(bg="#fff", fg="black")
            self.delete.config(bg="#fff", fg="black")
            self.courses.config(bg="#fff", fg="black")
        elif (btn == 2):
            self.view.config(bg="#fff", fg="black")
            self.add.config(bg="gray", fg="white")
            self.update.config(bg="#fff", fg="black")
            self.delete.config(bg="#fff", fg="black")
            self.courses.config(bg="#fff", fg="black")
        elif (btn == 3):
            self.view.config(bg="#fff", fg="black")
            self.add.config(bg="#fff", fg="black")
            self.update.config(bg="#fff", fg="black")
            self.delete.config(bg="gray", fg="white")
            self.courses.config(bg="#fff", fg="black")
        elif (btn == 4):
            self.view.config(bg="#fff", fg="black")
            self.add.config(bg="#fff", fg="black")
            self.update.config(bg="gray", fg="white")
            self.delete.config(bg="#fff", fg="black")
            self.courses.config(bg="#fff", fg="black")
        elif (btn == 5):
            self.view.config(bg="#fff", fg="black")
            self.add.config(bg="#fff", fg="black")
            self.update.config(bg="#fff", fg="black")
            self.delete.config(bg="#fff", fg="black")
            self.courses.config(bg="gray", fg="white")

    def main(self):
        self.frame()
        self.view_students_window()

    def add_student_window(self):
        self.reset_frame()
        self.frame()
        self.activeBtn(2)
        header = Label(self.active_window, fg="white", text="Add Student", font=("Segoe UI Black", 15, "bold"), pady=8,
                       bg="#2832C2", width=78)
        header.place(x=0, y=0)

        idCon = Frame(self.active_window)
        Label(idCon, text="Student ID :              ", font=L_FONT).grid(row=0, column=0)
        self.student_id = Entry(idCon, width=30)
        self.student_id.grid(row=0, column=1)

        nameCon = Frame(self.active_window)
        Label(nameCon, text="Student Name :        ", font=L_FONT).grid(row=0, column=0)
        self.name = Entry(nameCon, width=30)
        self.name.grid(row=0, column=1)

        self.gender_val = IntVar()
        genderCon = Frame(self.active_window)
        Label(genderCon, text="Student Gender :    ", font=L_FONT).grid(row=0, column=0)
        male = Radiobutton(genderCon, text="MALE", variable=self.gender_val, value=1)
        male.grid(row=0, column=1)
        female = Radiobutton(genderCon, text="FEMALE", variable=self.gender_val, value=2)
        female.grid(row=0, column=2)

        levelCon = Frame(self.active_window)
        Label(levelCon, text="Year Level :             ", font=L_FONT).grid(row=0, column=0)
        self.level = Entry(levelCon, width=30)
        self.level.grid(row=0, column=1)

        codeCon = Frame(self.active_window)
        Label(codeCon, text="Course Code :          ", font=L_FONT).grid(row=0, column=0)
        self.code = Entry(codeCon, width=30)
        self.code.grid(row=0, column=1)

        add = Button(self.active_window, text="Add", padx=100, font=("Arial", 12, "bold"), bg="#C5C6D0",
                     activebackground="green", activeforeground="white")

        idCon.place(x=100, y=140)
        nameCon.place(x=100, y=200)
        genderCon.place(x=100, y=260)
        levelCon.place(x=100, y=320)
        codeCon.place(x=100, y=380)
        add.place(x=350, y=440)

        add.config(
            command=lambda: self.add_student(self.student_id.get(), self.name.get().capitalize(), self.gender_val.get(),
                                             self.level.get(), self.code.get().upper()))

    def add_student(self, student_id, name, gender, level, code):
        if gender == 1:
            gender = "MALE"
        elif gender == 2:
            gender = "FEMALE"
        else:
            return messagebox.showwarning("Adding Failed", "Please fill the required fields")

        if not (student_id == "" or gender == "" or level == "" or code == "" or name == ""):
            mycursor.execute("SELECT * FROM students")
            if len(mycursor.fetchall()) == 0:
                mycursor.execute("INSERT INTO students (student_id,name,gender,level,code) VALUES (%s,%s,%s,%s,%s)",
                                 (student_id, name, gender, level, code))
                mydb.commit()
                self.name.delete(0, END)
                self.level.delete(0, END)
                self.student_id.delete(0, END)
                self.code.delete(0, END)
                return messagebox.showinfo("Successful", f"Added Successful ")
            else:
                mycursor.execute("SELECT * FROM students")
                for student in mycursor.fetchall():
                    print(student[1])
                    if student_id == student[1]:
                        pass
                    else:
                        mycursor.execute(
                            "INSERT INTO students (student_id,name,gender,level,code) VALUES (%s,%s,%s,%s,%s)",
                            (student_id, name, gender, level, code))
                        mydb.commit()
                        self.name.delete(0, END)
                        self.level.delete(0, END)
                        self.student_id.delete(0, END)
                        self.code.delete(0, END)
                        return messagebox.showinfo("Successful", f"Added Successful ")

            self.name.delete(0, END)
            self.level.delete(0, END)
            self.student_id.delete(0, END)
            self.code.delete(0, END)
            return messagebox.showwarning("Warning", f"Student with id of {student_id} is Already Exist")
        else:
            return messagebox.showwarning("Adding Failed", "Please fill the required fields")

    def view_students_window(self):
        self.reset_frame()
        self.frame()
        self.activeBtn(1)

        header = Label(self.active_window, fg="white", text="Students List", font=("Segoe UI Black", 15, "bold"),
                       pady=8,
                       bg="#2832C2")
        header.pack(fill=X)

        # Create a Frame to hold the Treeview and Scrollbar
        tree_frame = Frame(self.active_window)
        tree_frame.pack(fill=BOTH, expand=True)

        self.tree = ttk.Treeview(tree_frame, columns=("ID", "Name", "Gender", "Year Level", "Course Code"),
                                 show="headings")

        self.tree.heading("ID", text="Student ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Gender", text="Gender")
        self.tree.heading("Year Level", text="Year Level")
        self.tree.heading("Course Code", text="Course Code")
        self.tree.pack(side=LEFT, fill="both", expand=True)

        # Create a vertical scrollbar
        scrollbar = Scrollbar(tree_frame, orient=VERTICAL, command=self.tree.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Link the Treeview to the scrollbar
        self.tree.configure(yscrollcommand=scrollbar.set)

        mycursor.execute("SELECT * FROM students")
        for student in mycursor.fetchall():
            self.tree.insert("", "end", values=(student[1], student[2], student[3], student[4], student[5]))

    def select(self, event):
        item = self.tree.selection()
        item_text = self.tree.item(item, "values")

    def delete_student_window(self):
        self.reset_frame()
        self.frame()
        self.activeBtn(3)
        header = Label(self.active_window, fg="white", text="Delete Student", font=("Segoe UI Black", 15, "bold"),
                       pady=8,
                       bg="#990f02")
        header.pack(fill=X)

        style = ttk.Style()
        style.configure("Treeview",background=BG_COLOR,font=("Helvetica",10,"bold"))
        self.tree = ttk.Treeview(self.active_window,style="Treeview", columns=("ID", "Name", "Gender", "Year Level", "Course Code"),
                                 show="headings")

        self.tree.heading("ID", text="Student ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Gender", text="Gender")
        self.tree.heading("Year Level", text="Year Level")
        self.tree.heading("Course Code", text="Course Code")
        self.tree.pack(fill="both", expand=True)

        mycursor.execute("SELECT * FROM students")
        for student in mycursor.fetchall():
            self.tree.insert("", "end", values=(student[1], student[2], student[3], student[4], student[5]))
        self.tree.bind("<<TreeviewSelect>>", self.delete_student)

        #deleteBtn = Button(self.active_window,text='Delete',background="red",fg="white",font=("Arial", 12, "bold"),activeforeground="black",activebackground="maroon",padx=100)
        #deleteBtn.pack(side=BOTTOM)

    def delete_student(self, event):
        try:

            if messagebox.askyesnocancel("Delete Item", "Do you really want to delete this student?"):
                item = self.tree.selection()
                item_text = self.tree.item(item, "values")
                self.tree.delete(item)
                delete = "DELETE FROM students WHERE student_id = %s"
                studentID = (item_text[0],)
                mycursor.execute(delete, studentID)
                mydb.commit()

                return messagebox.showinfo("Successful", "Successfully Deleted")
            else:
                return None
        except Exception as e:
            return messagebox.showwarning("Deleting  Failed", e)

    def update_student_window(self):
        self.reset_frame()
        self.frame()
        self.activeBtn(4)
        header = Label(self.active_window, fg="white", text="Update Student", font=("Segoe UI Black", 15, "bold"),
                       pady=8,
                       bg="#2832C2")
        header.pack(fill=X)

        studentFrame = Frame(self.active_window)
        studentFrame.pack(side=TOP)
        self.tree = ttk.Treeview(studentFrame, columns=("ID", "Name", "Gender", "Year Level", "Course Code"),
                                 show="headings")

        self.tree.heading("ID", text="Student ID")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Gender", text="Gender")
        self.tree.heading("Year Level", text="Year Level")
        self.tree.heading("Course Code", text="Course Code")
        self.tree.pack(fill="both", expand=True)

        mycursor.execute("SELECT * FROM students")
        for student in mycursor.fetchall():
            self.tree.insert("", "end", values=(student[1], student[2], student[3], student[4], student[5]))

        self.tree.bind("<<TreeviewSelect>>", self.showUpdate)

        updateFrame = Canvas(self.active_window, height=600)

        idCon = Frame(updateFrame)
        Label(idCon, text="Student ID :              ", font=L_FONT).grid(row=0, column=0)
        self.student_id = Entry(idCon, width=30)
        self.student_id.grid(row=0, column=1)

        nameCon = Frame(updateFrame)
        Label(nameCon, text="Student Name :        ", font=L_FONT).grid(row=0, column=0)
        self.name = Entry(nameCon, width=30)
        self.name.grid(row=0, column=1)

        self.gender_val = IntVar()
        genderCon = Frame(updateFrame)
        Label(genderCon, text="Student Gender :    ", font=L_FONT).grid(row=0, column=0)
        male = Radiobutton(genderCon, text="MALE", variable=self.gender_val, value=1)
        male.grid(row=0, column=1)
        female = Radiobutton(genderCon, text="FEMALE", variable=self.gender_val, value=2)
        female.grid(row=0, column=2)

        levelCon = Frame(updateFrame)
        Label(levelCon, text="Year Level :             ", font=L_FONT).grid(row=0, column=0)
        self.level = Entry(levelCon, width=30)
        self.level.grid(row=0, column=1)

        codeCon = Frame(updateFrame)
        Label(codeCon, text="Course Code :          ", font=L_FONT).grid(row=0, column=0)
        self.code = Entry(codeCon, width=30)
        self.code.grid(row=0, column=1)
        updateBtn = Button(updateFrame, text="Update", padx=100, font=("Arial", 12, "bold"), bg="#C5C6D0",
                           activebackground="green", activeforeground="white")

        idCon.place(x=100, y=20)
        nameCon.place(x=100, y=60)
        genderCon.place(x=100, y=110)
        levelCon.place(x=100, y=150)
        codeCon.place(x=100, y=210)
        updateBtn.place(x=350, y=270)

        updateFrame.pack(fill=BOTH, side=BOTTOM)
        updateBtn.config(command=self.updateStudent)

    def showUpdate(self, event):
        self.name.delete(0, END)
        self.level.delete(0, END)
        self.student_id.delete(0, END)
        self.code.delete(0, END)
        self.gender_val.set(0)
        self.item = self.tree.selection()
        self.item_select = self.tree.item(self.item, "values")

        self.name.insert(0, self.item_select[1])
        self.level.insert(0, self.item_select[3])
        self.student_id.insert(0, self.item_select[0])
        self.code.insert(0, self.item_select[4])

        gen = 0
        if self.item_select[2] == "MALE":
            gen = 1
        elif self.item_select[2] == "FEMALE":
            gen = 2
        self.gender_val.set(gen)

    def updateStudent(self):
        student_id = self.student_id.get()
        name = self.name.get()
        level = self.level.get()
        gender = self.gender_val.get()
        code = self.code.get()

        if gender == 1:
            gender = "MALE"
        elif gender == 2:
            gender = "FEMALE"

        updateText = f"UPDATE students SET student_id=%s,name=%s,gender=%s,level=%s,code=%s WHERE student_id = {student_id}"
        values = (student_id, name.capitalize(), gender, level, code.upper())

        mycursor.execute(updateText, values)
        mydb.commit()

        self.tree.item(self.item, values=values)

    def displayCourses(self):
        self.reset_frame()
        self.frame()
        self.activeBtn(5)
        header = Label(self.active_window, fg="white", text="Courses List", font=("Segoe UI Black", 15, "bold"), pady=8,
                       bg="#2832C2")
        header.pack(fill=X)

        mycursor.execute("SELECT * FROM courses")

        frame = Frame(self.active_window, height=600, width=950)
        frame.pack(fill=X)
        cel1 = Frame(frame)
        Label(cel1, background="#59788E", text="Course Code", width=20, font=("Segoe UI Black", 10, "bold")).pack(
            side=LEFT)
        Label(cel1, background="#48AAAD", text="Course Name", width=97, font=("Segoe UI Black", 10, "bold")).pack(
            side=RIGHT)
        cel1.pack()
        for course in mycursor.fetchall():
            cel = Frame(frame)
            Label(cel, text=course[1], width=20).pack(side=LEFT)
            Label(cel, text=course[2], width=97).pack(side=RIGHT)
            cel.pack()


if __name__ == "__main__":
    root = Tk()
    root.geometry("1200x700+5+5")
    root.title("Students Information System")
    root.resizable(False, False)
    system = StudentsInformation(root)
    system.main()

    root.mainloop()
