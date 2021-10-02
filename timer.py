import pyttsx3
from datetime import datetime as dt
import time
import speech_recognition as sr
import re
from clock_caller import *
import winsound


def set_timer():
    while (True):
        def clear(): return os.system('cls')
        clear()
        speak("For how long?")
        timer = command()
        if 'minute' in timer or 'min' in timer or 'minut' in timer or 'minutes' in timer or 'a minute' in timer or 'a min' in timer or 'a minut' in timer or 'a minutes' in timer:
            speak("Alright " + timer + " starting...now.")

            if timer[0] == 'a':
                n = '1'
            else:
                n = re.findall('\d+', timer)
            s = int(n[0])*60
            time.sleep(s)
            freq = 100
            dur = 50
            for i in range(0, 5):
                winsound.Beep(freq, dur)
                freq += 100
                dur += 50
            speak("TIME'S UP!!!...TIME'S UP...")

            def clear(): return os.system('cls')
            clear()
            break

        elif 'hours' in timer or 'hour' in timer or 'ours' in timer or 'our' in timer or 'an hours' in timer or 'an hour' in timer or 'an ours' in timer or 'an our' in timer:

            speak("Alright " + timer + " starting...now.")
            if timer[0] == 'a':
                n = '1'
            else:
                n = re.findall('\d+', timer)
            s = int(n[0])*60*60
            time.sleep(s)
            speak("TIME'S UP!!!...TIME'S UP...")
            def clear(): return os.system('cls')
            clear()
            break

        elif 'second' in timer or 'seconds' in timer or 'sec' in timer or 'a second' in timer or 'a seconds' in timer or 'a sec' in timer:
            speak("Alright " + timer + " starting...now.")
            if timer[0] == 'a':
                n = '1'
            else:
                n = re.findall('\d+', timer)
            s = int(n[0])
            time.sleep(s)
            speak("TIME'S UP!!!...TIME'S UP...")
            def clear(): return os.system('cls')
            clear()
            break

        else:
            continue
