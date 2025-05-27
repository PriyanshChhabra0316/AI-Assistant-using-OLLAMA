import speech_recognition as sr
import os
import webbrowser
import ollama
import datetime

chatStr = ""

def chat(query):
    global chatStr
    try:
        print(f"Query: {query}")  
        chatStr += f"User: {query}\nPriyansh: "
        
        response = ollama.chat(model="mistral", messages=[{"role": "user", "content": query}])
        reply = response["message"]["content"].strip()
        print(f"Ollama Response: {reply}")  
        say(reply)
        chatStr += reply + "\n"
        return reply

    except Exception as e:
        print(f"Error in Ollama API call: {e}")
        say("Sorry, an error occurred.")
        return "Error"

def say(text):
    os.system(f'say "{text}"')

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            print("Error:", e)
            return "Some Error Occurred. Sorry from Priyansh"

if __name__ == '__main__':
    print('Welcome to Priyansh A.I')
    say("Welcome to Priyaansh A.I")

    while True:
        query = takeCommand()

        sites = {
            "youtube": "https://www.youtube.com",
            "wikipedia": "https://www.wikipedia.com",
            "google": "https://www.google.com"
        }
        for site in sites:
            if f"open {site}" in query.lower():
                say(f"Opening {site} sir...")
                webbrowser.open(sites[site])
                continue

        if "open music" in query:
            musicPath = "/Users/priyansh/Music"
            os.system(f"open {musicPath}")

        elif "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            minute = datetime.datetime.now().strftime("%M")
            say(f"Sir, the time is {hour} and {minute} minutes")

        elif "priyansh quit" in query.lower():
            say("Goodbye sir!")
            break

        elif "reset chat" in query.lower():
            chatStr = ""

        else:
            chat(query) 