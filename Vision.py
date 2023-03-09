from asyncio import subprocess
from csv import excel
from http.client import responses
from urllib import response
import chatgpt
import datetime
from distutils import command
from fileinput import close
from multiprocessing.connection import wait
import os
from random import random
from socket import socket
from telnetlib import IP
import pytz
import time
from numpy import size
import cv2
import pyautogui
import pyttsx3
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import speech_recognition as sr
import smtplib
import sys
from PyQt5 import QtWidgets , QtCore ,QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from  PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from VisionGui import Ui_VisionGui


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
engine.setProperty('rate',150)



def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()





def wish():
    hour = int(datetime.datetime.now().hour)

  # if hour>=6 and hour<=12:
  #      speak("Good Morning")
 #   elif hour>12 and hour<16:
  #      speak("Good Afternoon")
  # else:
    #    speak("Good Evening")
    speak("This is Vision,How can I help you")






class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.TaskExecution()

    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User Said: {query}")

        except Exception as e:
            return "none"
        query = query.lower()
        return query

            




    def TaskExecution(self):
        wish()
        while 1:
            self.query = self.takecommand()


            def text():
                text = self.query.replace('type', '')
                pyautogui.typewrite(text)

 


            def new_page():
                pyautogui.keyDown("ctrl")
                pyautogui.press("N")
                pyautogui.keyUp("ctrl")

            if "notepad" in self.query:
                os.system("start notepad.exe")
                time.sleep(1)
                if "type" in self.query:
                    text()

            
            elif "this PC" in self.query:
                npath = "C:\\Windows\\system32\\filemanager.exe"
                os.startfile(npath)
                time.sleep(5)

            elif "excel" in self.query:
                npath = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel"
                os.startfile(npath)
                time.sleep(4)
                if "new" in self.query:
                    new_page()



            elif "word" in self.query:
                npath = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word"
                os.startfile(npath)
                time.sleep(4)
                if "new" in self.query:
                    new_page()
                time.sleep(5)

            elif "powerPoint" in self.query:
                npath = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint"
                os.startfile(npath)
                time.sleep(4)
                if "new" in self.query:
                    new_page()
                time.sleep(5)

            elif "microsoft edge" in self.query:
                npath = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Edge"
                os.startfile(npath)
                time.sleep(5)

            elif "chrome" in self.query:
                npath = r"C:\Program Files (x86)\Google\Chrome\Application\Chrome.exe"
                os.system("npath")
                time.sleep(5)
            
            
            elif "command prompt" in self.query:
                os.system("start cmd.exe")
                time.sleep(5)

            
            elif "camera" in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, im =cap.read()
                    cv2.imshow('webcam',im)
                    k = cv2.waitKey(10)
                    if k==3:
                        break
                cap.release()
                cv2.destroyAllWindows()
                time.sleep(5)
                   
            
            elif 'ip address' in self.query:
               # hostname= socket.gethostname()
                ip = get("https://api64.ipify.org").text  #socket.gethostbyname(hostname)
                speak(f"Your IP Adress is "+ip)
                time.sleep(5)


            
            elif "wikipedia" in self.query:
                speak('Searching wikipedia...')
                query = self.query.replace("wikipedia" , '')
                result = wikipedia.summary(query, sentences=2)
                speak("Accorging to wikidepia")
                speak(result)
                time.sleep(5)

            elif 'open' and 'web' in self.query:
                web = self.query.replace('open'and'on'and'web'and' ','')
                link = f'https://{web}.com'
                webbrowser.open(link)
                time.sleep(5)

            elif  'play online' in self.query:
                query = self.query.replace('play online', '')
                kit.playonyt(query)
                time.sleep(20)
            
            elif 'play songs' in self.query:
                song = self.query.replace('play', '')
                speak('playing ' + song)
                kit.playonyt(song)
                time.sleep(20)

            elif "switch the window" in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")
                time.sleep(5)

            elif 'what is the date' in self.query:
               # date = self.query.replace('date','')
                today = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
                speak('Todays Date is')
                speak(today)

            
            elif "take a screenshot" in self.query:
                time.sleep(3)
                img=pyautogui.screenshot()
                random = random.random()
                img.save(F"{random}.png")
                speak("i am done sir, the screenshot is saved in our main folder. now i am ready for next task")

            elif " shutdown the system" in self.query:
                os.system("shutdown /s /t 1")

            
            elif " restart the system" in self.query:
                os.system("shutdown /r /t 1")

            
            elif " sleep the system " in self.query:
                os.system("rund1l32.exe powrprof.dil,SetSusoendState 0,1,0")



            elif "type" in self.query:
                text = self.query.replace('type', '')
                pyautogui.typewrite(text)
                speak('Any Thing else You want to type')
                self.takecommand()
                if "no" in self.query:
                   break
                


            elif 'thank you' in self.query:
                speak('Thank Your for Using Sir, Have a Great Day')
                pyautogui.keyDown("alt")
                pyautogui.press("F4")
                time.sleep(.5)
                pyautogui.keyUp("alt")
                sys.exit()

            else:
               chatgpt_api = chatGPT(secret_token)
               resp = chatgpt_api.send_message(self.query)
               out_result = resp('message')
               wait

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_VisionGui()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.pushButton.hide()
        self.ui.label_2.hide()
        self.ui.movie = QtGui.QMovie("C:\Vision\Media\Run1.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        startExecution.start()


app = QApplication(sys.argv)
Vision = Main()
Vision.show()
exit(app.exec_())

