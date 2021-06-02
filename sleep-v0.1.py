"""
SLEEP personal assistant - coded and created by Pedro Salviano

Enjoy using it, if you can, read all the code, especially the comments, so you can understand yhe functions and use it well.
"""

from os.path import sameopenfile
import speech_recognition as sr #Get the audio input from the user
from time import ctime #Current time
import time #Time Intervals
import os #Natural O.S functions
import pyttsx3 #Python text-to-speech-3
from gtts import gTTS #Google text-to-speech
from pygame import mixer #Playing audios
import random #Randomize some answers

#Words that can be used by the user to shutdown the program.
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
        user_name = r.recognize_google(audio, language='pt-BR')
        print("You said: " + user_name)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    return user_name

#Used to make SLEEP say something
def speak(audioString):
    print(audioString)
    engine = pyttsx3.init()
    engine.say(audioString)
    engine.runAndWait()

#Greets the user
def greeting():
    speak("Initializing the system...")
    time.sleep(1)
    speak("Hello! I'am SLEEP, your personal assistant.")
    time.sleep(1)
    speak("I'm in version 0.1 and it's a pleasure to help you")
    time.sleep(.5)
    speak("If you need help with my functions just say 'list of functions' and I will give you a complete list of my functions")
    time.sleep(.3)

#Gets the user audio input
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

#Function to confirm the shutdown of SLEEP
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

#Main function, makes everything work together.      
def sleep(data):
    if "list of functions" in data:
        speak("Do you need help with my functions? Here it's a list of what can I do")
        time.sleep(.5)
        speak("1 - Wait function, If the user says 'wait + time in seconds' I will sleep and wait;")
        speak("2 - How are you function;")
        speak("3 - What time is it function, if the user says 'what time is it' I will answer the day, day of the week, hour and minutes;")
        speak("4 - What's the weather like in, if the user says 'what's the weather like in + location' I will show the weather there;")
        speak("5 - Where is function, If the user says 'where is + location' I will show the location asked;")
        speak("6 - Shut down computer function, I can shutdown your computer for you, just say 'shut down computer' and it will turn off in 30 seconds;")
        speak("7 - Let's see my e-mails function, say 'let's see my e-mails' and I will show you;")
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
    
    if "let's see my emails" in data:
        speak("Opening your e-mails")
        os.system("start msedge https://mail.google.com/mail/u/0/#inbox")

# initialization
time.sleep(2) #Time to boot properly.
greeting() #Makes the greetings.
speak("So, how should I call you?") #Asks for the user preferred username.
user_name = getUserName() #Gets the input and changes the user_name variable.
speak(f"Hello {user_name}, what can I help you with?")
while 1:
    data = recordAudio()
    sleep(data)

#Avoid using complex sentences, be objective, the more direct you are with the bot, the better the interpretation and voice recognition.