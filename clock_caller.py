import pyttsx3
from datetime import datetime as dt
import time
import speech_recognition as sr
import sys
import os
import re

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#voice_id_Brian22 = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
engine.setProperty('voice', voices[0].id)
times = dt.now().time().strftime("%I:%M %p")
day = dt.today().strftime("%A %d %B")
year = dt.today().year
# engine.say('Hello Master, I am, Miss Minute in your service. Now it is ' + time + str(day) + str(year))
engine.runAndWait()


def speak(audio):
    engine.say(audio)
    print("Miss Minute : " + audio)
    engine.runAndWait()


def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 2
        audio = r.listen(source, timeout=None, phrase_time_limit=3.5)
    try:
        print("Recognising.....")
        print("You : " + r.recognize_google(audio, language='en-in'))
        return (r.recognize_google(audio)).lower()
    except sr.UnknownValueError:
        speak("Unable to catch!")
        return 'None'


def greeting():
    hour = dt.now().hour
    times = dt.now().time().strftime("%I:%M %p")
    if hour >= 0 and hour <= 12:
        wish = "Good Morning Master! I am, Ron in your service."
    elif hour > 12 and hour <= 18:
        wish = "Good afternoon Master! How can I help you?"
    else:
        wish = "Good evening Master! How can I help you?"
    speak(wish + " It's " + day + " today, and current time is " + times)


def tell_time():
    times = dt.now().time().strftime("%I:%M %p")
    speak("Current time is " + times)


def warn():
    speak("Seems liken no more command for me. Shall I got to sleep now")
    speechs = command()
    if ("yes" in speechs) or ("sure" in speechs) or ("yep" in speechs) or ("indeed" in speechs) or ("why not" in speechs) or ("go" in speechs) or ("yeah" in speechs):
        speak("Okay, In case you need anything, just say wake-up and I am ready at your service sir")
        os.system('E:/Minor/project/clock_bg.py')
        return True
    else:
        speak("seems you don't allow me to sleep. So how may I help you sir now?")
