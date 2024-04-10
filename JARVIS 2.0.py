  # importing necessary libraries
import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import pathlib
import textwrap
import google.generativeai as genai
from google.colab import userdata
from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text,">",predicate = lambda _:True))

google_api_key = 'YOUR-API-KEY-HERE'

genai.configure(api_key=google_api_key)
import os
os.environ[google_api_key]='YOUR-API-KEY-HERE'
model = genai.GenerativeModel('models/gemini-1.0-pro-latest')

# initialisation
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

# The engine.say(audio) method is used to specify what should be spoken, and engine.runAndWait() 
# is used to execute the speech synthesis and wait for it to complete before continuing with the rest of the code.

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hello Boss! I am JARVIS, How may I assist you today?")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"Boss's Command: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'D:\MUSICS'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "D:\aeyjeyaryan\JARVIS.py"
            os.startfile(codePath)

        elif 'shut up' in query:
            speak('I am sorry boss! I will shut up for a while!')

        elif 'meaning of your name' in query:
            speak('JARVIS stands for Just A Rather Very Intelligent System, I was introduced by Tony Stark also known as IronMan!')

        elif 'what is the name of your boss' in query:
            speak("Common Boss! I know its you, I know your voice! You're my boss, Aryan!")

        elif 'can you detect objects via vision' in query:
            speak("No boss! I have not reached there yet! But I am sure, you'll teach me")

        elif 'bye' in query:
            speak("Okay Boss! Have a great day! JARVIS, Signing out! Bye")      

        elif 'hi jarvis time to work' in query:
            speak("hello boss! JARVIS in your assistance here, tell me how can i help you?")
        else:
            response=takeCommand().lower()
            speak(f"According to the AI, {to_markdown(response.text)}")
   
# if that doesn't work, use this:

else:
    speak(f"According to the AI, {to_markdown(query)}")

                      

        
     
