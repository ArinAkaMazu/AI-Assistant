import pyttsx3                  #gives audio to pc
import speech_recognition       #understand the user input
import requests                 #used to make HTTP requests
from bs4 import BeautifulSoup   #extract info from HTML pages 
import datetime                 #helps with time ralated data
import os                       #helps using operating system freely
import pyautogui                #allowing use of mouse and keyboard
import random                   #choose random value
import webbrowser               #open stuff in browsers i.e URL
import speedtest                #checks internet speed
#----------------------------------------------------------------------------------------------------------
for i in range(3):
    a=input("enter the passowrd: ")
    pw_file=open("password.txt","r")
    pw=pw_file.read()
    pw_file.close()
    if (a==pw):
        print("Welcome back boss! Please speak [Wake up] to load me up once \"listening\" starts to pop")
        break
    elif (i==2 and a!=pw):
        exit()
    elif (a!=pw):
        print("Try Again")
#-------------------------------------------------------------------------------------------------------- 
#main engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id) #microsoft david voice
engine.setProperty("rate",170) #audio sound
def speak(audio): #speak function to enter input 
    engine.say(audio)
    engine.runAndWait()
#----------------------------------------------------------------------------------------------------------
def takeCommand():
#speech input command
    r=speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("listening.....")
        r.pause_threshold=1 #delay while speaking
        r.energy_threshold=300 #energy consumed by user while giving input
        audio=r.listen(source,0,4) #if no input given in 4 seconds goes to exception
    try:
        print("Processing...")
        query=r.recognize_google(audio,language="en-in")
        print(f"You Said {query}\n") #entered query
    except Exception as e:
        print("couldnt undetstand, try again") #result if no input given
        return "None"
    return query
#---------------------------------------------------------------------------------------------------------
def alarm(query):
    timehere=open("alarmtext.txt","a") #alarm function
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")
#---------------------------------------------------------------------------------------------------------
if __name__=="__main__":
    while True: #infinite loop until shutted down
        query=takeCommand().lower()
        if "wake up"in query:
    #boot command
            from Greet import greet
            greet()
#--------------------------------------------------------------------------------------------------------
    #Greet values
            while True:
                query= takeCommand().lower()
                if "stop listening" in query:
                    speak("going silent mode") #breaks and loop and stops taking input
                    break #breaks out of loop after saying "stop listening"
#-------------------------------------------------------------------------------------------------------- 
                elif "change password" in query:
                    speak("Whats the new password")
                    new_pw=input("Enter new password \n")
                    new_passowrd=open("password.txt","w")
                    new_passowrd.write(new_pw)
                    new_passowrd.close()
                    speak(f"setting {new_pw} as password")
                    speak("Password changed successfully!")
#-------------------------------------------------------------------------------------------------------- 
                elif "hello there" in query:
                    speak("General Kenobi!!!") #star wars reference 
                elif "hello" in query:
                    speak("Hello boss")
                elif "i am fine" in query:
                    speak("glad to know boss")
                elif "how are you" in query:
                    speak("I am fine boss, how are you?")
                elif "thank you" in query:
                    speak("Welcome, Boss")
#-------------------------------------------------------------------------------------------------------- 
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "resume" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:       #volume and youtube commands 
                    pyautogui.press("m")
                    speak("video muted")
                elif "unmute" in query:
                    pyautogui.press("m")
                    speak("video unmuted")
                elif "increse the volume" in query:
                    from keyboard import volumeup
                    speak("Turning volume up,sir")
                    volumeup()
                elif "decrese the volume" in query:
                    from keyboard import volumedown
                    speak("Turning volume down, sir")
                    volumedown()
#-------------------------------------------------------------------------------------------------------- 
                elif "internet speed" in query:
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()//1048576         
                    download_net = wifi.download()//1048576
                    print("Wifi Upload Speed is", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi Upload speed is {upload_net}")
                    speak(f"Wifi download speed is {download_net}")
#-------------------------------------------------------------------------------------------------------- 
                elif "news" in query:
                    from news import latestnews
                    latestnews()
#-------------------------------------------------------------------------------------------------------- 
                elif "open" in query:
                    from dictapps import openappweb #open apps  kkkk
                    openappweb(query)
                elif "close" in query:
                    from dictapps import closeappweb
                    closeappweb(query)
#--------------------------------------------------------------------------------------------------------
                elif "search on google" in query:
                    from search import searchGoogle #search input on google
                    searchGoogle(query)
                elif "search on youtube" in query:
                    from search import searchYoutube #search input on youtube
                    searchYoutube(query)
#--------------------------------------------------------------------------------------------------------
                elif "play me some music" in query: 
                    speak("Playing you some good music, boss")
                    a=(1,2,3)           #Plays random music/video from youtube
                    b=random.choice(a)
                    if b==1:
                        webbrowser.open("https://youtu.be/fhzKLBZJC3w?si=EkkEe8dfmZ2GtdI7")
                    elif b==2:
                        webbrowser.open("https://youtu.be/zuoVd2QNxJo?si=a6BgXrIZ8PyUSRfX")
                    elif b==3:
                        webbrowser.open("https://youtu.be/M2cckDmNLMI?si=vw6kY3zS1g1N9lSX")
#--------------------------------------------------------------------------------------------------------
                elif "temperature" in query:
                    search = "temperature in alwar"
                    url = f"https://www.google.com/search?q={search}" #Search wether on google 
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser") #This line uses the BeautifulSoup library to parse the HTML content of the web page retrieved by the requests.get(url)
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "temperature in alwar"
                    url = f"https://www.google.com/search?q={search}"
                    r  = requests.get(url)
                    data = BeautifulSoup(r.text,"html.parser")
                    temp = data.find("div", class_ = "BNeawe").text
                    speak(f"current{search} is {temp}")
#---------------------------------------------------------------------------------------------------------
                elif "time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    #tells current time
                    speak(f"Boss, its currently {strTime} right now")
                elif "set alarm" in query:
                    print("input time, Example: 10 and 10 and 10")
                    speak("please set the time")
                    a=input("Enter the time")
                    alarm(a)
                    speak("Done boss")
#---------------------------------------------------------------------------------------------------------
                elif "screenshot" in query:
                     im = pyautogui.screenshot() #captures screenshot
                     im.save("ss.jpg") #saves image by name of "ss.jpg"
                     speak("Screenshot taken and saved")
#---------------------------------------------------------------------------------------------------------
                elif "remind me" in query:
                    remindMe=query.replace("remind me","")
                    remindMe=query.replace("doc","")
                    speak("Ok i will"+ remindMe)
                    remind=open("remindMe.txt","w")
                    remind.write(remindMe)
                    remind.close()
                elif "show me my tasks" in query:
                    remind=open("remindMe.txt","r")
                    speak("here are your tasks"+ remind.read())
#---------------------------------------------------------------------------------------------------------
                elif "shutdown the system" in query:    #shut down command
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (y/n)")
                    if shutdown == "y": #shut down confirmation taken from user
                        os.system("shutdown /s /t 1")

                    elif shutdown == "n": #breaks out of loop if reply given no
                        break
#---------------------------------------------------------------------------------------------------------
                elif "good night" in query:
                    speak ("bye boss. Wake me, when you need me!")
                    exit() #exits the code