# Version Videoload 0.1.4
# -----------------------
# pacotes
from pytube import YouTube
from time import sleep
import settings as sett

# Testes de download
url_1 = 'https://youtu.be/ivPjMJl9yfY?si=gDxMZ6tvel7WUzuH'

# nota de sistema após download
nota = 'BAIXADO COM SUCESSO!'
barras = 80*'-' #:)

# diretorios de saida
diretorio = 'C:\\Users\\User\\Desktop\\GitHub\\diretorio'

# funçao de download de mp4
def BaixarMP4(link):
    try:
        video = YouTube(link)
        titulo = video.title
        dwd_streams = video.streams.filter(progressive=True, file_extension='mp4').first().download(output_path=diretorio)
        print(f'{barras}{titulo}\n{barras}\n{nota}')
    except:
        # entrada inválida ou link nao encontrado
        print('Link nao encontrado!')
        print(barras)
        sleep(2)
        sett.Tutorial()
        



