import pyttsx3
import speech_recognition as sr
import datetime
import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("hello sir good Morning!")
    
    elif hour>=12 and hour<18:
        speak("hello sir good Afternoom!")
    
    else:
        speak("hello sir good evening")


if __name__=="__main__":
    wishMe()