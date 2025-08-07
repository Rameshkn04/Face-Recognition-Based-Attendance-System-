# 🧠 Face Recognition Based Attendance System

An AI-powered desktop application that automates attendance marking using real-time face recognition. The system captures, identifies, and records attendance through a webcam feed, ensuring accuracy, speed, and contactless operation — ideal for schools, colleges, and workplaces.

---

## 📌 Features

- 🎥 Real-time face detection and recognition
- 👤 Student profile management with MySQL database
- 🗂 Attendance record logging with date & time
- 🔐 Admin login system
- 📢 Integrated voice assistant using `speech_recognition` & `pyttsx3`
- 💬 Fun chatbot features: Wikipedia search, programming jokes (`pyjokes`)
- 📲 SMS alerts via Twilio (optional)
- 📊 GUI interface using Tkinter

---

## 🛠 Tech Stack

| Component        | Technology                                     |
|------------------|------------------------------------------------|
| **Language**     | Python                                         |
| **Frontend**     | Tkinter (Python GUI)                           |
| **Backend**      | OpenCV, MySQL                                  |
| **Libraries**    | `opencv-python`, `face-recognition`, `Pillow`, `pyttsx3`, `speech_recognition`, `mysql-connector-python`, `pyjokes`, `wikipedia`, `twilio` |
| **Database**     | MySQL                                          |
| **Others**       | Twilio API (optional), `.env` or `config.py` for secrets |

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.8 – 3.11 (Recommended — some libraries may not work on 3.13)
- MySQL server installed
- Webcam connected
- Twilio account (optional for SMS alerts)
---
## 🚀 Installation Steps

### 1. 📥 Clone the Repository

```bash 
git clone https://github.com/Rameshkn04/Face-Recognition-Based-Attendance-System-.git
cd Face-Recognition-Based-Attendance-System-
```
---


### 2. 📦 Install Python Dependencies

Make sure you're in the project directory, then run:

```bash
pip install -r requirements.txt
```
### 3. 🛠️ Set Up MySQL Database

1. Open **phpMyAdmin** or any MySQL client.
2. Create a new database (e.g., `attendance_db`).
3. Import the provided `.sql` file (if available), or create tables manually based on your project files (e.g., `student.py`).

### 4. 🔐 Configure Credentials

Create a `config.py` file in the root directory of your project and add your credentials:

```python
# config.py

TWILIO_SID = "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
TWILIO_TOKEN = "your_twilio_auth_token"

DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "your_mysql_password"
DB_NAME = "attendance_db"
```
---

### 5. 🖥️ Run the Application

Launch the application using the following command:

```bash
python main.py
```
If you're using a specific Python version or full path, use:
```bash
C:/Users/your_username/AppData/Local/Programs/Python/Python311/python.exe main.py
```
6. ⏹️ Closing the Terminal or Stopping a Script
To stop a running Python script, press:

```bash
Ctrl + C
```
To exit the terminal session, type:
```bash
exit
```
If you're using VS Code, click the 🗑️ (trash icon) in the terminal tab to close it.

📄 requirements.txt (Example)
```text
Copy
Edit
opencv-python
face-recognition
Pillow
pyttsx3
SpeechRecognition
mysql-connector-python
pyjokes
wikipedia
twilio
```
Install dependencies:
```bash
pip install -r requirements.txt
```
## 👨‍💻 Author

**Ramesh K N**  
🎓 B.E. in AI & ML, CMR Institute of Technology  
🔗 [LinkedIn](https://www.linkedin.com/in/ramesh-kn)  
💻 [GitHub](https://github.com/Rameshkn04)

