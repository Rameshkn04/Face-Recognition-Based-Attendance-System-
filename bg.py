import tkinter as tk
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
import threading

class VideoBackgroundApp:
    def __init__(self, root, video_source):
        self.root = root
        self.root.title("Video Background App")

        # Create a frame for the video
        self.video_frame = ttk.Frame(root)
        self.video_frame.pack(side=tk.LEFT, padx=10, pady=10)

        # Create a label to display the video
        self.video_label = ttk.Label(self.video_frame)
        self.video_label.pack()

        # Open the video source
        self.cap = cv2.VideoCapture(video_source)

        # Create a thread to update the video in the label
        self.thread = threading.Thread(target=self.update_video, daemon=True)
        self.thread.start()

    def update_video(self):
        while True:
            # Read a frame from the video source
            ret, frame = self.cap.read()

            if ret:
                # Convert the frame to RGB
                rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

                # Convert the frame to a PIL Image
                img = Image.fromarray(rgb_frame)

                # Convert the PIL Image to a PhotoImage
                img_tk = ImageTk.PhotoImage(image=img)

                # Update the label with the new image
                self.video_label.img = img_tk
                self.video_label.configure(image=img_tk)
                self.root.update()

    def run(self):
        self.root.mainloop()

# Create the Tkinter root window
root = tk.Tk()

# Specify the video source (provide the video file path)
video_source = r"C:\Users\Ramesh K N\OneDrive\Desktop\Face Recognition System\collapse_Images\CMRIT-Banner-Video-1.mp4"

# Create the VideoBackgroundApp instance
app = VideoBackgroundApp(root, video_source)

# Run the application
app.run()
