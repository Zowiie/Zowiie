import re
import speech_recognition as sr
import time
from time import ctime
from activities.respondzowiie import respond
from activities.assist import digital_assistant

class CallLiz:
    def listenToLiz(self):
        r = sr.Recognizer()
        f = "Zo"
        pattern = re.compile("Zo.*|so*", re.IGNORECASE)
        with sr.Microphone() as source:
            print("Zoe is listening...")
            audio = r.listen(source)
        data = ""
        try:
            data = r.recognize_google(audio)
            print("You said: " + data)
            if pattern.match(data):
                listening = True
                respond("Hey Ravi")
                digital_assistant(data)
        except sr.UnknownValueError:
            print("Google Speech Recognition did not understand audio")
        except sr.RequestError as e:
            print("Request Failed; {0}".format(e))
        return data

listening = True
while listening == True:
    data = CallLiz().listenToLiz()
