import speech_recognition as sr
from translate import Translator
import convert



def main(base64):
    convert.convert(base64)
    sound = "temp.wav"

    r = sr.Recognizer()


    with sr.AudioFile(sound) as source:
        r.adjust_for_ambient_noise(source)


        print("Converting Audio To Text ..... ")


        audio = r.listen(source)
        
        



    try:
         text=r.recognize_google(audio, language="es")
         print(text)
         translator= Translator(to_lang="English",from_lang="es")
         translation = translator.translate(text)
         print(translation)
         return translation




    except Exception as e:
        print("Error {} : ".format(e) )


