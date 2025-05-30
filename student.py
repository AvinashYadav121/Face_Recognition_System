from  tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from tkcalendar import DateEntry
import cv2
import psycopg2

class Student:
    def __init__(self,root):
      self.root=root
      self.root.geometry("1530x790+0+0")
      self.root.title("face Recognition System")
      self.root.wm_iconbitmap("face.ico")



      # variables
      self.var_dep=StringVar()
      self.var_course=StringVar()
      self.var_year=StringVar()
      self.var_semester=StringVar()
      self.var_std_id=StringVar()
      self.var_std_name=StringVar()
      self.var_div=StringVar()
      self.var_roll=StringVar()
      self.var_gender=StringVar()
      self.var_dob=StringVar()
      self.var_email=StringVar()
      self.var_phone=StringVar()
      self.var_address=StringVar()
      self.var_teacher=StringVar()


      title_lbl=Label(text="",font=("times new roman",10,"bold"),bg="black",fg="red")
      title_lbl.place(x=0,y=0,width=1530,height=15)



       # firstImage

      img=Image.open(r"coll_Images/student1.png")
      img=img.resize((1500,160),Image.Resampling.LANCZOS)
      self.photoimg=ImageTk.PhotoImage(img)

      f_lbl=Label(self.root,image=self.photoimg)
      f_lbl.place(x=0,y=10,width=1500,height=160)

    

# backgroundImage
      img3=Image.open(r"coll_Images/bg1.jpg")
      img3=img3.resize((1530,810),Image.Resampling.LANCZOS)
      self.photoimg3=ImageTk.PhotoImage(img3)

      bg_img=Label(self.root,image=self.photoimg3)
      bg_img.place(x=0,y=160,width=1530,height=710)
      


      main_frame=Frame(bg_img,bd=2,bg="white")
      main_frame.place(x=10,y=10,width=1500,height=600)


      # left frame
      Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
      Left_frame.place(x=10,y=10,width=770,height=580)



      img_left=Image.open(r"coll_Images/s1.jpg")
      img_left=img_left.resize((750,130),Image.Resampling.LANCZOS)
      self.photoimg_left=ImageTk.PhotoImage(img_left)

      f_lbl=Label(Left_frame,image=self.photoimg_left)
      f_lbl.place(x=5,y=0,width=750,height=130)

# current course
      current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current corse information",font=("times new roman",12,"bold"))
      current_course_frame.place(x=5,y=125,width=750,height=120)

      # department

      dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
      dep_label.grid(row=0,column=0,padx=10)

      dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"), state="readonly",width=17)
      dep_combo['values']=("Select Department","COMPUTER APPLICATION", "CSE","AGRICULTURE","Mechanical","Electronics","Dairy","Fisheries")
      dep_combo.current(0)
      dep_combo.grid(row=0,column=1,padx=2,pady=10)

      # course
      course_label=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="white")
      course_label.grid(row=0,column=2,padx=10,sticky=W)

      course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"), state="readonly",width=17)
      course_combo['values']=("Select course","MSC IT","MCA","BCA","BSC IT","CE","btech","mtech","Ec","be","te")
      course_combo.current(0)
      course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

      # year
      year_label=Label(current_course_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
      year_label.grid(row=1,column=0,padx=10)

      year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"), state="readonly",width=17)
      year_combo['values']=("Select Year","1","2","3","4")
      year_combo.current(0)
      year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

      # semester
      semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
      semester_label.grid(row=1,column=2,padx=10,sticky=W)

      semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"), state="readonly",width=17)
      semester_combo['values']=("Select Semester","1","2","3","4","5","6","7","8")
      semester_combo.current(0)
      semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

# class student info
      class_Student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",13,"bold"))
      class_Student_frame.place(x=5,y=250,width=750,height=300)


      # student id
      studentId_label=Label(class_Student_frame,text="StudentID:",font=("times new roman",13,"bold"),bg="white")
      studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

      studentId_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))
      studentId_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)


      # student name

      studentName_label=Label(class_Student_frame,text="Student Name:",font=("times new roman",13,"bold"),bg="white")
      studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

      studentName_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",13,"bold"))
      studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

      # class division
      class_div_label=Label(class_Student_frame,text="Class Division:",font=("times new roman",13,"bold"),bg="white")
      class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

      # class_div_entry=ttk.Entry(class_Student_frame,textvariable=self.var_div,width=20,font=("times new roman",13,"bold"))
      # class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

      div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_div,font=("times new roman",13,"bold"), state="readonly",width=17)
      div_combo['values']=("Select Division","A","B","C","D")
      div_combo.current(0)
      div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

      # roll no
      roll_no_label=Label(class_Student_frame,text="RollNo:",font=("times new roman",13,"bold"),bg="white")
      roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

      roll_no_entry=ttk.Entry(class_Student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
      roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

      # gender
      gender_label=Label(class_Student_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white")
      gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

      # gender_entry=ttk.Entry(class_Student_frame,textvariable=self.var_gender,width=20,font=("times new roman",13,"bold"))
      # gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

      gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"), state="readonly",width=17)
      gender_combo['values']=("Select Gender","Male","Female","Other")
      gender_combo.current(0)
      gender_combo.grid(row=2,column=1,padx=2,pady=10,sticky=W)

      # dob
      date_label = Label(class_Student_frame, text="Date:", font=("times new roman", 13, "bold"), bg="white")
      date_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

      date_combo = DateEntry(class_Student_frame,textvariable=self.var_dob, font=("times new roman", 13, "bold"),state="readonly", width=15, background='darkblue',
                                foreground='white', borderwidth=2)
      date_combo.grid(row=2, column=3, padx=2, pady=10, sticky=W)


   #   dob_label=Label(class_Student_frame,text="DOB:",font=("times new roman",13,"bold"),bg="white")
    #  dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

     # dob_entry=ttk.Entry(class_Student_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
      #dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

      # email
      email_label=Label(class_Student_frame,text="Email:",font=("times new roman",13,"bold"),bg="white")
      email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

      email_entry=ttk.Entry(class_Student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
      email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

      # phone no
      phone_label=Label(class_Student_frame,text="MobileNo:",font=("times new roman",13,"bold"),bg="white")
      phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

      phone_entry=ttk.Entry(class_Student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
      phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

      # address class room
      address_label=Label(class_Student_frame,text="Address:",font=("times new roman",13,"bold"),bg="white")
      address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

      address_entry=ttk.Entry(class_Student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
      address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

      # teacher
      teacher_label=Label(class_Student_frame,text="Teacher Name:",font=("times new roman",13,"bold"),bg="white")
      teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

      teacher_entry=ttk.Entry(class_Student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",13,"bold"))
      teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)


      # radio buttons
      self.var_radio1=StringVar()
      radiobtn1=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="Take Photo Sample",value="yes")
      radiobtn1.grid(row=5,column=0)

      
      radiobtn2=ttk.Radiobutton(class_Student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
      radiobtn2.grid(row=5,column=1)

       # button frame

      btn_frame=Frame(class_Student_frame,bd=2,bg="white",relief=RIDGE)
      btn_frame.place(x=5,y=230,width=755,height=95)

      # save btn
      save_btn=Button(btn_frame,text="Save",command=self.add_data,width=12,font=("times new roman",12,"bold"),bg="lightblue")
      save_btn.grid(row=0,column=0)

      # update
      update_btn=Button(btn_frame,text="Update",command=self.update_data,width=12,font=("times new roman",12,"bold"),bg="lightblue")
      update_btn.grid(row=0,column=1)
      

      # delete
      delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=12,font=("times new roman",12,"bold"),bg="lightblue")
      delete_btn.grid(row=0,column=2)

      # reset
      reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=12,font=("times new roman",12,"bold"),bg="lightblue")
      reset_btn.grid(row=0,column=3)

      # take phtot sample
      take_photo_btn=Button(btn_frame,command=self.generate_dataset,text="Take Photo",width=12,font=("times new roman",12,"bold"),bg="lightblue")
      take_photo_btn.grid(row=0,column=4)


      update_photo_btn=Button(btn_frame,text="Update Photo",width=12,font=("times new roman",12,"bold"),bg="lightblue")
      update_photo_btn.grid(row=0,column=5)

      # right frame
      Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
      Right_frame.place(x=810,y=10,width=650,height=580)


      img_right=Image.open(r"coll_Images/s2.jpg")
      img_right=img_right.resize((750,130),Image.Resampling.LANCZOS)
      self.photoimg_right=ImageTk.PhotoImage(img_right)

      f_lbl=Label(Right_frame,image=self.photoimg_right)
      f_lbl.place(x=5,y=0,width=750,height=130)

      # search

      Search_frame=LabelFrame(Right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,"bold"))
      Search_frame.place(x=5,y=135,width=635,height=70)

      search_label=Label(Search_frame,text="Search:",font=("times new roman",15,"bold"),bg="white")
      search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

      search_combo=ttk.Combobox(Search_frame,font=("times new roman",13,"bold"), state="readonly",width=17)
      search_combo['values']=("Select ","Roll_No","Name","PhoneNo")
      search_combo.current(0)
      search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

      search_entry=ttk.Entry(Search_frame,width=15,font=("times new roman",13,"bold"))
      search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)


      search_btn=Button(Search_frame,text="Search",width=9,font=("times new roman",13,"bold"),bg="lightblue")
      search_btn.grid(row=0,column=3,padx=2)

      showAll_btn=Button(Search_frame,text="Show All",width=8,font=("times new roman",13,"bold"),bg="lightblue")
      showAll_btn.grid(row=0,column=4,padx=2)

 # table frame
      table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
      table_frame.place(x=5,y=210,width=635,height=330)


      scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
      scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
      self.student_table=ttk.Treeview(table_frame,columns= 
      
       
      ("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo")
      ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set) 
      scroll_x.pack(side=BOTTOM,fill=X)
      scroll_y.pack(side=RIGHT,fill=Y)
      scroll_x.config(command=self.student_table.xview)
      scroll_y.config(command=self.student_table.yview)


      self.student_table.heading("dep",text="Department")
      self.student_table.heading("course",text="Course")
      self.student_table.heading("year",text="Year")
      self.student_table.heading("sem",text="Semester")
      self.student_table.heading("id",text="StudentID")
      self.student_table.heading("name",text="Name")
      self.student_table.heading("div",text="Division")
      self.student_table.heading("roll",text="Roll_No")
      self.student_table.heading("gender",text="Gender")
      self.student_table.heading("dob",text="DOB")
      self.student_table.heading("email",text="Email")
      self.student_table.heading("phone",text="Phone")
      self.student_table.heading("address",text="Address")
      self.student_table.heading("teacher",text="Teacher")
      self.student_table.heading("photo",text="Status")
      self.student_table["show"]="headings"

      self.student_table.column("dep",width=100)
      self.student_table.column("course",width=100)
      self.student_table.column("year",width=100)
      self.student_table.column("sem",width=100)
      self.student_table.column("id",width=100)
      self.student_table.column("name",width=100)
      self.student_table.column("div",width=100)
      self.student_table.column("roll",width=100)
      self.student_table.column("gender",width=100)
      self.student_table.column("dob",width=100)
      self.student_table.column("email",width=100)
      self.student_table.column("phone",width=100)
      self.student_table.column("address",width=100)
      self.student_table.column("teacher",width=100)
      self.student_table.column("photo",width=100)

      self.student_table.pack(fill=BOTH,expand=1)
      self.student_table.pack(fill=BOTH,expand=1)
      self.student_table.bind("<ButtonRelease>",self.get_cursor)
      self.fetch_data()

    # function declaration
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Fields Are Required", parent=self.root)
        else:
            try:
                conn = psycopg2.connect(
                    host="localhost",
                    user="postgres",
                    password="Avinash@786",
                    database="face_recogniser"
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "INSERT INTO student (Dep, course, Year, Semester, Student_id, Name, Division, Roll, Gender, Dob, Email, Phone, Address, Teacher, Photosample) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_id.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                    )
                )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student Details have been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    def fetch_data(self):
        try:
            conn = psycopg2.connect(
                host="localhost",
                user="postgres",
                password="Avinash@786",
                database="face_recogniser"
            )
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM student")
            data = my_cursor.fetchall()

            if len(data) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("", END, values=i)
            conn.commit()
            conn.close()
        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

    def get_cursor(self, event=None):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        if data:
            self.var_dep.set(data[0])
            self.var_course.set(data[1])
            self.var_year.set(data[2])
            self.var_semester.set(data[3])
            self.var_std_id.set(data[4])
            self.var_std_name.set(data[5])
            self.var_div.set(data[6])
            self.var_roll.set(data[7])
            self.var_gender.set(data[8])
            self.var_dob.set(data[9])
            self.var_email.set(data[10])
            self.var_phone.set(data[11])
            self.var_address.set(data[12])
            self.var_teacher.set(data[13])
            self.var_radio1.set(data[14])
            
def update_data(self):
    if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
        messagebox.showerror("Error", "All fields are required", parent=self.root)
    else:
        try:
            update = messagebox.askyesno("Update", "Do You Want To Update Student details", parent=self.root)
            if update:
                conn = psycopg2.connect(
                    host="localhost",
                    user="postgres",
                    password="Avinash@786",
                    database="face_recogniser"
                )
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "UPDATE student SET Dep=%s, course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, Photosample=%s WHERE Student_id=%s",
                    (
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_div.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get(),
                    )
                )
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Student details successfully updated", parent=self.root)
            else:
                return
        except Exception as es:
            messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)

# delete function
def delete_data(self):
    if self.var_std_id.get() == "":
        messagebox.showerror("Error", "Student ID must be required", parent=self.root)
    else:
        try:
            # Confirm delete action with user
            delete = messagebox.askyesno("Student Delete Page", "Do you want to delete this student?", parent=self.root)
            if delete:  # If the user clicks "Yes"
                # Connect to the PostgreSQL database
                conn = psycopg2.connect(
                    host="localhost",
                    user="postgres",
                    password="Avinash@786",
                    database="face_recogniser"
                )
                my_cursor = conn.cursor()
                # SQL query to delete the student
                sql = "DELETE FROM student WHERE Student_id=%s"
                val = (self.var_std_id.get(),)
                # Execute the delete query
                my_cursor.execute(sql, val)
                # Commit the transaction
                conn.commit()
                # Fetch updated data
                self.fetch_data()
                # Close the connection
                conn.close()
                # Inform the user that the deletion was successful
                messagebox.showinfo("Delete", "Successfully deleted student details", parent=self.root)
            else:
                return  
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

# reset 
def reset_data(self): 
    self.var_dep.set("select Department") 
    self.var_course.set("select Course") 
    self.var_year.set("select Year") 
    self.var_semester.set("select Semester") 
    self.var_std_id.set("") 
    self.var_std_name.set("") 
    self.var_div.set("select Division") 
    self.var_roll.set("") 
    self.var_gender.set("Male") 
    self.var_dob.set("") 
    self.var_email.set("") 
    self.var_phone.set("") 
    self.var_address.set("") 
    self.var_teacher.set("") 
    self.var_radio1.set("")        

# generate data set 
def generate_dataset(self):
    if self.var_dep.get() == "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
        messagebox.showerror("Error", "All fields are required", parent=self.root)
    else:
        try:
            # Use PostgreSQL instead of MySQL
            conn = psycopg2.connect(
                host="localhost",
                user="postgres",
                password="Avinash@786",
                database="face_recogniser"
            )
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM student")
            myresult = my_cursor.fetchall()
            id = 0
            for _ in myresult:
                id += 1

            my_cursor.execute(
                "UPDATE student SET Dep=%s, course=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, Photosample=%s WHERE Student_id=%s",
                (
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get(),
                )
            )
            conn.commit()
            self.fetch_data()
            self.reset_data()
            conn.close()

            #   load data
            face_classifier = cv2.CascadeClassifier(r"haarcascade_frontalface_default.xml")

            def face_cropped(img):
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                for (x, y, w, h) in faces:
                    face_cropped = img[y:y + h, x:x + w]
                    return face_cropped

            cap = cv2.VideoCapture(0)
            img_id = 0
            while True:
                _, my_frame = cap.read()
                if face_cropped(my_frame) is not None:
                    img_id += 1
                    face = cv2.resize(face_cropped(my_frame), (450, 450))
                    face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                    file_name_path = "data/user." + str(self.var_std_id.get()) + "." + str(img_id) + ".jpg"
                    cv2.imwrite(file_name_path, face)
                    cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                    cv2.imshow("cropped Face", face)

                if cv2.waitKey(1) == 13 or int(img_id) == 100:
                    break
            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result", "Generating Data sets completed!!")

        except Exception as es:
            messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)