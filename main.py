import speech_recognition as sr
import webbrowser
import objc
import pyttsx3
import musiclibrary
import requests
recogniser = sr.Recognizer()
newsapi = "9751e93272c1467396b38e612b943036"

def speak(text):
   engine = pyttsx3.init("nsss")
   engine.say(text)
   engine.runAndWait()



def processCommand(c):
   if "open google" in c.lower():
      webbrowser.open("https://google.com")
   elif "open instagram" in c.lower():
      webbrowser.open("https://instagram.com")
   elif "open docs" in c.lower():
      webbrowser.open("https://docs.google.com") 
   elif c.lower().startswith("play"):
      song = c.lower().split(" ")[1]
      link = musiclibrary.music[song]
      webbrowser.open(link)
   elif "news" in c.lower():
      r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
      if r.status_code == 200:
        # Parse the JSON response
        data = r.json()

        # Extract the headlines
        articles = data.get('articles', [])
        
        # Print the list of titles
        for article in articles:
           speak(article['title'])
   else:
      #let openai handle the request!!!!
      pass
if __name__ == "__main__":
    speak("Initialising Jarvis")
    # listen for the wake-up word - Jarvis
    while True:
        # obtain audio from the microphone
        r = sr.Recognizer()
    # recognize speech using google
        try:
         with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
            print("recognising")
         command = r.recognize_google(audio)
         if(command.lower() == "jarvis"):
            speak("'sup??!?")
            with sr.Microphone() as source:
                print("I'm active!")
                audio = r.listen(source)
                command = r.recognize_google(audio)
                processCommand(command)
        except sr.UnknownValueError:
            print("google could not understand audio")
        except Exception as e:
            print("Error; {0}".format(e))
