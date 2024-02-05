import pyttsx3
import datetime 
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)
#main engine from main.py
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def greet(): 
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning,boss")
    #if morning 12 am to 12 pm
    elif hour>12 and hour<=18:
        speak("Good Afternoon,boss")
    #if noon 12 pm to 6 pm
    else:
        speak("Good evening,boss")
    #if evening after 6pm
    speak("Lets get to work, shall we")