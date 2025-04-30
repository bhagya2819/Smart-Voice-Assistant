import os
import re
import sqlite3
import webbrowser
from playsound import playsound
import eel
import requests
import pyautogui
from engine.command import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit
import wikipedia
import threading
def check_alarms():
    pass

# Start alarm checker in the background
threading.Thread(target=check_alarms, daemon=True).start()

conn = sqlite3.connect("sophia.db")
cursor = conn.cursor()


def playAssistantSound():
    sound_path = os.path.join(os.getcwd(), "www", "assets", "audio", "start_sound.mp3")
    playsound(sound_path)



#click sound for mic button

@eel.expose
def playClickSound():
    music_dir = "www\\assets\\audio\\click_sound.mp3"
    playsound(music_dir)
 

def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "").strip()
    query=query.lower()

    if query != "":
        
        try:
            # Try to find the application in sys_command table
            cursor.execute('SELECT path FROM sys_command WHERE LOWER(name) = ?', (query,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening " + query)
                os.startfile(results[0][0])
                return

            # If not found, try to find the URL in web_command table
            cursor.execute('SELECT url FROM web_command WHERE LOWER(name) = ?', (query,))
            results = cursor.fetchall()
            
            if len(results) != 0:
                speak("Opening " + query)
                webbrowser.open(results[0][0])
                return

            # If still not found, try to open using os.system
            speak("Opening " + query)
            try:
                os.system('start ' + query)
            except Exception as e:
                speak(f"Unable to open {query}. Error: {str(e)}")

        except Exception as e:
            speak(f"Something went wrong: {str(e)}")



def PlayYoutube(query):
    search_term = extract_yt_term(query)
    if search_term:
        speak("Playing " + search_term + " on YouTube")
        kit.playonyt(search_term)
    # else:
    #     speak("Sorry, I couldn't find what to play on YouTube.")


def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else None



import requests
from engine.command import speak

import requests
import eel
from engine.command import speak

@eel.expose
def fetchNews():
    speak("Fetching the latest news for you...")

    try:
        url = "https://newsapi.org/v2/top-headlines?language=en&apiKey=075fad185130480ea9e6178a3400aa21"
        response = requests.get(url)
        data = response.json()

        headlines = []

        if data["status"] == "ok":
            articles = data["articles"][:5]
            if not articles:
                speak("Sorry, there are no headlines right now.")
            else:
                for i, article in enumerate(articles, start=1):
                    title = article.get("title", "No title")
                    headlines.append(f"News {i}: {title}")
                    speak(f"News {i}: {title}")
        else:
            headlines.append("Error: News API returned an error.")

        # Send headlines to frontend
        eel.displayNewsInFrontend(headlines)

    except Exception as e:
        error_msg = f"Error fetching news: {str(e)}"
        speak(error_msg)
        eel.displayNews([error_msg])

import subprocess
import time

def takeNote(query):
    # Extract note content
    note_text = query.replace("take note", "").strip()
    
    if note_text:
        speak("Opening Notepad and typing your note.")
        
        # Step 1: Open Notepad
        subprocess.Popen(["notepad.exe"])
        time.sleep(1.5)  # Give it time to open
        
        # Step 2: Type the note
        pyautogui.write(note_text, interval=0.05)
        
        # (Optional) Auto-save with Ctrl+S and file name
        # speak("Saving the note.")
        # pyautogui.hotkey("ctrl", "s")
        # time.sleep(1)
        # pyautogui.write("note.txt")
        # pyautogui.press("enter")
    else:
        speak("Please say the note after 'take note'.")

import webbrowser

def searchGoogle(query):
    query = query.replace("search", "").replace("on google", "").strip()
    
    if query:
        speak(f"Searching for {query} on Google.")
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
    else:
        speak("Please say what you want to search after 'search' on Google.")

def searchWikipedia(query):
    query = query.replace("search", "").replace("on wikipedia", "").strip()
    if query:
        speak(f"Fetching information about {query} from Wikipedia.")
        try:
            summary = wikipedia.summary(query, sentences=2)
            speak(f"Here's what I found: {summary}")
        except wikipedia.exceptions.DisambiguationError as e:
            speak(f"Sorry, there are multiple results for {query}. Please be more specific.")
        except wikipedia.exceptions.PageError:
            speak("Sorry, I couldn't find a Wikipedia page for that.")
        except Exception as e:
            speak(f"An error occurred: {e}")
    else:
        speak("Please tell me what to search on Wikipedia.")

import pyautogui
import time
from engine.command import speak


# **Take a Screenshot**
def takeScreenshot():
    speak("Taking screenshot")
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    speak("Screenshot saved")


# **Type Text**
def typeText(query):
    text = query.replace("type", "").strip()
    if text:
        speak(f"Typing {text}")
        pyautogui.write(text, interval=0.1)
    else:
        speak("What should I type?")


# **Press Keys (Enter, Spacebar, etc.)**
def pressKey(query):
    key = query.replace("press", "").strip()
    if key:
        speak(f"Pressing {key}")
        pyautogui.press(key)
    else:
        speak("Please specify which key to press.")


# **Scroll Pages**
def scrollPage(query):
    if "down" in query:
        speak("Scrolling down")
        pyautogui.scroll(-500)  # negative for down
    elif "up" in query:
        speak("Scrolling up")
        pyautogui.scroll(500)  # positive for up
    else:
        speak("Please specify whether to scroll up or down.")


# **Open Files/Folders**
def openFile(query):
    file_path = query.replace("open", "").strip()
    if file_path:
        speak(f"Opening {file_path}")
        try:
            os.startfile(file_path)
        except Exception as e:
            speak(f"Error opening {file_path}: {str(e)}")
    else:
        speak("Please specify the file or folder to open.")


# **Close Applications**
def closeApplication(query):
    app_name = query.replace("close", "").strip()
    if app_name:
        speak(f"Closing {app_name}")
        # Logic to close the app based on name can be added here
        # Example: os.system(f"taskkill /im {app_name}.exe")
    else:
        speak("Please specify the application to close.")


# **Shutdown or Restart System**
def shutdownSystem(query):
    if "shutdown" in query:
        speak("Shutting down the system.")
        os.system("shutdown /s /f /t 0")
    elif "restart" in query:
        speak("Restarting the system.")
        os.system("shutdown /r /f /t 0")
    else:
        speak("Please specify whether to shutdown or restart the system.")

import datetime
import time
import threading
from engine.command import speak

alarms = []

def check_alarms():
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        for alarm_time in alarms:
            if now == alarm_time:
                speak(f"Alarm ringing. It's {alarm_time}")
                alarms.remove(alarm_time)
        time.sleep(30)

def set_alarm(query):
    try:
        query = query.lower().replace("set an alarm for", "").strip()
        alarm_time = datetime.datetime.strptime(query, "%I %p").strftime("%H:%M")
        alarms.append(alarm_time)
        speak(f"Alarm set for {query}")
    except Exception as e:
        speak("Sorry, I couldn't set the alarm. Please say the time in format like 8 AM.")


def set_timer(query):
    import re

    try:
        minutes = 0
        seconds = 0
        match_min = re.search(r'(\d+)\s*minute', query)
        match_sec = re.search(r'(\d+)\s*second', query)

        if match_min:
            minutes = int(match_min.group(1))
        if match_sec:
            seconds = int(match_sec.group(1))

        total_seconds = minutes * 60 + seconds
        if total_seconds == 0:
            speak("Please say a valid timer duration.")
            return

        speak(f"Setting a timer for {minutes} minutes and {seconds} seconds.")
        time.sleep(total_seconds)
        speak("Time's up!")
    except Exception as e:
        speak("Sorry, I couldn't set the timer.")

import requests
from bs4 import BeautifulSoup
from engine.command import speak

import requests
from bs4 import BeautifulSoup
from engine.command import speak

def fetch_stock_price(query):
    try:
        company = query.lower().replace("stock price of", "").strip()
        search_query = f"{company} stock price"
        url = f"https://www.google.com/search?q={search_query}"

        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        # Try to find the stock price in different potential locations
        price_element = soup.find("div", {"class": "YMlKec fxKbKc"})  # Google stock price result element
        
        if price_element:
            price = price_element.text
            speak(f"The current stock price of {company} is {price}")
        else:
            speak(f"Sorry, I couldn't find the stock price for {company}.")

    except Exception as e:
        speak("An error occurred while fetching the stock price.")
