import tkinter as tk
from tkinter import Image, ttk
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import speech_recognition as sr
import pyttsx3
import datetime
import subprocess
import wikipedia
import pyjokes
import smtplib
import ssl
import requests
import threading
import webbrowser
from twilio.rest import Client

class VoiceAssistantApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Sweetie The Voice Assistant")
        self.master.geometry("1530x790+0+0")

        #bg Image
        img3 = Image.open(r"collapse_Images\jarvis02.jpg")
        img3 = img3.resize((1530,790),Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)


        bg_img = Label(self.master,image=self.photoimg3)
        bg_img.place(x=0,y=0,width=1530,height=790)

        title_lbl = Label(bg_img,text="WELCOME TO VOICE ASSISTANT",font=("times new roman",35,"bold"),bg="white",fg="darkgreen")
        title_lbl.place(x=0,y=0,width=1530,height=45)
    
        

        self.tabel_frame = Frame(self.master,bd=2,bg="white",relief=RIDGE)
        self.tabel_frame.place(x=200,y=200,width=1000,height=500)

        img4 = Image.open(r"collapse_Images\sweetie.jpg")
        img4 = img4.resize((1530,790),Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        bg_img = Label(self.tabel_frame,image=self.photoimg4)
        bg_img.place(x=0,y=0,width=1000,height=500)

        scroll_x = ttk.Scrollbar(self.tabel_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(self.tabel_frame,orient=VERTICAL)
        
        self.student_table = ttk.Treeview(self.tabel_frame,columns="",xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.output_label = Label(self.tabel_frame, text="Welcome to Voice Assistant!",font=("times new roman",15,"bold"),fg="darkgreen")
        self.output_label.pack(pady=10)

        self.user_input_label = Label(self.tabel_frame, text="",font=("times new roman",13,"bold"),fg="darkgreen")
        self.user_input_label.pack(pady=50)

        self.listen_button = Button(self.tabel_frame, text="Listen", command=self.listen_command,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        self.listen_button.pack()

        self.stop_button = Button(self.tabel_frame, text="Stop", command=self.stop_listening,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        self.stop_button.pack()
        self.stop_button.configure(state=tk.DISABLED)

        self.exit_button = Button(self.tabel_frame, text="Exit", command=self.exit_app,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        self.exit_button.pack()

        self.running = False

        # Initialize the speech engine
        self.engine = pyttsx3.init('sapi5')
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)

        # Initialize Twilio client
        self.twilio_client = Client('AC21271be6fd46c587ca1a4fff4045c9cb', 'c1abdba9bcee6ce4f41d716a25ae7f73')

        # Button to initiate call
        self.call_button = Button(self.tabel_frame, text="Make Call", command=self.make_phone_call, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        self.call_button.pack()

    def make_phone_call(self):
        to_number = '+91 9035903245'  # Replace with the number you want to call
        from_number = '+17632252704'  # Replace with your Twilio phone number

        try:
            call = self.twilio_client.calls.create(
                to=to_number,
                from_=from_number,
                url='http://demo.twilio.com/docs/voice.xml'  # URL for TwiML instructions
            )
            self.output_label.config(text="Call initiated successfully!")
            print("Call initiated successfully!")
        except Exception as e:
            self.output_label.config(text=f"Error making call: {e}")
            print(f"Error making call: {e}")

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def get_audio(self):
        r = sr.Recognizer() 
        audio = '' 
        with sr.Microphone() as source: 
            self.speak("Listening...") 
            audio = r.listen(source, phrase_time_limit=5)
        try: 
            text = r.recognize_google(audio, language='en-US') 
            self.user_input_label.config(text=f"You said: {text}")
            return text
        except sr.UnknownValueError:
            self.user_input_label.config(text="Sorry, I couldn't understand that.")
            return ""
        except sr.RequestError:
            self.user_input_label.config(text="Sorry, I couldn't access Google Speech Recognition.")
            return ""

    def process_audio(self):
        while self.running:
            query = self.get_audio()
            if query:
                query = query.lower()

                if "stop" in query:
                    self.speak("Goodbye!")
                    self.stop_listening()
                    return
                if "exit" in query:
                    self.speak("Goodbye!")
                    self.master.destroy()
                    return

                if "open word" in query:
                    subprocess.Popen(["C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"])
                    self.speak("Opening Microsoft Word")
                elif "hello sweetie" in query:
                    self.output_label.config(text="Hello What Can I do for You?")
                    self.speak("Hello What Can I do for You?")
                
                elif "what is your name" in query:
                    self.output_label.config(text="I am sweety your personal assistant")
                    self.speak("I am sweety your personal assistant")
                
                elif "tell me your history" in query:
                    self.output_label.config(text="Ya sure I was named by Developer Ramesh and his team in memory of Ramesh's cat, Sweetie, who tragically passed away in a dog attack and couldn't survive.")
                    self.speak("Ya sure I  was named by Developer Ramesh and his team in memory of Ramesh's cat, Sweetie, who tragically passed away in a dog attack and couldn't survive.")

                elif "give me developers details" in query:
                    self.output_label.config(text="Choose Developer : Say: Developer1 : RAMESH KN\n Developer2 : Shivanand Gopal \n Developer 3 : Prajwal B Gowda")
                    self.speak("Choose Developer : Say: Developer1 for RAMESH KN\n Developer2 for Shivanand Gopal \n Developer 3 for Prajwal B Gowda")   

                elif "developer 1" in query:
                    self.output_label.config(text="RAMESH KN\n Phone Number : 9035903245\n Branch : AIML \n Address : Bangalore")
                    self.speak("RAMESH KN\n Phone Number : 9035903245\n Branch : AIML \n Address : Bangalore")   

                elif "call Developer" in query:
                    self.output_label.config(text="Calling...")
                    self.speak("Calling...")
                    
                    # Make a phone call using Twilio
                    self.make_phone_call()
                
                elif "who are the developers of this project" in query:
                    self.output_label.config(text="The developers of these project are \n1.RAMESH KN\n 2.SHIVANAND GOPAL GUNDAPPAGOL\n 3.PRAJWAL B GOWDA\n")
                    self.speak("The developers of these project are \nRAMESH KN\n SHIVANAND GOPAL GUNDAPPAGOL\n PRAJWAL B GOWDA\n")

                elif "can you help me" in query:
                    self.output_label.config(text="Please follow the steps \nStep 1 : Fill the Student Details of student 1 with photo. \nStep 2: then train the photos. \nStep 3 : goto Face Regoniser. \nStep 4: goto attendance sheet Import csv file \nStep 5: you can  export it .\nstep 6 : Exit.\n Important Note : CSV file Should be open while marking attendance.\nThank you Any other Help..")
                    self.speak("Please follow the steps Step 1 : Fill the Student Details of student 1 with photo. Step 2: then train the photos. Step 3 : goto Face Regoniser. Step 4: goto attendance sheet Import csv file Step 5: you can export it step 6 : Exit.Important Note : CSV file Should be open while marking attendance..Thank you Any other Help..")

                elif "date" in query:
                    now = datetime.datetime.now()
                    self.output_label.config(text=f"Today is {now.strftime('%A, %B %d, %Y')}")
                    self.speak(f"Today is {now.strftime('%A, %B %d, %Y')}")
                elif "time" in query:
                    now = datetime.datetime.now()
                    self.output_label.config(text=f"The time is {now.strftime('%I:%M %p')}")
                    self.speak(f"The time is {now.strftime('%I:%M %p')}")
                elif "thank you" in query:
                    self.output_label.config(text="You're welcome!")
                    self.speak("You're welcome!")
                
                elif "search" in query:
                    search_query = query.replace("search", "").strip()
                    search_result = wikipedia.summary(search_query, sentences=2)
                    self.output_label.config(text=search_result)
                    self.speak(search_result)
                elif "joke" in query:
                    joke = pyjokes.get_joke()
                    self.output_label.config(text=joke)
                    self.speak(joke)
                
                elif "open google" in query:
                    webbrowser.open("https://www.google.com")
                    self.speak("Opening Google")
                elif "open youtube" in query:
                    webbrowser.open("https://www.youtube.com")
                    self.speak("Opening YouTube")
                elif "open instagram" in query:
                    webbrowser.open("https://www.instagram.com")
                    self.speak("Opening Instagram")
                elif "open facebook" in query:
                    webbrowser.open("https://www.facebook.com")
                    self.speak("Opening Facebook")
                else:
                    self.output_label.config(text="Sorry, I couldn't understand that.")
                    self.speak("Sorry, I couldn't understand that.")
                

    def listen_command(self):
        self.running = True
        self.listen_button.configure(state=tk.DISABLED)
        self.stop_button.configure(state=tk.NORMAL)
        threading.Thread(target=self.process_audio).start()

    def stop_listening(self):
        self.running = False
        self.listen_button.configure(state=tk.NORMAL)
        self.stop_button.configure(state=tk.DISABLED)
        self.speak("Goodbye!")

    


    def exit_app(self):
        self.running = False 
        self.master.destroy()




def main():
    root = tk.Tk()
    app = VoiceAssistantApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
    root = tk.Tk()
    app = VoiceAssistantApp(root)
    root.mainloop()