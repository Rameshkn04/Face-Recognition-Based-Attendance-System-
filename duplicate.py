import tkinter as tk
from tkinter import ttk
import speech_recognition as sr
import openai
import webbrowser

# Set your OpenAI API key here
openai.api_key = 'YOUR_OPENAI_API_KEY'

class SweetyAssistant:
    def __init__(self, root):
        self.root = root
        self.root.title("Sweety - Your Voice Assistant")

        self.label = ttk.Label(root, text="Say a command:")
        self.label.pack(pady=10)

        self.entry = ttk.Entry(root, width=40)
        self.entry.pack(pady=10)

        self.button = ttk.Button(root, text="Speak", command=self.process_command)
        self.button.pack(pady=10)

    def process_command(self):
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            print("Listening...")
            audio_data = recognizer.listen(source)
            print("Processing...")

        try:
            command = recognizer.recognize_google(audio_data).lower()
            print("You said:", command)
            self.entry.delete(0, tk.END)
            self.entry.insert(0, command)
            self.execute_command(command)
        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")

    def execute_command(self, command):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=command,
            max_tokens=100
        )

        result = response.choices[0].text.strip()
        print("Response:", result)

        # You can add more actions based on the command
        if "open youtube" in result:
            # Implement code to open YouTube
            webbrowser.open("https://www.youtube.com")
            print("Opening YouTube...")
        elif "open google" in result:
            # Implement code to open Google
            webbrowser.open("https://www.google.com")
            print("Opening Google...")
        # Add more commands as needed

if __name__ == "__main__":
    root = tk.Tk()
    sweety = SweetyAssistant(root)
    root.mainloop()
