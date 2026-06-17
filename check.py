import pyttsx3
import time
engine=pyttsx3.init()

engine.say("Hello Master")
engine.runAndWait()
time.sleep(2)
engine.say("How are you")
engine.runAndWait()


