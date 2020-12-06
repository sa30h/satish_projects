import pyttsx3
import platform
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser



engine=pyttsx3.init('sapi5')
voice=engine.getProperty('voices')
engine.setProperty('voice',voice[0].id)
rate=engine.getProperty('rate')
engine.setProperty('rate',135)

def command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......//////////....////")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing.....////////..////")
        query=r.recognize_google(audio,'en-in')
        print("User Said:{query} \n")
    except Exception as e:
        print("I did't understand!!! Please Repeat!!")
        return "none"
    return query


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def system_info():
    machine=platform.machine()
    version=platform.version()
    users=platform.uname()
    platform_info=platform.system()
    processor=platform.processor()
    speak(processor)

def greet():
    current_time=datetime.datetime.now()
    year=current_time.year
    return year


if __name__=='__main__':
    speak("hello mr parmod")
    while True:
        query=command().lower()

        if "wikipedia" in query:
            print("searching wikipeadia")
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query,sentences=2)
            print(results)
            speak("according to wikipedia")
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "sleep" in query:
            speak("Ok sir, i am signing out and this is edited in github")
            exit()
            



