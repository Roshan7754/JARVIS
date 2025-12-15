import pyttsx3
import speech_recognition as sr
import eel
import time

def speak(text):
    Engine = pyttsx3.init('sapi5')
    voices = Engine.getProperty('voices')
    Engine.setProperty('voice', voices[0].id)
    Engine.setProperty('rate', 150)
    eel.DisplayMessage(text)
    
    Engine.say(text)
    Engine.runAndWait()

def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('listening...')
        eel.DisplayMessage('listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 10, 6)
    try:
        print('recognizing')
        eel.DisplayMessage('recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        eel.DisplayMessage(query)
        time.sleep(2)
        eel.showHood()
    except Exception as e:
        return ""
    return query.lower()

@eel.expose
def allCommand():
    query = takecommand()
    print(query)

    if "open" in query:
        from Engine.feature import opencommand
        opencommand(query)
    else:
        print(not run)