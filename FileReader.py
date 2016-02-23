import sys
from win32com.client import constants
import win32com.client
import requests
import PyPDF2

speaker = win32com.client.Dispatch("SAPI.SpVoice")

print("this program can read Text and PDF files only..")
fileType=raw_input("enter our file path along with filename:-->")

if fileType.endswith('.pdf'): 
    pdfFileObj = open(fileType, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pageNo=input("Enter your page No to start:--> ")
    
    for i in range(pageNo,pdfReader.numPages):
        pageObj = pdfReader.getPage(i)
        #print(pageObj.extractText())  
        speaker.Speak(pageObj.extractText())
    speaker.Speak("Reading the file completed")

else:
    Fo=open(fileType)
    for line in Fo.readlines():
    #print("speaking started")
    #print (line)
        speaker.Speak(line)
    speaker.Speak("Reading the file completed")