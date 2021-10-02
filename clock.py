import sys
import os
from timer import *
from reminder_clock import *
from clock_caller import *

greeting()


i = 0

if __name__ == "__main__":
    def clear(): return os.system('cls')
    clear()
    while True:

        if i >= 2:
            i = 0
            des = warn()
            if des:
                sys.exit()
        else:
            speech = command().lower()
            if speech == 'none':
                i += 1
            else:
                def clear(): return os.system('cls')
                clear()
                i = 0
                if "hi" in speech or "hai" in speech or "hay" in speech or "hello" in speech or "whatsapp" in speech or "how are you" in speech:
                    greeting()

                elif "bye" in speech or "goodbye" in speech:
                    speak("Have a great day! Good Bye!")
                    # os.system('pythonw bg.py')
                    sys.exit()

                elif "tell time" in speech or "what is time" in speech or "time now" in speech or "clock" in speech:
                    tell_time()

                elif "set reminder" in speech or "set a reminder" in speech or "set reminders" in speech or "new reminder" in speech:
                    set_reminder()

                elif "set timer" in speech or "start timer" in speech or "start countdown" in speech or "set countdown" in speech or "new timer" in speech or "new countdown" in speech:
                    set_timer()
                elif "sleep" in speech:
                    os.system('E:/Minor/project/clock_bg.py')

                else:
                    speak(
                        "Sorry, Unable to recognise your command now, As I am still learning.")
