import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
r = sr.Recognizer()
mic = sr.Microphone()

nome = input("Qual o seu nome?")

with mic as fonte:
    r.adjust_for_ambient_noise(fonte)
    print("Me chame pelo meu nome")
    audio = r.listen(fonte)
    print("Enviando para reconhecimento!")

    try:
        text = r.recognize_google(audio, language="pt-BR")
        if text == "Python":
            print("Seja bem vindo {}".format(nome))
            engine.say("Seja bem vindo {}".format(nome))
            engine.runAndWait()
            engine.stop()
            while True:
                r.adjust_for_ambient_noise(fonte)
                print("="*70)
                print("Em que posso te ajudar!")
                audio = r.listen(fonte)
                print("Enviando para reconhecimento!")
                try:
                    text = r.recognize_google(audio, language="pt-BR")
                    print(text)
                    engine.say(text)
                    engine.runAndWait()
                    engine.stop()
                    if text == "dispensado":
                        print("Ok indo dormir, até mais.")
                        break
                except:
                    print("Não entendi o que você falou!")
                    engine.say("Não entendi o que você falou!")
                    engine.runAndWait()
                    engine.stop()
        else:
            engine.say("Fale meu nome certo!")
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