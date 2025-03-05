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

    # Open Code: It opens a code editor or file.
    def open_code(self, path):
        os.startfile(path)
    
    # Tell Time: It tells the current time.
    def tell_time(self):
        from datetime import datetime
        str_time = datetime.now().strftime("%H:%M:%S")
        self.speech_module.speak(f"Sir, the time is {str_time}")

    # Search Wikipedia: It searches for a query on Wikipedia and speaks a summary.
    def search_wikipedia(self, query):
        try:
            results = wikipedia.summary(query, sentences=2)
            self.speech_module.speak("According to Wikipedia, " + results)
            print(results)
        except Exception as e:
            print(e)
            self.speech_module.speak("Sorry, I could not fetch results from Wikipedia.")

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


if __name__ == "__main__":
    # Create a dummy speech module for testing purposes.
    class DummySpeechModule:
        def speak(self, text):
            print("Speak:", text)
    
    dummy_speech = DummySpeechModule()
    task = TaskModule(dummy_speech)
    
    # Test open_website (Be cautious: this will open a browser window)
    # print("Testing open_website:")
    # task.open_website("https://www.google.com")
    
    # Test open_code (Be cautious: this will attempt to open a file)
    # print("Testing open_code:")
    # task.open_code("D:\\Python_Class\\mycalci.py")
    
    # # Test tell_time
    # print("Testing tell_time:")
    # task.tell_time()
    
    # # Test search_wikipedia
    print("Testing search_wikipedia:")
    # task.search_wikipedia("Python programming")
    task.search_wikipedia("Virat Kohli")
    
    # Test play_music (Ensure the path exists and has valid music files)
    # print("Testing play_music:")
    # task.play_music("D:\\M.TECH DATA SCIENCE\\My project\\Ai assistance\\AiAssistancePython")
    
    # Test send_email (Make sure your .env is set up correctly and be careful sending emails)
    print("Testing send_email:")
    # task.send_email("example@example.com", "This is a test email.")

