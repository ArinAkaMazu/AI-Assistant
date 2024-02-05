import pyttsx3
import datetime

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def greet():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning,boss")
    #if morning
    elif hour>12 and hour<=18:
        speak("Good Afternoon,boss")
    #if noon
    else:
        speak("Good evening,boss")
    #if evening
    speak("Lets get to work, shall we")