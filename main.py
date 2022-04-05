import speech_recognition as sr
from time import ctime
import time
import gtts
from gtts import gTTS
import os

# Global variable
listening = True
name = ""


# Audio respond
def respond(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("speech.mp3")
    os.system("start speech.mp3")

# Ask the user for the name
def name():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio)
    except sr.UnknownValueError:
        respond("I didn't catch that")
    return data


# Start the program by asking the users'name and initialize
# user's name
time.sleep(2)
respond("Hi, what is your name?")
time.sleep(2)
name = name()
respond("Hi " + name + " what can I do for you?")


# Make the program listen to users
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("I am listening...")
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        respond("I do not understand that")
    except sr.RequestError as e:
        respond("Request Failed")
    return data


# Basic response
def voiced_response(data):
    global listening

    # Ask about the bot name
    if "your name" in data:
        listening = True
        respond("My name is AlabaBot")

    # Normal greeting
    if "how are you" in data:
        listening = True
        respond("I am well")

    # Ask about initialized name
    if "my name" in data:
        listening = True
        respond("Your name is: " + name)

    # Ask about the time
    if "time" in data:
        listening = True
        respond(ctime())

    # Prompt the bot to stop listening
    if "stop" in data:
        listening = False
        print('Listening stopped')
        return listening
    return listening

# activate voice response method
while listening == True:
    time.sleep(1)
    data = listen()
    listening = voiced_response(data)
