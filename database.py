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


#------------------------------------------------------------------------
# PAG ACTIVE NA ANG SERVER ITO UNANG IRUN NYO DAHIL ITO GAGAWA NG TABLE NG STUDENTS, TATANGGALIN NYO LANG SA PAGKACOMMENT
# mycursor.execute("""
#                  CREATE TABLE students(
#                  id INT AUTO_INCREMENT PRIMARY KEY,
#                  student_id VARCHAR(200),
#                  name VARCHAR(200),
#                  gender VARCHAR(200),
#                  level VARCHAR(200),
#                  code VARCHAR(20)
#                  )
#                  """)



#------------------------------------------------------------------------
# KAPAG OKAY NA YUNG STUDENT NA TABLE ETO NAMAN ANG ISUNOD NYO SIGRURADUHIN NYO LANG NA NAKA COMMENT ULIT YUNG PAGGAWA NG STUDENT TABLE

# mycursor.execute("""
#                  CREATE TABLE courses(
#                  id INT AUTO_INCREMENT PRIMARY KEY,
#                  course_code VARCHAR(20),
#                  course_name VARCHAR(200)
#                  )
#                  """)



#------------------------------------------------------------------------
# PAG MERONG COURSES TABLE NA ETO NAMAN , PALTAN NYO NA LNG YUNG COURSE_CODE AT CURSE_NAME KUNG ANONG I AADD NYO SA COURSE

# course_code = "CPE"
# course_name = "COMPUTER ENGINEERING"
#
# values = (course_code,course_name)
#mycursor.execute("INSERT INTO courses (course_code,course_name) VALUES (%s,%s)",values)
#------------------------------------------------------------------------

mydb.commit()