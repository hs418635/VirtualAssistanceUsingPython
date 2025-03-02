# step 1
# This module is responsible for speech recognition and speech synthesis.
# It also uses the datetime module to get the current time.

import pyttsx3 # text to speech conversion library
import speech_recognition as sr # speech recognition library
import datetime

engine = pyttsx3.init()

# The SpeechModule class has three methods:
class SpeechModule:

    # The __init__ method initializes the pyttsx3 engine and sets the voice property.
    def __init__(self):
        self.engine = pyttsx3.init('sapi5')
        voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', voices[0].id)

    # The speak method takes an audio string as input and speaks it using the pyttsx3 engine.
    def speak(self, audio):
        self.engine.say(audio)
        self.engine.runAndWait()

    # The wish_me method wishes the user based on the current time and introduces the assistant.
    def wish_me(self):
        hour = int(datetime.datetime.now().hour)
        if 0 <= hour <= 12:
            greeting = "Good Morning!"
        elif 12 < hour < 18:
            greeting = "Good Afternoon!"
        else:
            greeting = "Good Evening!"
        print(greeting)
        self.speak(greeting)
        self.speak("I am your personal assistant. Please tell me how may I help you.")

    # The take_command method listens to the user's voice input using the microphone and returns the recognized text.
    def take_command(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.record(source, duration=4)
        # If the recognition fails, it returns "None".
        try:
            print("Recognizing...")
            query = recognizer.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            return query.lower()
        except Exception:
            print("Say that again please...")
            return "None"
