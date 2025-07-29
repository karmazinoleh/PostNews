from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from myauth.forms import UserForm


# Create your views here.
def login_view(request):
    error = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('news_home')
        else:
            error = 'Invalid username or password'

    data = {
        'error': error
    }
    return render(request, 'auth/login.html', data)

def register_view(request):
    #Remake registration using UserForm()
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            error = 'Incorrect data'
        elif User.objects.filter(username=username).exists():
            error = 'Username already taken'
        else:
            user = User.objects.create_user(username=username, password=password1)
            login(request, user)
            return redirect('news_home')

    data = {
        'error': error
    }

    return render(request, 'auth/register.html', data)


def logout_view(request):
    logout(request)
    return redirect('login')