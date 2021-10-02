import pyttsx3
from datetime import datetime as dt
import time
import speech_recognition as sr
import re
from clock_caller import *


def set_reminder():
    speak("What's the reminder?")
    rem = command()
    speak("OK "+rem+" When do you want to be reminded ?")
    rem_time = command()
    if "after" in rem_time or "hours" in rem_time:
        speak("Ok. I remind you " + rem_time)
        n = re.findall('\d+', rem_time)
        time.sleep(int(10))
        speak('Its time to ' + rem)
