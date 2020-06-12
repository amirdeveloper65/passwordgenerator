from django.shortcuts import render
import random

def home(request):
    return render(request,'generator/home.html')

def password(request):
    length=int(request.GET.get('length',12))
    characters=list('abcdefghijklmnopqrstuvwxyz')
    thepassword=''
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('*&%$#@'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))        
    for i in range(length):
        thepassword += random.choice(characters)
    return render(request ,'generator/password.html', {'password':thepassword})    

def about(request):
    return render(request,'generator/about.html')


# Create your views here.
