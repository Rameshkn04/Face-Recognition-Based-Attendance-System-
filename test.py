import cv2

# Load the pre-trained Haar Cascade face classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open a video capture object (0 corresponds to the default camera, you can replace it with a video file path)
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the video capture
    ret, frame = cap.read()

    # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Display the result
    cv2.imshow('Detected Faces', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the window
cap.release()
cv2.destroyAllWindows()





#===========================================2======
vedio = cv2.VideoCapture(0)
    face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
                
                id = 0
                count = 0

                while True:
                     ret,my_frame = vedio.read()
                     gray = cv2.cvtColor(my_frame,cv2.COLOR_BGR2GRAY)
                     faces = face_classifier.detectMultiScale(gray,1.3,5)
                     for (x,y,w,h) in faces:
                          id +=1
                          count += 1
                          cv2.imwrite('data/user.'+str(id)+"."+str(count)+".jpg",gray[y:y+h,x:x+w])
                          cv2.rectangle(my_frame,(x,y),(x+w,y+h),(50,50,255),1)
                     cv2.imshow("Frame",my_frame)

                     k=cv2.waitKey(1)

                     if count>=100:
                          break
                vedio.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Successfully captured")


#=======================================
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Face_Recognition:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        
        #first
        img_top = Image.open(r"collapse_Images\m03.jpeg")
        img_top = img_top.resize((650,700),Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image = self.photoimg_top)
        f_lbl.place(x=0,y=55,width=650,height=700)

        #second
        img_bottom = Image.open(r"collapse_Images\m03.jpeg")
        img_bottom = img_bottom.resize((950,700),Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root,image = self.photoimg_bottom)
        f_lbl.place(x=650,y=55,width=950,height=700)
        
         # button
        b1_1 = Button(f_lbl,text="Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",18,"bold"),bg="dark green",fg="white")
        b1_1.place(x=365,y=620,width=200,height=40)

        #==================Face recognition
    def face_recog(self):
        def draw_boundray(img,classifier,scaleFactor,minNeighbour,color,text,clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BAYER_BG2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbour)

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+h])
                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost",username="root",password="Ramu@2004",database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from student where Student_id=%s"+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Roll from student where Student_id=%s"+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Dep from student where Student_id=%s"+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                if confidence>77:
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                coord=[x,y,w,h]
            return coord
        
        def recognize(img,clf,faceCascade):
            coord = draw_boundray(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret,img = video_cap.read()
            img = recognize(img,clf,faceCascade)
            cv2.imshow("Welcome To face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()




if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()


    #===========================
    face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                     gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                     faces = face_classifier.detectMultiScale(gray,1.3,5)
                     #scaling factor = 1.3
                     #Mininmum Neighbour = 5

                     for(x,y,w,h) in faces:
                          face_cropped = img[y:y+h,x:x+w]
                          return face_cropped
                     cap = cv2.VideoCapture(0)
                     img_id = 0
                     while True:
                          ret,my_frame=cap.read()
                          if face_cropped(my_frame) is not None :
                              img_id += 1
                              face = cv2.resize(face_cropped(my_frame),(450,450))
                              face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                              file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                              cv2.imwrite(file_name_path,face)
                              cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                              cv2.imshow("Cropped Face",face)

                          if cv2.waitKey(1)==13 or int(img_id)==100:
                               break
                     cap.release()
                     cv2.destroyAllWindows()
                     
                     messagebox.showinfo("Result","Generating data sets completed!!!!")


        ############################
                     face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                     gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                     faces = face_classifier.detectMultiScale(gray,1.3,5)
                     #scaling factor = 1.3
                     #Mininmum Neighbour = 5

                     for(x,y,w,h) in faces:
                          face_cropped = img[y:y+h,x:x+w]
                          return face_cropped
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None :
                         img_id += 1
                         face = cv2.resize(face_cropped(my_frame),(450,450))
                         face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                         file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                         cv2.imwrite(file_name_path,face)
                         cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                         cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                         break
                    cap.release()
                    cv2.destroyAllWindows()
                     
                    messagebox.showinfo("Result","Generating data sets completed!!!!")


                    #===============xxxxxxxxxxxxxxxxxxx=
                my_cursor.execute("select Name from student where Student_id=%s"+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Roll from student where Student_id=%s"+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Dep from student where Student_id=%s"+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("select Student_id from student where Student_id=%s"+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)
    

#------------------------new-----------------
    vedio = cv2.VideoCapture(0)
                face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

                faces_data = []

                img_id = 0
                count = 0

                while True:
                     ret,my_frame = vedio.read()
                     gray = cv2.cvtColor(my_frame,cv2.COLOR_BGR2GRAY)
                     faces = face_classifier.detectMultiScale(gray,1.3,5)
                     for (x,y,w,h) in faces:
                          crop_img = my_frame[y:y+h, x:x+h]
                          resized_img = cv2.resize(crop_img,(50,50))
                          if len(faces_data)<=100 and img_id%10==0:
                               faces_data.append(resized_img)
                          img_id +=1
                          count += 1
                          cv2.putText(my_frame,str(len(faces_data)),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(50,50,255),2)
                          cv2.imwrite('data/user.'+str(id)+"."+str(img_id)+".jpg",gray[y:y+h,x:x+w])
                          cv2.rectangle(my_frame,(x,y),(x+w,y+h),(50,50,255),1)
                     cv2.imshow("Frame",my_frame)

                     k=cv2.waitKey(1)==13

                     if img_id==100:
                          break
                vedio.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completed!!!!")