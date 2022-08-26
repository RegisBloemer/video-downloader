from pytube import YouTube
import sys

#video = YouTube("https://www.youtube.com/watch?v=ADf0yIKx-FQ").streams.filter(res="1080p", file_extesion="mp4").first().download('/home/regisnb/Documentos/')
try:
    video_url = sys.argv[1]
    print(video_url)
    path = sys.argv[2]
    video = YouTube(video_url)
    video = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(path)

except: 
    print(f'Não foi possível fazer o download do vídeo [{video.title}]')