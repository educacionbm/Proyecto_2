"""
Objetivo: Etapa de Conversor de Voz a Texto
Entradas: Audio
Salidas: texto, del tipo STRING

"""
import speech_recognition as sr
import time

r = sr.Recognizer() #Instancia reconocedora
audio_file = sr.AudioFile('Improve your Speaking and Conversational skills with me.wav')

with audio_file as source: # Creando el audio como fuente para analizar posteriormente
    audio_analizar = r.record(source)

texto = r.recognize_google(audio_analizar,language='en-EN')
time.sleep(1.5)
print(texto)

