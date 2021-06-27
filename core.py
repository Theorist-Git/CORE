import os
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takecommand():
    """
    takes input from user microphone
    and returns a string as output
    i.e speech to text function
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print("user said\n", query)

    except Exception as e:
        print(e)
        print("say that again would ya")
        return "None"
    return query


def greetings():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning")
    elif hour == 12:
        speak("Good Afternoon")
    elif 12 < hour <= 21:
        speak("Good Evening")
    else:
        speak("Good Night")

    speak("I am CORE")


if __name__ == '__main__':
    greetings()
    query = takecommand().lower()
    # Logic for executing tasks bases on query
    if 'wikipedia' in query:
        speak("Searching Wikipedia")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=1)
        speak("According to wikipedia")
        speak(results)
    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    elif 'play music' in query:
        music_dir = 'D:\\Music\\Opera\\Franco Corelli'
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[0]))



