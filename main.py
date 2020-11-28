import speech_recognition as sr
import pyttsx3 as pyt3
import wolframalpha as wAlpha
import wikipedia as wiki

engine = pyt3.init()
r = sr.Recognizer()

app_id = 'VY3754-26T7L7R4RV'
client = wAlpha.Client(app_id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


voiceSrc = sr.Microphone(2)


def commandMe():
    with voiceSrc as source:
        print("speak")
        audio = r.listen(source)  # either record with timeout or just listen

    # recognize speech using Google Speech Recognition
    try:
        res = r.recognize_google(audio)

    except sr.UnknownValueError:
        speak("I am sorry. I can't clearly understand what you are saying. Can you please repeat it?")
        return 'repeat'

    except sr.RequestError as e:
        speak("Could not connect to the internet")
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return 'quit'

    return res


while True:
    # speak
    speak("What can I do for you?")
    res = commandMe().lower()
    print(res)
    if 'quit' in res:
        print('quitted')
        break
    elif 'done' not in res or 'quit' not in res :
        if 'wikipedia' in res:
            speak("Okay I am listening..")
            res = commandMe()
            results = wiki.summary(res, sentences=2)
            print(results)
            speak("According to wikipedia, " + results)
            break
        # else:
        #     results = client.query(res)
        #     ans = next(results.results).text
        #     print(ans)
        #     speak(ans)
        #     break
    elif 'repeat' in res:
        continue

print("Program ended")
