import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
r = sr.Recognizer()
mic = sr.Microphone()

nome = input("Qual o seu nome?")

with mic as fonte:
    r.adjust_for_ambient_noise(fonte)
    print("Fale alguma coisa!")
    audio = r.listen(fonte)
    print("Enviando para reconhecimento!")

    try:
        text = r.recognize_google(audio, language="pt-BR")
        print("{}, você disse: {}".format(nome, text))
        engine.say("{}, você disse: {}".format(nome, text))
        engine.runAndWait()
        engine.stop()

        text = text.lower()
        if text == "que horas são":
            print("LISO")
            engine.say("LISO")
            engine.runAndWait()
            engine.stop()

    except:
        print("Não entendi o que você falou!")
        engine.say("Não entendi o que você falou!")
        engine.runAndWait()
        engine.stop()