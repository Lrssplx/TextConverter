from gtts import gTTS
tts = gTTS('Oi, só estou testando mesmo.', lang='pt-br')

with open("ola3.mp3", "wb") as archivo:
    tts.write_to_fp(archivo)
    