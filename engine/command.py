import time
import pyttsx3
import speech_recognition as sr
import eel
import threading


# Initialize text-to-speech engine globally
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 170)

def speak(text):
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        eel.DisplayMessage('Listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        try:
            audio = r.listen(source, timeout=10, phrase_time_limit=6)
            print('Recognizing...')
            eel.DisplayMessage('Recognizing...')
            query = r.recognize_google(audio, language='en')
            print(f'User said: {query}')
            time.sleep(2)
            eel.DisplayMessage(query)
            eel.ShowHood()
            return query.lower()

        except Exception as e:
            print("Recognition error:", e)
            eel.DisplayMessage("Sorry, I couldn't recognize your voice.")
            return ""

@eel.expose
def allCommands():
    query = takeCommand()
    print(query)

    # # 💬 First check for personal conversation
    # if handlePersonalQuestions(query):
    #     return

    if 'open' in query:
        from engine.features import openCommand
        openCommand(query)

    elif 'on youtube' in query:
        from engine.features import PlayYoutube
        PlayYoutube(query)

    elif 'news' in query:
        from engine.features import fetchNews
        fetchNews()

    elif 'take note' in query:
        from engine.features import takeNote
        takeNote(query)

    elif 'search' in query and 'on google' in query:
        from engine.features import searchGoogle
        searchGoogle(query)

    elif 'search' in query and 'on wikipedia' in query:
        from engine.features import searchWikipedia
        searchWikipedia(query)

    elif 'take screenshot' in query:
        from engine.features import takeScreenshot
        takeScreenshot()

    elif 'type' in query:
        from engine.features import typeText
        typeText(query)

    elif 'press' in query:
        from engine.features import pressKey
        pressKey(query)

    elif 'scroll' in query:
        from engine.features import scrollPage
        scrollPage(query)

    elif 'shutdown' in query or 'restart' in query:
        from engine.features import shutdownSystem
        shutdownSystem(query)

    elif 'set an alarm for' in query:
        from engine.features import set_alarm
        set_alarm(query)

    elif 'set a timer for' in query:
        from engine.features import set_timer
        set_timer(query)

    elif 'stock price of' in query:
        from engine.features import fetch_stock_price
        fetch_stock_price(query)

    eel.ShowHood()
