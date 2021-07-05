#VERSION 0.1

"""
SLEEP assistente pessoal - codado e criado por Pedro Salviano

Se divirta utilizando, se puder, leia todo o código fonte, especialmente os comentários para que possa entender todas as funções e utilizá-las corretamente.
"""

from os.path import sameopenfile
import speech_recognition as sr #Pega o audio do usuário
from time import ctime #Módulo para indicar o tempo atual
import time #Intervalos de tempo
import os #Biblioteca que realiza funções naturais do sistema
import pyttsx3 #Python text-to-speech-3
from gtts import gTTS #Google text-to-speech
from pygame import mixer #Tocar áudios
import random #Aleatorizar algumas respostas, para que não fique repetitivo.

#Palavras que podem ser utilizadas para finalizar o programa.
words_to_terminate = ['desligar']
user_name = ""

def getUserName():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Diga algo!")
        audio = r.listen(source)

    # Reconhecimento de fala utilizando a API do google.
    user_name = ""
    try:
        # Usa a API-key padrão.
        # Para utilizar outra API-KEY: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        user_name = r.recognize_google(audio, language='PT-BR')
        print("Você disse: " + user_name)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    return user_name

#Função utilizada para fazer SLEEP dizer algo.
def speak(audioString):
    print(audioString)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    #engine.setProperty('voice', voices[1].id)
    engine.say(audioString)
    engine.runAndWait()

#Cumprimenta o usuário
def greeting():
    speak("Inicializando...")
    time.sleep(1)
    speak("Olá! Eu sou SLEEP, sua assistente pessoal.")
    time.sleep(1)
    speak("Estou na versão 0.1 e é um prazer te ajudar!")
    time.sleep(.5)
    speak("Se precisar de ajuda com as minhas funções apenas diga 'lista de funções' e eu irei te dar uma lista completa com todas as minhas funcionalidades.")
    time.sleep(.3)
    speak("No caso onde você queira me desligar apenas diga: 'desligar'.")

#Pega a entrada de áudio do usuário
def recordAudio():
    #Grava a entrada de áudio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Aguardando o usuário.")
        audio = r.listen(source)

    #Reconhecimento de voz utilizando API do google.
    data = ""
    try:
        #Usa a API-KEY padrão
        #Para utilizar outra API-KEY: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        data = r.recognize_google(audio, language='PT-BR')
        print("Você disse: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    return data

#Função para confirmar o desligamento do SLEEP
def terminate(data):
    for word in words_to_terminate:
        if word in data:
            speak("Deseja me desligar?")
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Diga algo! (Confirme sua resposta)")
                audio = r.listen(source)
            response = ""
            try:
                response = r.recognize_google(audio, language='PT-BR')
                print("Você idsse: " + data)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
            if "sim" or "com certeza" or "afirmativo" in response:
                speak(f"Ok, até mais {user_name}, foi um prazer falar com você!")
                exit()
            else:
                pass

#Função principal, faz tudo funcionar junto.      
def sleep(data):
    if "lista de funções" in data:
        speak("Precisa de ajuda com as minhas funções? Aqui vai uma lista do que posso fazer.")
        time.sleep(.5)
        speak("1 - Função de esperar, se o usuário disser 'esperar + tempo em segundos' eu irei dormir e esperar.")
        speak("2 - Função 'Como você está?';")
        speak("3 - Função 'Que horas são?', se o usuário disser 'Que horas são?' eu irei responder o dia, dia da semana, hora e minutos atuais.")
        speak("4 - Função 'Como está o clima em ...', se o usuário disser 'Como está o clima em ...' + localização eu irei mostrar o clima em tal, vale lembrar que é necessária uma conexão com a internet para a realização de tal função.")
        speak("5 - Função 'Onde é...', no caso onde o usuário disser 'Onde é + localização' eu irei mostrar o local perguntado.")
        speak("6 - Função de desligar o computador, caso queira que eu desligue seu computador apenas diga 'desligar computador' e eu irei.")
        speak("7 - Função 'Vamos ver meus e-mails', caso o usuário diga 'vamos ver meus e-mails' eu o mostrarei.")
        speak("8 - Função 'Me mostre fotos de ...', caso o usuário diga 'me mostre fotos de + objeto/pessoa/animal' eu irei mostrar, essa função também precisa de uma conexão com a Internet para ser realizada.")
        speak("9 - Função de verificação do sistema, caso o usuário diga 'verifique o sistema' eu irei iniciar uma verificação através de uma ferramenta nativa.")
    
    if "esperar" in data:
        data = data.split(' ')
        time_to_sleep = data[1]
        speak(f"Ok, eu esperarei por seus comandos por {time_to_sleep} segundos.")
        time.sleep(int(time_to_sleep))
        speak(f"Olá, posso te ajudar agora {user_name}?")
    
    if "como você está" in data:
        responses = ["Melhor que você.", "Estou bem, espero que você também esteja tendo um dia ótimo.", "Isso não te interessa.", "Estou bem, pronto para ajudar."]
        response = random.choice(responses)
        speak(response)

    if "Que horas são" in data:
        speak(ctime())

    if "onde é" in data:
        data = data.split(" ")
        location = data[2]
        speak("Espere um pouco, te mostrarei onde " + location + " é.")
        os.system("start msedge https://www.google.nl/maps/place/" + location + "/&amp;")

    if "desligar computador" in data:
        speak("Desligando!")
        speak("Seu computador será desligado em 30 segundos.")
        os.system("shutdown /s /t 30")

    if "Como está o clima em" in data:
        speak("Ok, irei te mostrar agora.")
        data = data.split(" ")
        string = "+".join(data)
        os.system("start msedge https://www.google.com/search?q=" + string)
    
    if "vamos ver meus emails" in data:
        speak("Abrindo seus e-mails.")
        os.system("start msedge https://mail.google.com/mail/u/0/#inbox")
    
    if "me mostre fotos de" in data:
        speak("Ok, eu irei te mostrar!")
        data = data.split(" ")
        string = "+".join(data)
        os.system("start msedge https://www.google.com/search?q=" + string)

    if "Verifique o sistema" in data:
        speak("Iniciando verificação do sistema. Aguarde, isso pode demorar alguns minutos.")
        resultado = os.system("sfc /scannow")
        if resultado == 0:
            speak("Verificação concluída - Nenhuma violação de integridade do sistema foi encontrada.")
        else:
            speak("Verificação concluída - A integridade do sistema pode ter sido violada de alguma forma, é recomendado que tome providências para corrigir.")
    
    #Verifica se uma das palavras para terminar está em 'data'.
    terminate(data)

#Inicialização.
time.sleep(2)
greeting()
speak("Então, como devo te chamar?")
user_name = getUserName()
speak(f"Olá {user_name}, com o que posso te ajudar?")
while 1:
    data = recordAudio()
    sleep(data)

#Evite utilizar frases complexas, seja objetivo, quanto mais objetivo você for melhor o reconhecimento de fala funcionará.