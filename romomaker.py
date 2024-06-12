import pyttsx3
import os
engine = pyttsx3.init() #We initialize the text-to-speech engine using pyttsx3.init().
if __name__ == '__main__':
    print("Welcome to RoboSpeaker")
    while True:
        x = input("Enter what you want to speak: ")
        if x.lower() == "q":
            break
        engine.say(x)#If the user enters anything else, we use engine.say(x) to provide the text to the text-to-speech engine.
        engine.runAndWait()#We call engine.runAndWait() to wait for the text to be spoken before continuing the loop.
        #pip install pyttsx3