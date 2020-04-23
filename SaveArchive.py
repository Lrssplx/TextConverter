from gtts import gTTS
tts = gTTS('Olá, estou convertendo texto em voz.', lang='pt-br')
tts.save("ola.mp3")