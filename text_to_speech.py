import sys
from win32com.client import constants
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
print ("Type word or phrase, then enter.")
print ("Ctrl+Z then enter to exit.")
while 1:
   try:
      s = raw_input()
      speaker.Speak(s)
   except:
      if sys.exc_type is EOFError:
         sys.exit()
