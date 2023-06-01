#Scheduler used for repeting the same things in a given time

import schedule
import time
import pyttsx3
import os

engine = pyttsx3.init()

def say_good_morning():
    engine.say("vivvek vivvek vivvek")
    print("dw")
    engine.runAndWait()

# schedule saying "Good morning" every 5 minutes
schedule.every(1).seconds.do(say_good_morning)

while True:
    schedule.run_pending()
    time.sleep(1)
    print("fir se suruu kroo")



