#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      gshiv
#
# Created:     30-01-2016
# Copyright:   (c) gshiv 2016
# Licence:     <your licence>
#for SpeechRecognition module: pip install SpeechRecognition
#Ex: C:\Python34\Scripts>pip install SpeechRecognition
#-------------------------------------------------------------------------------

import speech_recognition as sr
#module for Speech Reconition
import os
import datetime as dt
r = sr.Recognizer()
m = sr.Microphone()

def Notebook():
    destDir=r"Documents\Notebook"
    if not os.path.isdir(destDir):
        os.makedirs(destDir)
    fileName=dt.datetime.today().strftime("%m%d%Y")+".txt"
    Location="{0}{1}{2}".format(destDir,"\\",fileName)
    listItem=os.listdir(destDir)
    for fileName in listItem:
        write=os.open(Location,"rb")
        write.append()
    return "success"

def speaker():
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

voice=speaker()
print(voice)
if voice in ["Facebook","facebook"]:
        os.startfile("http://www.facebook.com")
elif voice in ["File Explorer","Explorer","File","file","fileexplorer"]:
        os.startfile("D:/")
elif voice=="Twitter":
        os.startfile("http://www.twitter.com")
elif voice in ["NoteBook","notebook","note book","noteBook","Notebook"]:
        print("opening notebook")
        Notebook()

###
