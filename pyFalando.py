import pyttsx3

text = input("Qual o seu nome? ")

engine = pyttsx3.init()

engine.say("Prazer " + text)
engine.runAndWait()
engine.stop()
