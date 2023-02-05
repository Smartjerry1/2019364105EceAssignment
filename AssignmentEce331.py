import speech_recognition as sr

r = sr.Recognizer()
havard_S = sr.AudioFile('newProject.wav')

with havard_S as source:
    audio = r.record(source)
    
r.recognize_google(audio)