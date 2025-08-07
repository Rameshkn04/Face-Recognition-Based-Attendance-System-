from tkinter import*
from PIL import Image,ImageTk
import webbrowser
import time
from voiceChatbot import VoiceAssistantApp


class Helpsupport:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x780+0+0")
        self.root.title("Face_Recogonition_System")

# This part is image labels setting start 
        # first header image  
        img=Image.open(r"collapse_Images\banner1.jpg")
        img=img.resize((1530,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        # set image as lable
        f_lb1 = Label(self.root,image=self.photoimg)
        f_lb1.place(x=0,y=0,width=1530,height=130)

        # backgorund image 
        bg1=Image.open(r"collapse_Images\helpb1.webp")
        bg1=bg1.resize((1530,768),Image.LANCZOS)
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=130,width=1530,height=768)


        #title section
        title_lb1 = Label(bg_img,text="Help Support",font=("verdana",30,"bold"),bg="white",fg="navyblue")
        title_lb1.place(x=0,y=0,width=1530,height=45)

        # Create buttons below the section 
        # ------------------------------------------------------------------------------------------------------------------- 
        # student button 1
        std_img_btn2=Image.open(r"collapse_Images\web.png")
        std_img_btn2=std_img_btn2.resize((180,180),Image.LANCZOS)
        self.std_img2=ImageTk.PhotoImage(std_img_btn2)

        std_b2 = Button(bg_img,command=self.website,image=self.std_img2,cursor="hand2")
        std_b2.place(x=120,y=200,width=180,height=180)

        std_b1_2 = Button(bg_img,command=self.website,text="Website",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_2.place(x=120,y=380,width=180,height=45)

        # student button 2
        std_img_btn=Image.open(r"collapse_Images\instagram.jpg")
        std_img_btn=std_img_btn.resize((180,180),Image.LANCZOS)
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.instagram,image=self.std_img1,cursor="hand2")
        std_b1.place(x=350,y=200,width=180,height=180)

        std_b1_1 = Button(bg_img,command=self.instagram,text="Instagram",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        std_b1_1.place(x=350,y=380,width=180,height=45)

        # Detect Face  button 2
        det_img_btn=Image.open(r"collapse_Images\facebook.jpg")
        det_img_btn=det_img_btn.resize((180,180),Image.LANCZOS)
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.facebook,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=580,y=200,width=180,height=180)

        det_b1_1 = Button(bg_img,command=self.facebook,text="Facebook",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        det_b1_1.place(x=580,y=380,width=180,height=45)

         # Attendance System  button 3
        att_img_btn=Image.open(r"collapse_Images\youtube.png")
        att_img_btn=att_img_btn.resize((180,180),Image.LANCZOS)
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.youtube,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=810,y=200,width=180,height=180)

        att_b1_1 = Button(bg_img,command=self.youtube,text="Youtube",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        att_b1_1.place(x=810,y=380,width=180,height=45)

         # Help  Support  button 4
        hlp_img_btn=Image.open(r"collapse_Images\gmail.png")
        hlp_img_btn=hlp_img_btn.resize((180,180),Image.LANCZOS)
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img,command=self.gmail,image=self.hlp_img1,cursor="hand2",)
        hlp_b1.place(x=1040,y=200,width=180,height=180)

        hlp_b1_1 = Button(bg_img,command=self.gmail,text="Gmail",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        hlp_b1_1.place(x=1040,y=380,width=180,height=45)

        # Help  Support  button 4
        guidence_btn=Image.open(r"collapse_Images\iron man.jpg")
        guidence_btn=guidence_btn.resize((180,180),Image.LANCZOS)
        self.guidence1=ImageTk.PhotoImage(guidence_btn)

        guidence_b1 = Button(bg_img,command=self.voice,image=self.guidence1,cursor="hand2",)
        guidence_b1.place(x=1270,y=200,width=180,height=180)

        guidence_b1_1 = Button(bg_img,command=self.voice,text="Voice Chat boot",cursor="hand2",font=("tahoma",15,"bold"),bg="white",fg="navyblue")
        guidence_b1_1.place(x=1270,y=380,width=180,height=45)


        # create function for button 
    
    
    def website(self):
        self.new = 1
        self.url = "https://google.com/"
        webbrowser.open(self.url,new=self.new)

    def instagram(self):
        self.new = 1
        self.url = "https://instagram.com/"
        webbrowser.open(self.url,new=self.new)
    
    def facebook(self):
        self.new = 1
        self.url = "https://www.facebook.com/"
        webbrowser.open(self.url,new=self.new)
    
    def youtube(self):
        self.new = 1
        self.url = "https://www.youtube.com/channel/UCwpFCX_Z4SVkAT_6hPeUnsA"
        webbrowser.open(self.url,new=self.new)
    
    def gmail(self):
        self.new = 1
        self.url = "https://www.gmail.com"
        webbrowser.open(self.url,new=self.new)

    def voice(self):
        self.new_window = Toplevel(self.root)
        self.app = VoiceAssistantApp(self.new_window)

    




if __name__ == "__main__":
    root=Tk()
    obj=Helpsupport(root)
    root.mainloop()