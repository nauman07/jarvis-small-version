import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
from selenium import webdriver
import os
#import pyautogui
import psutil
import pyjokes

engine=pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

    
def time():
    
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date= int(datetime.datetime.now().day)
    speak("the current date is")
    speak(date)
    speak(month)
    speak(year)
#speak("Hello Mister Nauman I am Jarvis the date is")
#date()
#speak("And the time is")
#time()
def wishme():
    speak("Welcome Back sir!")
    
    time()
  
    date()
    hour = datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("Good Morning Sir!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")
    elif hour>=18 and hour<24:
        speak("Good Evening Sir!")
    else:
        speak("Good night sir")
    speak("Jarvis At your service please tell me how can  I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio=r.listen(source)

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en_in')
        print(query)
    except Exception as e:
        print(e)
        speak("say again....")
        return "None"
    return query
def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login('Naumanurrahman@gmail.com','Nauman123')
    server.sendmail('Naumanurrahman@gmail.com',to,content)
    server.close()

#def screenshot():
#    img = pyautogui.screenshot()
#    img.save('ss.png')

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+usage+'percent')
def battery():
    battery=psutil.sensors_battery()
    speak("sir we have ")
    speak(battery.percent)
    speak(" percent energy")

def jokes():
    speak(pyjokes.get_joke())
    speak("ha  hah hah hah")

if __name__=="__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'wikipedia' in query:
            try:
                speak("Searching....")
                query =query.replace("wikipedia","")
                result = wikipedia.summary(query,sentences=4)
                print(result)
                speak(result)
            except Exception as e:
                speak("please properly speak")
        elif 'send email' in query:
            try:
                speak("What should I write")
                content = takeCommand()
                print(content)
                #speak ("tell the address")
                #gadd='@gmail.com'
                #gadd2=takeCommand()
                #to=str(gadd+gadd2)
                to='nabjad258@gmail.com'
                sendEmail(to,content)
                speak(content)
                speak("email has been sent")
            except Exception as e:
                speak("unable to send email")

        elif 'search in chrome' in query :
            speak("what should i search?")
            #search=takeCommand().lower()
        
            # Taking input from user 
            search_string = takeCommand().lower() 
            print(search_string)
            speak("searching")
            # This is done to structure the string  
            # into search url.(This can be ignored) 
            search_string = search_string.replace(' ', '+')  
              
            # Assigning the browser variable with chromedriver of Chrome. 
            # Any other browser and its respective webdriver  
            # like geckodriver for Mozilla Firefox can be used 
            browser = webdriver.Chrome('chromedriver') 
              
            for i in range(1): 
                matched_elements = browser.get("https://www.google.com/search?q=" +
                                                 search_string + "&start=" + str(i)) 
            #chromepath = 'C:/Program Files (x86/Google/hrome/Application/chrome.exe %s'
            #wb.get(chromepath).open_new_tab(search+'.com')


        elif 'logout' in query:
            speak("do you really want to logout?")
            respo = takeCommand().lower()
            if respo=="yes":
                os.system("shutdown -1")
            speak("forfeiting the operation")
        elif 'shutdown' in query:
            speak("do you really want to shutdown?")
            respo = takeCommand().lower()
            if respo=="yes":
                os.system("shutdown /s /t 1")
            speak("forfeiting the operation")
        elif 'logout' in query:
            speak("do you really want to restart?")
            respo= takeCommand().lower()
            if respo=="yes":
                os.system("shutdown /r /t 1")
            speak("forfeiting the operation")
            
        elif 'play songs' in query:
            songs_dir='F:/201'
            songs=os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))

        elif 'remember that' in query:
            speak("what should i remember")
            data=takeCommand()
            speak("ypu said me to remember that"+data)
            remember=open('data.txt','w')
            remember.write(data)
            remember.close()

        elif 'do you remember' in query:
            remember=open('data.txt','r')
            speak("I remember you said"+remember.read())

        #elif 'take screenshot' in query:
         #   screenshot()
          #  speak("screenshot is been taken and saved as ss.png")

        elif 'cpu usage' in query:
            cpu()

        elif 'energy' in query:
            battery()
            
        elif 'joke' in query:
            jokes()
        elif 'offline' in query:
            speak("going offline")
            quit()

        
