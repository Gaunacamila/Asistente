import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
    ##Reconoce la voz
engine = pyttsx3.init()
##inicializar
##Cambio
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)
#cambiar la voz


engine.say("Buenos días My love")
engine.runAndWait()
try:
    with sr.Microphone() as source:
    #Llama a la función Microphone as source :
                print("habla Guei")
                voice = listener.listen(source)
                rec = listener.recognize_google(voice)
                print(rec)
except:
    pass
#Ignorar  prueba