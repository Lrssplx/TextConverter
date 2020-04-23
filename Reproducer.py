from gtts import gTTS
from playsound import playsound
NOME_ARCHIVO = "somGerado.mp3"
tts = gTTS('Oi, estou testando para que você reproduza aqui mesmo seu áudio .', lang='pt-br')
#tts = gTTS(' Te amo desgraça, te amo desgraça, eu te amo de graça, te amo desgraça ', lang='pt-br')
# Nota: podríamos llamar directamente a save
with open(NOME_ARCHIVO, "wb") as archivo:
    tts.write_to_fp(archivo)

playsound(NOME_ARCHIVO)