from tkinter import* 
from tkinter import ttk
from PIL import Image,ImageTk
from register import Register
import mysql.connector
from time import strftime
from tkinter import messagebox
import cv2
import tkinter.messagebox
# --------------------------
from train import Train
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from Help import Helpsupport
import os
import psycopg2


class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1530x790+0+0")

        # variables 
        self.var_ssq=StringVar()
        self.var_sa=StringVar()
        self.var_pwd=StringVar()

        bg_path = r"coll_Images/loginBg1.jpg"
        

        frame1= Frame(self.root,bg="#002B53")
        frame1.place(x=560,y=170,width=340,height=450)

        log1_path = r"coll_Images/log1.png"
        

        get_str = Label(frame1,text="Login",font=("times new roman",20,"bold"),fg="white",bg="#002B53")
        get_str.place(x=140,y=100)

        #label1 
        username =lb1= Label(frame1,text="Username:",font=("times new roman",15,"bold"),fg="white",bg="#002B53")
        username.place(x=30,y=160)

        #entry1 
        self.txtuser=ttk.Entry(frame1,font=("times new roman",15,"bold"))
        self.txtuser.place(x=33,y=190,width=270)


        #label2 
        pwd =lb1= Label(frame1,text="Password:",font=("times new roman",15,"bold"),fg="white",bg="#002B53")
        pwd.place(x=30,y=230)

        #entry2 
        self.txtpwd=ttk.Entry(frame1,font=("times new roman",15,"bold"))
        self.txtpwd.place(x=33,y=260,width=270)


        # Creating Button Login
        loginbtn=Button(frame1,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#002B53",bg="white",activeforeground="white",activebackground="#007ACC")
        loginbtn.place(x=33,y=320,width=270,height=35)


        # Creating Button Registration
        loginbtn=Button(frame1,command=self.reg,text="Register",font=("times new roman",10,"bold"),bd=0,relief=RIDGE,fg="white",bg="#002B53",activeforeground="orange",activebackground="#002B53")
        loginbtn.place(x=33,y=370,width=50,height=20)


        # Creating Button Forget
        loginbtn=Button(frame1,command=self.forget_pwd,text="Forget",font=("times new roman",10,"bold"),bd=0,relief=RIDGE,fg="white",bg="#002B53",activeforeground="orange",activebackground="#002B53")
        loginbtn.place(x=90,y=370,width=50,height=20)


    #  THis function is for open register window
    def reg(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if (self.txtuser.get()=="" or self.txtpwd.get()==""):
            messagebox.showerror("Error","All Field Required!")
        elif(self.txtuser.get()=="admin" and self.txtpwd.get()=="admin"):
            messagebox.showinfo("Sussessfully","Welcome to Attendance Managment System Using Facial Recognition")
        else:
            # messagebox.showerror("Error","Please Check Username or Password !")
            try:
                conn = psycopg2.connect(
                    dbname='face_recognition',
                    user='root',
                    password='Avinash@786',
                    host='localhost',
                    port=5432
                )
                mycursor = conn.cursor()
                mycursor.execute("SELECT * FROM regteach WHERE email=%s AND pwd=%s", (
                    self.txtuser.get(),
                    self.txtpwd.get()
                ))
                row = mycursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Username and Password!")
                else:
                    open_min = messagebox.askyesno("YesNo", "Access only Admin")
                    if open_min > 0:
                        self.new_window = Toplevel(self.root)
                        self.app = Face_Recognition_System(self.new_window)
                    else:
                        if not open_min:
                            return
                conn.commit()
                conn.close()
            except Exception as e:
                messagebox.showerror("Database Error", f"Error connecting to database:\n{e}")
#=======================Reset Passowrd Function=============================
    def reset_pass(self):
        if self.var_ssq.get()=="Select":
            messagebox.showerror("Error","Select the Security Question!",parent=self.root2)
        elif(self.var_sa.get()==""):
            messagebox.showerror("Error","Please Enter the Answer!",parent=self.root2)
        elif(self.var_pwd.get()==""):
            messagebox.showerror("Error","Please Enter the New Password!",parent=self.root2)
        else:
            conn = psycopg2.connect(
            dbname='face_recognition',
            user='root',
            password='Avinash@786',
            host='localhost',
            port=5432
            )
            mycursor = conn.cursor()
            query = "SELECT * FROM regteach WHERE email=%s AND ss_que=%s AND s_ans=%s"
            value = (self.txtuser.get(), self.var_ssq.get(), self.var_sa.get())
            mycursor.execute(query, value)
            row = mycursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Please Enter the Correct Answer!", parent=self.root2)
            else:
                query=("update regteach set pwd=%s where email=%s")
                value=(self.var_pwd.get(),self.txtuser.get())
                mycursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Successfully Your password has been rest, Please login with new Password!",parent=self.root2)
                



# =====================Forget window=========================================
    def forget_pwd(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email ID to reset Password!")
        else:
            conn = psycopg2.connect(
                dbname='face_recognition',
                user='root',
                password='Avinash@786',
                host='localhost',
                port=5432
            )
            mycursor = conn.cursor()
            query=("select * from regteach where email=%s")
            value=(self.txtuser.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("Error","Please Enter the Valid Email ID!")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("400x400+610+170")
                l=Label(self.root2,text="Forget Password",font=("times new roman",30,"bold"),fg="#002B53",bg="#fff")
                l.place(x=0,y=10,relwidth=1)
                # -------------------fields-------------------
                #label1 
                ssq =lb1= Label(self.root2,text="Select Security Question:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                ssq.place(x=70,y=80)

                #Combo Box1
                self.combo_security = ttk.Combobox(self.root2,textvariable=self.var_ssq,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security["values"]=("Select","Your Date of Birth","Your Nick Name","Your Favorite Book")
                self.combo_security.current(0)
                self.combo_security.place(x=70,y=110,width=270)


                #label2 
                sa =lb1= Label(self.root2,text="Security Answer:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                sa.place(x=70,y=150)

                #entry2 
                self.txtpwd=ttk.Entry(self.root2,textvariable=self.var_sa,font=("times new roman",15,"bold"))
                self.txtpwd.place(x=70,y=180,width=270)

                #label2 
                new_pwd =lb1= Label(self.root2,text="New Password:",font=("times new roman",15,"bold"),fg="#002B53",bg="#F2F2F2")
                new_pwd.place(x=70,y=220)

                #entry2 
                self.new_pwd=ttk.Entry(self.root2,textvariable=self.var_pwd,font=("times new roman",15,"bold"))
                self.new_pwd.place(x=70,y=250,width=270)

                # Creating Button New Password
                loginbtn=Button(self.root2,command=self.reset_pass,text="Reset Password",font=("times new roman",15,"bold"),bd=0,relief=RIDGE,fg="#fff",bg="#002B53",activeforeground="white",activebackground="#007ACC")
                loginbtn.place(x=70,y=300,width=270,height=35)


            

# =====================main program Face deteion system====================
class Face_Recognition_System:
    def __init__(self,root):
      self.root=root
      self.root.geometry("1530x790+0+0")
      self.root.title("face Recognition System")
      self.root.wm_iconbitmap("face.ico")



      
      img=Image.open(r"coll_Images/background.jpg")
      img=img.resize((500,130),Image.Resampling.LANCZOS)
      self.photoimg=ImageTk.PhotoImage(img)

      f_lbl=Label(self.root,image=self.photoimg)
      f_lbl.place(x=0,y=0,width=500,height=130)

    # SecondImage


      img1=Image.open(r"coll_Images/background.jpg")
      img1=img1.resize((500,130),Image.Resampling.LANCZOS)
      self.photoimg1=ImageTk.PhotoImage(img1)

      f_lbl=Label(self.root,image=self.photoimg1)
      f_lbl.place(x=500,y=0,width=500,height=130)

    # thirdImage
      img2=Image.open(r"coll_Images/background.jpg")
      img2=img2.resize((1000,130),Image.Resampling.LANCZOS)
      self.photoimg2=ImageTk.PhotoImage(img2)

      f_lbl=Label(self.root,image=self.photoimg2)
      f_lbl.place(x=1000,y=0,width=550,height=130)


  # backgroundImage
      img3=Image.open(r"coll_Images/background.jpg")
      img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
      self.photoimg3=ImageTk.PhotoImage(img3)

      bg_img=Label(self.root,image=self.photoimg3)
      bg_img.place(x=0,y=130,width=1530,height=710)

      title_lbl=Label(bg_img,text=" ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="black",fg="red")
      title_lbl.place(x=0,y=0,width=1530,height=80)

      # ///////////time
      def time():
          string = strftime('%H:%M:%S %p')
          lbl.config(text = string)
          lbl.after(1000,time)

      lbl = Label(title_lbl,font=("times new roman",14,"bold"),bg="white",fg="blue")
      lbl.place(x=0,y=0,width=110,height=50) 
      time()


      # buttons


      img4=Image.open(r"coll_Images/student_details.jpg")
      img4=img4.resize((220,220),Image.Resampling.LANCZOS)
      self.photoimg4=ImageTk.PhotoImage(img4)

      b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
      b1.place(x=200,y=100,width=220,height=220)

      b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="red")
      b1_1.place(x=200,y=300,width=220,height=40)

# face button
      img5=Image.open(r"coll_Images/face_detector.jpg")
      img5=img5.resize((220,220),Image.Resampling.LANCZOS)
      self.photoimg5=ImageTk.PhotoImage(img5)

      b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data)
      b1.place(x=500,y=100,width=220,height=220)

      b1_1=Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="black",fg="red")
      b1_1.place(x=500,y=300,width=220,height=40)


#   Attendance
      
      img6=Image.open(r"coll_Images/attendance.jpg")
      img6=img6.resize((220,220),Image.Resampling.LANCZOS)
      self.photoimg6=ImageTk.PhotoImage(img6)

      b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance_data)
      b1.place(x=800,y=100,width=220,height=220)

      b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="black",fg="red")
      b1_1.place(x=800,y=300,width=220,height=40)


# help
      img7=Image.open(r"coll_Images/hlp.jpg")
      img7=img7.resize((220,220),Image.Resampling.LANCZOS)
      self.photoimg7=ImageTk.PhotoImage(img7)

      b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
      b1.place(x=1100,y=100,width=220,height=220)

      b1_1=Button(bg_img,text="HelpSupport",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="black",fg="red")
      b1_1.place(x=1100,y=300,width=220,height=40)


# train

      img8=Image.open(r"coll_Images/Train_Data.jpg")
      img8=img8.resize((220,220),Image.Resampling.LANCZOS)
      self.photoimg8=ImageTk.PhotoImage(img8)

      b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
      b1.place(x=200,y=380,width=220,height=220)

      b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="black",fg="red")
      b1_1.place(x=200,y=580,width=220,height=40)

# photo button

      img9=Image.open(r"coll_Images/Photos.jpg")
      img9=img9.resize((220,220),Image.Resampling.LANCZOS)
      self.photoimg9=ImageTk.PhotoImage(img9)

      b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
      b1.place(x=500,y=380,width=220,height=220)

      b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="black",fg="red")
      b1_1.place(x=500,y=580,width=220,height=40)


# developer
      img10=Image.open(r"coll_Images/developer.jpg")
      img10=img10.resize((220,220),Image.Resampling.LANCZOS)
      self.photoimg10=ImageTk.PhotoImage(img10)

      b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
      b1.place(x=800,y=380,width=220,height=220)

      b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="black",fg="red")
      b1_1.place(x=800,y=580,width=220,height=40)


      # exit
      img11=Image.open(r"coll_Images/exit.jpg")
      img11=img11.resize((220,220),Image.Resampling.LANCZOS)
      self.photoimg11=ImageTk.PhotoImage(img11)

      b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.exit)
      b1.place(x=1100,y=380,width=220,height=220)

      b1_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="black",fg="red")
      b1_1.place(x=1100,y=580,width=220,height=40)

    def open_img(self):
        os.startfile("data")

    def exit(self):
      self.exit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit",parent=self.root)
      if self.exit >0:
           self.root.destroy()
      else:
           return    
         


      # function butons
    def student_details(self):
         self.new_window=Toplevel(self.root)
         self.app=Student(self.new_window)

    def train_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Train(self.new_window)
      
    def face_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Face_Recognition(self.new_window)


    def attendance_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Attendance(self.new_window)   


    def help_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Helpsupport(self.new_window)    


    def developer_data(self):
         self.new_window=Toplevel(self.root)
         self.app=Developer(self.new_window)

    
    def open_img(self):
        os.startfile("data")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training data sets completed!!!")
    
  




if __name__ == "__main__":
    root=Tk()
    app=Login(root)
    root.mainloop()