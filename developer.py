from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        img_top = Image.open(r"collapse_Images\developersbg.png")
        img_top = img_top.resize((1530,720),Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root,image = self.photoimg_top)
        f_lbl.place(x=0,y=55,width=1530,height=720)
        
        #Frame
        main_frame = Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=10,y=5,width=450,height=600)

        img_top1 = Image.open(r"collapse_Images\Rameshfr.jpg")
        img_top1 = img_top1.resize((145,200),Image.LANCZOS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl1 = Label(main_frame,image = self.photoimg_top1)
        f_lbl1.place(x=300,y=0,width=145,height=200)

        #Developer info
        dep_label = Label(main_frame,text="Hello Buddies...\n\n I am Ramesh KN\n\n From Chikmagalur\n\t\n Currently Studying \n\nBachelor of Engineering \n\n at  CMRIT College\n\n AIML Department",font=("times new roman",16,"bold"),fg="blue",bg="white")
        dep_label.place(x=0,y=5)

        #Frame2
        main_frame1 = Frame(f_lbl,bd=2,bg="white")
        main_frame1.place(x=540,y=5,width=450,height=600)

        img_top2 = Image.open(r"collapse_Images\shivanandfr.jpg")
        img_top2 = img_top2.resize((145,200),Image.LANCZOS)
        self.photoimg_top2 = ImageTk.PhotoImage(img_top2)

        f_lbl2 = Label(main_frame1,image = self.photoimg_top2)
        f_lbl2.place(x=300,y=0,width=145,height=200)

        #Developer info
        dep_label2 = Label(main_frame1,text="Hello Friends...\n\n I am Shivanand\n\n From Gokak\n\t\n Currently Studying \n\nBachelor of Engineering \n\n at  CMRIT College\n\n AIML Department",font=("times new roman",16,"bold"),fg="green",bg="white")
        dep_label2.place(x=0,y=5)

        #Frame3
        main_frame3 = Frame(f_lbl,bd=2,bg="white")
        main_frame3.place(x=1050,y=5,width=450,height=600)
        img_top3 = Image.open(r"collapse_Images\prajwalfr.jpg")
        img_top3 = img_top3.resize((145,200),Image.LANCZOS)
        self.photoimg_top3 = ImageTk.PhotoImage(img_top3)

        f_lbl2 = Label(main_frame3,image = self.photoimg_top3)
        f_lbl2.place(x=300,y=0,width=145,height=200)

        #Developer info
        dep_label3 = Label(main_frame3,text="Hello Guys...\n\n I am Prajwal B Gowda\n\n From Mysuru\n\t\n Currently Studying \n\nBachelor of Engineering \n\n at  CMRIT College\n\n AIML Department",font=("times new roman",16,"bold"),fg="purple",bg="white")
        dep_label3.place(x=0,y=5)






if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()