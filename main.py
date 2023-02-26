import subprocess
import wolframalpha
import pyttsx3
import json
import random as ra
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import winshell
import pyjokes
import ctypes
import time
import requests
from ecapture import ecapture as ec
from urllib.request import urlopen
import songs

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 160)
keep_doing = True
wolframalpha_api = "**"
openweather_api = "**"
news_api = "**"

def speak(text1):
    engine.say(text1)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listning.....")
        r.energy_threshold = 150
        r.pause_threshold = 1
        text2 = r.listen(source)
    try:
        print("Recognizing......")
        query = r.recognize_google(text2, language='en-in')
        print("user said: " + query + "\n")
        return query
    except Exception as e:
        # print(e)
        print("speak again \n")
        return "None"


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        speak("good morning")
    elif hour >= 12 and hour < 18:
        speak("good afternoon")
    else:
        speak("good evening")

    speak("I am slovish. i am your assistant")


def givewikipedia(query):
    results = []
    speak("Searching... Wait!")
    query = query.replace('wikipedia', '')
    results.append( wikipedia.summary(query, sentences=2))
    speak("according to wikipedia")
    return results


def givedatetime():
    time = datetime.datetime.now().strftime("%H:%M:%S")
    date = datetime.date.today()
    print(time)
    print(date)
    return [f"Current time is {time} , Todays date is {date}"]


def musicsystem():
    dir1 = "slovishmusic"
    listofsong = os.listdir(dir1)
    print(listofsong)
    speak("please say any name of the song either i will play random")
    songs.start(listofsong)
    inp = takecommand().lower()+".mp3"
    if inp in listofsong:
        os.startfile(os.path.join(dir1, inp))
    else:
        os.startfile(os.path.join(dir1, ra.choice(listofsong)))

def start_doing():
    global keep_doing
    keep_doing = True


def command_search():
    query = takecommand().lower()
    return search_for_query(query)


def text_search(text):
    query = text.lower()
    return search_for_query(query)

def search_for_query(query):
    qa = {"who are you": ["i am slovish your voice assistant. i am here to help you"],
          "who created you who made you": ["it's funny but i do have only one parent. vishal created me", "i have been developed by vishal","vishal created me for minimizing his task"],
          "how are you": ["i am good", "i am fine thankyou for asking", "ohh its getting terrible today i am feeling very hot in here","feeling great to talk to you"],
          "why you were created": ["to ease your task","its a secret"],
          "what is your name what's your name": ["my name is slovish"],
          "change name": ["sorry i love my name so i would not change it", "my developer won't allow me to do that"],
          "who am i": ["i am pretty sure you are human","a geek who loves technology"],
          "reason behind your name": ["my creator is a gamer guy. my name comes from his gaming profile","there is long story behing my name"],
          "what is love": ["complete waste of time and money","waamen things","it is 7th sense that destroy all other senses"],
          "will you be my gf will you be my bf": ["yes sure first buy me a bugatti","sorry you can't afford my expences", "i am just 5 week young. i am too young for this", "i am not sure about that, may be you should give me some time"],
          "i love you": ["go do studies don't waste your time", "It's hard to understand"]
          }
    done = True
    for item in list(qa.keys()):
        if query in item:
            done = False
            try:
               speak(ra.choice(qa[item]))
            except Exception as e:
               pass

    if done:
        if 'wikipedia' in query:
               return givewikipedia(query)

        elif 'open youtube' in query:
            speak("opening")
            query = query.replace('open youtube', "")
            webbrowser.open(f'https://www.youtube.com/results?search_query={query}')

        elif 'google search' in query:
            speak("searching")
            query = query.replace('google search', "")
            webbrowser.open(f'https://www.google.com/search?q={query}')

        elif "open leetcode" in query:
            webbrowser.open(f'https://leetcode.com/vishalkrishnajha2001/')

        elif "open github" in query:
            webbrowser.open(f'https://github.com/slovish')

        elif "open codechef" in query:
            webbrowser.open(f'https://www.codechef.com/users/spt2020200027')

        elif "portfolio" in query:
            webbrowser.open(f'https://slovish.github.io/portfolio/')

        elif "open code" in query:
            codepath = "C:\\Users\\Vishal jha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'play music' in query or "play song" in query:
            musicsystem()

        elif "time" in query or "date" in query :
            return givedatetime()

        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("google.com")

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            return [joke]

        elif "calculate" in query:
            client = wolframalpha.Client(wolframalpha_api)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            return ["The answer is " + answer]

        elif 'search' in query or 'play' in query:
            query = query.replace("search", "")
            query = query.replace("play", "")
            webbrowser.open(query)

        elif 'news' in query:
            result = []
            try:
                speak("what kind of news you will like to hear")
                speak("give me context like global, indian, sports or anything")
                this = takecommand()
                jsonObj = urlopen(f"https://newsapi.org/v2/everything?q={this}&from=2023-01-25&sortBy=publishedAt&apiKey={news_api}")
                data = json.load(jsonObj)
                i = 1
                speak(f'here are some top 5 news from {this}')
                for item in data['articles']:
                    print(str(i) + '. ' + item['title'] + '\n')
                    result.append(item['title'])
                    i += 1
                    if i > 5:
                        break
            except Exception as e:
                print(str(e))
            return result

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call(["shutdown", "/h"])

        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()

        elif 'shutdown system' in query:
            speak("See you again. Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            speak("Recycle Bin Recycled")

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.com/maps/place/"+ location )

        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Camera", "pic.jpg")

        elif "weather" in query:
            speak(" City name ")
            print("City name : ")
            city_name = takecommand().lower()
            base_url1 = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},&limit={1}&appid={openweather_api}"
            response_lat_lon = requests.get(base_url1)
            lat_lon  = response_lat_lon.json()
            lat = lat_lon[0]["lat"]
            lon = lat_lon[0]["lon"]

            base_url2 = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={openweather_api}"
            response = requests.get(base_url2)
            x = response.json()
            print(x)
            if x["name"] != "None":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                results = [f"Temperature = {current_temperature} kelvin", f"atmospheric pressure = {current_pressure} hPa",
                           f"Humidity = {current_humidity}%", f"Description = {weather_description}"]
                return results
            else:
                speak("City Not Found ")

        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")

        elif "what is" in query or "who is" in query:
            client = wolframalpha.Client(wolframalpha_api)
            res = client.query(query)
            try:
                print(next(res.results).text)
                return [next(res.results).text]
            except StopIteration:
                print("No results")

        elif "mute" in query or "don't listen" in query or "stop listening" in query or "stop" in query:
            global keep_doing
            speak('thank you')
            keep_doing = False