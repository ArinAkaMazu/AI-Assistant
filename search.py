import speech_recognition
import pyttsx3
import pywhatkit 
import webbrowser
import wikipedia

def takeCommand():
    r=speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("listening.....")
        r.pause_threshold=1
        r.energy_threshold=300
        audio=r.listen(source,0,4)
    try:
        print("Processing...")
        query=r.recognize_google(audio,language="en-in")
        print(f"You Said {query}\n")
    except Exception as e:
        print("couldnt undetstand, try again")
        return "None"
    return query
query=takeCommand().lower()
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query= query.replace("doc","")
        query= query.replace("google search","")
        query= query.replace("google","")
        speak("Here are the results from web")

        try:
            pywhatkit.search(query)
            result=googleScrap.summary(query,1)
            speak(result)

        except:
            speak("No results found")

def searchYoutube(query):
    if "youtube" in query:
        speak("searching on youtube...")
        query= query.replace("doc","")
        query= query.replace("youtube search","")
        query= query.replace("youtube","")
        web= "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Here you go, Boss")
