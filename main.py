import pyttsx3
import speech_recognition
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
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
if __name__=="__main__":
    while True:
        query=takeCommand().lower()
        if "wake up"in query:
            from Greet import greet
            greet()
            
            while True:
                query= takeCommand().lower()
                if "good night" in query:
                    speak("Bye boss, wake me; when you need me")
                    break
                elif "hello there" in query:
                    speak("Hi boss, how are you doing?")
                elif "i am fine" in query:
                    speak("glad to know boss")
                elif "how are you" in query:
                    speak("I am fine boss, how are you?")
                elif "thank you" in query:
                    speak("Welcome, Boss")
                elif "google" in query:
                    from search import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from search import searchYoutube
                    searchYoutube(query)
                
                

