
import os

os.environ['LD_LIBRARY_PATH'] = '/path/to/libespeak.so.1'

import subprocess
import wolframalpha
import wikipedia
import speech_recognition as sr
import ecapture
import requests
import playsound
import json
import datetime
import shutil
from gtts import gTTS
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
from urllib.request import urlopen

import warnings

warnings.filterwarnings("ignore")

import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

def speak(audio):
  engine.say(audio)
  engine.runAndWait()

def response(text):
  print(text)

  tts = gTTS(text=text, lang="en")

  audio = "Audio.mp3"
  tts.save(audio)

  playsound.playsound(audio)

  os.remove(audio)

def say_hello(text):
  greet = ["hi", "hello", "hey", "hola", "greeting", "wassup", "howdy",
           "what's good", "hey there"]

  response = ["hi", "hello", "hey", "hola", "greeting", "wassup", "howdy",
              "what's good", "hey there"]

  for word in text.split():
    if word.lower in greet:
      return random.choice(response)

  return ""

def wishme():
  hour = int(datetime.datetime.now().hour)
  if hour >= 0 and hour < 12:
    speak("Good Morning!")

  elif hour >= 12 and hour < 18:
    speak("Good Afternoon!")

  else:
    speak("Good Evening!")

  assname = ("ace")
  speak("""hello, i am ace. your assistant. I am here to make
  your life easier,
  you can command me to perform various cooking tasks
  such as making your
  favourite dishes""")


def username():
  speak("what should i call you?")
  uname = takeCommand()

  speak("Welcome Mister")
  speak(uname)
  columns = shutil.get_terminal_size().columns

  print("###".center(columns))
  print("Welocme Mr.", uname.center(columns))
  print("###".center(columns))

  speak("How can i help you")


def takeCommand():
  r = sr.Recognizer()

  try:
    with sr.Microphone() as source:

      print("Listening....")
      r.pause_thershold = 1
      audio = r.listen(source)

  except OSError as e:
    if e.errno == -9999:
      print("Error: No default input device available.")
      return None
    else:
      raise e

  try:

    print("Recognizing....")
    query = r.recognize_google(audio, lang = "en-in")
    print(f"user said: {query}\n")

  except Exception as e:
    print(e)
    print("Unable to Recognize your voice.")
    return "None"

  return query

if __name__ == "__main__":
  clear = lambda: os.system("cls")

  clear()
  wishme()
  username()

  while True:

    query = takeCommand().lower()


  if "wikipedia" in query:
    speak("searching wikipedia....")
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, senteces = 3)
    speak("According to wikipedia")
    print(results)
    speak(results)

  elif "how are you" in query:
    speak("Thanks for asking. I am doing well")
    speak("how are you")

  elif "who i am" in query:
    speak("if you talk me so definitely your human.")

  elif "who are you" in query:
    speak("My name is ace. your cooking assistant.")

  elif "good morning" in query:
    speak("A warm" +query)
    speak("how are you")
    speak(assname)

  elif "ace" in query:

    wishme()
    speak("I am your cooking assistant")
    speak(assname)

  elif "fine" in query or "good" in query:
    speak("It is good to know that your fine")

  elif "reason for you" in query:
    speak("I was created as an cookign assistant")

  elif "what's your name" or "what is your name" in query:
    speak("My friends call me")
    speak (assname)
    print("My friends call me", assname)

  elif "open web application" in query:
    speak("Here you go to aichefmaster web application\n")
    webbrower.open("web.aichefmaster.com")

  elif "Tender coconut pudding" in query:
    speak("""Here is your tender coconut pudding dish. Creamy, melt in the mouth,
     this tender coconut pudding is the showstopper of all puddings.
     Popular known as Elaneer pudding in Kerala,
     this delicious pudding is bound to win your heart.""")
    webbrowser.open("https://web.aichefmaster.com/dish/Tender%20coconut%20pudding")

  elif "step 1" in query:
    speak("""the first step is. In a saucepan, pour full fat milk and let it come to a boil.
    To the milk add sugar and condensed milk,
    stir continuously until the sugar has completely dissolved.
    Turn off the flame. for the 4 minutes. the main ingredients is
     milk, sugar, condensed milk, tender coconut pulp, agar agar, almonds.""")
    webbrowser.open("/video/TenderCoconutPudding/TenderCoconutPadding-Step1.mp4")

  elif "step 2" in query or "next step" in query:
    speak("""the second step is. Soak agar agar in 1 cup of water for 10 minutes.
    After that boil the agar agar water until it has completely dissolved in the water.
    for the 8 minutes. the main ingredients is
    milk, sugar, condensed milk, tender coconut pulp, agar agar, almonds.""")
    webbrowser.open("/video/TenderCoconutPudding/TenderCoconutPadding-Step2.mp4")

  elif "step 3" in query or "next step" in query:
    speak("""the third step is. In a mixer grinder jar, add the tender coconut pulp obtained by
    scooping out the flesh of the tender coconut. Grind it into a smooth paste.
    for the 7 minutes. the main ingredients is
    milk, sugar, condensed milk, tender coconut pulp, agar agar, almonds.""")
    webbrowser.open("/video/TenderCoconutPudding/TenderCoconutPadding-Step3.mp4")

  elif "step 4" in query or "next step" in query:
    speak("""the fourth step is. Keep the milk saucepan over medium flame and
    add the agar agar water to the milk while continuously stirring.
    Turn off the flame. for the 6 minutes. the main ingredients is
    milk, sugar, condensed milk, tender coconut pulp, agar agar, almonds.""")
    webbrowser.open("/video/TenderCoconutPudding/TenderCoconutPadding-Step4.mp4")

  elif "step 5" in query or "next step" in query:
    speak("""the fifth step is. Now add the grinded tender coconut pulp and
    mix well until everything is well incorporated in the milk. for the 5 minutes.
    the main ingredients is
    milk, sugar, condensed milk, tender coconut pulp, agar agar, almonds.""")
    webbrowser.open("/video/TenderCoconutPudding/TenderCoconutPadding-Step5.mp4")

  elif "step 6" in query or "next step" in query:
    speak("""the sixth step is. Pour into an aluminium mould and let it
    cool down for 20 minutes. Let it further set in the fridge for about 3-4 hours.
    for the 16 minutes. the main ingredients is
    milk, sugar, condensed milk, tender coconut pulp, agar agar, almonds.""")
    webbrowser.open("/video/TenderCoconutPudding/TenderCoconutPadding-Step6.mp4")

  elif "step 7" in query or "next step" in query:
      speak("""the seventh step is. Demould the pudding from the mould and
      garnish it using chopped almonds. for the 11 minutes. the main ingredients is
    milk, sugar, condensed milk, tender coconut pulp, agar agar, almonds.""")
    webbrowser.open("/video/TenderCoconutPudding/TenderCoconutPadding-Step7.mp4")

  elif "step 8" in query:
      speak("Serve cold. and Enjoy your meal.")
      webbrowser.open("/video/TenderCoconutPudding/TenderCoconutPadding-Step8.mp4")

  elif "open portfolio" in query:
    speak("Here you go to aichefmaster portfolio\n")
    webbrower.open("aichefmaster.com")

  elif "search" in query or "play" in query:
    query = query.replace("search", "")
    query = query.replace("play", "")
    webbrower.open(query)

  elif "don't listen" in query or "stop listening" in query:
    speak("for how much time you want to stop")
    a = int(takeCommand())
    time.sleep(a)
    print(a)

  elif "exit" in query:
    speak("Thanks for giving me your precious time")
    exit()
