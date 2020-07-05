import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voice')
#print(voices[0].id)

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am machine who created by Prince Prashant saini sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and return string output
    r = sr.Recognizer()
    with sr.microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing/...")
        query = r.recognize_google(audio, Language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        # print(e)
        print("please Pardon...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('jprpeoplesuv@gmail.com', 'your-password')
    server.sendmail('jprpeoplesuv@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    # while True:
    if 1:
        query = takecommand().lower()
        # Logic for exicuting task for quary

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            webbrowser.open("facebook.com")

        elif 'open repl' in query:
            webbrowser.open("repl.it")

        elif 'play music' in query:
            music_dr = 'D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, song[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f'sir, the time is(strTime)')

        elif 'open code' in query:
            codePath = "C:\\"
            os.startfile(codePath)

        elif 'send email to Prince Prashant saini' in query:
            try:
                speak("what should I say")
                content = takeCommand()
                to = "Princeprashantsaini@gmail.com"
                sendEmail(to, content)
                speak(" Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry sir Email not send rightnow")
