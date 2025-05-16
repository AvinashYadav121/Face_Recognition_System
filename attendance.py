from  tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
class Attendance:
    def __init__(self,root):
      self.root=root
      self.root.geometry("1530x790+0+0")
      self.root.title("face Recognition System")
      self.root.wm_iconbitmap("face.ico")

      # ////variable///////////
      self.var_atten_id=StringVar()
      
      self.var_atten_roll=StringVar()
      
      self.var_atten_name=StringVar()
      
      self.var_atten_dep=StringVar()
      
      self.var_atten_time=StringVar()
      
      self.var_atten_date=StringVar()
      
      self.var_atten_attendance=StringVar()


      # image

      img=Image.open(r"coll_Images\a5.png")
      img=img.resize((1530,160),Image.Resampling.LANCZOS)
      self.photoimg=ImageTk.PhotoImage(img)

      f_lbl=Label(self.root,image=self.photoimg)
      f_lbl.place(x=0,y=0,width=1530,height=160)

      img3=Image.open(r"coll_Images\bg1.jpg")
      img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
      self.photoimg3=ImageTk.PhotoImage(img3)

      bg_img=Label(self.root,image=self.photoimg3)
      bg_img.place(x=0,y=160,width=1530,height=710)

      main_frame=Frame(bg_img,bd=2,bg="white")
      main_frame.place(x=10,y=10,width=1480,height=600)


      # left frame
      Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,"bold"))
      Left_frame.place(x=10,y=10,width=770,height=580)

      img_left=Image.open(r"coll_Images\s2.jpg")
      img_left=img_left.resize((750,200),Image.Resampling.LANCZOS)
      self.photoimg_left=ImageTk.PhotoImage(img_left)

      f_lbl=Label(Left_frame,image=self.photoimg_left)
      f_lbl.place(x=5,y=0,width=750,height=200)


      left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE ,bg="white")
      left_inside_frame.place(x=10,y=220,width=740,height=320)


      # attendance


      AttendanceId_label=Label(left_inside_frame,text="AttendanceID:",font=("times new roman",13,"bold"),bg="white")
      AttendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

      Attendance_entry=ttk.Entry(left_inside_frame,width=20,font=("times new roman",13,"bold"))
      Attendance_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

      # name

      name_label=Label(left_inside_frame,text="Name:",font=("times new roman",13,"bold"),bg="white")
      name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

      name_entry=ttk.Entry(left_inside_frame,width=20,font=("times new roman",13,"bold"))
      name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

      # roll

      roll_label=Label(left_inside_frame,text="RollNo:",font=("times new roman",13,"bold"),bg="white")
      roll_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

      roll_entry=ttk.Entry(left_inside_frame,width=20,font=("times new roman",13,"bold"))
      roll_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

      # department

      dep_label=Label(left_inside_frame,text="Department:",font=("times new roman",13,"bold"),bg="white")
      dep_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

      dep_entry=ttk.Entry(left_inside_frame,width=20,font=("times new roman",13,"bold"))
      dep_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

      # time

      time_label=Label(left_inside_frame,text="Time:",font=("times new roman",13,"bold"),bg="white")
      time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

      time_entry=ttk.Entry(left_inside_frame,width=20,font=("times new roman",13,"bold"))
      time_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)


      # date

      date_label=Label(left_inside_frame,text="RollNo:",font=("times new roman",13,"bold"),bg="white")
      date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

      date_entry=ttk.Entry(left_inside_frame,width=20,font=("times new roman",13,"bold"))
      date_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)


      # attendance

      attendance_label=Label(left_inside_frame,text="RollNo:",font=("times new roman",13,"bold"),bg="white")
      attendance_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

      self.atten_status=ttk.Combobox(left_inside_frame,width=20,font="comicsansns 11 bold",state="readonly")
      self.atten_status["values"]=("Status","Present","Absent")
      self.atten_status.grid(row=3,column=1,pady=8)
      self.atten_status.current(0)


      # buttons

      btn_frame=Frame(left_inside_frame,bd=2,bg="white",relief=RIDGE)
      btn_frame.place(x=5,y=200,width=725,height=35)


      save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=17,font=("times new roman",13,"bold"),bg="lightblue")
      save_btn.grid(row=0,column=0)

      # update
      update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=17,font=("times new roman",13,"bold"),bg="lightblue")
      update_btn.grid(row=0,column=1)
      

      # delete
      delete_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="lightblue")
      delete_btn.grid(row=0,column=2)

      # reset
      reset_btn=Button(btn_frame,text="Reset",command=self.rest_data,width=17,font=("times new roman",13,"bold"),bg="lightblue")
      reset_btn.grid(row=0,column=3)

      









# right frame
      Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance  Details",font=("times new roman",12,"bold"))
      Right_frame.place(x=810,y=10,width=650,height=580)

      table_frame=Frame(Right_frame,bd=2,bg="white",relief=RIDGE)
      table_frame.place(x=5,y=5,width=625,height=550)

    #  scroll bar
      scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
      scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
      self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance")
                                              ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

      scroll_x.pack(side=BOTTOM,fill=X)
      scroll_y.pack(side=RIGHT,fill=Y)

      scroll_x.config(command=self.AttendanceReportTable.xview)
      scroll_y.config(command=self.AttendanceReportTable.yview)

      self.AttendanceReportTable.heading("id",text="Attendance ID")
      self.AttendanceReportTable.heading("roll",text="Roll")
      self.AttendanceReportTable.heading("name",text="Name ID")
      self.AttendanceReportTable.heading("department",text="Department")
      self.AttendanceReportTable.heading("time",text="Time")
      self.AttendanceReportTable.heading("date",text="Date")
      self.AttendanceReportTable.heading("attendance",text="Attendance ")
      self.AttendanceReportTable["show"]="headings"

      self.AttendanceReportTable.column("id",width=100)
      self.AttendanceReportTable.column("roll",width=100)
      self.AttendanceReportTable.column("name",width=100)
      self.AttendanceReportTable.column("department",width=100)
      self.AttendanceReportTable.column("time",width=100)
      self.AttendanceReportTable.column("date",width=100)
      self.AttendanceReportTable.column("attendance",width=100)


      self.AttendanceReportTable.pack(fill=BOTH,expand=1)

      self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
      # self.fetchData()

      # ////////////////fetch///////
    def fetchData(self,rows):
         self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
         for i in rows:
             self.AttendanceReportTable.insert("",END,values=i)

            #  //////////////import///////////////
   
    def importCsv(self):     
        global mydata 
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV file","*.csv"),("All file","*.*")),parent=self.root)  
        with open(fln) as myfile:
            csvread=csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata) 


    #  ////////////export //////////////        
    def exportCsv(self):
        try:
            if len(mydata)<1:
              messagebox.showerror("No Data","No Data Found to export",parent=self.root)
              return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV file","*.csv"),("All file","*.*")),parent=self.root) 
            with open(fln,mode="w",newline="")as myfile:
                export_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    export_write.writerow(i)
                messagebox.showinfo("Data Export","Your data exported to"+os.path.basename(fln)+"Successfully") 
        except Exception as es:
             messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)         
              

    # ///////update//////////
    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)

        rows = content['values']

        self.var_atten_id.set(rows[0]),
        self.var_atten_roll.set(rows[1]),
        self.var_atten_name.set(rows[2]),
        self.var_atten_dep.set(rows[3]),
        self.var_atten_time.set(rows[4]),
        self.var_atten_date.set(rows[5]),
        self.var_atten_attendance.set(rows[6]),



    def rest_data(self):    
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_id.date("")
        self.var_atten_attendance.set("")


if __name__== "__main__":
    root = Tk()
    obj=Attendance(root)
    root.mainloop()      