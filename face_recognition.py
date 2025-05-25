from tkinter import *
from register import *
from PIL import Image, ImageTk
from tkinter import messagebox
# import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np
import threading
import psycopg2

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("face.ico")

        # Title
        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"), bg="black", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Image
        img_top = Image.open(r"coll_Images/r1.jpg")
        img_top = img_top.resize((1530, 725), Image.Resampling.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=55, width=1530, height=725)

        # Recognize Button
        b1_1 = Button(f_lbl, text="Recognise", cursor="hand2", command=self.face_recog, font=("times new roman", 15, "bold"), bg="black", fg="red")
        b1_1.place(x=550, y=680, width=430, height=40)

    def mark_attendance(self, i, r, n, d):
        try:
            with open("attendance.csv", "r+", newline="\n") as f:
                myDataList = f.readlines()
                name_list = [entry.split(",")[0] for entry in myDataList]
                
                if i not in name_list and r not in name_list and n not in name_list and d not in name_list:
                    now = datetime.now()
                    d1 = now.strftime("%d/%m/%Y")
                    dtString = now.strftime("%H:%M:%S")
                    f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to mark attendance: {str(e)}")
            def face_recog(self):

                def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
                    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)
                    coord = []

                    for (x, y, w, h) in features:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                        id, predict = clf.predict(gray_image[y:y + h, x:x + w])
                        confidence = int((100 * (1 - predict / 300)))

                        try:
                            conn = psycopg2.connect(
                                host="localhost",
                                port="5432",
                                user="postgres",
                                password="123",
                                dbname="face_recogniser"
                            )
                            my_cursor = conn.cursor()
                            
                            # Fetch student details based on ID
                            my_cursor.execute("SELECT Name FROM student WHERE Student_id = %s", (str(id),))
                            n = my_cursor.fetchone()
                            n = "+".join(n) if n else "Unknown"
                            
                            my_cursor.execute("SELECT Roll FROM student WHERE Student_id = %s", (str(id),))
                            r = my_cursor.fetchone()
                            r = "+".join(r) if r else "Unknown"
                            
                            my_cursor.execute("SELECT Dep FROM student WHERE Student_id = %s", (str(id),))
                            d = my_cursor.fetchone()
                            d = "+".join(d) if d else "Unknown"
                            
                            my_cursor.execute("SELECT Student_id FROM student WHERE Student_id = %s", (str(id),))
                            i = my_cursor.fetchone()
                            i = "+".join(i) if i else "Unknown"

                            if confidence > 70:
                                cv2.putText(img, f"Student_id:{i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                                cv2.putText(img, f"Roll:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                                cv2.putText(img, f"Name:{n}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                                cv2.putText(img, f"Department:{d}", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                                self.mark_attendance(i, r, n, d)
                            else:
                                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                                cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                            my_cursor.close()
                            conn.close()

                        except psycopg2.Error as e:
                            messagebox.showerror("Database Error", f"Failed to connect to database: {str(e)}")

                        coord = [x, y, w, h]

                    return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
            return img

        # Load face cascade and the trained classifier
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()

        # Check if the classifier file exists
        if not os.path.exists("classifier.xml"):
            messagebox.showerror("Error", "Training file not found!")
            return

        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        if not video_cap.isOpened():
            messagebox.showerror("Error", "Unable to access the camera.")
            return

        def capture_video():
            while True:
                ret, img = video_cap.read()
                if not ret:
                    break
                img = recognize(img, clf, faceCascade)
                cv2.imshow("Face Recognition", img)

                if cv2.waitKey(1) == 13:  # Enter key to break
                    break

            video_cap.release()
            cv2.destroyAllWindows()

        # Run face recognition in a separate thread to avoid freezing the GUI
        threading.Thread(target=capture_video, daemon=True).start()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
