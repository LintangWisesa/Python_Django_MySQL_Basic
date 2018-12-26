from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Selamat datang di posts!")
    return render(request, 'posts/index.html')