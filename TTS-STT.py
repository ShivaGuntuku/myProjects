import speech_recognition as sr
#module for Speech Reconition
import os
import datetime as dt 

import sys
from win32com.client import constants
import win32com.client 
#tts modules namespaces

r = sr.Recognizer()
m = sr.Microphone()
def Listener():
    try:
        print("A moment of silence, please...")
        with m as source:
            r.adjust_for_ambient_noise(source)
            print("Set minimum energy threshold to {}".format(r.energy_threshold))
            while True:
                print("Say something!")
                audio = r.listen(source)
                print("Got it! Now to recognize it...")
                try:
                    # recognize speech using Google Speech Recognition
                    value = r.recognize_google(audio)
                    return value
                    # we need some special handling here to correctly print unicode characters to standard output
                    """if str is bytes: # this version of Python uses bytes for strings (Python 2)
                        print(u"You said {}".format(value).encode("utf-8"))
                    else: # this version of Python uses unicode for strings (Python 3+)
                        print("You said {}".format(value))"""
                except LookupError:
                    print("Oops! Didn't catch that")
    except KeyboardInterrupt:
        pass


def speaker(voice):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    print ("Type word or phrase, then enter.")
    print ("Ctrl+Z then enter to exit.")
    for i in range(5):
        try:
            #s = raw_input()
            s=voice
            speaker.Speak(s)
        except:
            if sys.exc_type is EOFError:
                sys.exit()    
    
voice=Listener()
print(voice)
speaker(voice)
print("succeesss")