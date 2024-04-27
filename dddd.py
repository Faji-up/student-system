from MySQLdb import *
from tkinter import *
from tkinter import ttk,messagebox
from tkinter import ttk, Scrollbar
mydb = connect(
     host = "localhost",
     user = "root",
     passwd = "",
     db = "students"
 )
mycursor = mydb.cursor()

#mycursor.execute("DROP TABLE courses")
# mycursor.execute("""
#                  CREATE TABLE courses(
#                  id INT AUTO_INCREMENT PRIMARY KEY,
#                  course_code VARCHAR(20),
#                  course_name VARCHAR(200)
#                  )
#                  """)
course_code = "CPE"
course_name = "COMPUTER ENGINEERING"

values = (course_code,course_name)

#mycursor.execute("INSERT INTO courses (course_code,course_name) VALUES (%s,%s)",values)

mydb.commit()