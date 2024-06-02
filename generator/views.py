from django.shortcuts import render
from django.http import HttpResponse
import random

def home_view(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request,'generator/about.html')

def password(request):
    generatedPassword = ''
    length = int(request.GET.get('length'))

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('upppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    
    for _ in range(length):
        generatedPassword+= random.choice(characters)


    return render(request, 'generator/password.html', {'password':generatedPassword})