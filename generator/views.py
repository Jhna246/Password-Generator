from django.shortcuts import render
from django.http import HttpResponse
import random
import string

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')


def password(request):
    alphabet_lower = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase

    thepassword = ''
    characters = list(alphabet_lower)
    numbers = list('1234567890')
    length = int(request.GET.get('length', 10))
    special = list('!@#$%^&*')

    if request.GET.get('upper'):
        characters.extend(alphabet_upper)

    if request.GET.get('numbers'):
        characters.extend(numbers)
    
    if request.GET.get('special'):
        characters.extend(special)

    for i in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'generatedpassword':thepassword})


def about(request):
    return render(request, 'generator/about.html')
