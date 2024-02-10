import pyttsx3 #gives audio to pc
import speech_recognition #understand the user input
import requests 
from bs4 import BeautifulSoup
import datetime
import os
import pyautogui
import keyboard
#----------------------------------------------------------------------------------------------------------
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
def alarm(query):
    timehere=open("alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")
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
                    break #end of loop after saying "good night"/shutting down
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
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
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
                elif "open" in query:
                    from dictapps import openappweb #open apps  
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
                elif "good night" in query:
                    speak ("bye boss. Wake me, when you need me!")
                    exit() #exits the code 18