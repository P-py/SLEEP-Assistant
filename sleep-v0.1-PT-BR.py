# VERSION 0.2.6
# Please go and read README.md file for correct usage

"""
SLEEP assistente pessoal - codado e criado por Pedro Salviano

Se divirta utilizando, se puder, leia todo o código fonte, especialmente os comentários para que possa entender todas as funções e utilizá-las corretamente.
"""

import speech_recognition as sr #Pega o audio do usuário
from time import ctime #Módulo para indicar o tempo atual
import time #Intervalos de tempo
import os #Biblioteca que realiza funções naturais do sistema
import pyttsx3 #Python text-to-speech-3
from gtts import gTTS #Google text-to-speech
from pygame import mixer #Tocar áudios
import random #Aleatorizar algumas respostas, para que não fique repetitivo.
from newsapi import NewsApiClient #API que é responsável por lidar com a coleta das notícias mais recentes
import json #Administração de dados JSON
import requests #HTTP Requests
import math
import serial #Comunicação serial
import pyautogui
import wikipedia #API da Wikipedia
import subprocess
import datetime
import winsound


# Configurando as TOKENS
def init_tokens():
    with open("./data/newsapitoken.0", "r", encoding="utf-8") as f:
        NEWSAPITOKEN = f.read()
    try:
        newsapi = NewsApiClient(api_key=NEWSAPITOKEN)
    except:
        speak("Por favor, entre na pasta raiz do programa, na subpasta 'data' e digite a sua API KEY da Newsapi para funcionamento correto.")

#Palavras que podem ser utilizadas para finalizar o programa.
TERMINATE_STRS = ['desligar']
AFFIRMATIVES = ['sim', 'com certeza', 'afirmativo', 'positivo']
user_name = ""
NOTE_STRS = ['anote', 'faça uma anotação']
POMODORO_STRS = ['ligue o relógio pomodoro', 'relógio pomodoro', 'relógio de pomodoro']

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

#Subfunção/feature utilizada em outras features, coleta o tempo e data atual, em formato completo ou apenas horário.
"""

Utiliza métodos da biblioteca time como time.localtime() que retorna uma "time.scruct_time", e time.strftime() que formata struct_time em uma string.
NOTA: O strftime funciona de acordo com parâmetros específicos: https://www.tutorialspoint.com/python/time_strftime.htm


getting_localtime('complete') ~ retornará uma string completa com: "[Dia da semana], [Data] - [Horário]"
getting_localtime('hour-minute') ~ retornará uma string com apenas horário: "[Hora]:[Minuto]"
"""
def getting_localtime(type_of_time):
    string = []
    def day():
        if time.strftime("%A", time.localtime()) == "Monday":
            string.append("Segunda-feira")
        elif time.strftime("%A", time.localtime()) == "Tuesday":
            string.append("Terça-feira")
        elif time.strftime("%A", time.localtime()) == "Wednesday":
            string.append("Quarta-feira")
        elif time.strftime("%A", time.localtime()) == "Thursday":
            string.append("Quinta-feira")
        elif time.strftime("%A", time.localtime()) == "Friday":
            string.append("Sexta-feira")
        elif time.strftime("%A", time.localtime()) == "Saturday":
            string.append("Sábado")
        elif time.strftime("%A", time.localtime()) == "Sunday":
            string.append("Domingo")
    def day_of_month():
        string.append(time.strftime("%d", time.localtime()))
    
    def month():
        if time.strftime("%B", time.localtime()) == "January":
            string.append("Janeiro")
        elif time.strftime("%B", time.localtime()) == "Frebruary":
            string.append("Fevereiro")
        elif time.strftime("%B", time.localtime()) == "March":
            string.append("Março")
        elif time.strftime("%B", time.localtime()) == "April":
            string.append("Abril")
        elif time.strftime("%B", time.localtime()) == "May":
            string.append("Maio")
        elif time.strftime("%B", time.localtime()) == "June":
            string.append("Junho")
        elif time.strftime("%B", time.localtime()) == "July":
            string.append("Julho")
        elif time.strftime("%B", time.localtime()) == "August":
            string.append("Agosto")
        elif time.strftime("%B", time.localtime()) == "September":
            string.append("Setembro")
        elif time.strftime("%B", time.localtime()) == "October":
            string.append("Outubro")
        elif time.strftime("%B", time.localtime()) == "November":
            string.append("Novembro")
        elif time.strftime("%B", time.localtime()) == "December":
            string.append("Dezembro")
    
    def year():
        string.append(time.strftime("%Y", time.localtime()))

    def hour_and_minute():
        string.append(time.strftime("%H:%M", time.localtime()))

    if type_of_time == 'hour-minute':
        hour_and_minute()
        return(string[0])

    elif type_of_time == 'complete':
        day()
        day_of_month()
        month()
        year()
        hour_and_minute()
        return(string[0] + ", " + string[1] + " de " + string[2] + " de " + string[3] + ", " + string[4])

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
    
    data = data.lower()
    return data

#Função para confirmar o desligamento do SLEEP
def terminate(data):
    for word in TERMINATE_STRS:
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

    if "que horas são" in data:
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

    if "como está o clima em" in data:
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

    if "verifique o sistema" in data:
        speak("Iniciando verificação do sistema. Aguarde, isso pode demorar alguns minutos.")
        resultado = os.system("sfc /scannow")
        if resultado == 0:
            speak("Verificação concluída - Nenhuma violação de integridade do sistema foi encontrada.")
        else:
            speak("Verificação concluída - A integridade do sistema pode ter sido violada de alguma forma, é recomendado que tome providências para corrigir.")
    
    if "bom dia" in data:
        speak(f"Bom dia {user_name}.")
        speak(f"A data e horário atuais são {ctime()}")
        speak(f"Irei te mostrar as principais notícias.")
        os.system("start msedge https://news.google.com/")

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