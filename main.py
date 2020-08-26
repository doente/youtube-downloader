import youtube_dl
import os
import sys

directory = (os.getcwd() + '/Downloads')
ydl_opts = {}

def main():
    arg = sys.argv[1]
    try:
        os.chdir(directory)
        print(f'Foi detectado que a pasta {directory} já existe e o arquivo está sendo baixado:')
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f'{arg}'])
    except OSError:
        os.mkdir(directory)
        print(f'A pasta {directory} não existia e foi criada pelo Script, o arquivo está sendo baixado:')
        os.chdir(directory)
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([f'{arg}'])
try:
    main()
except IndexError:
    print('Não foi detectado nenhum URL!')