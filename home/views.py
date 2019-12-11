from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html')

def maintenance(request):
    return render(request, 'home/maintenance.html')
