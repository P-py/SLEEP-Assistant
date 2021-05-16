from os.path import sameopenfile
import speech_recognition as sr
from time import ctime
import time
import os
import pyttsx3
from gtts import gTTS
from pygame import mixer
import random

words_to_terminate = ['bye', 'shutdown', 'exit', 'quit', 'gotosleep', 'goodbye']
user_name = ""

def getUserName():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    user_name = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        user_name = r.recognize_google(audio)
        print("You said: " + user_name)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    return user_name

def speak(audioString):
    print(audioString)
    engine = pyttsx3.init()
    engine.say(audioString)
    engine.runAndWait()

def greeting():
    speak("Initializing the system...")
    time.sleep(1)
    speak("Hello! I'am SLEEP, your personal assistant.")
    time.sleep(1)
    speak("I'm in version 0.1, my functions now are:")
    time.sleep(.5)
    speak("Wait function, If the user says 'wait + time in seconds' I will sleep and wait;")
    speak("How are you function;")
    speak("What time is it function, if the user says 'what time is it' I will answer the day, day of the week, hour and minutes;")
    speak("What's the weather like in, if the user says 'what's the weather like in + location' I will show the weather there.")
    speak("Shut down computer function, I can shutdown your computer for you, just say 'shut down computer' and it will turn off in 30 seconds.")
    time.sleep(.3)


def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Waiting for the user")
        audio = r.listen(source)

    # Speech recognition using Google Speech Recognition
    data = ""
    try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return data


def terminate(data):
    for word in words_to_terminate:
        if word in data:
            speak("Do you want to turn me off?")
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Say something!")
                audio = r.listen(source)
            response = ""
            try:
                response = r.recognize_google(audio)
                print("You said: " + data)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
            if "yes" or "yeah" or "for sure" or "affimative" in response:
                speak(f"Ok, bye {user_name}, nice to meet you!")
                exit()
            else:
                pass
            
def jarvis(data):    
    if "wait" in data:
        data = data.split(' ')
        time_to_sleep = data[1]
        speak(f"Ok, I will wait you commands for {time_to_sleep} seconds")
        time.sleep(int(time_to_sleep))
        speak(f"Hello, can I help you now {user_name}?")
    if "how are you" in data:
        responses = ["better than you, bro.", "I'm fine, hope you having a good fucking day too.", "That is out of your bussiness", "I'm fine, ready to help."]
        response = random.choice(responses)
        speak(response)

    if "what time is it" in data:
        speak(ctime())

    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on, I will show you where " + location + " is.")
        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")

    if "shut down computer" in data:
        speak("shutting it down babe")
        speak("Your computer will be shutt down in 30 seconds")
        os.system("shutdown /s /t 30")

    if "what's the weather like in" in data:
        speak("Ok, I will show you")
        data = data.split(" ")
        string = "+".join(data)
        os.system("start msedge https://www.google.com/search?q=" + string)
    
    if "classroom" in data:
        data = data.split(" ")
        area = data[1]
        if area == 'mathematics':
            speak("Opening your fucking fundamental math classroom, lets'go")
            os.system("start msedge https://classroom.google.com/u/1/c/MTk3MjY4MDI1MjI0")
        if area == 'chemistry':
            speak("Opening your chemistry classroom, let's cook some meth in the kitchen, like Heisenberg")
            os.system("start msedge https://classroom.google.com/u/1/c/MjM0MzkwODEwNDU1")
        if area == 'history':
            speak("Opening your history classroom, let's conquer Jerusalém man.")
            os.system("start msedge https://classroom.google.com/u/1/c/MTk3MjQzMzU5MDAx")
        if area == 'glass':
            speak("Opening your physics 1 classroom. Double physics bro? What. the. fuck.")
            os.system("start msedge https://classroom.google.com/u/1/c/MjM0MjU3MTk0Mzgz")
        if area.lower() == 'electro':
            speak("Opening your physics 2 classroom.")
            os.system("start msedge https://classroom.google.com/u/1/c/MjM0NzIyNjAzMjQz")
        else:
            pass

# initialization
time.sleep(2)
greeting()
speak("So, how should I call you?")
user_name = getUserName()
speak(f"Hello {user_name}, what can I help you with?")
while 1:
    data = recordAudio()
    jarvis(data)
