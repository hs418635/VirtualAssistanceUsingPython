# step 3
# The TaskModule class is responsible for performing various tasks based on the user's voice commands.

from speech_module import SpeechModule
from task_module import TaskModule

if __name__ == "__main__": # __name__ is a built-in variable that returns the name of the current module.
    speech = SpeechModule()
    task = TaskModule(speech)

    speech.wish_me()
    input("Press any key to start my Chatbot...")

    while True:
        query = speech.take_command()

        if "search engine" in query:
            input("Press any key when you are ready to speak...")
            while True:
                query = speech.take_command()
                if query == "search engine exit":
                    break
                task.search_wikipedia(query)
        elif "open youtube" in query:
            task.open_website("youtube.com")
        elif "open google" in query:
            task.open_website("google.com")
        elif "play music" in query:
            task.play_music("D:\\M.TECH DATA SCIENCE\\My project\\Ai assistance\\AiAssistancePython")
        elif "the time" in query:
            task.tell_time()
        elif "open code" in query:
            task.open_code("D:\\Python_Class\\mycalci.py")
        elif "send email" in query:
            speech.speak("What should I say?")
            content = speech.take_command()
            task.send_email("hs864135@gmail.com", content)
        elif "exit" in query:
            break
