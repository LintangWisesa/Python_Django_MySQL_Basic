from django.shortcuts import render
from django.http import HttpResponse
from .models import Posts

def index(request):
    # // menampilkan Teks selamat datang:
    # return HttpResponse("Selamat datang di posts!")
    # // menampilkan file template layout html:
    return render(request, 'posts/index.html')

    # posts = Posts.objects.all()[:10]
    # context = {
    #     'title': 'Latest Posts',
    #     'posts': posts
    # }
    # return HttpResponse(context)