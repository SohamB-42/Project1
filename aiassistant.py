import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import pyaudio
import webbrowser
import subprocess
import os
import pywhatkit
import pyjokes
import pyautogui
import time

import threading
import winsound


from dotenv import load_dotenv



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning, I am NOVA, your Assistant! How may I help you?")
    elif hour>=12 and hour<17:
        speak("Good Afternoon, I am NOVA,your Assistant! How may I help you?")
    else:
        speak("Good Evening, I am NOVA, your Assistant! How may I help you?")
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query
    
def set_reminder(reminder_time, reminder_message):
    def reminder():
        while True:
            current_time = datetime.datetime.now().strftime("%H:%M")
            if current_time == reminder_time:
                print(f"Reminder alert: {reminder_message}")
                winsound.Beep(1000, 1000)  
                speak(f"Reminder: {reminder_message}")
                break 
            time.sleep(5)  # Check every 5 seconds
    threading.Thread(target=reminder).start()


def set_alarm(alarm_time):
    def alarm():
        while True:
            current_time = datetime.datetime.now().strftime("%H:%M")
            if current_time == alarm_time:
                for i in range(5):  # Repeat 5 times
                    print(f"Alarm! Wake up! ({i+1})")
                    time.sleep(3)  # Wait 3 seconds before repeating
                break
            time.sleep(10)
    threading.Thread(target=alarm).start()


# Setting Brave as the default browser
brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
webbrowser.register('brave', None, webbrowser.BackgroundBrowser(brave_path))
        
if __name__ == "__main__":
    try:
        wish()
        while True:
            query = listen().lower()

            if query == "none":
                continue

            if 'wikipedia' in query: #search on wikipedia
                speak("Searching wikipedia...")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=4)
                speak("According to wikipedia")
                print(results)
                speak(results)
            elif 'open youtube' in query: #open YouTube
                speak("Opening youtube...")
                webbrowser.get('brave').open("https://www.youtube.com")
            elif 'open google' in query: #open Google
                speak("Opening google...")
                webbrowser.get('brave').open("https://www.google.com")
            elif 'open spotify' in query: #open Spotify
                speak("Opening Spotify...")
                webbrowser.get('brave').open("https://open.spotify.com")
            elif 'the time' in query:
                time = datetime.datetime.now().strftime("%I:%M:%S %p")
                speak("The current time is: " + time)
                print("The current time is: " + time)
            elif 'search' in query: #search on google
                speak("Opening brave...")
                webbrowser.get('brave').open("https://www.google.com/search?q=" + query.replace('search', '').strip())
            elif 'open code' in query: #open Visual Studio Code
                speak("Opening Visual Studio Code...")
                codePath = "C:\\Users\\User\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
            elif 'open chatgpt' in query: #open chatgpt
                speak("Opening ChatGPT...")
                webbrowser.get('brave').open("https://www.chatgpt.com")
            elif 'joke' in query: #tell a joke
                joke = pyjokes.get_joke()
                speak(joke)
                print(joke)
            elif 'play' in query: #play on YouTube
                media = query.replace('play', '')
                speak('playing ' + media)
                pywhatkit.playonyt(media)
            elif 'pause' in query or 'play' in query: #play/pause
                speak("Toggling play/pause on YouTube...")
                pyautogui.press('space')
            elif 'next video' in query: #next video
                speak("Playing next video on YouTube...")
                pyautogui.hotkey('shift', 'n')
            elif 'previous video' in query: #previous video
                speak("Playing previous video on YouTube...")
                pyautogui.hotkey('shift', 'p')
            elif 'volume up' in query: #increase volume
                speak("Increasing volume on YouTube...")
                pyautogui.press('up')
            elif 'volume down' in query: #decrease volume
                speak("Decreasing volume on YouTube...")
                pyautogui.press('down')
            elif 'mute' in query: #mute volume
                speak("Muting volume on YouTube...")
                pyautogui.press('m')
            elif 'unmute' in query: #unmute volume
                speak("Unmuting volume on YouTube...")
                pyautogui.press('m')
            elif 'full screen' in query: #full screen
                speak("Toggling full screen on YouTube...")
                pyautogui.press('f')
            elif 'exit full screen' in query: #exit full screen
                speak("Exiting full screen on YouTube...")
                pyautogui.press('f')
            elif 'scroll up' in query: #scroll up
                speak("Scrolling up ...")
                pyautogui.scroll(200)
            elif 'scroll down' in query: #scroll down
                speak("Scrolling down ...")
                pyautogui.scroll(-200)

            elif 'open calculator' in query: #calculator
                subprocess.Popen('C:\\Windows\\System32\\calc.exe')
            elif 'open notepad' in query: #notepad
                subprocess.Popen('C:\\Windows\\System32\\notepad.exe')
            elif 'open command prompt' in query: #command prompt
                subprocess.Popen('C:\\Windows\\System32\\cmd.exe')
            elif 'open settings' in query: #settings
                subprocess.Popen('C:\\Windows\\System32\\ms-settings.exe')
            elif 'open calendar' in query: #calendar
                subprocess.Popen('C:\\Windows\\System32\\calendar.exe')
            elif 'open camera' in query: #camera
                subprocess.Popen('C:\\Windows\\System32\\camera.exe')
            elif 'open maps' in query: #maps
                subprocess.Popen('C:\\Windows\\System32\\maps.exe')
            elif 'open photos' in query: #photos
                subprocess.Popen('C:\\Windows\\System32\\photos.exe')
            elif 'open weather' in query: #weather
                subprocess.Popen('C:\\Windows\\System32\\ms-weather.exe')
        
            elif 'open news' in query: #news
                subprocess.Popen('C:\\Windows\\System32\\news.exe')
            elif 'open store' in query: #microsoft store
                subprocess.Popen('C:\\Windows\\System32\\ms-windows-store://home')
            
            elif 'open edge' in query: #edge
                subprocess.Popen('C:\\Windows\\System32\\msedge.exe')

            elif 'reminder' in query: #reminder
                speak("What should I remind you about?")
                reminder_message = listen()
                speak("At what time should I remind you?")
                reminder_time = listen()
                set_reminder(reminder_time, reminder_message)
                speak(f"Reminder set for {reminder_time}")
            elif 'alarm' in query: #alarm
                speak("At what time should I set the alarm?")
                alarm_time = listen()
                set_alarm(alarm_time)
                speak(f"Alarm set for {alarm_time}")
            elif 'shutdown' in query: #shutdown
                speak("Shutting down the system...")
                os.system("shutdown /s /t 1")
            elif 'restart' in query: #restart
                speak("Restarting the system...")
                os.system("shutdown /r /t 1")
            
            elif 'what is your name' in query:
                speak("I am NOVA, your Assistant!")
            elif 'how are you' in query:
                speak("I am fine, thank you!")
            elif 'who are you' in query:
                speak("I am NOVA, your Assistant!")
            elif 'thank' in query:
                speak("You're welcome!")
         
            elif 'exit' in query:
                speak("Goodbye Boss, have a nice day!")
                pyautogui.hotkey('ctrl', 'alt', 'm')  
                break
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Ensure the pyttsx3 engine shuts down properly
        engine.stop()
        print("Exiting program...")
        exit(0)



