from gtts import gTTS
tts = gTTS('Olá! estou convertendo texto em voz.', lang='pt-br')
tts_ingles = gTTS('Hello! testing ', lang='en')
tts_frances = gTTS('Bonsoir! Elliot', lang='fr-fr')

with open("oi4.mp3", "wb") as archivo:
    tts.write_to_fp(archivo)
    tts_ingles.write_to_fp(archivo)
    tts_frances.write_to_fp(archivo)