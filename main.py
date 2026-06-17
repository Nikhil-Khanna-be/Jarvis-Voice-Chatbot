import speech_recognition as sr
import webbrowser
import pyttsx3
import MusicLibrary
import requests
import asyncio
import edge_tts
import tempfile
import os
from playsound import playsound

recognizer=sr.Recognizer()
engine=pyttsx3.init()
newsapi="32c09af009434b48ab471a00e14d3cf2"

def speak_old(text):
    engine.stop()
    engine.say(text)
    engine.runAndWait()

def speak(text):
    async def _speak():
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
            temp_file = fp.name

        communicate = edge_tts.Communicate(
            text=text,
            voice="en-US-AriaNeural"
        )

        await communicate.save(temp_file)

        playsound(temp_file)

        os.remove(temp_file)

    asyncio.run(_speak())



def processCommand(c):
    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        speak("Opening Facebook")
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        speak("Opening Youtube")
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        speak("Opening LinkedIn")
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=MusicLibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r=requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if(r.status_code==200):
            data=r.json()
            articles=data.get("articles",[])
            for article in articles:
                speak(article["title"])






if __name__=="__main__":
    speak("Initializing Jarvis....")
    
    
    while True:
        # obtain audio from the microphone
        print("Recognizing...")
        # recognize speech using Sphinx
        try:
            with sr.Microphone() as source:
                print("Listening")
                
                audio = recognizer.listen(source,timeout=1,phrase_time_limit=1)
            word=recognizer.recognize_google(audio)
            if "jarvis" in word.lower():
                print("Jarvis Active...")
                speak("Yes")
                
                with sr.Microphone() as source:
                    audio = recognizer.listen(source)
                    command=recognizer.recognize_google(audio)
                    print(command)

                    processCommand(command)
        except Exception as e:
            print("Error")
