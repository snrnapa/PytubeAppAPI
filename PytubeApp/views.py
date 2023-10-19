from django.shortcuts import render
from yt_dlp import YoutubeDL 
from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello, world. 一応webアプリのひな型作れたから、これでyoutubedl実装していくで！！！")


def youtube_download(request):

    target_url = request.GET['youtube_url']
    ydl_opts = {'format': 'best'}

    print('***********開始*******************')
    print(target_url)
    with YoutubeDL(ydl_opts) as ydl:
        result = ydl.download([target_url])
    return HttpResponse(result)