import pyttsx3
import speech_recognition
#----------------------------------------------------------------------------------------------------------
#main engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id) #microsoft david voice
engine.setProperty("rate",170) #audio sound

def speak(audio):
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
if __name__=="__main__":
    while True:
        query=takeCommand().lower()
        if "wake up"in query:
    #boot command
            from Greet import greet
            greet()
#------------------------------------------------------------------------------------------------------
    #Greet values
            while True:
                query= takeCommand().lower()
                if "good night" in query:
                    speak("Bye boss, wake me; when you need me") #shut down command
                    break #end of loop after saying "good night"/shutting down
                elif "hello there" in query:
                    speak("Hi boss, how are you doing?")
                elif "i am fine" in query:
                    speak("glad to know boss")
                elif "how are you" in query:
                    speak("I am fine boss, how are you?")
                elif "thank you" in query:
                    speak("Welcome, Boss")
#------------------------------------------------------------------------------------------------------
                elif "google" in query:
                    from search import searchGoogle #search input on google
                    searchGoogle(query)
                elif "youtube" in query:
                    from search import searchYoutube #search input on youtube
                    searchYoutube(query)
                
                

