# step2 - Task Module
# Author- Himanshu Suryavanshi
# It uses the wikipedia library to search for information on Wikipedia, the webbrowser library to open websites, the os library to play music and open files, and the smtplib library to send emails.


import wikipedia
import webbrowser
import os
import smtplib
import random
from dotenv import load_dotenv # pip install python-dotenv


# Load environment variables from .env
load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

#  The TaskModule class has methods to perform the following tasks:
class TaskModule:
    def __init__(self, speech_module):
        self.speech_module = speech_module

    # Open Website: It opens a website in the default web browser.
    def open_website(self, site):
        webbrowser.open(site)

    def play_music(self, music_dir):
        if os.path.exists(music_dir):
            songs = [file for file in os.listdir(music_dir) if file.endswith(('.mp3', '.wav'))]
            if songs:
                song_to_play = random.choice(songs)  # Randomly select a song
                os.startfile(os.path.join(music_dir, song_to_play))
            else:
                print("No music files found in the directory.")
        else:
            print("Music directory does not exist.")

    # Tell Time: It tells the current time.
    def tell_time(self):
        from datetime import datetime
        str_time = datetime.now().strftime("%H:%M:%S")
        self.speech_module.speak(f"Sir, the time is {str_time}")

    # Open Code: It opens a code editor or file.
    def open_code(self, path):
        os.startfile(path)

    # Send Email: It sends an email using the smtplib library.
    def send_email(self, to, content):
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo() # Extended Hello is a command sent by an email server to identify itself when connecting to another email server
            server.starttls() # Start Transport Layer Security is a cryptographic protocol that provides security over a computer network
            server.login(EMAIL_USER, EMAIL_PASS)
            server.sendmail(EMAIL_USER, to, content)
            server.quit()
            self.speech_module.speak("Email has been sent!")
        except Exception as e:
            print(e)
            self.speech_module.speak("Sorry, I am not able to send this email.")
