import speech_recognition as sr
import playsound
from time import ctime
from gtts import gTTS
import webbrowser
import os

# pip install speechrecognition
# pip install pyaudio


class Speech:

    def __init__(self, name):
        self.name = name

    r = sr.Recognizer()

    def get_speech(self, question=''):
        with sr.Microphone() as voice_source:
            if question != '':
                self.response_audio(question)
            audio = self.r.listen(voice_source)
            voice_record = ''
            try:
                voice_record = self.r.recognize_google(audio)
            except sr.UnknownValueError:
                print("Error unknown record recognized")
            except sr.RequestError:
                print("Error please check the Internet connection")
            return voice_record

    def response_speech(self, voice_record, status):
        if 'start' in voice_record:
            return True
        elif 'stop' in voice_record:
            return False
        elif status:
            if 'what is your name' in voice_record:
                self.response_audio(f'My Name is {self.name}')
            if 'what time is it' in voice_record:
                self.response_audio(ctime())
            if 'search' in voice_record:
                search = self.get_speech('What you search for?')
                url = 'https://www.google.de/search?q=' + search
                webbrowser.get().open(url)
                self.response_audio('Here is the result what I found for ' + search)
            if 'location' in voice_record:
                location = self.get_speech('Which location you looking for?')
                url = 'https://www.google.nl/maps/place/' + location + '/&amp;'
                webbrowser.get().open(url)
                self.response_audio('Here is the result I found for ' + location)
            return status
        else:
            return status

    @staticmethod
    def response_audio(audio):
        tts = gTTS(text=audio, lang='en')
        file = 'audio.mp3'
        tts.save(file)
        playsound.playsound(file)
        os.remove(file)
