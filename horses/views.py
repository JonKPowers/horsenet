from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def horses(request):
    return render(request, 'horses.html')


def races(request):
    return render(request, 'races.html')


def tracks(request):
    return render(request, 'tracks.html')


def deepnet(request):
    return render(request, 'deepnet.html')
