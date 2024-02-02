import pyttsx3
def speak(text):
    engine= pyttsx3.init()
    voices=engine.getProperty("voices")
    id=r"HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
    engine.setProperty("voice",id)
    engine.say(text=text)
    engine.runAndWait()
speak("Hello simple. go study we need to work")
    
    